import csv, glob, json, os, xml.etree.ElementTree as ET

CUTOFF='2024-06-12T20:29:59Z'
jan=json.load(open('jan_full_route_inventory.json'))
changed={c['id']:c for c in json.load(open('changed_union.json'))}

# Route membership across core and sensitivity checks.
membership={}
def add_members(path, label_prefix=''):
    data=json.load(open(path))
    if path.endswith('gateway_sensitivity_all.json'): data=data['results']
    for key,v in data.items():
        for sc in ['base_ways','closure_ways']:
            for wid in v.get(sc,[]): membership.setdefault(int(wid),set()).add(f'{label_prefix}{key}:{sc.split("_")[0]}')
for p,l in [('jan_sensitivity_routes.json','Jan/'),('gate2a_results.json','Jun/'),('gate2a_sensitivity.json','JunSens/'),('gateway_sensitivity_all.json','JunGate/')]: add_members(p,l)

def history_path(wid):
    paths=[f'osm_history/changed_ways/{wid}.osm',f'osm_history/candidate_ways/{wid}.osm',f'osm_history/extra_ways/{wid}.osm',f'osm_history/way_{wid}.osm',f'osm_history/way_{wid}_history.osm']
    return next((p for p in paths if os.path.exists(p)),None)

def way_versions(wid):
    p=history_path(wid)
    if not p:return []
    return ET.parse(p).getroot().findall('way')

def tags(w): return {t.attrib['k']:t.attrib['v'] for t in w.findall('tag')}
def nodes(w): return [int(n.attrib['ref']) for n in w.findall('nd')]
def next_ts(ws,w):
    later=[x for x in ws if int(x.attrib['version'])>int(w.attrib['version'])]
    return min(later,key=lambda x:int(x.attrib['version'])).attrib['timestamp'] if later else ''

routing_keys={'highway','oneway','access','motor_vehicle','construction','junction'}
rows=[]

# 113 modified route-dependent January ways.
for wid,c in sorted(changed.items()):
    ws=way_versions(wid)
    jw=jan[str(wid)]
    w=max([x for x in ws if x.attrib['timestamp']<=CUTOFF],key=lambda x:int(x.attrib['version']))
    td=c['tagdiff']
    if set(td)&routing_keys: typ='B_ROUTING_ATTRIBUTE'
    elif c['nodes_changed'] and (c['jan_nodes'][0]!=c['june_nodes'][0] or c['jan_nodes'][-1]!=c['june_nodes'][-1]): typ='C_TOPOLOGY'
    else: typ='A_NON_MATERIAL'
    material='NO'
    action='Use 12-Jun version; no route/corridor effect'
    if wid in {664585317,1106503266}:
        material='YES_REPRESENTATION_ONLY'; action='Apply oneway=yes; route shifts to parallel carriageway; distance/corridor stable'
    rows.append({
        'object':f'way/{wid}','jan_version':jw['version'],'jan_valid_from':jw['timestamp'],'jan_valid_to':w.attrib['timestamp'] if int(w.attrib['version'])>jw['version'] else '',
        'june_version':w.attrib['version'],'june_valid_from':w.attrib['timestamp'],'june_valid_to':next_ts(ws,w),'change_type':typ,
        'route_affected':' | '.join(sorted(membership.get(wid,set()))),'material':material,'action':action,
        'tag_change_json':json.dumps(td,ensure_ascii=False,separators=(',',':')),
        'june_tags_json':json.dumps(tags(w),ensure_ascii=False,separators=(',',':')),
        'june_node_ids_json':json.dumps(nodes(w),separators=(',',':')),
        'parent_child':'','history_url':f'https://www.openstreetmap.org/way/{wid}/history'
    })

# Two January Haraz ways deleted and replaced before cutoff.
replacement='1270179067,1287287400,1287287401'
for wid in [924025918,924025921]:
    ws=way_versions(wid); jw=jan[str(wid)]; visible=[x for x in ws if x.attrib.get('visible','true')=='true']; old=max(visible,key=lambda x:int(x.attrib['version']))
    deletion=min([x for x in ws if x.attrib.get('visible')=='false'],key=lambda x:int(x.attrib['version']))
    rows.append({'object':f'way/{wid}','jan_version':jw['version'],'jan_valid_from':jw['timestamp'],'jan_valid_to':deletion.attrib['timestamp'],'june_version':f'deleted v{deletion.attrib["version"]}','june_valid_from':deletion.attrib['timestamp'],'june_valid_to':'','change_type':'D_HISTORICAL_STATUS','route_affected':' | '.join(sorted(membership.get(wid,set()))),'material':'YES_TOPOLOGY_RECONCILIATION','action':'Remove obsolete ID; insert historically valid descendants','tag_change_json':'{"visible":[true,false]}','june_tags_json':'{}','june_node_ids_json':'[]','parent_child':f'replaced by {replacement}','history_url':f'https://www.openstreetmap.org/way/{wid}/history'})

# New descendants actually traversed by the reconciled core/sensitivity routes.
new_ids=sorted(set(membership)-set(map(int,jan)))
for wid in new_ids:
    ws=way_versions(wid)
    if not ws: continue
    w=max([x for x in ws if x.attrib['timestamp']<=CUTOFF],key=lambda x:int(x.attrib['version']))
    if w.attrib.get('visible','true')!='true': continue
    rows.append({'object':f'way/{wid}','jan_version':'ABSENT','jan_valid_from':'','jan_valid_to':w.attrib['timestamp'],'june_version':w.attrib['version'],'june_valid_from':w.attrib['timestamp'],'june_valid_to':next_ts(ws,w),'change_type':'C_TOPOLOGY','route_affected':' | '.join(sorted(membership.get(wid,set()))),'material':'YES_TOPOLOGY_RECONCILIATION','action':'Insert split/child way valid at cutoff','tag_change_json':'{"state":["absent","created"]}','june_tags_json':json.dumps(tags(w),ensure_ascii=False,separators=(',',':')),'june_node_ids_json':json.dumps(nodes(w),separators=(',',':')),'parent_child':'created in changeset affecting route-dependent predecessor','history_url':f'https://www.openstreetmap.org/way/{wid}/history'})

fields=['object','jan_version','jan_valid_from','jan_valid_to','june_version','june_valid_from','june_valid_to','change_type','route_affected','material','action','tag_change_json','june_tags_json','june_node_ids_json','parent_child','history_url']
with open('Gate2A_Historical_Change_Ledger.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(sorted(rows,key=lambda r:int(r['object'].split('/')[1])))
print('ledger rows',len(rows))
from collections import Counter
print(Counter(r['change_type'] for r in rows));print(Counter(r['material'] for r in rows))
