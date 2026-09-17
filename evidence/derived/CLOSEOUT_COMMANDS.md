# Closeout audit — exact commands, hashes, and artifact provenance

All commands run from the repository root with `iran-240101.osm.pbf`
(recovered original, SHA-256
`1ce7fe2c2d28973f692699f5ab8b815e12099b3efc2a6e66fb25e2030e471e4c`,
202,051,103 bytes) and `june_reconciled_partial_CANDIDATE.osm` (SHA-256
`2d7f63ae00dd86f2f23020515dce671c617b6b976fce63f3119023d13edad0ed`)
present alongside `src/*.py`, under the frozen environment in
`environment/ENVIRONMENT.md`.

**Correction to the prior version of this file:** it claimed
`final_evidence.py` alone reproduces every derived artifact. That was
false — `final_evidence.py` produces only `qa_stats.json` and
`restriction_final.json`. Every artifact below is mapped to the specific
script that actually produces it, with no script credited for output it
does not generate.

## Artifact -> generating script map

| Artifact | Generating script | Depends on |
|---|---|---|
| `qa_stats.json` | `src/final_evidence.py` | both graphs |
| `restriction_final.json` | `src/final_evidence.py` | both graphs, `osm_history/restrictions/*.osm` |
| `parity_18routes.json` (copied from `full_parity.json`) | `src/full_audit.py` | both graphs |
| `restriction_audit_dual_date.json` (copied from `restriction_final.json` of an earlier stage) | `src/restriction_audit_dual.py` | both graphs, `osm_history/restrictions/*.osm` |
| `manual_qa_stats.json` (copied from `qa_stats.json`) | `src/final_evidence.py` | both graphs |
| `haraz_tehran_north_table.json` | ad hoc query against `jan_route_way_meta.json`/`jun_route_way_meta.json` (produced by `src/full_audit.py`), filtered by ref/name; **not currently a standalone committed script** — this is a named gap, not a hidden one. The filter logic (`ref in ('77','3','14') or 'هراز'/'Haraz'/'شمال'/'North' in name`) is stated here so it can be reproduced. |
| `january_recomputed_results.json` | `src/gate2a_reconcile.py` (`__main__` block) | January graph only; **not committed** (9.5 MB, exceeds the "compact" bar — regenerate on demand) |
| `haraz_geometry_resolution.json` | `src/haraz_geometry_resolution.py` | both graphs, both raw source files (needs `locations=True` node resolution) |
| `jan_restrictions_from_pbf.json` | `src/jan_restrictions_from_pbf.py` | January PBF only |
| `extra_relations_check.json` | `src/check_extra_relations.py` | both graphs |
| `gateway_sensitivity_bidirectional.json` | `src/gateway_sensitivity_bidirectional.py` | both graphs |
| `route_narratives.json` | `src/route_narrative.py` | both graphs |
| `parent_child_geometric_check.md` | manually written, reporting the *first-pass* (single-endpoint) geometric check; **superseded** by `haraz_geometry_resolution.json`'s independent-spatial-search result, which corrected the first pass's methodology (it originally compared only against the ledger's claimed replacement ways, not an independent search) |
| `restriction_fragment_hashes.txt` | `sha256sum osm_history/restrictions/*.osm` | the 31 externally-supplied relation-history files (not committed; see `RESTRICTION_AUDIT_PROVENANCE.md`) |

## Commands

```
python3 src/full_audit.py                        # parity_18routes.json source
python3 src/restriction_audit_dual.py             # restriction_audit_dual_date.json source
python3 src/final_evidence.py                     # qa_stats.json, restriction_final.json
python3 src/haraz_geometry_resolution.py           # haraz geometry resolution (run twice)
python3 src/jan_restrictions_from_pbf.py           # direct January PBF relation extraction
python3 src/check_extra_relations.py               # violation check for the 9 relations found only by direct extraction
python3 src/gateway_sensitivity_bidirectional.py   # bidirectional gateway sensitivity (run twice)
python3 src/route_narrative.py                     # human-readable route narratives for manual QA
```

## Script hashes

```
2715f96620d0c35a0ed3080662f6de990d18baeb71ec3b35270bf2e1c90cb2f7  src/gate2a_reconcile.py
05f869e1380549a3b11bf0a4eb359931ff2b7c5210862c04dff200ce0ae467c1  src/full_audit.py
a1c8ce3f299aaabfd6dd33429f7135f5360934eab668857d9ec6e01d6c212b60  src/restriction_audit_dual.py
38d119acdad423a1557e8fc152b5c83d04b78d2a6885110a5c9479fb3dda5144  src/final_evidence.py
79bfdb0ab459218aef13d9213b78aa4ef8b9c05311b754cc41b44c973a87c58f  src/haraz_geometry_resolution.py
b1980ec6467189a7bbc4f713cb2cdae7857524eae0919bc26921addf67b4a9e9  src/jan_restrictions_from_pbf.py
e823ff0f8f2cc2bf7ee5da358cde5e88282c952229d40bb4a0c0deea296746b9  src/check_extra_relations.py
8545a71ca60070f4a21212093d049f9f9aabe97d0f5ffe3d573264713284154b  src/gateway_sensitivity_bidirectional.py
c3ef70da15c1a5751837fe17df45873db624f6c102d75a16e515c50a6b7e357d  src/route_narrative.py
```

## Determinism evidence (every script re-run, byte-identical each time)

```
qa_stats.json                              -- final_evidence.py, 2 runs, identical
restriction_final.json                     -- final_evidence.py, 2 runs, identical
haraz_geometry_resolution.json              -- haraz_geometry_resolution.py, 2 runs, identical
gateway_sensitivity_bidirectional.json      -- gateway_sensitivity_bidirectional.py, 2 runs, identical
gate1_reproduced.json (January routing)     -- gate2a_reconcile.py, 2 runs, identical (see run log Stage 4)
gate2a_results.json (June routing)          -- compute_gate2a_results.py, 2 runs, identical (see run log Stage 3)
```

`full_audit.py`, `restriction_audit_dual.py`, `jan_restrictions_from_pbf.py`,
`check_extra_relations.py`, and `route_narrative.py` were each run once in
this session; their outputs are deterministic Dijkstra/graph-traversal
computations with no random state (same guarantee as the scripts above),
but a second confirming run was not separately executed for each due to
time budget in this audit pass. This is stated rather than implied as
equivalent to the scripts that were explicitly reproduced twice.

## Input hashes

```
1ce7fe2c2d28973f692699f5ab8b815e12099b3efc2a6e66fb25e2030e471e4c  iran-240101.osm.pbf (202,051,103 bytes; NOT committed, per repository policy)
2d7f63ae00dd86f2f23020515dce671c617b6b976fce63f3119023d13edad0ed  june_reconciled_partial_CANDIDATE.osm (NOT committed, per repository policy)
```

31 restriction-history fragment hashes: `evidence/derived/
restriction_fragment_hashes.txt` (fragments themselves not committed — see
`RESTRICTION_AUDIT_PROVENANCE.md`).

Raw PBF/OSM inputs are excluded from this repository per `.gitignore` and
explicit instruction.
