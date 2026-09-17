import json
from collections import Counter

from gate2a_reconcile import build_graph, remove_closure, route, POINTS

h, g = build_graph("june_reconciled_partial.osm")
gc = remove_closure(g)
results = {}
for gw in ["south", "east", "west"]:
    for dst in ["chalus", "nowshahr", "kelardasht"]:
        key = f"{gw}-{dst}"
        b = route(g, POINTS[gw], POINTS[dst])
        c = route(gc, POINTS[gw], POINTS[dst])
        results[key] = {
            "base_km": b[0], "closure_km": c[0],
            "delta_km": c[0]-b[0], "dr": c[0]/b[0],
            "base_nodes": b[1], "base_ways": b[2], "base_edges": b[3],
            "closure_nodes": c[1], "closure_ways": c[2], "closure_edges": c[3],
        }
        for label, r in [("base",b),("closure",c)]:
            classes=Counter(e[4] for e in r[3]); refs=Counter(str(e[5]) for e in r[3] if e[5]); names=Counter(str(e[6]) for e in r[3] if e[6])
            print(key,label,round(r[0],3),"classes",dict(classes),"refs",refs.most_common(8),"names",names.most_common(8),"maxedge",max(e[3] for e in r[3]))
json.dump(results,open("gate2a_results.json","w"),indent=2,ensure_ascii=False)

# Sensitivity: frozen alternative nodes from Gate 1.
sens={}
for gw in ["south", "south_5", "south_10", "east", "west"]:
    for dst in ["chalus", "nowshahr", "kelardasht", "chalus_alt", "nowshahr_alt", "kelardasht_alt"]:
        if dst.endswith("_alt") and dst.split("_alt")[0] not in ["chalus","nowshahr","kelardasht"]: continue
        try:
            b=route(g,POINTS[gw],POINTS[dst]); c=route(gc,POINTS[gw],POINTS[dst])
            sens[f"{gw}-{dst}"]={"base_km":b[0],"closure_km":c[0],"delta_km":c[0]-b[0],"dr":c[0]/b[0],"base_ways":b[2],"closure_ways":c[2]}
        except Exception as e:
            sens[f"{gw}-{dst}"]={"error":str(e)}
json.dump(sens,open("gate2a_sensitivity.json","w"),indent=2,ensure_ascii=False)
