# GATE 2A-R — FINAL CLOSEOUT REPORT

Branch: `research/gate2ar-paired-reconstruction`. Not merged to `main`.

## Provenance statement

- Strict Gate 2A was impossible because Gate 1's original numeric outputs
  (distances, routes, connectivity classifications) were never preserved
  anywhere this session could reach — only Gate 1's specification document
  was.
- The original January binary source was recovered exactly by recorded
  hash: an 8-fragment upload reassembled to 202,051,103 bytes with SHA-256
  `1ce7fe2c2d28973f692699f5ab8b815e12099b3efc2a6e66fb25e2030e471e4c`,
  matching the hash orphaned since the start of this exercise. A separate,
  earlier 78,241,792-byte transfer of the same nominal file was corrupted
  (truncated after the node section) and is preserved unchanged in
  `docs/GATE2AR_RUN_LOG.md` as historical evidence, not deleted.
- Every January route figure in this report is a **fresh, reproducible
  recomputation from the recovered original source** — not a recovered
  Gate 1 output. Two independent runs of the routing code against this
  source produced byte-identical results.
- All distances in this report are **MODELLED FROM PAIRED RETROSPECTIVE
  HISTORICAL NETWORKS.** No travel time, traffic, EO-derived exposure, or
  tourism-impact quantity appears anywhere in this report.

---

## A. Gate 2A-R Verdict

**GO** — bounded strictly to the frozen scientific question below. This is
not GO_TO_GATE_2B; see the closing section.

All formal stability rules in `docs/GATE2AR_PROTOCOL_AMENDMENT.md` were
checked directly, not assumed:

1. All nine connectivity classifications: stable (CONNECTED, both dates).
2. No dominant-corridor change from unresolved topology: none found.
3. Distance difference ≤2% on every pair: actual maximum is 0.011%.
4. Gateway sensitivity: low (see section J).
5. Destination-node sensitivity: does not determine the result (section K).
6. Manual QA: passed on every route, both dates (section L).
7. Deterministic from frozen environment and inputs: confirmed by two
   independent runs, byte-identical, for routing, restriction audit, and
   QA statistics.

One residual item is recorded rather than smoothed over: a specific
"parent/child" way-replacement claim in the change ledger (two short
January way segments vs. three June replacement ways) does not hold up
under direct coordinate-level geometric verification — the claimed
correspondence points are 500-720 m apart (`evidence/derived/
parent_child_geometric_check.md`). This affects a segment whose aggregate
contribution to route length is 0.011% of a 317 km route and does not
change the dominant corridor. It is classified `UNCERTAIN` in section C
and does **not** create a decisive alternative corridor, so per the
protocol's own rule it does not convert this into a NO-GO — but it is not
resolved either, and is named as a limitation.

## B. Historical Change Ledger

`evidence/Gate2A_Historical_Change_Ledger.csv`, 130 rows, unchanged from
the earlier stage. Classification breakdown: `A_NON_MATERIAL` 80,
`C_TOPOLOGY` 34, `B_ROUTING_ATTRIBUTE` 14, `D_HISTORICAL_STATUS` 2.
Cross-referenced in section C below against actual route way-lists from
both dates (not merely cited by category).

## C. Haraz Resolution / Tehran–North Historical Status

Route-relevant table only (not general road history): every way tagged
`ref=77` (Haraz), `ref=3` (Tehran–North Freeway), or `ref=14` (Shahid
Hemmat / Zeynoddin connectors feeding the freeway) that is actually used
by any of the 18 January or June routes. Full machine-readable table:
`evidence/derived/haraz_tehran_north_table.json` (271 unique way IDs).

| Way ID(s) | Ref | Section | Jan status | 12-Jun status | Classification | Action |
|---|---|---|---|---|---|---|
| 262 of 271 ways | 77/3/14 | Haraz, Tehran–North, connectors | present, version ≤ Jan cutoff | present, unchanged or later non-material edit | `CONFIRMED_OPERATIONAL` | none — no route effect |
| 924025918, 924025921 | 77 | Haraz, short 2-node segments | present (v4/v5) | deleted before June (per ledger) | `UNCERTAIN` | flagged; see geometric check below |
| 1254832046, 1254832048, 1270177767/68/70, 1270179067, 1280188385, 1287287400, 1287287401 | 77/14 | claimed replacements for the above | absent (`jan_v ABSENT`) | created v1-2, all ≤ 12 June 2024 | `SUPPORTED_OPERATIONAL` (existed by cutoff; unconfirmed as literal geometric successor) | flagged; see geometric check below |

**Geometric verification result** (`evidence/derived/
parent_child_geometric_check.md`): the claimed January→June replacement
correspondence for the way pair above does not hold at the coordinate
level — nearest-point distances of 508–720 m were measured directly from
both source files, not assumed from the ledger's text. This is the one
open item in this report.

**Explicit finding on network evolution:** across all 271 route-relevant
Haraz/Tehran–North/connector ways, only 9 (created after January, all
dated on or before 12 June 2024) and 2 (deleted after January, before
June) show any topology change. No infrastructure in this set was created
after the frozen 12 June 2024 cutoff — the latest creation timestamp found
is `2024-06-08T08:11:11Z`, before the cutoff. **The January representation
neither creates nor removes a usable corridor relative to 12 June 2024;
it differs only in exactly which OSM way IDs represent an already-existing
alignment on a short sub-segment**, and that difference does not change
route distance beyond 0.011% or the dominant-corridor classification. No
`UNCERTAIN` section here produces a decisive southern alternative.

## D. (folded into C above, per the route-relevant-only framing)

## E. Frozen Historical Network Specification

- Gateways: south/Karaj (node `31086990`), east/Amol (node `6208746864`),
  west/Ramsar (node `8595307908`).
- Destinations: Chalus (`1375231380`), Nowshahr (`4998048119`), Kelardasht
  (`3323917713`). All resolve to real coordinates in both January and June
  graphs; unchanged from the frozen specification.
- Event chronology: 13 June 2024 ~20:30 local through documented reopening
  16 June 2024 afternoon (per the amendment; supersedes the earlier
  13–14 June wording, which is not silently retained).
- Historical network cutoffs: January `2024-01-01T21:21:15Z` (Geofabrik
  replication state), June `2024-06-12T23:59:59` Iran Standard Time
  (`2024-06-12T20:29:59Z` UTC).
- Closure representation: contiguous directed edges incident to Darband
  node `3294759340`, within the previously supported bounded segment.
  Present and resolvable in both graphs.
- Road filter: motorway/trunk/primary/secondary (+ links), Routes 230/240
  excluded, distance-only weighting, `oneway` and roundabout direction
  respected. Unchanged from prior stages — no routing parameter was
  altered in this audit.

## F. January Reference vs June Historical Comparison

| Pair | Jan base km | Jun base km | % diff | Jan closure km | Jun closure km | % diff |
|---|---|---|---|---|---|---|
| south-chalus | 151.239 | 151.229 | -0.006% | 316.961 | 316.925 | -0.011% |
| south-nowshahr | 158.724 | 158.714 | -0.006% | 311.029 | 310.994 | -0.011% |
| south-kelardasht | 145.681 | 145.671 | -0.007% | 364.321 | 364.286 | -0.010% |
| east-chalus | 99.571 | 99.568 | -0.003% | 99.571 | 99.568 | -0.003% |
| east-nowshahr | 93.639 | 93.637 | -0.003% | 93.639 | 93.637 | -0.003% |
| east-kelardasht | 146.931 | 146.928 | -0.002% | 146.931 | 146.928 | -0.002% |
| west-chalus | 79.402 | 79.406 | +0.005% | 79.402 | 79.406 | +0.005% |
| west-nowshahr | 87.036 | 87.040 | +0.004% | 87.036 | 87.040 | +0.004% |
| west-kelardasht | 84.202 | 84.206 | +0.004% | 84.202 | 84.206 | +0.004% |

Maximum absolute difference across all 18 route-states: **0.011%.**

## G. Reconciled Baseline Table

| Gateway | Destination | Jan km | Jun km | Dominant corridor (both dates) |
|---|---|---|---|---|
| south | chalus | 151.239 | 151.229 | ref 59 (Chalus Road) |
| south | nowshahr | 158.724 | 158.714 | ref 59 |
| south | kelardasht | 145.681 | 145.671 | ref 59 |
| east | chalus | 99.571 | 99.568 | ref 22 |
| east | nowshahr | 93.639 | 93.637 | ref 22 |
| east | kelardasht | 146.931 | 146.928 | ref 22 |
| west | chalus | 79.402 | 79.406 | ref 22 |
| west | nowshahr | 87.036 | 87.040 | ref 22 |
| west | kelardasht | 84.202 | 84.206 | ref 22 / unref'd local roads (Kelardasht) |

## H. Reconciled Closure Table

| Gateway | Destination | Jan km | Jun km | Dominant corridor (both dates) | Path identical to baseline? |
|---|---|---|---|---|---|
| south | chalus | 316.961 | 316.925 | ref 77 (Haraz) | No (both dates) |
| south | nowshahr | 311.029 | 310.994 | ref 77 | No (both dates) |
| south | kelardasht | 364.321 | 364.286 | ref 77 | No (both dates) |
| east | chalus | 99.571 | 99.568 | ref 22 | **Yes** — verified by direct node-path equality, both dates |
| east | nowshahr | 93.639 | 93.637 | ref 22 | **Yes**, both dates |
| east | kelardasht | 146.931 | 146.928 | ref 22 | **Yes**, both dates |
| west | chalus | 79.402 | 79.406 | ref 22 | **Yes**, both dates |
| west | nowshahr | 87.036 | 87.040 | ref 22 | **Yes**, both dates |
| west | kelardasht | 84.202 | 84.206 | (unref'd) | **Yes**, both dates |

East/west closure-equals-baseline identity was verified by comparing full
node-path sequences, not inferred from equal distance
(`evidence/derived/parity_18routes.json`, `jan_closure_equals_base` /
`jun_closure_equals_base` fields — `true` for all six east/west pairs,
`false` for all three south pairs, both dates).

## I. Reconciled Detour Table

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

## J. Gateway Sensitivity

Computed for January (`src/compute_jan_sensitivity_union.py`) at gateway
shifts of +0/+5/+10 km along the southern approach, and at the fixed east/
west gateway nodes, then compared to the previously supplied June
sensitivity figures. Detour ratios track within 0.001–0.004 across every
shift for the south gateway (e.g. `south_10-kelardasht`: Jan 2.776, Jun
2.775). No shift changes which pairs detour materially (south only) or the
dominant corridor. **Gateway sensitivity: low, stable across dates.**

## K. Destination-Node Sensitivity

Alternate destination nodes (`chalus_alt`, `nowshahr_alt`, `kelardasht_alt`)
computed for both dates. Detour ratios differ from the primary node by at
most ~0.13 (e.g. south-kelardasht 2.501 primary vs 2.532 alt) but the
qualitative pattern (south detours materially, east/west do not) is
unchanged under either node choice, in both January and June.
**Destination-node sensitivity: present but does not determine the
substantive result.**

## L. Manual Route QA

Full statistics: `evidence/derived/manual_qa_stats.json`. For every one of
the 18 route-states (9 pairs x base/closure), both dates:

| Check | Result (all 18 route-states, both dates) |
|---|---|
| Follows real continuous roads (graph-connected shortest path) | PASS |
| No disconnected geometry jump | PASS — shortest-path construction guarantees edge continuity; no exception raised on any of 36 route computations (18 states x 2 dates) |
| One-way structure respected | PASS — enforced structurally by `truthy_oneway()` at graph-build time; no route uses a reverse-only edge |
| No improper private/service-road use | PASS — `off_major_classes_present` is `[]` for every route-state; only motorway/trunk/primary/secondary (+links) appear |
| No mapping-error shortcut | PASS — minimum edge length across all routes is 0.09 m (a real micro-segment at an intersection, not a zero-length artifact); maximum is 2.05 km (a single long freeway way, not an implausible jump) |
| Bridges/tunnels connect topologically | PASS — no `InvalidLocationError` or broken chain encountered building any route; way tags for tunnel sections (e.g. `تونل جاده هراز`, `تونل وانا`) appear mid-route, not as dead ends |
| No infrastructure unavailable at the applicable date | PASS for 269/271 route-relevant Haraz/Tehran-North ways (section C); `UNCERTAIN` for the 2+9 ways in the one flagged reconciliation, not `FAIL` — no route uses infrastructure created after its own cutoff |
| Physical corridor classification correct | PASS — dominant ref matches the named corridor (59=Chalus Road, 77=Haraz, 22=coastal/Amol) in every case |

**Verdict per route-state: PASS**, with one **ABSTAIN-on-a-sub-segment**
(the flagged 924025918/921 reconciliation) rather than a clean PASS on
that specific short segment. No route-state is FAIL.

This QA is software-assisted structural review (edge/way/ref sequence
inspection against known corridor names and classes), not visual
satellite-imagery inspection. That distinction is stated rather than
implied.

## M. Updated Evidence Ledger

| Evidence class | Status |
|---|---|
| Confirmed disruption (Darband closure) | CONFIRMED (prior stage, unchanged) |
| Historical network, January | CONFIRMED — recovered exact source, validated, recomputed twice deterministically |
| Historical network, June | CONFIRMED (prior stage, unchanged) |
| Nine-pair parity (18 route-states) | CONFIRMED for 269/271 route-relevant ways; UNCERTAIN for the 2+9-way reconciliation noted in section C |
| Turn restrictions, both dates | CONFIRMED — 0 violations, 25 (Jan) / 26 (Jun) relations checked, deterministic across two runs |
| Gateway/destination sensitivity | CONFIRMED — low, stable |
| Manual route QA | CONFIRMED — PASS on all 18 route-states, one flagged sub-segment |
| EO/tourism/travel-time claims | ABSTAIN — out of scope, not evaluated, not claimed |

## N. Triggered or Nearly Triggered Kill Tests

- **Nearly triggered, did not trigger:** the parent/child geometric check
  (section C). Per the amendment's own rule, an `UNCERTAIN` classification
  only triggers NO-GO if it creates a decisive alternative corridor. It
  does not (same corridor, 0.011% distance effect) — recorded as a
  limitation, not a failure.
- **Not triggered:** source-provenance gate (January source recovered and
  validated), restriction-violation gate (zero violations either date),
  2% stability rule (max 0.011%), gateway/destination sensitivity gate
  (low both), manual QA gate (no FAIL).
- **Structural asymmetry (June route-bounded vs January full-envelope)**
  remains a recorded limitation, tested by Method B parity rather than
  resolved by acquiring a matched complete-envelope June extract (which
  this session does not have). The test passed, but this is evidence of
  no observed problem, not proof no problem exists.

---

## Closing statement

This report's verdict is **GO on historical-network stability only**:
the nine gateway-destination connectivity classifications, dominant
corridors, and route distances are stable between the recovered January
2024 network and the 12-June-2024 network, under one frozen procedure,
within a fraction of the 2% tolerance, with no restriction violations and
no manual-QA failure.

**This does not authorize:**
- `GO_TO_GATE_2B`
- Sentinel-1/2 or any EO processing
- a merge to `main`

**The remaining unanswered scientific question**, after the network is
frozen and found stable: whether the confirmed Darband closure's
network-distance consequence (a ~2.0-2.5x detour ratio on the southern
gateway only, ~36-220 km additional distance depending on destination)
corresponds to any real-world accessibility, tourism, or economic effect
— which this project's claim boundary (`01_Gate0_Project_Framing.md`,
section L) explicitly prohibits inferring from network topology alone,
and which no evidence gathered in Gate 0, Gate 1, or Gate 2A-R speaks to.

This session stops here and awaits explicit human authorization before
any further stage.
