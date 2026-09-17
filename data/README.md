# Data manifest

Raw and reconstructed OSM files are not stored in normal Git history.

## January 2024 candidate

- Local filename: `iran-240101_CANDIDATE.osm.pbf`
- Declared size: 78,241,792 bytes
- Declared SHA-256: `950579c941f4bcb57a442c7945968a932dae3e73d3112837c16a0811325ebdb6`
- Bounding box (from PBF header): 44.023–63.354°E, 24.039–39.790°N
- Generator (from PBF header): `osmium/1.14.0`
- Replication timestamp (from PBF header): `2024-01-01T21:21:15Z`
- Replication sequence: `3926`
- Replication base URL: `http://download.geofabrik.de/asia/iran-updates`
- Status: candidate retrospective source; not recovered Gate 1 evidence

The unavailable source formerly associated with Gate 1 had the orphaned hash
`1ce7fe2c2d28973f692699f5ab8b815e12099b3efc2a6e66fb25e2030e471e4c`.
The hashes differ and equivalence must not be claimed.

### Status: BLOCKED_CORRUPTED_INPUT (not a final NO-GO)

Fragment- and whole-file SHA-256 verification **passed exactly** against the
declared checksums (`PBF_PARTS_SHA256SUMS` and the whole-file hash above), and
`file(1)` correctly identifies the reassembled artifact as PBF-formatted data.

However, hash and format checks only prove the bytes are what was declared —
they do not prove the content is a complete OSM dataset. Parsing the
reassembled file with `osmium` (v4.3.1, Python bindings) under the frozen
environment below produces:

```
nodes seen:      14,136,000
ways seen:       0
relations seen:  0
error: RuntimeError: PBF error: unexpected EOF
```

The parser consumes the entire node section successfully and then fails with
a genuine mid-stream truncation — not a clean end-of-file after the last
valid block. **No way or relation data is present in this file.**

This is recorded as a fact about the received artifact, not a reassembly
error: the four fragments summed to the declared byte count exactly, and the
reassembled file's hash matched the declared hash exactly, before parsing was
attempted.

**Root cause, as reported to this repository:** the transferred candidate
(78,241,792 bytes) is a truncated copy of the official Geofabrik archive,
which the official Geofabrik index reportedly lists at 202,051,103 bytes.
That size figure has not yet been independently verified from this session
(see "Official replacement source" below) — it is recorded here as reported,
not as confirmed.

This finding is preserved unchanged below the following section; it is not
deleted or rewritten by the replacement attempt. It classifies as
**BLOCKED_CORRUPTED_INPUT**, distinct from a scientific NO-GO on the paired
reconstruction — the failure is in the transferred artifact, not in the
underlying network or the closure representation.

### Official replacement source — ACQUISITION BLOCKED (network egress policy)

Attempted retrieval:

- Target URL: `https://download.geofabrik.de/asia/iran-240101.osm.pbf`
- Attempt timestamp: `2026-09-17T09:57:22Z`
- Result: `curl: (56) CONNECT tunnel failed, response 403`
- Session's egress-proxy status log records this explicitly:
  `{"kind":"connect_rejected","detail":"gateway answered 403 to CONNECT
  (policy denial or upstream failure)","host":"download.geofabrik.de:443"}`

This session's outbound HTTPS is routed through a policy-enforcing egress
proxy. `download.geofabrik.de` is not on this session's allowed-host list.
The proxy's own operational guidance is explicit: a 403 from the proxy is an
organizational policy denial, and the correct response is to **report the
blocked host, not retry or route around it**. No bytes of the official
replacement were received. Consequently none of the following can be
reported yet, because they were never obtained: final URL after redirects,
HTTP status from the origin server, exact byte count, SHA-256, PBF generator
string, bounding box, replication timestamp, replication sequence, or
replication base URL for the official file.

**Consequence:** the January side of the Gate 2A-R paired reconstruction
remains blocked — not because the network or the closure representation are
scientifically unstable, but because no complete January source has reached
this session yet. This is an acquisition blocker, not a content blocker on
the June side, and not evidence against the January candidate's plausible
dating (the truncated file's own replication metadata, recorded above,
independently matched Iran's real bounding box and a real Geofabrik
replication feed).

**What would unblock this:** either (a) this session's egress allowlist is
extended to include `download.geofabrik.de` (a decision outside this
session's control), or (b) the official 202,051,103-byte archive is supplied
directly to this session the same way the earlier candidate fragments were —
as an upload — so it can be hashed, parsed, and verified here without a live
fetch.

## June 2024 network

- Local filename: `june_reconciled_partial_CANDIDATE.osm` (route-bounded
  historical extract; not a full regional extract)
- SHA-256: `2d7f63ae00dd86f2f23020515dce671c617b6b976fce63f3119023d13edad0ed`
- Generator: `Overpass API 0.7.62.11 87bfad18`
- Acquisition method: per-way `[date:"2024-06-12T20:29:59Z"]` Overpass QL
  queries against explicit way-ID lists, recorded verbatim in `queries/`
  (14 query files, `00.ql`–`13.ql`)
- Verified directly from raw file content (not merely asserted): 0 of 18,957
  node elements and 0 of 1,062 way elements carry a version timestamp later
  than `2024-06-12T20:29:59Z`. The latest way timestamp present is
  `2024-06-12T13:52:36Z`, before the frozen cutoff.
- License: © OpenStreetMap contributors, ODbL (per in-file `<note>`)
- Status: candidate retrospective source; historically well-formed by direct
  inspection; parses to completion; used to reproduce the previously supplied
  `gate2a_results.json` figures bit-for-bit under the frozen environment
  below (see `docs/GATE2AR_RUN_LOG.md`)
- Known limitation: this is a route-bounded subset (specific way IDs chosen
  in advance), not a bbox+road-class extraction like the January candidate.
  The two sources are not currently built by an identical *acquisition*
  method — only by an identical *graph-building* code path once loaded. This
  asymmetry is unresolved and is recorded, not hidden.

## Publication rule

Do not add raw `.pbf`, `.osm` or `.osc` files to normal Git history. Publish a
retrieval/filtering recipe and checksum, or use an explicitly managed release
asset only when redistribution and licensing have been reviewed.
