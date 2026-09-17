# Closeout audit — exact commands and hashes

All commands run from the repository root with `iran-240101.osm.pbf`
(recovered original, SHA-256
`1ce7fe2c2d28973f692699f5ab8b815e12099b3efc2a6e66fb25e2030e471e4c`,
202,051,103 bytes) and `june_reconciled_partial_CANDIDATE.osm` (SHA-256
`2d7f63ae00dd86f2f23020515dce671c617b6b976fce63f3119023d13edad0ed`)
present alongside `src/*.py`, under the frozen environment in
`environment/ENVIRONMENT.md`.

## Commands

```
python3 src/full_audit.py          # 18-route parity (9 pairs x base/closure)
python3 src/restriction_audit_dual.py   # January + June turn-restriction audit
python3 src/final_evidence.py      # combined: routing, QA stats, restriction audit
```

`final_evidence.py` supersedes `full_audit.py` and
`restriction_audit_dual.py` as the single canonical run (it reproduces
both of their outputs plus manual-QA statistics from one graph build,
avoiding redundant ~80s rebuilds). All three are committed for audit
transparency; the reported figures in `GATE2AR_FINAL_REPORT.md` come from
`final_evidence.py`.

## Script hashes

```
2715f96620d0c35a0ed3080662f6de990d18baeb71ec3b35270bf2e1c90cb2f7  src/gate2a_reconcile.py
05f869e1380549a3b11bf0a4eb359931ff2b7c5210862c04dff200ce0ae467c1  src/full_audit.py
a1c8ce3f299aaabfd6dd33429f7135f5360934eab668857d9ec6e01d6c212b60  src/restriction_audit_dual.py
38d119acdad423a1557e8fc152b5c83d04b78d2a6885110a5c9479fb3dda5144  src/final_evidence.py
```

## Output hashes (from `final_evidence.py`, run twice, byte-identical both times)

```
50aff72110ae8cfc12324d23f4aec896c812bc73639a1d96f98184a8f656b7a1  qa_stats.json
961d6669922819e473f493239c9a51bd5b1e64a41134e0eea5c115c245ee34e1  restriction_final.json
```

## Output hash (from `full_audit.py`)

```
c8e3236f33dc2559d44fb3b75eec4f763bcd7f506e82483f0039943d12a3ee81  full_parity.json
```

## Determinism evidence

- `final_evidence.py` run twice: `qa_stats.json` and `restriction_final.json`
  byte-identical both times (`diff` exit 0).
- Earlier stage: `src/gate2a_reconcile.py` (January) and
  `src/compute_gate2a_results.py` (June) each run twice, byte-identical
  results both times (see `docs/GATE2AR_RUN_LOG.md`, Stage 4).

## Input hashes

```
1ce7fe2c2d28973f692699f5ab8b815e12099b3efc2a6e66fb25e2030e471e4c  iran-240101.osm.pbf (202,051,103 bytes; NOT committed, per repository policy)
2d7f63ae00dd86f2f23020515dce671c617b6b976fce63f3119023d13edad0ed  june_reconciled_partial_CANDIDATE.osm (NOT committed, per repository policy)
```

Raw PBF/OSM inputs are excluded from this repository per `.gitignore` and
explicit instruction; their acquisition, checksums, and header metadata
are documented in `data/README.md`.
