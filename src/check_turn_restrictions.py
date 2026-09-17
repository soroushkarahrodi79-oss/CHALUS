import glob,json,xml.etree.ElementTree as ET

cut='2024-06-12T20:29:59Z'
rels=[]
for p in glob.glob('osm_history/restrictions/*.osm'):
    root=ET.parse(p).getroot(); rs=[r for r in root.findall('relation') if r.attrib['timestamp']<=cut]
    if not rs: continue
    r=max(rs,key=lambda x:int(x.attrib['version']))
    if r.attrib.get('visible','true')!='true': continue
    tags={t.attrib['k']:t.attrib['v'] for t in r.findall('tag')}
    members=[(m.attrib['type'],int(m.attrib['ref']),m.attrib['role']) for m in r.findall('member')]
    rels.append({'id':int(r.attrib['id']),'restriction':tags.get('restriction'),'members':members})

routes=json.load(open('gate2a_results.json'))
viol=[]; relevant=[]
for key,r in routes.items():
    for scenario in ['base','closure']:
        edges=r[scenario+'_edges']; ways=[e[2] for e in edges]
        nodes=r[scenario+'_nodes']
        for rel in rels:
            mem={role:(typ,ref) for typ,ref,role in rel['members']}
            member_ways={ref for typ,ref,role in rel['members'] if typ=='way'}
            if not member_ways.intersection(ways): continue
            relevant.append((key,scenario,rel['id']))
            fromid=mem.get('from',(None,None))[1]; toid=mem.get('to',(None,None))[1]; via=mem.get('via')
            hit=False
            if via and via[0]=='node':
                vn=via[1]
                for i in range(len(edges)-1):
                    if edges[i][1]==vn and edges[i][2]==fromid and edges[i+1][0]==vn and edges[i+1][2]==toid:
                        # Same-way no_u_turn does not prohibit straight continuation.
                        if rel['restriction']=='no_u_turn' and nodes[i]!=nodes[i+2]:
                            continue
                        hit=True
            elif via and via[0]=='way':
                vw=via[1]
                # Detect contiguous from->via->to way sequence.
                comp=[]
                for w in ways:
                    if not comp or comp[-1]!=w: comp.append(w)
                for i in range(len(comp)-2):
                    if comp[i:i+3]==[fromid,vw,toid]: hit=True
            if hit: viol.append((key,scenario,rel['id'],rel['restriction']))
print('relations at cutoff',len(rels),'route-relation contacts',len(set(relevant)),'violations',viol)
json.dump({'relations':rels,'relevant_contacts':sorted(set(relevant)),'violations':viol},open('restriction_audit.json','w'),indent=2)
