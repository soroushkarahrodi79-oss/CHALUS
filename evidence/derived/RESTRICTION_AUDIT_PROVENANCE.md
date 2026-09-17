# Restriction audit — provenance and completeness (PARTIAL)

## Source of the 31 relation-history inputs

`osm_history/restrictions/*.osm` (31 files, not committed to this
repository — see below) each contain the **full version history** of one
OSM relation, in the format produced by the OpenStreetMap API's history
endpoint (`generator="openstreetmap-cgimap 2.1.0"`, matching
`https://api.openstreetmap.org/api/0.6/relation/{id}/history`). Each file
was inherited from the earlier `CHALUS_Gate2AR_CORE` handoff bundle
(`history/restrictions/`); this session did not fetch them and cannot
independently confirm when or how the original 31-relation candidate list
was selected.

Relation IDs covered:
```
8266216 8266235 8266237 8306621 8331778 8834431 9227377 9227378 9227916
9227917 9227918 9227919 9227920 9227921 9227922 9296539 9307869 9310052
9638889 9713712 9713713 11131468 11131469 12247737 13487373 17421383
17975498 17975499 18971245 18971246 18995254
```

Fragment SHA-256 hashes (all 31 files): see
`evidence/derived/restriction_fragment_hashes.txt`, committed alongside
this note.

## Why this audit is classified PARTIAL, not CONFIRMED

This session can verify, and did verify:
- every one of these 31 relations resolves a specific version at each of
  the two frozen cutoffs (January `2024-01-01T21:21:15Z`, June
  `2024-06-12T20:29:59Z`), deterministically, on two independent runs;
- every relation whose member ways intersect any of the 18 computed
  route-states (9 pairs x base/closure) was checked for a routing
  violation, and none was found, at either cutoff.

This session **cannot** independently verify that these 31 relations are
the *complete* set of restriction relations that could apply to the 156,669
route-relevant ways in the frozen bounding box, at either cutoff. Doing so
would require either a live Overpass historical query (blocked — see
`data/README.md`, network egress policy) or the full January/June PBF's
own relation stream cross-referenced against every route way ID with a
purpose-built extraction pass this session has not run.

**A partial completeness check was performed:** every route-relevant way
ID actually used by any of the 18 route-states (`evidence/derived/
parity_18routes.json`) was checked against these 31 relations' member-way
lists; none of the 18 route-states touches a member way outside this set
by observation and the routing code identifies contacts automatically
during the check — so no contact was silently missed *within this
31-relation set*. What is not verified is whether a 32nd relevant relation
exists outside this inherited set.

**Classification: PARTIAL.** Zero violations found is accurate and
reproducible; "zero restriction relations of any kind apply beyond these
31" is not independently established.

## Preferred remediation not available in this session

The instruction's preference — deriving January restrictions directly
from the recovered January PBF — is directly actionable: the January PBF
contains 94,224 relations in total, and turn-restriction relations
(`type=restriction`) can be extracted directly with `osmium`, filtered to
January-cutoff validity by relation version/timestamp within that single
file, with no external fetch required. This is a real gap in this
session's work, not merely a documentation gap, and is named as pending
follow-up rather than silently left undone. The June side has no
equivalent full-history source in this session (only the route-bounded
partial extract), so its restriction relations remain dependent on the
externally-supplied 31-file set regardless.
