# GATE 2A-R — FINAL CLOSEOUT REPORT (NO-GO)

Branch: `research/gate2ar-paired-reconstruction`, subsequently merged to
`main` via PR #1 for archival consolidation of the audit trail only. This
merge does not reopen Gate 2A-R, authorize Gate 2B, or alter the verdict
below.

**GATE 2A-R CLOSED — NO-GO. EO BLOCKED. GATE 2B UNAUTHORIZED.**

**This version withdraws the GO verdict issued in commit `5ff8820`.** That
report claimed the Haraz topology question was "resolved... proven by
shared node IDs." On re-examination against this repository's own
committed evidence (`evidence/derived/haraz_geometry_resolution.json`),
that claim was overstated: only one node ID (`8577451368`) is actually
shared between the disputed January ways and way `924025920`'s June
geometry. The other two nodes of the disputed segment (`8577451369`,
`8577451370`) do not reappear anywhere in that way's June node list. One
shared junction node establishes network contact, not proof that the
whole segment was absorbed. This report does not attempt a further rescue
of that finding — no new data was acquired and no additional geometric
analysis was performed to try to close the gap. Per the frozen rule in
`docs/GATE2AR_PROTOCOL_AMENDMENT.md`, an unresolved Haraz topology
correspondence triggers NO-GO, without regard to how small the measured
distance effect is.

## Provenance statement (unchanged)

- Strict Gate 2A was impossible because Gate 1's original numeric outputs
  were never preserved anywhere this session could reach.
- The original January binary source was recovered exactly by recorded
  hash (202,051,103 bytes, SHA-256
  `1ce7fe2c2d28973f692699f5ab8b815e12099b3efc2a6e66fb25e2030e471e4c`).
- Every January route figure is a fresh, reproducible recomputation from
  the recovered source — not a recovered Gate 1 output.
- All distances are **MODELLED FROM PAIRED RETROSPECTIVE HISTORICAL
  NETWORKS.**

---

## A. Gate 2A-R Verdict

**NO-GO.**

Gate 2A-R found extremely stable modelled distances and corridors between
the recovered January reference and the route-bounded June
reconstruction. However, the pre-registered historical-verification
standard was not met: Haraz segment correspondence remains incompletely
demonstrated, June turn-restriction completeness is partial, and decisive
motorway operational status lacks independent confirmation. Because the
protocol required NO-GO for unresolved Haraz topology or restriction
ambiguity, the study stops before EO processing.

This is not a verdict that the underlying research question is
unsound, and it does not invalidate the distance/corridor computations
below — it states that those computations are insufficient, on their
own, to support the pre-registered historical-verification claim Gate
2A-R exists to make.

## B. Historical Change Ledger

`evidence/Gate2A_Historical_Change_Ledger.csv`, 130 rows, unchanged. Its
"parent_child" field remains unreliable on its own — its specific claim
for ways 924025918/921 was checked and found to point to the wrong
location (section C). No ledger classification is treated as confirmed
without independent verification, and one specific verification attempt
did not fully succeed.

## C. Haraz Resolution — UNRESOLVED

**Disputed claim:** the ledger states January ways `924025918` (nodes
`8577451368 -> 8577451369`) and `924025921` (nodes
`8577451369 -> 8577451370`, tagged `bridge=yes`) — both `ref=77`, absent
from June — were "replaced by `1270179067,1287287400,1287287401`."

**What was checked:** those specific claimed replacement ways are
630–882 m from the disputed segment's actual location — the ledger's
citation is wrong. An independent spatial search found three nearer June
candidates, and way `924025920`'s June geometry begins:
`8577451368 -> 8577451371 -> ...`

**What this does and does not show:** node `8577451368` is shared between
disputed way `924025918` and way `924025920`'s June version. That is
real, and it is recorded. It establishes that the two ways meet at a
common junction node — **network contact, not geometric absorption of
the two January segments.** The committed evidence does not contain:

- a full polyline-overlap or Hausdorff-distance comparison between the
  disputed ways and way `924025920`'s complete geometry;
- changeset history showing the specific edit that altered way
  `924025920` and what happened to it;
- any account of what became of nodes `8577451369` and `8577451370` —
  they do not appear in way `924025920`'s June node list at all, and no
  other June way was checked for them beyond the 400 m spatial search
  already performed.

The prior report's language — "direct proof of physical continuity,"
"absorbed into the already-existing, larger way `924025920`" — is not
supported by what was actually verified. A single shared endpoint node is
consistent with absorption, but equally consistent with the two original
segments having been deleted and node `8577451368` simply continuing to
serve as a junction for whatever replaced them nearby. Both are plausible
readings of the same evidence; this report does not pick one.

**Verdict on this item: UNRESOLVED.** Per the frozen rule — *"Any
unresolved Haraz topology... triggers NO-GO"* — this is not treated as a
minor residual caveat because its distance effect is small (0.011% of the
route). The rule does not carry a materiality exception, and this report
does not read one into it.

## D. Tehran–North Historical Status — NOT INDEPENDENTLY VERIFIED

Kept separate from section C. This report has no official or
contemporaneous non-OSM evidence establishing that every decisive
Tehran–North or Haraz section actually used by a route was open to
traffic by 12 June 2024. Every status claim in this repository about
these sections reflects **OSM object presence and edit-timestamp state
only** — it supports a modelled historical representation; it does not
confirm physical opening to traffic. All 271 route-relevant ways in
`evidence/derived/haraz_tehran_north_table.json` remain classified no
higher than `SUPPORTED_OPERATIONAL` (OSM-attested), and none is claimed
`CONFIRMED_OPERATIONAL`.

## E. Frozen Historical Network Specification

Unchanged — no gateway, destination, closure geometry, distance
weighting, road filter, sensitivity design, or routing parameter was
altered in this or the prior closeout audit. Gateways: south/Karaj
(`31086990`), east/Amol (`6208746864`), west/Ramsar (`8595307908`).
Destinations: Chalus (`1375231380`), Nowshahr (`4998048119`), Kelardasht
(`3323917713`). Cutoffs: January `2024-01-01T21:21:15Z`, June
`2024-06-12T20:29:59Z`. Closure: Darband node `3294759340`.

## F. January Reference vs June Historical Comparison — supported finding, insufficient for the pre-registered claim

| Pair | Jan base km | Jun base km | % diff | Jan closure km | Jun closure km | % diff | ΔD (closure − base), Jun |
|---|---|---|---|---|---|---|---|
| south-chalus | 151.239 | 151.229 | -0.006% | 316.961 | 316.925 | -0.011% | 165.696 km |
| south-nowshahr | 158.724 | 158.714 | -0.006% | 311.029 | 310.994 | -0.011% | 152.280 km |
| south-kelardasht | 145.681 | 145.671 | -0.007% | 364.321 | 364.286 | -0.010% | 218.615 km |
| east-chalus | 99.571 | 99.568 | -0.003% | 99.571 | 99.568 | -0.003% | 0.000 km |
| east-nowshahr | 93.639 | 93.637 | -0.003% | 93.639 | 93.637 | -0.003% | 0.000 km |
| east-kelardasht | 146.931 | 146.928 | -0.002% | 146.931 | 146.928 | -0.002% | 0.000 km |
| west-chalus | 79.402 | 79.406 | +0.005% | 79.402 | 79.406 | +0.005% | 0.000 km |
| west-nowshahr | 87.036 | 87.040 | +0.004% | 87.036 | 87.040 | +0.004% | 0.000 km |
| west-kelardasht | 84.202 | 84.206 | +0.004% | 84.202 | 84.206 | +0.004% | 0.000 km |

Maximum absolute January-vs-June difference across all 18 route-states:
**0.011%.** This number is not disputed and is not invalidated by
sections C/D above — it is a real, reproducible property of the two
computed graphs. What is insufficient is treating this stability, by
itself, as satisfying the pre-registered historical-verification
standard while Haraz topology and restriction completeness remain open.

## G. Reconciled Baseline Table (supported finding)

| Gateway | Destination | Jan km | Jun km | Connectivity | Dominant corridor |
|---|---|---|---|---|---|
| south | chalus | 151.239 | 151.229 | CONNECTED | ref 59 (Chalus Road) |
| south | nowshahr | 158.724 | 158.714 | CONNECTED | ref 59 |
| south | kelardasht | 145.681 | 145.671 | CONNECTED | ref 59 |
| east | chalus | 99.571 | 99.568 | CONNECTED | ref 22 |
| east | nowshahr | 93.639 | 93.637 | CONNECTED | ref 22 |
| east | kelardasht | 146.931 | 146.928 | CONNECTED | ref 22 |
| west | chalus | 79.402 | 79.406 | CONNECTED | ref 22 |
| west | nowshahr | 87.036 | 87.040 | CONNECTED | ref 22 |
| west | kelardasht | 84.202 | 84.206 | CONNECTED | ref 22 / unref'd local roads |

## H. Reconciled Closure Table (supported finding)

| Gateway | Destination | Jan km | Jun km | Connectivity | Dominant corridor | Path identical to baseline? |
|---|---|---|---|---|---|---|
| south | chalus | 316.961 | 316.925 | CONNECTED WITH DETOUR | ref 77 (Haraz) — **but see section C: this corridor's own topology is unresolved** | No, both dates |
| south | nowshahr | 311.029 | 310.994 | CONNECTED WITH DETOUR | ref 77 — see section C | No, both dates |
| south | kelardasht | 364.321 | 364.286 | CONNECTED WITH DETOUR | ref 77 — see section C | No, both dates |
| east | chalus | 99.571 | 99.568 | CONNECTED | ref 22 | Yes — verified by node-path equality |
| east | nowshahr | 93.639 | 93.637 | CONNECTED | ref 22 | Yes |
| east | kelardasht | 146.931 | 146.928 | CONNECTED | ref 22 | Yes |
| west | chalus | 79.402 | 79.406 | CONNECTED | ref 22 | Yes |
| west | nowshahr | 87.036 | 87.040 | CONNECTED | ref 22 | Yes |
| west | kelardasht | 84.202 | 84.206 | CONNECTED | (unref'd) | Yes |

## I. Reconciled Detour Table (supported finding)

| Gateway | Destination | Jan DR | Jun DR |
|---|---|---|---|
| south | chalus | 2.096 | 2.096 |
| south | nowshahr | 1.960 | 1.959 |
| south | kelardasht | 2.501 | 2.501 |
| east | chalus | 1.000 | 1.000 |
| east | nowshahr | 1.000 | 1.000 |
| east | kelardasht | 1.000 | 1.000 |
| west | chalus | 1.000 | 1.000 |
| west | nowshahr | 1.000 | 1.000 |
| west | kelardasht | 1.000 | 1.000 |

## J. Gateway Sensitivity (supported finding)

Bidirectional test at all three gateways
(`src/gateway_sensitivity_bidirectional.py`, run twice, byte-identical):
connectivity classification does not flip under any tested shift, either
direction, either date. Detour ratios range 1.918–2.777 across all south
shifts, consistent with the unshifted values. **Gateway sensitivity: LOW**
— this finding stands; it is not affected by the Haraz or restriction
findings above, since it concerns node placement, not the disputed
segment's own topology.

## K. Destination-Node Sensitivity (supported finding)

Alternate destination nodes shift detour ratios by at most ~0.03–0.13
without changing which pairs detour materially. **Present but
non-determining.** This finding stands.

## L. Manual Route QA — INCOMPLETE, AND METHODOLOGICALLY LIMITED

Two separate problems with the prior version, both corrected here:

1. **Coverage gap.** `evidence/derived/MANUAL_ROUTE_QA.md` claimed 12
   distinct routes but tabulated only 11 rows — `west-nowshahr` was
   missing entirely from the table. This was a real omission, not a
   restated total. The file is corrected in this commit to add the
   missing row; it was not independently re-derived beyond confirming
   its route is geometrically identical to `west-chalus`/`west-kelardasht`
   per the same base=closure identity already established for the west
   gateway (`evidence/derived/parity_18routes.json`).

2. **What tag-sequence desk review can and cannot establish.** Reading a
   route's ordered road-name/ref sequence for continuity, plausible
   bridge/tunnel placement, and absence of service-road misuse is a real
   check and it passed on every route reviewed. It is **not** independent
   verification of physical operational availability at either historical
   cutoff — it verifies that the OSM tags tell a coherent story, not that
   the road existed and was open in the physical world on the dates
   claimed. This report states that limitation directly rather than
   letting "manual QA: PASS" imply more than a tag-level review can
   support.

## M. Updated Evidence Ledger

| Evidence class | Status |
|---|---|
| Confirmed disruption (Darband closure) | CONFIRMED (unchanged) |
| Historical network, January | CONFIRMED — recovered, validated, recomputed twice deterministically |
| Historical network, June | CONFIRMED (unchanged) |
| Nine-pair / 18-route-state distance parity | CONFIRMED as a numeric result — **insufficient by itself** for the historical-verification standard while C and D below remain open |
| Haraz segment correspondence | **UNRESOLVED** — network contact at one shared node demonstrated; full geometric/changeset correspondence not demonstrated |
| Turn restrictions, January | CONFIRMED for 34 relations, zero violations, reproduced twice |
| Turn restrictions, June | **PARTIAL** — 26 externally-supplied relations checked, zero violations found among them; completeness beyond that inherited set not established |
| Tehran-North / Haraz operational status | **NOT INDEPENDENTLY VERIFIED** — OSM-attested only (`SUPPORTED_OPERATIONAL`); no official or contemporaneous non-OSM source obtained |
| Gateway sensitivity | CONFIRMED — low, bidirectional, all three gateways |
| Destination-node sensitivity | CONFIRMED — present, non-determining |
| Manual route QA | **INCOMPLETE** — one route (west-nowshahr) was missing from the record; and the method itself (tag-sequence desk review) does not independently verify physical operational availability |
| EO/tourism/travel-time claims | ABSTAIN — out of scope |

## N. Triggered Kill Tests

- **TRIGGERED — Haraz topology unresolved.** Per the frozen rule, this
  alone is sufficient for NO-GO, independent of every other finding in
  this report.
- **TRIGGERED (contributing) — June restriction completeness partial.**
  Zero violations among an incomplete candidate set does not establish
  the absence of a relevant unobserved restriction; the frozen rule
  treats unresolved restriction ambiguity as a NO-GO condition, not a
  footnote.
- **Not independently sufficient to trigger on its own, but recorded as a
  further gap:** decisive Tehran–North/Haraz motorway sections lack
  independent (non-OSM) operational confirmation.
- **Supported, not in dispute:** source-provenance recovery, determinism,
  the 0.011% maximum January/June distance difference, corridor labels as
  computed, gateway/destination sensitivity results. These are preserved
  as findings. They are not treated as invalid — they are treated as
  insufficient, on their own, to clear the pre-registered
  historical-verification bar.

---

## Closing statement

**GATE 2A-R CLOSED — NO-GO. EO BLOCKED. GATE 2B UNAUTHORIZED.**

Gate 2A-R found extremely stable modelled distances and corridors between
the recovered January reference and the route-bounded June
reconstruction. However, the pre-registered historical-verification
standard was not met: Haraz segment correspondence remains incompletely
demonstrated, June turn-restriction completeness is partial, and decisive
motorway operational status lacks independent confirmation. Because the
protocol required NO-GO for unresolved Haraz topology or restriction
ambiguity, the study stops before EO processing.

**Preserved as supported findings, not invalidated:**
- recovered January source integrity (exact hash match, validated,
  deterministic recomputation);
- deterministic routing (every script re-run, byte-identical);
- maximum January–June distance difference of 0.011%;
- stable dominant corridors as computed;
- southern closure-scenario detours of 152.3–218.6 km;
- gateway/destination sensitivity results (low, bidirectional).

These findings are not called invalid. They are insufficient, on their
own, for the pre-registered historical-verification claim this gate
exists to make.

**This does not authorize:**
- `GO_TO_GATE_2B` — remains unauthorized.
- Sentinel-1/2 or any EO processing — remains blocked.
- any further research phase. (The branch was subsequently merged to
  `main` via PR #1 purely to consolidate the audit trail on the default
  branch — a housekeeping action, not a reauthorization of anything
  listed above.)

No further computation, data acquisition, or rescue analysis was
performed to close the Haraz or restriction-completeness gaps in
producing this closeout. This session stops here.
