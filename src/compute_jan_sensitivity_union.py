import json
from gate2a_reconcile import build_graph, remove_closure, route, POINTS

h,g=build_graph('iran-240101.osm.pbf'); gc=remove_closure(g)
out={}; union=set()
for gw in ['south','south_5','south_10','east','west']:
    for dst in ['chalus','nowshahr','kelardasht','chalus_alt','nowshahr_alt','kelardasht_alt']:
        try:
            b=route(g,POINTS[gw],POINTS[dst]); c=route(gc,POINTS[gw],POINTS[dst])
            out[f'{gw}-{dst}']={'base_km':b[0],'closure_km':c[0],'dr':c[0]/b[0],'base_ways':b[2],'closure_ways':c[2]}
            union.update(b[2]);union.update(c[2])
            print(gw,dst,round(b[0],3),round(c[0],3),round(c[0]/b[0],3),flush=True)
        except Exception as e: print(gw,dst,type(e).__name__,flush=True)
json.dump(out,open('jan_sensitivity_routes.json','w'),indent=2,ensure_ascii=False)
json.dump({str(w):h.ways[w] for w in sorted(union)},open('jan_full_route_inventory.json','w'),indent=2,ensure_ascii=False)
print('union',len(union),flush=True)
