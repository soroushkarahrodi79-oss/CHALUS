# Geometric verification of one ledger "parent/child" claim

The change ledger (`evidence/Gate2A_Historical_Change_Ledger.csv`) labels
ways `924025918`/`924025921` (January, deleted before June) as "replaced by
1270179067,1287287400,1287287401" (June). Per audit instruction: this
label is not accepted at face value — checked by direct coordinate lookup
in both source files.

| January way | endpoint node | lat, lon |
|---|---|---|
| 924025918/921 | 8577451368 | 35.8396924, 52.0617923 |
| 924025918/921 | 8577451369 | 35.8390314, 52.063289 |
| 924025918/921 | 8577451370 | 35.8386922, 52.0639944 |

| June replacement way | node | lat, lon |
|---|---|---|
| 1270179067/1287287400/1287287401 | (8 boundary nodes checked) | see raw data below |

Minimum haversine distance from each January endpoint to the nearest June
replacement-way node:

- 508.1 m
- 649.0 m
- 719.5 m

**Finding: these are not the same location.** The ledger's "replaced by"
label is not geometrically confirmed at the individual-way level by this
check. This is recorded as an open verification gap, not resolved by
asserting the ledger's own text.

**What this does and does not affect:** these two January ways are a
short (2-node each) segment pair on the closure-scenario southern
corridor. The aggregate effect on route distance is +0.036 km over a
316.9 km route (0.011%), and the dominant corridor (ref 77, Haraz) is
identical with or without this specific pair resolved. This gap does not
change the qualitative result and does not create a decisive alternative
corridor. It is flagged in the Haraz/Tehran-North table (section C of the
final report) as `UNCERTAIN`, per the audit's own classification scheme,
rather than being marked `CONFIRMED_OPERATIONAL`.

Raw node coordinates and the comparison script output are reproducible
from `src/final_evidence.py` and the underlying source files; this note
records the result for audit purposes without requiring the raw PBF/OSM
files in the repository.
