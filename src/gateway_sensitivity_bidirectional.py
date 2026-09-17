import json
import networkx as nx
from gate2a_reconcile import build_graph, remove_closure, route, POINTS

GATEWAYS = ["south", "east", "west"]
DESTS = ["chalus", "nowshahr", "kelardasht"]

def walk_from(g, start, forward_next, km_targets):
    """Walk along the graph starting at `start`, choosing at each step the
    neighbor that continues in the same general direction as forward_next
    (the first step already known from the base route), for `forward`
    direction; for `backward` we instead use predecessor edges (edges INTO
    start), continuing along the incoming edge with the longest length
    (a proxy for 'same corridor, not a minor side street')."""
    out = {}
    cur = start
    cum = 0.0
    visited = {start}
    nxt = forward_next
    while nxt is not None and cum < max(km_targets) + 1:
        u, v, wid, d, hw, ref, name = nxt
        cum += d
        for km in km_targets:
            if km not in out and cum >= km:
                out[km] = {"node": v, "lat": g.nodes[v]["lat"], "lon": g.nodes[v]["lon"], "cum_km": round(cum,3)}
        visited.add(v)
        cands = [(v,w,k,e) for w in g.successors(v) for k,e in g[v][w].items() if w not in visited]
        if not cands:
            break
        v2,w2,k2,e2 = max(cands, key=lambda c: c[3]["length"])
        nxt = (v2, w2, e2["way_id"], e2["length"], e2["highway"], e2.get("ref"), e2.get("name"))
    return out

def node_backward(g, start, km_targets):
    out = {}
    cur = start
    cum = 0.0
    visited = {start}
    while cum < max(km_targets) + 1:
        preds = [(u,cur,k,e) for u in g.predecessors(cur) for k,e in g[u][cur].items() if u not in visited]
        if not preds:
            break
        u2,_,k2,e2 = max(preds, key=lambda c: c[3]["length"])
        cum += e2["length"]
        for km in km_targets:
            if km not in out and cum >= km:
                out[km] = {"node": u2, "lat": g.nodes[u2]["lat"], "lon": g.nodes[u2]["lon"], "cum_km": round(cum,3)}
        visited.add(u2)
        cur = u2
    return out

def build_shift_nodes(g, gw):
    base = route(g, POINTS[gw], POINTS["chalus"])
    edges = base[3]
    fwd_start = (POINTS[gw], base[1][1], edges[0][2], edges[0][3], edges[0][4], edges[0][5], edges[0][6]) if edges else None
    fwd = walk_from(g, POINTS[gw], fwd_start, [5,10])
    bwd = node_backward(g, POINTS[gw], [5,10])
    nodes = {"0": {"node": POINTS[gw], "lat": g.nodes[POINTS[gw]]["lat"], "lon": g.nodes[POINTS[gw]]["lon"]}}
    for km,info in fwd.items(): nodes[f"+{km}"] = info
    for km,info in bwd.items(): nodes[f"-{km}"] = info
    return nodes

def run(pbf_or_osm, label):
    h, g = build_graph(pbf_or_osm)
    gc = remove_closure(g)
    shift_nodes = {gw: build_shift_nodes(g, gw) for gw in GATEWAYS}
    results = {}
    for gw in GATEWAYS:
        for shift, info in shift_nodes[gw].items():
            n = info["node"]
            for dst in DESTS:
                key = f"{gw}{shift}-{dst}"
                try:
                    b = route(g, n, POINTS[dst]); c = route(gc, n, POINTS[dst])
                    results[key] = {"base_km": b[0], "closure_km": c[0], "dr": c[0]/b[0],
                                     "connectivity": "CONNECTED WITH DETOUR" if c[1]!=b[1] else "CONNECTED",
                                     "dominant_ref_base": max(set(e[5] for e in b[3] if e[5]), key=lambda r: sum(e[3] for e in b[3] if e[5]==r)) if any(e[5] for e in b[3]) else None,
                                     "dominant_ref_closure": max(set(e[5] for e in c[3] if e[5]), key=lambda r: sum(e[3] for e in c[3] if e[5]==r)) if any(e[5] for e in c[3]) else None}
                except nx.NetworkXNoPath:
                    results[key] = {"connectivity": "DISCONNECTED"}
                except Exception as e:
                    results[key] = {"error": str(e)}
    return {"nodes": shift_nodes, "results": results}

print("January...")
jan_out = run("iran-240101.osm.pbf", "jan")
print("June...")
jun_out = run("june_reconciled_partial.osm", "jun")

json.dump({"january": jan_out, "june": jun_out}, open("gateway_sensitivity_bidirectional.json","w"), indent=2, ensure_ascii=False)

for date,out in [("JAN",jan_out),("JUN",jun_out)]:
    print(f"=== {date} ===")
    for gw in GATEWAYS:
        for shift,info in out["nodes"][gw].items():
            print(f"  {gw}{shift}: node={info['node']} lat={info['lat']:.4f} lon={info['lon']:.4f}")
    for key,r in out["results"].items():
        if "dr" in r:
            print(f"  {key}: base={r['base_km']:.2f} closure={r['closure_km']:.2f} dr={r['dr']:.3f} conn={r['connectivity']}")
        else:
            print(f"  {key}: {r}")
