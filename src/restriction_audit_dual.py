import glob, json, xml.etree.ElementTree as ET
from gate2a_reconcile import build_graph, remove_closure, route, POINTS

JAN_CUT = "2024-01-01T21:21:15Z"
JUN_CUT = "2024-06-12T20:29:59Z"
PAIRS = [(gw,dst) for gw in ["south","east","west"] for dst in ["chalus","nowshahr","kelardasht"]]

def relation_at_cutoff(path, cutoff):
    root = ET.parse(path).getroot()
    rels = [r for r in root.findall('relation') if r.attrib['timestamp'] <= cutoff]
    if not rels:
        return None
    r = max(rels, key=lambda x: int(x.attrib['version']))
    if r.attrib.get('visible','true') != 'true':
        return None
    tags = {t.attrib['k']: t.attrib['v'] for t in r.findall('tag')}
    if tags.get('type') != 'restriction':
        return None
    members = [(m.attrib['type'], int(m.attrib['ref']), m.attrib['role']) for m in r.findall('member')]
    return {'id': int(r.attrib['id']), 'version': int(r.attrib['version']), 'timestamp': r.attrib['timestamp'],
            'restriction': tags.get('restriction'), 'members': members}

def load_relations(cutoff):
    out = []
    for p in sorted(glob.glob('osm_history/restrictions/*.osm')):
        rel = relation_at_cutoff(p, cutoff)
        if rel:
            out.append(rel)
    return out

def check_violations(rels, routedata):
    relevant = []
    violations = []
    for key,_ in [(f"{g}-{d}",None) for g,d in PAIRS]:
        for scenario in ['base','closure']:
            edges = routedata[key][scenario][3]
            nodes = routedata[key][scenario][1]
            ways = [e[2] for e in edges]
            for rel in rels:
                mem = {role:(typ,ref) for typ,ref,role in rel['members']}
                member_ways = {ref for typ,ref,role in rel['members'] if typ=='way'}
                if not member_ways.intersection(ways):
                    continue
                relevant.append((key, scenario, rel['id']))
                fromid = mem.get('from',(None,None))[1]; toid = mem.get('to',(None,None))[1]; via = mem.get('via')
                hit = False
                if via and via[0]=='node':
                    vn = via[1]
                    for i in range(len(edges)-1):
                        if edges[i][1]==vn and edges[i][2]==fromid and edges[i+1][0]==vn and edges[i+1][2]==toid:
                            if rel['restriction']=='no_u_turn' and nodes[i]!=nodes[i+2]:
                                continue
                            hit = True
                elif via and via[0]=='way':
                    vw = via[1]
                    comp = []
                    for w in ways:
                        if not comp or comp[-1]!=w: comp.append(w)
                    for i in range(len(comp)-2):
                        if comp[i:i+3]==[fromid, vw, toid]: hit = True
                if hit:
                    violations.append((key, scenario, rel['id'], rel['restriction']))
    return sorted(set(relevant)), violations

print("Building January graph...")
hj, gj = build_graph("iran-240101.osm.pbf"); gjc = remove_closure(gj)
jan_routes = {f"{g}-{d}": {"base": route(gj, POINTS[g], POINTS[d]), "closure": route(gjc, POINTS[g], POINTS[d])} for g,d in PAIRS}

print("Building June graph...")
hy, gy = build_graph("june_reconciled_partial.osm"); gyc = remove_closure(gy)
jun_routes = {f"{g}-{d}": {"base": route(gy, POINTS[g], POINTS[d]), "closure": route(gyc, POINTS[g], POINTS[d])} for g,d in PAIRS}

jan_rels = load_relations(JAN_CUT)
jun_rels = load_relations(JUN_CUT)
print(f"January-cutoff relations valid: {len(jan_rels)}")
print(f"June-cutoff relations valid: {len(jun_rels)}")

jan_relevant, jan_viol = check_violations(jan_rels, jan_routes)
jun_relevant, jun_viol = check_violations(jun_rels, jun_routes)

print("January route-relation contacts:", len(jan_relevant), "violations:", jan_viol)
print("June route-relation contacts:", len(jun_relevant), "violations:", jun_viol)

out = {
    "january": {"cutoff": JAN_CUT, "relations": jan_rels, "relevant_contacts": jan_relevant, "violations": jan_viol},
    "june": {"cutoff": JUN_CUT, "relations": jun_rels, "relevant_contacts": jun_relevant, "violations": jun_viol},
}
json.dump(out, open("restriction_audit_dual.json","w"), indent=2, ensure_ascii=False)
print("done")
