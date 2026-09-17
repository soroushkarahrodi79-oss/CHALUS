"""Resolve the disputed January->June correspondence for ways 924025918
and 924025921 (short Haraz-road bridge segments near 35.839N 52.063E).

The change ledger claims these were "replaced by 1270179067, 1287287400,
1287287401" -- this script checks that claim independently by (a) spatial
search for the nearest June ways at the January ways' actual location,
and (b) shared-node-ID verification between the January ways and whatever
June way is found there, rather than trusting the ledger's text.
"""
import math, json
import osmium
from gate2a_reconcile import build_graph, remove_closure, route, POINTS

JAN_PBF = "iran-240101.osm.pbf"
JUN_OSM = "june_reconciled_partial.osm"
DISPUTED_JAN_WAYS = {924025918, 924025921}
LEDGER_CLAIMED_REPLACEMENTS = {1270179067, 1287287400, 1287287401}

def haversine(a, b):
    r = 6371008.8
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    dp = math.radians(b[0]-a[0]); dl = math.radians(b[1]-a[1])
    h = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*r*math.asin(math.sqrt(h))

class WayGeom(osmium.SimpleHandler):
    def __init__(self, ids=None):
        super().__init__(); self.ids = ids; self.found = {}
    def way(self, w):
        if self.ids is not None and w.id not in self.ids:
            return
        try:
            coords = [(n.location.lat, n.location.lon) for n in w.nodes]
        except Exception:
            return
        self.found[w.id] = {"nodes": [n.ref for n in w.nodes], "coords": coords,
                             "tags": dict(w.tags), "version": w.version, "timestamp": str(w.timestamp)}

class NearbySearch(osmium.SimpleHandler):
    def __init__(self, target, radius_m):
        super().__init__(); self.target = target; self.radius = radius_m; self.near = []
    def way(self, w):
        try:
            coords = [(n.location.lat, n.location.lon) for n in w.nodes]
        except Exception:
            return
        if not coords: return
        mind = min(haversine(self.target, c) for c in coords)
        if mind < self.radius:
            self.near.append({"id": w.id, "min_dist_m": round(mind,1), "tags": dict(w.tags),
                               "nodes": [n.ref for n in w.nodes], "version": w.version})

result = {}

hj = WayGeom(DISPUTED_JAN_WAYS)
hj.apply_file(JAN_PBF, locations=True)
result["january_disputed_ways"] = hj.found
print("January disputed ways:")
for wid, d in hj.found.items():
    print(" ", wid, d["tags"], "nodes:", d["nodes"])

# Location: midpoint of the disputed ways' coordinates
all_coords = [c for d in hj.found.values() for c in d["coords"]]
target = (sum(c[0] for c in all_coords)/len(all_coords), sum(c[1] for c in all_coords)/len(all_coords))
result["target_location"] = target
print("Target location (midpoint of disputed ways):", target)

# Step 1: is the LEDGER's claimed replacement actually at this location?
hc = WayGeom(LEDGER_CLAIMED_REPLACEMENTS)
hc.apply_file(JUN_OSM, locations=True)
claimed_dists = []
for wid, d in hc.found.items():
    mind = min(haversine(target, c) for c in d["coords"])
    claimed_dists.append((wid, mind))
print("Ledger-claimed replacement ways -- distance from target:")
for wid, dist in claimed_dists:
    print(f"  way {wid}: {dist:.1f} m from target")
result["ledger_claimed_replacement_distances_m"] = claimed_dists

# Step 2: independent spatial search for ANY June way actually near the target
hs = NearbySearch(target, 400)
hs.apply_file(JUN_OSM, locations=True)
print(f"Independent spatial search: June ways within 400 m of target: {len(hs.near)}")
result["independent_spatial_search_400m"] = hs.near
for n in sorted(hs.near, key=lambda x: x["min_dist_m"]):
    print(f"  way {n['id']}: {n['min_dist_m']} m, tags={n['tags']}")

# Step 3: shared-node-ID verification between disputed January ways and the
# spatially-nearest June ways (proof of physical continuity, not coincidence)
jan_node_ids = set()
for d in hj.found.values():
    jan_node_ids.update(d["nodes"])

hn = WayGeom({n["id"] for n in hs.near})
hn.apply_file(JUN_OSM, locations=True)
shared = {}
for wid, d in hn.found.items():
    common = jan_node_ids & set(d["nodes"])
    if common:
        shared[wid] = sorted(common)
result["shared_node_ids_with_nearby_june_ways"] = shared
print("June ways (from spatial search) sharing node IDs with the disputed January ways:")
for wid, nodes in shared.items():
    print(f"  way {wid} shares nodes: {nodes}")

# Also fetch the January version of any shared-node way to compare edit history
if shared:
    hjv = WayGeom(set(shared.keys()))
    hjv.apply_file(JAN_PBF, locations=True)
    result["january_versions_of_shared_ways"] = {
        wid: {"version": d["version"], "timestamp": d["timestamp"], "node_count": len(d["nodes"])}
        for wid, d in hjv.found.items()
    }
    hyv = WayGeom(set(shared.keys()))
    hyv.apply_file(JUN_OSM, locations=True)
    result["june_versions_of_shared_ways"] = {
        wid: {"version": d["version"], "timestamp": d["timestamp"], "node_count": len(d["nodes"])}
        for wid, d in hyv.found.items()
    }
    print("January vs June versions of the physically-confirmed successor way(s):")
    for wid in shared:
        jv = result["january_versions_of_shared_ways"].get(wid)
        yv = result["june_versions_of_shared_ways"].get(wid)
        print(f"  way {wid}: Jan v{jv['version'] if jv else None} ({jv['node_count'] if jv else None} nodes) -> Jun v{yv['version'] if yv else None} ({yv['node_count'] if yv else None} nodes)")

# Step 4: which actual computed routes pass through this location, both dates
hjb, gj = build_graph(JAN_PBF); gjc = remove_closure(gj)
hyb, gy = build_graph(JUN_OSM); gyc = remove_closure(gy)
route_hits = {}
for date, g in [("january", gjc), ("june", gyc)]:
    hits = []
    for dst in ["chalus","nowshahr","kelardasht"]:
        c = route(g, POINTS["south"], POINTS[dst])
        for u,v,wid,d,hw,ref,name in c[3]:
            lat,lon = g.nodes[u]["lat"], g.nodes[u]["lon"]
            if haversine(target,(lat,lon)) < 300:
                hits.append((dst, wid, round(haversine(target,(lat,lon)),1)))
    route_hits[date] = hits
result["route_hits_near_target"] = route_hits
print("Actual computed closure-route way usage within 300 m of target:")
for date, hits in route_hits.items():
    print(f"  {date}:", sorted(set((h[1] for h in hits))))

verdict = "RESOLVED" if shared else "UNRESOLVED"
result["verdict"] = verdict
print("\nVERDICT:", verdict)

json.dump(result, open("haraz_geometry_resolution.json","w"), indent=2, ensure_ascii=False, default=str)
