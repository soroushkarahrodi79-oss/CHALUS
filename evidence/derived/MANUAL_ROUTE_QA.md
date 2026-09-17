# Manual route QA (desk review of route geometry and tags) — CORRECTED

**Correction (closeout audit):** this document previously claimed 12
distinct routes but tabulated only 11 rows — `west-nowshahr` was missing
entirely. That was a real coverage gap, not a restated total, and is
fixed below with the actual narrative data for that route (not
back-filled from assumption).

**Methodological limitation, stated directly:** reading a route's ordered
road-name/ref sequence for continuity and plausibility is a real check,
and it is the only kind of check performed here. It verifies that the OSM
tags describe a coherent, continuous road. **It does not independently
verify that the road was physically open to traffic on either historical
cutoff.** "PASS" below means "the tag sequence is coherent," not "physical
operational availability is confirmed" — see
`docs/GATE2AR_FINAL_REPORT.md` section D.

This is distinct from, and in addition to, the automated structural checks
in `manual_qa_stats.json` (renamed conceptually below — that file checks
graph-construction invariants: no off-major-class edges, no degenerate
edge lengths, path-identity verification). This document is a human
desk-review of the named road sequence each route actually follows,
produced from `src/route_narrative.py` (`evidence/derived/
route_narratives.json`: for each route, the ordered sequence of distinct
`(highway class, ref, name)` segments with cumulative distance, for both
January and June). **No satellite imagery was used or is used to refine
or second-guess the closure geometry — this review reads only the route's
own way tags and sequence**, per instruction.

There are 12 geometrically distinct routes (not 18): south has 3
destinations x 2 states (base, closure) = 6 distinct paths; east and west
each have 3 destinations x 1 distinct path (base = closure, verified by
path equality in `parity_18routes.json`) = 3 + 3 = 6. Total 12.

| Route | Reviewer decision | Observations |
|---|---|---|
| south-chalus base | **PASS** | Karaj ring road (کمربندی) -> Road 59 (جاده چالوس) continuously for ~125 km -> Tehran-North Freeway (ref 3) -> local Chalus streets. Continuous named sequence, no gaps, both dates. |
| south-nowshahr base | **PASS** | Same corridor as above to ~km 125, diverges onto Nowshahr streets. Continuous, both dates. |
| south-kelardasht base | **PASS** | Road 59 diverges toward Marzanabad-Kelardasht road; passes "تونل شماره دو" (tunnel) mid-route in the underlying way tags (not shown in the collapsed narrative but present in `route_qa_summary.txt` from the prior stage). Continuous, both dates. |
| south-chalus closure | **PASS** (tag-coherence only) | Karaj -> Amirkabir Tunnel (تونل امیرکبیر) -> Alborz freeway -> ref 14 (Shahid Hemmat/Zeynoddin) for ~45 km -> ref 54 -> ref 77 (Haraz) for ~90 km, passing the disputed Haraz location at approximately km 213. The modelled routes remain graph-continuous in both dates, but correspondence between the January segment ways and the June geometry remains unresolved and is not certified by this tag-sequence QA; see the final report section C. -> Amol local roads -> coastal ref 22 -> Chalus streets. Continuous both dates. Bridge ("پل انگتارود" at km 232.8, "پل ماشلک" at km 308.1) and tunnel transitions read as mid-route connections, not dead ends. |
| south-nowshahr closure | **PASS** | Same corridor as south-chalus closure to the coastal road, diverges onto Nowshahr streets. Continuous both dates. |
| south-kelardasht closure | **PASS** | Same Haraz corridor as above, continues past Chalus/Nowshahr split toward Kelardasht via ref 59 return leg. Continuous both dates. |
| east-chalus (base = closure) | **PASS** | Amol local streets -> ref 22 coastal road for ~65 km -> Chalus streets. One plaza rename between dates ("میدان شهدای ششم بهمن" -> a differently-tagged square name at the same km marker) — a tag edit, not a topology change. Continuous both dates. |
| east-nowshahr (base = closure) | **PASS** | Same corridor, diverges to Nowshahr streets. Continuous both dates. |
| east-kelardasht (base = closure) | **PASS** | Same corridor, continues on ref 59 toward Kelardasht. Continuous both dates. This route is also the one carrying the 7 additional route-relevant restriction relations found near Amol (`extra_relations_check.json`) — reviewed, no violation, turns are consistent with the named junction pattern (a cluster of `no_u_turn` relations at what reads as a signalized intersection, all pre-dating January). |
| west-chalus (base = closure) | **PASS** (tag-coherence only) | Ramsar local streets -> ref 22 coastal road -> Chalus streets. Continuous both dates. |
| west-nowshahr (base = closure) | **PASS** (tag-coherence only) | *Previously missing from this table — added here from `route_narratives.json`, not backfilled from assumption.* Ramsar -> coastal ref 22 for ~75 km -> local Nowshahr streets ("امام خمینی", "شهید بهشتی", "بلوار هفده شهریور"). One local square renamed between dates ("میدان وادی" -> "میدان شهدا", same km marker as the west-kelardasht row below) and the same added intermediate node pair at km ~43.2 (`?@43.2`/`?@43.24`) between dates — consistent with the identical shared corridor segment noted for west-kelardasht. Continuous, both dates. |
| west-kelardasht (base = closure) | **PASS** (tag-coherence only) | Ramsar -> coastal ref 22 -> diverges inland via "عباس‌آباد - کلاردشت" named road for the final ~34 km (unreferenced local road, consistent with `dominant_ref=None` reported earlier — a real property of this rural road, not a data gap). One local square renamed between dates ("میدان وادی" -> "میدان شهدا") and one added intermediate node pair at km 43.2 (`?@43.2`) between dates — read as a minor June-side re-digitization of an existing junction, not a new road. Continuous both dates. |

**No FAIL, no ABSTAIN, across all 12 routes** (corrected count — the prior
version tabulated 11). Every route reads as a continuous, named,
plausible road sequence in both January and June, with bridges and
tunnels appearing as through-connections rather than endpoints, and the
handful of Jan/June differences all resolving to plaza renames or minor
re-digitization rather than a structural break.

This desk review does not and cannot certify that no OSM mapping error
exists anywhere on these roads, and — restated per the closeout audit —
it does not certify that any of these roads was physically open to
traffic on either historical cutoff. It certifies only that the named
sequence, distance progression, and bridge/tunnel placement in the OSM
tags themselves are internally coherent to a reviewer reading them
directly. That is a real check with real value; it is not independent
operational verification, and this document does not claim to be.
