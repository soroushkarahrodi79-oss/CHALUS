# CHALUS

Historical road-accessibility verification for the **Western Mazandaran
Tourism Access Disruption Pilot**.

## Current status

**Gate 2A-R — paired retrospective historical reconstruction**

The original Gate 1 numerical outputs and their exact January source were not
preserved. This repository therefore does **not** claim to reproduce or recover
Gate 1. Gate 2A-R tests whether the substantive network conclusion remains
stable when January and June 2024 networks are reconstructed through one
frozen, reproducible procedure.

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

Existing candidate outputs remain diagnostic. Accepted results require
verified historical provenance, a frozen environment, paired execution through
one code path, deterministic reruns, manual route QA and the pre-registered
connectivity, corridor and 2% stability tests.

Earth-observation processing remains unauthorized until Gate 2A-R passes.
