import json
from gate2a_reconcile import build_graph, remove_closure, route, POINTS

def narrative(edges):
    out = []
    last = None
    total = 0.0
    for u,v,wid,d,hw,ref,name in edges:
        total += d
        key = (hw, ref, name)
        if key != last:
            out.append({"highway": hw, "ref": ref, "name": name, "start_km": round(total-d,2)})
            last = key
    return out

hj, gj = build_graph("iran-240101.osm.pbf"); gjc = remove_closure(gj)
hy, gy = build_graph("june_reconciled_partial.osm"); gyc = remove_closure(gy)

result = {}
for gw in ["south","east","west"]:
    for dst in ["chalus","nowshahr","kelardasht"]:
        for scenario, gjx, gyx in [("base", gj, gy), ("closure", gjc, gyc)]:
            jb = route(gjx, POINTS[gw], POINTS[dst])
            yb = route(gyx, POINTS[gw], POINTS[dst])
            key = f"{gw}-{dst}-{scenario}"
            result[key] = {
                "jan_total_km": round(jb[0],3), "jan_narrative": narrative(jb[3]),
                "jun_total_km": round(yb[0],3), "jun_narrative": narrative(yb[3]),
            }

json.dump(result, open("route_narratives.json","w"), indent=2, ensure_ascii=False)
for key, r in result.items():
    print(f"=== {key} === jan={r['jan_total_km']}km jun={r['jun_total_km']}km")
    print("  JAN:", " -> ".join(f"{n['ref'] or n['name'] or '?'}@{n['start_km']}" for n in r['jan_narrative']))
    print("  JUN:", " -> ".join(f"{n['ref'] or n['name'] or '?'}@{n['start_km']}" for n in r['jun_narrative']))
