import json
from gate2a_reconcile import build_graph, remove_closure, route, POINTS

extra_rels = [
 {'id': 8259827, 'restriction': 'no_left_turn', 'members': [('way',325786256,'from'),('node',5548397028,'via'),('way',582250715,'to')]},
 {'id': 8259828, 'restriction': 'no_u_turn', 'members': [('node',5548397028,'via'),('way',584849620,'from'),('way',584849620,'to')]},
 {'id': 8259829, 'restriction': 'no_u_turn', 'members': [('way',584849620,'from'),('node',5569007733,'via'),('way',584849620,'to')]},
 {'id': 8259830, 'restriction': 'no_u_turn', 'members': [('way',584850084,'from'),('node',5569007733,'via'),('way',584850084,'to')]},
 {'id': 8259831, 'restriction': 'no_u_turn', 'members': [('way',584850084,'from'),('node',5569007734,'via'),('way',584850084,'to')]},
 {'id': 8259832, 'restriction': 'no_u_turn', 'members': [('way',582250714,'from'),('node',5569007734,'via'),('way',582250714,'to')]},
 {'id': 12255025, 'restriction': 'no_left_turn', 'members': [('way',325786279,'from'),('way',782050040,'to')]},
 {'id': 14725086, 'restriction': 'no_left_turn', 'members': [('way',1106503268,'from'),('node',5093179824,'via'),('way',664585318,'to')]},
 {'id': 15976034, 'restriction': 'only_right_turn', 'members': [('way',1181854408,'from'),('node',27216646,'via')]},
]

def check(rels, routedata):
    relevant, violations = [], []
    for key in routedata:
        for scenario in ['base','closure']:
            edges = routedata[key][scenario][3]
            nodes = routedata[key][scenario][1]
            ways = [e[2] for e in edges]
            for rel in rels:
                mem = {role:(typ,ref) for typ,ref,role in rel['members']}
                member_ways = {ref for typ,ref,role in rel['members'] if typ=='way'}
                if not member_ways.intersection(ways): continue
                relevant.append((key,scenario,rel['id']))
                fromid = mem.get('from',(None,None))[1]; toid = mem.get('to',(None,None))[1]; via = mem.get('via')
                hit=False
                if via and via[0]=='node':
                    vn = via[1]
                    for i in range(len(edges)-1):
                        if edges[i][1]==vn and edges[i][2]==fromid and edges[i+1][0]==vn and edges[i+1][2]==toid:
                            if rel['restriction']=='no_u_turn' and nodes[i]!=nodes[i+2]: continue
                            hit=True
                if hit: violations.append((key,scenario,rel['id'],rel['restriction']))
    return sorted(set(relevant)), violations

PAIRS=[(g,d) for g in ["south","east","west"] for d in ["chalus","nowshahr","kelardasht"]]
hj,gj=build_graph("iran-240101.osm.pbf"); gjc=remove_closure(gj)
jan_routes={f"{g}-{d}":{"base":route(gj,POINTS[g],POINTS[d]),"closure":route(gjc,POINTS[g],POINTS[d])} for g,d in PAIRS}
hy,gy=build_graph("june_reconciled_partial.osm"); gyc=remove_closure(gy)
jun_routes={f"{g}-{d}":{"base":route(gy,POINTS[g],POINTS[d]),"closure":route(gyc,POINTS[g],POINTS[d])} for g,d in PAIRS}

jr,jv = check(extra_rels, jan_routes)
yr,yv = check(extra_rels, jun_routes)
print("January contacts with the 9 extra relations:", jr, "violations:", jv)
print("June contacts with the 9 extra relations:", yr, "violations:", yv)
json.dump({"january":{"contacts":jr,"violations":jv},"june":{"contacts":yr,"violations":yv}}, open("extra_relations_check.json","w"), indent=2, default=str)
