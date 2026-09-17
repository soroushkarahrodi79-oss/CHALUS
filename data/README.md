# Data manifest

Raw and reconstructed OSM files are not stored in normal Git history.

## January 2024 candidate

- Local filename: `iran-240101_CANDIDATE.osm.pbf`
- Size: 78,241,792 bytes
- SHA-256: `950579c941f4bcb57a442c7945968a932dae3e73d3112837c16a0811325ebdb6`
- Bounding box: 44.023–63.354°E, 24.039–39.790°N
- Generator: `osmium/1.14.0`
- Replication timestamp: `2024-01-01T21:21:15Z`
- Replication sequence: `3926`
- Replication base URL: `http://download.geofabrik.de/asia/iran-updates`
- Status: candidate retrospective source; not recovered Gate 1 evidence

The unavailable source formerly associated with Gate 1 had the orphaned hash
`1ce7fe2c2d28973f692699f5ab8b815e12099b3efc2a6e66fb25e2030e471e4c`.
The hashes differ and equivalence must not be claimed.

## June 2024 network

The route-bounded historical June reconstruction remains provisional until its
source provenance, cutoff, construction procedure and checksum are documented
and both dates are recomputed through the same frozen environment.

## Publication rule

Do not add raw `.pbf`, `.osm` or `.osc` files to normal Git history. Publish a
retrieval/filtering recipe and checksum, or use an explicitly managed release
asset only when redistribution and licensing have been reviewed.
