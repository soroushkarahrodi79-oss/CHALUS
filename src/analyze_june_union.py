import json
from collections import Counter

import networkx as nx

from gate2a_reconcile import RoadHandler, build_graph, remove_closure, route, POINTS

jan = json.load(open("jan_way_inventory.json"))
h, g = build_graph("june_union.osm")
print("june graph", g.number_of_nodes(), g.number_of_edges(), "ways", len(h.ways))
missing = sorted(set(map(int, jan)) - set(h.ways))
changed = []
for sid, jw in jan.items():
    wid = int(sid)
    if wid not in h.ways:
        continue
    uw = h.ways[wid]
    tagdiff = {k:(jw['tags'].get(k),uw['tags'].get(k)) for k in set(jw['tags'])|set(uw['tags']) if jw['tags'].get(k)!=uw['tags'].get(k)}
    nodes_changed = jw['nodes'] != uw['nodes']
    if jw['version'] != uw['version'] or nodes_changed or tagdiff:
        changed.append({
            "id": wid,
            "jan_version": jw['version'],
            "june_version": uw['version'],
            "jan_ts": jw['timestamp'],
            "june_ts": uw['timestamp'],
            "nodes_changed": nodes_changed,
            "jan_nodes": jw['nodes'],
            "june_nodes": uw['nodes'],
            "tagdiff": tagdiff,
            "jan_tags": jw['tags'],
            "june_tags": uw['tags'],
        })
print("missing", len(missing), missing)
print("changed", len(changed), Counter(('nodes' if c['nodes_changed'] else 'tags') for c in changed))
json.dump(changed, open("changed_union.json","w"), indent=2, ensure_ascii=False)

gc = remove_closure(g)
results = {}
for gw in ["south","east","west"]:
    for dst in ["chalus","nowshahr","kelardasht"]:
        key=f"{gw}-{dst}"
        try:
            b=route(g,POINTS[gw],POINTS[dst]); c=route(gc,POINTS[gw],POINTS[dst])
            results[key]={"base_km":b[0],"closure_km":c[0],"base_ways":b[2],"closure_ways":c[2],"base_edges":b[3],"closure_edges":c[3]}
            print(key,round(b[0],3),round(c[0],3),round(c[0]/b[0],4),len(b[2]),len(c[2]))
        except Exception as e:
            print(key,"ERROR",type(e).__name__,str(e))
json.dump(results,open("june_union_results.json","w"),indent=2,ensure_ascii=False)
