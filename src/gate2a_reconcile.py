import math
import json
from collections import defaultdict

import networkx as nx
import osmium

BBOX = (49.70, 35.35, 53.20, 37.15)

POINTS = {
    "south": 31086990,
    "south_5": 3241439201,
    "south_10": 31087836,
    "east": 6208746864,
    "west": 8595307908,
    "chalus": 1375231380,
    "nowshahr": 4998048119,
    "kelardasht": 3323917713,
    "chalus_alt": 3724790673,
    "nowshahr_alt": 6239259168,
    "kelardasht_alt": 5559267651,
}

MAJOR = {
    "motorway", "motorway_link", "trunk", "trunk_link",
    "primary", "primary_link", "secondary", "secondary_link",
}


def haversine(a, b):
    lat1, lon1 = a
    lat2, lon2 = b
    r = 6371.0088
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2-lat1)
    dl = math.radians(lon2-lon1)
    h = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*r*math.asin(math.sqrt(h))


def truthy_oneway(tags):
    val = tags.get("oneway", "").lower()
    if val in {"yes", "1", "true"}:
        return 1
    if val == "-1":
        return -1
    if tags.get("junction") == "roundabout":
        return 1
    return 0


class RoadHandler(osmium.SimpleHandler):
    def __init__(self):
        super().__init__()
        self.nodes = {}
        self.ways = {}
        self.point_nodes = {}

    def node(self, n):
        if n.id in POINTS.values() or n.id in {3294759340, 6221341191, 2141920981}:
            self.point_nodes[n.id] = (n.location.lat, n.location.lon)

    def way(self, w):
        hw = w.tags.get("highway")
        if hw not in MAJOR:
            return
        ref = (w.tags.get("ref") or "").strip()
        # Gate 1 excluded 230/240 mountain shortcuts.
        if ref in {"230", "240", "Road 230", "Road 240"}:
            return
        coords = []
        ids = []
        try:
            for n in w.nodes:
                lon, lat = n.location.lon, n.location.lat
                if BBOX[0]-0.05 <= lon <= BBOX[2]+0.05 and BBOX[1]-0.05 <= lat <= BBOX[3]+0.05:
                    self.nodes[n.ref] = (lat, lon)
                    coords.append((lat, lon))
                    ids.append(n.ref)
                else:
                    coords.append(None)
                    ids.append(n.ref)
        except osmium.InvalidLocationError:
            return
        tags = {k: v for k, v in w.tags}
        self.ways[w.id] = {"id": w.id, "version": w.version, "timestamp": str(w.timestamp), "tags": tags, "nodes": ids, "coords": coords}


def build_graph(pbf):
    h = RoadHandler()
    h.apply_file(pbf, locations=True)
    g = nx.MultiDiGraph()
    for nid, pos in h.nodes.items():
        g.add_node(nid, lat=pos[0], lon=pos[1])
    for wid, w in h.ways.items():
        ow = truthy_oneway(w["tags"])
        for i in range(len(w["nodes"])-1):
            u, v = w["nodes"][i], w["nodes"][i+1]
            a, b = w["coords"][i], w["coords"][i+1]
            if a is None or b is None or u not in g or v not in g:
                continue
            d = haversine(a, b)
            data = {"length": d, "way_id": wid, "highway": w["tags"].get("highway"), "ref": w["tags"].get("ref"), "name": w["tags"].get("name")}
            if ow >= 0:
                g.add_edge(u, v, **data)
            if ow <= 0:
                g.add_edge(v, u, **data)
    return h, g


def route(g, src, dst):
    path = nx.shortest_path(g, src, dst, weight="length")
    total = 0.0
    way_ids = []
    edge_records = []
    for u, v in zip(path, path[1:]):
        candidates = g.get_edge_data(u, v)
        k, e = min(candidates.items(), key=lambda kv: kv[1]["length"])
        total += e["length"]
        way_ids.append(e["way_id"])
        edge_records.append((u, v, e["way_id"], e["length"], e["highway"], e.get("ref"), e.get("name")))
    return total, path, list(dict.fromkeys(way_ids)), edge_records


def remove_closure(g):
    out = g.copy()
    center = 3294759340
    for u, v in list(out.in_edges(center)) + list(out.out_edges(center)):
        if out.has_edge(u, v):
            out.remove_edges_from([(u, v, k) for k in list(out[u][v])])
    return out


if __name__ == "__main__":
    h, g = build_graph("iran-240101.osm.pbf")
    print("graph", g.number_of_nodes(), g.number_of_edges(), "ways", len(h.ways))
    print("points", json.dumps({k: h.point_nodes.get(v) for k,v in POINTS.items()}, indent=2))
    results = {}
    gc = remove_closure(g)
    for gw in ["south", "east", "west"]:
        for dst in ["chalus", "nowshahr", "kelardasht"]:
            key = f"{gw}-{dst}"
            try:
                b = route(g, POINTS[gw], POINTS[dst])
                c = route(gc, POINTS[gw], POINTS[dst])
                results[key] = {"base_km": b[0], "closure_km": c[0], "base_ways": b[2], "closure_ways": c[2], "base_edges": b[3], "closure_edges": c[3]}
                print(key, round(b[0], 3), round(c[0], 3), round(c[0]/b[0], 4), len(b[2]), len(c[2]))
            except Exception as e:
                print(key, "ERROR", type(e).__name__, str(e))
    with open("gate1_reproduced.json", "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    with open("jan_way_inventory.json", "w") as f:
        union = sorted({wid for r in results.values() for field in ("base_ways","closure_ways") for wid in r[field]})
        json.dump({str(wid): h.ways[wid] for wid in union}, f, indent=2, ensure_ascii=False)
    print("union ways", len(union))
