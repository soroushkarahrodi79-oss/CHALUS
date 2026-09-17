import json, osmium
from collections import Counter
from gate2a_reconcile import build_graph, remove_closure, route, POINTS

PAIRS = [(gw,dst) for gw in ["south","east","west"] for dst in ["chalus","nowshahr","kelardasht"]]

def full_route_data(g, gc):
    out = {}
    for gw,dst in PAIRS:
        b = route(g, POINTS[gw], POINTS[dst])
        c = route(gc, POINTS[gw], POINTS[dst])
        out[f"{gw}-{dst}"] = {"base": b, "closure": c}
    return out

print("Building January graph...")
hj, gj = build_graph("iran-240101.osm.pbf")
gjc = remove_closure(gj)
jan = full_route_data(gj, gjc)

print("Building June graph...")
hy, gy = build_graph("june_reconciled_partial.osm")
gyc = remove_closure(gy)
jun = full_route_data(gy, gyc)

result = {}
for key,_ in [(f"{g}-{d}", None) for g,d in PAIRS]:
    result[key] = {}
    for scenario in ["base","closure"]:
        jb = jan[key][scenario]
        yb = jun[key][scenario]
        jways = set(jb[2]); yways = set(yb[2])
        shared = jways & yways
        jonly = jways - yways
        yonly = yways - jways
        # dominant corridor = most common ref among edges (by length-weighted)
        def dom_ref(edges):
            c = Counter()
            for u,v,wid,d,hw,ref,name in edges:
                c[ref] += d
            if not c: return None
            return c.most_common(1)[0][0]
        identical_path = (jb[1] == yb[1]) if scenario=="closure" and jan[key]["base"][1]==jb[1] else None
        result[key][scenario] = {
            "jan_km": round(jb[0],3), "jun_km": round(yb[0],3),
            "jan_edges": len(jb[3]), "jun_edges": len(yb[3]),
            "jan_ways": len(jways), "jun_ways": len(yways),
            "shared_ways": len(shared), "jan_only": sorted(jonly), "jun_only": sorted(yonly),
            "jan_dominant_ref": dom_ref(jb[3]), "jun_dominant_ref": dom_ref(yb[3]),
        }
    # identity check: is closure route same as base route (within same date)?
    result[key]["jan_closure_equals_base"] = (jan[key]["base"][1] == jan[key]["closure"][1])
    result[key]["jun_closure_equals_base"] = (jun[key]["base"][1] == jun[key]["closure"][1])

with open("full_parity.json","w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

for key in result:
    r = result[key]
    print(key, "jan_close==base:", r["jan_closure_equals_base"], "jun_close==base:", r["jun_closure_equals_base"])
    for sc in ["base","closure"]:
        s=r[sc]
        print(f"  {sc}: jan_ways={s['jan_ways']} jun_ways={s['jun_ways']} shared={s['shared_ways']} jan_only={len(s['jan_only'])} jun_only={len(s['jun_only'])} jan_ref={s['jan_dominant_ref']} jun_ref={s['jun_dominant_ref']}")

# Save way inventories for both dates (for change-ledger cross-reference)
jan_way_meta = {str(w): {"tags": hj.ways[w]["tags"], "version": hj.ways[w]["version"], "timestamp": hj.ways[w]["timestamp"]}
                 for pair in jan.values() for scenario in pair.values() for w in scenario[2]}
jun_way_meta = {str(w): {"tags": hy.ways[w]["tags"], "version": hy.ways[w]["version"], "timestamp": hy.ways[w]["timestamp"]}
                 for pair in jun.values() for scenario in pair.values() for w in scenario[2]}
json.dump(jan_way_meta, open("jan_route_way_meta.json","w"), indent=2, ensure_ascii=False)
json.dump(jun_way_meta, open("jun_route_way_meta.json","w"), indent=2, ensure_ascii=False)
print("jan route ways:", len(jan_way_meta), "jun route ways:", len(jun_way_meta))
