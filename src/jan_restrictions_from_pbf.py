"""Extract all type=restriction relations directly from the January PBF,
independent of the externally-supplied 31-file history set, to check
whether any route-relevant restriction relation was missed by that set."""
import json, osmium
from gate2a_reconcile import build_graph, remove_closure, route, POINTS

class RelHandler(osmium.SimpleHandler):
    def __init__(self):
        super().__init__(); self.rels = []
    def relation(self, r):
        if r.tags.get('type') == 'restriction':
            members = [(m.type, m.ref, m.role) for m in r.members]
            self.rels.append({'id': r.id, 'version': r.version, 'timestamp': str(r.timestamp),
                               'restriction': r.tags.get('restriction'), 'members': members})

h = RelHandler()
h.apply_file("iran-240101.osm.pbf")
print("Total type=restriction relations found directly in January PBF:", len(h.rels))

# way IDs actually used by all 18 January route-states
hj, gj = build_graph("iran-240101.osm.pbf"); gjc = remove_closure(gj)
route_ways = set()
for gw in ["south","east","west"]:
    for dst in ["chalus","nowshahr","kelardasht"]:
        b = route(gj, POINTS[gw], POINTS[dst]); c = route(gjc, POINTS[gw], POINTS[dst])
        route_ways.update(b[2]); route_ways.update(c[2])

relevant = [r for r in h.rels if any(m[0] in ('w','way') and m[1] in route_ways for m in r['members'])]
print("Of those, relations with a member way actually used by a January route:", len(relevant))

# cross-check against the externally-supplied 31-relation set
external_ids = {8266216,8266235,8266237,8306621,8331778,8834431,9227377,9227378,9227916,
                 9227917,9227918,9227919,9227920,9227921,9227922,9296539,9307869,9310052,
                 9638889,9713712,9713713,11131468,11131469,12247737,13487373,17421383,
                 17975498,17975499,18971245,18971246,18995254}
relevant_ids = {r['id'] for r in relevant}
print("Relevant relation IDs found directly from PBF:", sorted(relevant_ids))
print("Present in externally-supplied 31-file set:", relevant_ids & external_ids)
print("MISSING from externally-supplied set (found only via direct PBF extraction):", relevant_ids - external_ids)

json.dump({
    "total_restriction_relations_in_january_pbf": len(h.rels),
    "route_relevant_relations": relevant,
    "route_relevant_ids": sorted(relevant_ids),
    "missing_from_external_31_file_set": sorted(relevant_ids - external_ids),
}, open("jan_restrictions_from_pbf.json","w"), indent=2, ensure_ascii=False)
