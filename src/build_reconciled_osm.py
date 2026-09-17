import glob
import json
import xml.etree.ElementTree as ET

CUTOFF = "2024-06-12T20:29:59Z"
ALLOWED = {"motorway", "motorway_link", "trunk", "trunk_link", "primary", "primary_link", "secondary", "secondary_link"}

base_tree = ET.parse("june_union.osm")
base = base_tree.getroot()
existing_nodes = {int(n.attrib["id"]): n for n in base.findall("node")}
existing_ways = {int(w.attrib["id"]): w for w in base.findall("way")}

# Candidate sibling ways created in changesets that changed a route-dependent January way.
selected_ways = {}
for p in glob.glob("osm_history/candidate_ways/*.osm"):
    root = ET.parse(p).getroot()
    valid = [w for w in root.findall("way") if w.attrib["timestamp"] <= CUTOFF]
    if not valid:
        continue
    w = max(valid, key=lambda x: int(x.attrib["version"]))
    if w.attrib.get("visible", "true") != "true":
        continue
    tags = {t.attrib["k"]: t.attrib["v"] for t in w.findall("tag")}
    if tags.get("highway") not in ALLOWED:
        continue
    selected_ways[int(w.attrib["id"])] = w

# Gate 1 sensitivity-route ways not present in the nine core-path union.
for p in glob.glob("osm_history/extra_ways/*.osm"):
    root = ET.parse(p).getroot()
    valid = [w for w in root.findall("way") if w.attrib["timestamp"] <= CUTOFF]
    if not valid:
        continue
    w = max(valid, key=lambda x: int(x.attrib["version"]))
    if w.attrib.get("visible", "true") != "true":
        continue
    tags = {t.attrib["k"]: t.attrib["v"] for t in w.findall("tag")}
    if tags.get("highway") in ALLOWED:
        selected_ways[int(w.attrib["id"])] = w

# Gather latest node states present in the relevant changesets.
node_versions = {}
for p in glob.glob("osm_history/changesets/*.osc"):
    root = ET.parse(p).getroot()
    for action in root:
        for n in action.findall("node"):
            if n.attrib["timestamp"] > CUTOFF:
                continue
            nid = int(n.attrib["id"])
            if nid not in node_versions or int(n.attrib["version"]) > int(node_versions[nid].attrib["version"]):
                node_versions[nid] = n

# Complete candidate-only nodes from their full histories.
for p in glob.glob("osm_history/candidate_nodes/*.osm"):
    root = ET.parse(p).getroot()
    valid = [n for n in root.findall("node") if n.attrib["timestamp"] <= CUTOFF]
    if not valid:
        continue
    n = max(valid, key=lambda x: int(x.attrib["version"]))
    nid = int(n.attrib["id"])
    if nid not in node_versions or int(n.attrib["version"]) > int(node_versions[nid].attrib["version"]):
        node_versions[nid] = n

needed = {int(nd.attrib["ref"]) for w in selected_ways.values() for nd in w.findall("nd")}
missing = sorted(needed - set(existing_nodes) - set(node_versions))
print("selected sibling ways", len(selected_ways), "needed nodes", len(needed), "missing nodes", len(missing))
open("missing_candidate_nodes.txt", "w").write("\n".join(map(str, missing)))

for nid in sorted(needed - set(existing_nodes)):
    if nid in node_versions and node_versions[nid].attrib.get("visible", "true") == "true":
        base.insert(0, node_versions[nid])
for wid, w in selected_ways.items():
    if wid not in existing_ways:
        base.append(w)

base_tree.write("june_reconciled_partial.osm", encoding="utf-8", xml_declaration=True)
json.dump({str(wid): {"version": int(w.attrib["version"]), "timestamp": w.attrib["timestamp"], "changeset": int(w.attrib["changeset"]), "nodes": [int(nd.attrib["ref"]) for nd in w.findall("nd")], "tags": {t.attrib["k"]:t.attrib["v"] for t in w.findall("tag")}} for wid,w in selected_ways.items()}, open("selected_sibling_ways.json","w"), indent=2, ensure_ascii=False)
