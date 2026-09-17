# Frozen execution environment — Gate 2A-R

Recorded at first execution attempt of the paired reconstruction.

- OS / kernel: Linux 6.18.44-fc-v33, x86_64
- Python: 3.11.15
- Dependency pins: see `requirements.txt` (installed via `pip install -r requirements.txt`,
  derived from `requirements.in`)
- Random state: none used. Route computation is deterministic shortest-path
  (Dijkstra via `networkx.shortest_path`, weight = great-circle length); no
  seeded randomness anywhere in `src/gate2a_reconcile.py` or its callers.

## Commands run (June side — completed)

```
python3 src/compute_gate2a_results.py
```

- Input: `june_reconciled_partial_CANDIDATE.osm`
  (SHA-256 `2d7f63ae00dd86f2f23020515dce671c617b6b976fce63f3119023d13edad0ed`)
- Output: `gate2a_results.json`, `gate2a_sensitivity.json` (not committed —
  provisional generated output per repository policy)
- Result: numerically identical to the previously supplied candidate
  `gate2a_results.json` for all nine gateway-destination pairs. See
  `docs/GATE2AR_RUN_LOG.md` for the reproduced figures.

## Commands run (January side — failed)

```
python3 src/gate2a_reconcile.py
```

- Input: `iran-240101_CANDIDATE.osm.pbf`
  (SHA-256 `950579c941f4bcb57a442c7945968a932dae3e73d3112837c16a0811325ebdb6`,
  matches declared hash exactly)
- Result: `RuntimeError: PBF error: unexpected EOF` after parsing 14,136,000
  nodes and 0 ways. No output produced. See `data/README.md` and
  `docs/GATE2AR_RUN_LOG.md` for details.

## Reproducibility note

The June-side command was re-run twice against the same input; both runs
produced byte-identical `gate2a_results.json` output, confirming the
graph-building and routing code path is deterministic under this
environment. The January-side command was not re-runnable to a result — it
fails deterministically at the same point (same node count, same error)
on repeated attempts, which rules out a transient I/O fault and points to a
structural property of the input file itself.
