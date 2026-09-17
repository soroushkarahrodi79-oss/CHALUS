import json
from gate2a_reconcile import build_graph,remove_closure,route,POINTS

h,g=build_graph('june_reconciled_partial.osm'); gc=remove_closure(g)

def node_at_distance(gw, km):
    r=route(g,POINTS[gw],POINTS['chalus'])
    cum=0.0
    for u,v,wid,d,*_ in r[3]:
        cum+=d
        if cum>=km: return v,cum,g.nodes[v]['lat'],g.nodes[v]['lon']
    raise RuntimeError

shifts={
    'south':{0:POINTS['south'],5:POINTS['south_5'],10:POINTS['south_10']},
    'east':{},'west':{}
}
for gw in ['east','west']:
    shifts[gw][0]=POINTS[gw]
    for km in [5,10]:
        n,c,lat,lon=node_at_distance(gw,km);shifts[gw][km]=n

out={'nodes':{},'results':{}}
for gw,pts in shifts.items():
    out['nodes'][gw]={}
    for shift,n in pts.items():
        out['nodes'][gw][str(shift)]={'node':n,'lat':g.nodes[n]['lat'],'lon':g.nodes[n]['lon']}
        for dst in ['chalus','nowshahr','kelardasht']:
            b=route(g,n,POINTS[dst]);c=route(gc,n,POINTS[dst])
            out['results'][f'{gw}+{shift}-{dst}']={'base_km':b[0],'closure_km':c[0],'delta_km':c[0]-b[0],'dr':c[0]/b[0],'base_ways':b[2],'closure_ways':c[2]}
json.dump(out,open('gateway_sensitivity_all.json','w'),indent=2,ensure_ascii=False)
print(json.dumps(out['nodes'],indent=2))
for k,v in out['results'].items():print(k,round(v['base_km'],2),round(v['closure_km'],2),round(v['dr'],3))
