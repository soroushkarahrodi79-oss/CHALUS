# GATE 2A-R — FINAL CLOSEOUT REPORT (CORRECTED)

Branch: `research/gate2ar-paired-reconstruction`. Not merged to `main`.

**This version corrects the prior report** (commit `d7c07ce`), which issued
GO while an explicitly unresolved Haraz topology question was still open —
a violation of the amendment's own pre-registered kill rule. That report's
status is retracted; see `docs/GATE2AR_RUN_LOG.md` for the retraction
record. This report resolves the open item with independent geometric
evidence rather than waiving the rule, and corrects several other
overstatements identified in the closeout audit.

## Provenance statement

- Strict Gate 2A was impossible because Gate 1's original numeric outputs
  were never preserved anywhere this session could reach — only Gate 1's
  specification document was.
- The original January binary source was recovered exactly by recorded
  hash (202,051,103 bytes, SHA-256
  `1ce7fe2c2d28973f692699f5ab8b815e12099b3efc2a6e66fb25e2030e471e4c`). A
  separate, earlier truncated transfer (78,241,792 bytes) is preserved
  unchanged in `docs/GATE2AR_RUN_LOG.md` as historical evidence.
- Every January route figure is a **fresh, reproducible recomputation**
  from the recovered source, run twice, byte-identical both times — not a
  recovered Gate 1 output.
- All distances are **MODELLED FROM PAIRED RETROSPECTIVE HISTORICAL
  NETWORKS.** No travel time, traffic, EO-derived exposure, or
  tourism-impact quantity appears anywhere in this report.

---

## A. Gate 2A-R Verdict

**GO** — bounded strictly to historical-network stability, and issued only
after the previously-unresolved item was actually resolved, not waived.

The amendment's rule is explicit: *"Any unresolved Haraz topology... or
materially different reasonable reconstruction triggers NO-GO."* The prior
report found an unresolved item and issued GO anyway by arguing its effect
was small — that is exactly the "silently weaken the kill test after
seeing favorable results" failure mode named in this audit's instructions.
This report instead did the work the rule demands: see section C. The
topology is now resolved with direct, independent evidence (shared OSM
node IDs between the January and June ways, not the change ledger's
claim, which was itself checked and found wrong). Because it is resolved,
not merely small, the automatic NO-GO does not apply.

All seven stability rules were re-checked directly:

1. Connectivity: stable, both dates (section G/H, corrected vocabulary).
2. No dominant-corridor change from unresolved topology: **now genuinely
   true** — the one candidate exception is resolved (section C).
3. Distance difference ≤2%: actual maximum 0.011% (section F).
4. Gateway sensitivity: low, tested bidirectionally at all three gateways,
   not just the southern approach (section J).
5. Destination-node sensitivity: present but non-determining (section K).
6. Manual QA: a genuine desk review of named route geometry (not automated
   connectivity restated as manual QA) passed on all 12 distinct routes,
   both dates (section L).
7. Deterministic: every script re-run at least twice, byte-identical
   output confirmed for each (section M / `evidence/derived/
   CLOSEOUT_COMMANDS.md`).

## B. Historical Change Ledger

`evidence/Gate2A_Historical_Change_Ledger.csv`, 130 rows, unchanged.
**Correction:** this audit found that the ledger's "parent_child" field is
not reliable evidence on its own — see section C, where its specific claim
for ways 924025918/921 was checked and found to point to the wrong
location entirely. The ledger's *classification* (`C_TOPOLOGY`,
`D_HISTORICAL_STATUS`, etc.) is treated as a lead to verify, not a
conclusion to cite.

## C. Haraz Resolution

**Disputed claim:** the ledger states January ways `924025918` (2 nodes)
and `924025921` (2 nodes, tagged `bridge=yes`) — both `ref=77`, "جاده
هراز" (Haraz Road), absent from June — were "replaced by
`1270179067,1287287400,1287287401`."

**Independent check performed** (`src/haraz_geometry_resolution.py`,
run twice, byte-identical): the ledger's claimed replacement ways are
630–882 m from the disputed ways' actual location — not a plausible
direct-replacement distance. An independent spatial search (not
ledger-guided) for June ways within 400 m of that location found three
candidates: `924025920` (82 m), `924025919` (106 m), `924025923` (135 m).

**Decisive evidence:** way `924025920`'s June version (v10, 19 nodes)
begins at node `8577451368` — the exact starting node of disputed way
`924025918`. Way `924025920`'s January version (v5, 16 nodes) ends at
node `8577451370` — the exact ending node of disputed way `924025921`.
These are not coincidentally similar IDs; they are the **same OSM node
IDs**, present in both the disputed January ways and way 924025920's node
list in both its January and June versions. This is direct proof of
physical continuity: the short bridge segment represented as two separate
way objects in January (`924025918` + `924025921`, ~200 m together) was
absorbed into the already-existing, larger way `924025920` by June — an
OSM way-merge/re-digitization, not a road closure, demolition, or
realignment. Confirmed further by the actual computed routes: both the
January and June south-corridor closure routes to all three destinations
pass directly through this exact location (`route_hits_near_target` in
`evidence/derived/haraz_geometry_resolution.json`), using `924025919` and
`924025920` in both dates, with `924025918`/`924025921` used only in the
January version (because they still existed as separate objects then) and
folded into `924025920` by June.

**The ledger's specific "replaced by" annotation was wrong** — a real
error, not a documentation nuance. The correct successor, established
independently, is way `924025920` (with `924025919` as its unchanged
bridge-adjacent neighbor in both dates).

**Verdict on this item: RESOLVED.** Not "small effect, therefore waived" —
resolved, with the successor way identified and its physical continuity
proven by shared node IDs, not asserted from ledger text. Aggregate route
effect: 0.036–0.036 km out of ~317 km (0.011%), consistent with what a
real way-merge of an already-short segment would produce, now explained
rather than merely bounded.

## D. Tehran–North Historical Status

Kept separate from section C per instruction, and corrected against the
overclaim in the prior report: **OSM object presence or edit timestamp
alone does not prove physical operational status.** This session has no
independent official source (news article, road-authority record,
construction-completion notice) for any Tehran–North Freeway or Haraz
section's opening date — obtaining one would require a web fetch this
session's network policy does not permit for arbitrary hosts, and none
was already present in any supplied evidence bundle.

Corrected table (271 route-relevant ways tagged `ref=77`, `ref=3`, or
`ref=14`, from `evidence/derived/haraz_tehran_north_table.json`):

| Status | Count | Basis | Classification |
|---|---|---|---|
| OSM object present at both cutoffs, version/edit timestamp ≤ respective cutoff, no independent operational source | 262 | OSM presence + timestamp only | **SUPPORTED_OPERATIONAL** (downgraded from the prior report's incorrect `CONFIRMED_OPERATIONAL` — CONFIRMED would require independent evidence this session does not have) |
| The one resolved reconciliation (way 924025918/921 -> 924025920/919) | 2 | Section C, shared-node proof | **SUPPORTED_OPERATIONAL** — physical continuity proven at the OSM-geometry level, still not independently confirmed as "operational" by any non-OSM source |
| Ledger-claimed but incorrect "replacement" ways (1270179067, 1287287400, 1287287401, and the other June-only splits in that immediate cluster) | 9 | Exist in OSM by their creation timestamp (all ≤ 12 June 2024), located ~600–900 m from the disputed segment, i.e. a genuinely separate stretch of the same named road, unrelated to the disputed pair | **SUPPORTED_OPERATIONAL** for their own segment, independent of section C's resolution |

**No way in this set is `NOT_YET_OPEN`** — no creation timestamp falls
after 12 June 2024; latest is `2024-06-08T08:11:11Z`.

**No way in this set is `UNCERTAIN`** in the final classification, because
the one candidate for that label (section C) was resolved rather than left
open. Per instruction, an `UNCERTAIN` section must not create a decisive
southern alternative if one remains — moot here since none remains
unresolved, but noted for completeness.

**Corrected claim wording, per instruction:** every statement in this
report about Tehran–North or Haraz infrastructure "existing" or being
"created/edited" before a cutoff refers to **OSM object state**, not
independently confirmed physical construction or opening. This report
does not claim physical-world confirmation it does not have.

## E. Frozen Historical Network Specification

Unchanged from the prior report — no gateway, destination, closure
geometry, distance weighting, road filter, sensitivity design, or routing
parameter was altered in this audit, per instruction. Gateways:
south/Karaj (`31086990`), east/Amol (`6208746864`), west/Ramsar
(`8595307908`). Destinations: Chalus (`1375231380`), Nowshahr
(`4998048119`), Kelardasht (`3323917713`). Cutoffs: January
`2024-01-01T21:21:15Z`, June `2024-06-12T20:29:59Z`. Closure: Darband node
`3294759340`. Event chronology: 13 June ~20:30 through 16 June afternoon
(supersedes 13–14 June).

## F. January Reference vs June Historical Comparison

| Pair | Jan base km | Jun base km | % diff | Jan closure km | Jun closure km | % diff | ΔD (closure − base), Jun |
|---|---|---|---|---|---|---|---|
| south-chalus | 151.239 | 151.229 | -0.006% | 316.961 | 316.925 | -0.011% | **165.696 km** |
| south-nowshahr | 158.724 | 158.714 | -0.006% | 311.029 | 310.994 | -0.011% | **152.280 km** |
| south-kelardasht | 145.681 | 145.671 | -0.007% | 364.321 | 364.286 | -0.010% | **218.615 km** |
| east-chalus | 99.571 | 99.568 | -0.003% | 99.571 | 99.568 | -0.003% | 0.000 km |
| east-nowshahr | 93.639 | 93.637 | -0.003% | 93.639 | 93.637 | -0.003% | 0.000 km |
| east-kelardasht | 146.931 | 146.928 | -0.002% | 146.931 | 146.928 | -0.002% | 0.000 km |
| west-chalus | 79.402 | 79.406 | +0.005% | 79.402 | 79.406 | +0.005% | 0.000 km |
| west-nowshahr | 87.036 | 87.040 | +0.004% | 87.036 | 87.040 | +0.004% | 0.000 km |
| west-kelardasht | 84.202 | 84.206 | +0.004% | 84.202 | 84.206 | +0.004% | 0.000 km |

**Correction:** the prior report's closing statement said "~36–220 km
additional distance" — the 36 km figure was wrong (it conflated the
Haraz-segment discrepancy, ~0.036 km, with the route-level ΔD, which is
two orders of magnitude larger). The actual ΔD range on the southern
gateway is **152.3–218.6 km**, shown per-pair above; east/west ΔD is
exactly 0.000 km in both dates because those closure paths are identical
to their own baselines (verified by path equality, not inferred).

Maximum absolute January-vs-June difference across all 18 route-states:
**0.011%.**

## G. Reconciled Baseline Table

| Gateway | Destination | Jan km | Jun km | Connectivity | Dominant corridor |
|---|---|---|---|---|---|
| south | chalus | 151.239 | 151.229 | **CONNECTED** | ref 59 (Chalus Road) |
| south | nowshahr | 158.724 | 158.714 | **CONNECTED** | ref 59 |
| south | kelardasht | 145.681 | 145.671 | **CONNECTED** | ref 59 |
| east | chalus | 99.571 | 99.568 | **CONNECTED** | ref 22 |
| east | nowshahr | 93.639 | 93.637 | **CONNECTED** | ref 22 |
| east | kelardasht | 146.931 | 146.928 | **CONNECTED** | ref 22 |
| west | chalus | 79.402 | 79.406 | **CONNECTED** | ref 22 |
| west | nowshahr | 87.036 | 87.040 | **CONNECTED** | ref 22 |
| west | kelardasht | 84.202 | 84.206 | **CONNECTED** | ref 22 / unref'd local roads |

## H. Reconciled Closure Table

**Corrected connectivity vocabulary** per instruction: baseline is
`CONNECTED`; the closure scenario for a route that genuinely detours is
`CONNECTED WITH DETOUR`, and for a route whose path is unaffected by the
closure it remains `CONNECTED` (not restated as detoured). The prior
report said "CONNECTED" uniformly while also reporting detour ratios up
to 2.50 in the same table — that was an internal inconsistency, corrected
here.

| Gateway | Destination | Jan km | Jun km | Connectivity | Dominant corridor | Path identical to baseline? |
|---|---|---|---|---|---|---|
| south | chalus | 316.961 | 316.925 | **CONNECTED WITH DETOUR** | ref 77 (Haraz) | No, both dates |
| south | nowshahr | 311.029 | 310.994 | **CONNECTED WITH DETOUR** | ref 77 | No, both dates |
| south | kelardasht | 364.321 | 364.286 | **CONNECTED WITH DETOUR** | ref 77 | No, both dates |
| east | chalus | 99.571 | 99.568 | **CONNECTED** | ref 22 | **Yes** — verified by node-path equality |
| east | nowshahr | 93.639 | 93.637 | **CONNECTED** | ref 22 | **Yes** |
| east | kelardasht | 146.931 | 146.928 | **CONNECTED** | ref 22 | **Yes** |
| west | chalus | 79.402 | 79.406 | **CONNECTED** | ref 22 | **Yes** |
| west | nowshahr | 87.036 | 87.040 | **CONNECTED** | ref 22 | **Yes** |
| west | kelardasht | 84.202 | 84.206 | **CONNECTED** | (unref'd) | **Yes** |

**Stability, correctly defined per instruction:** stability means the
classification is identical between January and June, not that baseline
and closure share a classification. On that definition: all nine pairs
are stable (each pair's classification matches itself across dates; no
pair flips from CONNECTED to DISCONNECTED, or from CONNECTED WITH DETOUR
to a different corridor, between January and June).

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

## J. Gateway Sensitivity (bidirectional, all three gateways)

**Correction:** the prior report tested only `south`/`south_5`/`south_10`
(one direction) plus fixed `east`/`west` nodes with no shift at all. This
audit re-ran gateway sensitivity properly
(`src/gateway_sensitivity_bidirectional.py`, run twice, byte-identical):
±5/±10 km along the southern approach (both directions available), +5/+10
km forward for east and west (both available, both dates), and backward
shifts for east/west where the frozen bounding box's road network
actually extends far enough to support one — it does not extend far
enough for a −5/−10 km backward shift at the west gateway in either date,
or beyond −5 km at the east gateway in January; this is reported as a
genuine boundary-of-modeled-region limit, not silently omitted.

Connectivity classification is **CONNECTED WITH DETOUR for every south
shift, both directions, both magnitudes, both dates**, and **CONNECTED
for every east/west shift, both directions where available, both dates**
— no shift flips the classification. Detour ratios range 1.918–2.777
across all south shifts (both dates), consistent with the unshifted
2.096/1.960/2.501. **Gateway sensitivity: LOW**, confirmed bidirectionally,
not just in the single direction previously tested.

## K. Destination-Node Sensitivity

Unchanged from the prior report: alternate destination nodes shift detour
ratios by at most ~0.03–0.13 without changing which pairs detour
materially. **Present but non-determining.**

## L. Manual Route QA

**Correction:** the prior report's "manual QA" was automated structural
statistics (edge class, min/max length) mislabeled as manual review. That
material is retained as `evidence/derived/manual_qa_stats.json`, now
explicitly named **automated structural QA**. A genuine manual desk
review of named route geometry (12 distinct routes, both dates, reading
the actual road-name/ref sequence a human can inspect) was produced
separately: `evidence/derived/MANUAL_ROUTE_QA.md`. Result: **PASS on all
12 routes, both dates, zero FAIL, zero ABSTAIN.** No satellite imagery was
used, per instruction.

## M. Updated Evidence Ledger

| Evidence class | Status |
|---|---|
| Confirmed disruption (Darband closure) | CONFIRMED (unchanged) |
| Historical network, January | CONFIRMED — recovered, validated, recomputed twice deterministically |
| Historical network, June | CONFIRMED (unchanged) |
| Nine-pair / 18-route-state parity | CONFIRMED — one prior open item (Haraz) now RESOLVED with independent evidence |
| Turn restrictions, January | CONFIRMED for 34 relations (25 externally-supplied + 9 found by direct PBF extraction, `src/jan_restrictions_from_pbf.py`), zero violations, reproduced twice |
| Turn restrictions, June | **PARTIAL** — 26 externally-supplied relations checked, zero violations, but completeness against the full June network cannot be independently established without a full June-side historical source (see `evidence/derived/RESTRICTION_AUDIT_PROVENANCE.md`) |
| Gateway sensitivity | CONFIRMED — low, bidirectional, all three gateways |
| Destination-node sensitivity | CONFIRMED — present, non-determining |
| Manual route QA | CONFIRMED — genuine desk review, PASS on all 12 routes |
| Tehran-North / Haraz operational status | **SUPPORTED_OPERATIONAL only** — OSM-attested, not independently confirmed; downgraded from the prior report's incorrect CONFIRMED_OPERATIONAL |
| EO/tourism/travel-time claims | ABSTAIN — out of scope |

## N. Triggered or Nearly Triggered Kill Tests

- **Nearly triggered NO-GO, then resolved rather than waived:** the Haraz
  topology question (section C). The distinction matters and is stated
  again here: this report does not claim GO because the effect was small;
  it claims GO because the specific claimed replacement was checked,
  found wrong, and the actual physical successor was identified with
  node-level proof.
- **Not triggered:** source-provenance gate, restriction-violation gate
  (zero violations on 34 January + 26 June relations), 2% stability rule
  (max 0.011%), gateway-sensitivity gate (low, bidirectional), manual-QA
  gate (12/12 PASS).
- **Recorded limitation, not a triggered kill test:** June-side
  restriction-completeness remains PARTIAL, and the June route-bounded
  vs. January complete-envelope acquisition asymmetry remains a tested
  (Method B, prior stage) but not eliminated limitation.

---

## Closing statement

**Verdict: GO on historical-network stability only.** The nine
gateway-destination connectivity classifications, dominant corridors, and
route distances are stable between the recovered January 2024 network and
the 12-June-2024 network, within 0.011% of each other, with zero
restriction violations on 34 (January) and 26 (June) checked relations,
genuine manual QA passing on all 12 distinct routes, and gateway
sensitivity confirmed low in both directions at all three gateways. The
one item that was open in the prior version of this report — Haraz
topology correspondence — is resolved with direct node-level evidence, not
waived because its effect was small.

**This does not authorize:**
- `GO_TO_GATE_2B`
- Sentinel-1/2 or any EO processing
- a merge to `main`

**The remaining unanswered scientific question:** whether the confirmed
Darband closure's network-distance consequence (152.3–218.6 km additional
distance, southern gateway only; east/west unaffected) corresponds to any
real-world accessibility, tourism, or economic effect. This project's
claim boundary (`01_Gate0_Project_Framing.md`, section L) prohibits
inferring that from network topology alone, and nothing gathered in Gate
0, Gate 1, or Gate 2A-R speaks to it.

This session stops here and awaits explicit human authorization before
any further stage.
