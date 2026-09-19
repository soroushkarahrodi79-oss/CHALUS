# CHALUS

Historical road-accessibility verification for the **Western Mazandaran
Tourism Access Disruption Pilot**.

## Current status

**GATE 2A-R CLOSED — NO-GO. EO BLOCKED. GATE 2B UNAUTHORIZED.**

Gate 2A-R found extremely stable modelled distances and corridors between
the recovered January reference and the route-bounded June
reconstruction (maximum 0.011% difference across all nine
gateway-destination pairs). However, the pre-registered
historical-verification standard was not met: Haraz segment
correspondence remains incompletely demonstrated, June turn-restriction
completeness is partial, and decisive motorway operational status lacks
independent confirmation. Because the protocol required NO-GO for
unresolved Haraz topology or restriction ambiguity, the study stops
before EO processing. See
[the final closeout report](docs/GATE2AR_FINAL_REPORT.md).

The original Gate 1 numerical outputs and their exact January source were not
preserved. This repository therefore does **not** claim to reproduce or recover
Gate 1. Gate 2A-R tested whether the substantive network conclusion remains
stable when January and June 2024 networks are reconstructed through one
frozen, reproducible procedure — it does, numerically, but that numeric
stability was not sufficient on its own to close the gate.

## Frozen analytical system

- Destinations: Chalus, Nowshahr and Kelardasht
- Gateways: Karaj/south, Amol/east and Ramsar/west
- Event: 13–16 June 2024
- Pre-event cutoff: 12 June 2024, 23:59:59 Iran Standard Time
- Closure scenario: supported bounded Darband segment on Road 59
- Weighting: distance only

## Claim boundary

The project may estimate modelled gateway-specific route-distance changes
after removing an independently documented bounded closure segment. It does
not infer tourist delay, cancellations, demand, revenue loss, destination
resilience or required infrastructure investment.

## Repository policy

Large raw OSM/PBF files, reconstructed extracts and provisional route outputs
are excluded from Git history. Their provenance and checksums belong in the
[data manifest](data/README.md).

See the [Gate 2A-R protocol amendment](docs/GATE2AR_PROTOCOL_AMENDMENT.md).

## Evidence status

Gate 2A-R closed with a NO-GO verdict (see status above). Existing
candidate outputs and computed distances are preserved as supported
findings, not deleted, but the pre-registered historical-verification
standard (Haraz segment correspondence, restriction completeness,
independent motorway operational status) was not fully met.

Earth-observation processing remains unauthorized. Gate 2B remains
unauthorized. The research branch was merged to `main` (PR #1) only to
consolidate the complete audit trail on the default branch; this merge is
a repository-housekeeping action, not a scientific event — it does not
reopen Gate 2A-R, does not authorize Gate 2B or EO processing, and does
not alter the NO-GO verdict.
