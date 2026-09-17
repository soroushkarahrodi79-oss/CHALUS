# Gate 2A-R run log — stage 1 (June-source provenance) and stage 2 (frozen environment)

Status: **paired reconstruction cannot proceed yet.** June side is
reproducible and verified. January side is blocked by a source-data
integrity failure, documented in `data/README.md`.

## Stage 1 — June-source provenance verification

Verified directly from the raw file, not taken on trust:

- Generator string in file: `Overpass API 0.7.62.11 87bfad18`
- All 14 acquisition queries recorded in `queries/00.ql`–`13.ql`. Each is an
  Overpass QL `way(id:...)` query against an explicit way-ID list, scoped
  with `[date:"2024-06-12T20:29:59Z"]` and `out meta` (to preserve version/
  timestamp/changeset metadata needed for the historical-change ledger).
- Historical cutoff enforcement checked by direct scan of the file: 0 of
  18,957 nodes and 0 of 1,062 ways carry a timestamp after
  `2024-06-12T20:29:59Z`; latest way timestamp present is
  `2024-06-12T13:52:36Z`.
- `evidence/Gate2A_Historical_Change_Ledger.csv` (130 rows) cross-references
  every way affected by a January→June version change, with per-way
  `jan_version`/`june_version`, validity windows, and a change classification
  (`A_NON_MATERIAL`, `B_ROUTING_ATTRIBUTE`, `C_TOPOLOGY`,
  `D_HISTORICAL_STATUS`). 17 rows are flagged `YES_TOPOLOGY_RECONCILIATION`.

Known limitation, stated plainly: the June source is a route-bounded subset
built from a hand-specified way-ID list, not a bbox+road-class extraction.
The January source is a full-country PBF requiring the bbox+road-class
filter in `src/gate2a_reconcile.py` to be applied at build time. Both go
through the *same graph-building code* (`build_graph()` in
`gate2a_reconcile.py`, shared by both `compute_gate2a_results.py` and the
`__main__` block), but the *acquisition* methods differ. This is not the
same as a matched paired extraction, and is recorded here rather than
smoothed over.

## Stage 2 — frozen environment

Recorded in `environment/ENVIRONMENT.md` and `environment/requirements.txt`.
Python 3.11.15, Linux x86_64, pinned `networkx==3.6.1`, `osmium==4.3.1`,
`matplotlib==3.11.2`. No randomness in the routing algorithm.

## Stage 3 — paired reconstruction attempt

### June side — reproduced independently, twice, byte-identical

Command: `python3 src/compute_gate2a_results.py` against
`june_reconciled_partial_CANDIDATE.osm`. Two consecutive runs produced
byte-identical `gate2a_results.json` (SHA-256
`2e69e48d2b1a6b65e50df4d5c61aadd3ed743a792136188e2fcefc5d8bd62a57` both
times).

Reproduced figures (nine gateway-destination pairs, distance in km, labelled
per the amendment protocol):

**MODELLED FROM PAIRED RETROSPECTIVE HISTORICAL NETWORKS — June 2024 side only**

| Gateway | Destination | Baseline km | Closure-scenario km | Detour ratio |
|---|---|---|---|---|
| south (Karaj) | chalus | 151.229 | 316.925 | 2.096 |
| south (Karaj) | nowshahr | 158.714 | 310.994 | 1.959 |
| south (Karaj) | kelardasht | 145.671 | 364.286 | 2.501 |
| east (Amol) | chalus | 99.568 | 99.568 | 1.000 |
| east (Amol) | nowshahr | 93.637 | 93.637 | 1.000 |
| east (Amol) | kelardasht | 146.928 | 146.928 | 1.000 |
| west (Ramsar) | chalus | 79.406 | 79.406 | 1.000 |
| west (Ramsar) | nowshahr | 87.040 | 87.040 | 1.000 |
| west (Ramsar) | kelardasht | 84.206 | 84.206 | 1.000 |

Note what this table is and is not: the east and west gateways show a
detour ratio of exactly 1.000 because the Darband closure node
(`3294759340`) does not lie on their shortest paths in this graph — it is a
southern-corridor closure. That is an expected structural result of the
frozen closure definition, not a sign the closure was ignored.

### January side — BLOCKED

Command: `python3 src/gate2a_reconcile.py` against
`iran-240101_CANDIDATE.osm.pbf` (hash-verified, see `data/README.md`).

Result: `RuntimeError: PBF error: unexpected EOF` after 14,136,000 nodes and
0 ways. Reproduced on a second attempt with an identical failure signature
(same node count, same error), ruling out a transient fault.

**No January baseline distance, closure distance, node sequence, way
sequence, or connectivity classification exists from this run.** None is
fabricated here. The comparison table required by the protocol amendment
(January vs June, percentage difference, stability verdict) cannot be
produced.

## Interim conclusion

Per `docs/GATE2AR_PROTOCOL_AMENDMENT.md` §"Mandatory source-provenance
gate": *"If historical validity cannot be established, return NO-GO."* The
January candidate's historical dating is plausible (Geofabrik replication
metadata checks out — see `data/README.md`), but its **completeness** cannot
be established — it contains no road (way) data at all. That is a harder
failure than a provenance question: there is nothing to route on.

**Verdict for this stage: NO-GO on the paired reconstruction, pending a
January source that parses to completion.** This is not a verdict on the
underlying research question — the June side remains internally consistent
and reproducible, and the January provenance metadata is genuinely
promising. What is missing is a January file that actually contains roads.

## What would unblock this

A January-dated OSM/PBF source (any acquisition method, any provider) that:
1. parses to completion under `osmium` (nodes, ways, and ideally relations,
   with no truncation), and
2. covers the same bounding box needed by `src/gate2a_reconcile.py`
   (`BBOX = (49.70, 35.35, 53.20, 37.15)`).

It does not need to match the orphaned `1ce7fe2c...` hash — per the
amendment protocol, equivalence to the original Gate 1 source is not being
claimed either way. It only needs to be a real, complete, dated network.
