# GATE 2A-R — Paired Retrospective Historical Reconstruction

## Decision being amended

The original Gate 2A required comparison against preserved Gate 1 route
outputs. Final recovery established that those original outputs and their exact
January source were not preserved. Strict Gate 2A is therefore impossible.

Gate 2A-R does not recover or reproduce Gate 1. It performs a new, paired,
retrospective reconstruction to test whether the substantive network conclusion
is stable across map vintages when both sides use one frozen procedure.

## Frozen scientific question

Do the nine gateway–destination connectivity classifications, dominant physical
corridors and route distances remain materially stable between an explicitly
documented January 2024 reference network and the network valid at
2024-06-12T20:29:59Z, when both are reconstructed with the same frozen code,
routing rules and node definitions?

## Frozen system

Gateways:

- South / Karaj: OSM node `31086990`
- East / Amol: OSM node `6208746864`
- West / Ramsar: OSM node `8595307908`

Destinations:

- Chalus: OSM node `1375231380`
- Nowshahr: OSM node `4998048119`
- Kelardasht: OSM node `3323917713`

Each identity and functional rationale must be confirmed in writing before
routing. If any node cannot be historically represented at both cutoffs, stop.

Event chronology is frozen as 13 June 2024 at approximately 20:30 local time
through documented reopening on 16 June 2024 in the afternoon. The historical
network cutoff remains 12 June 2024 at 23:59:59 local time. The earlier 13–14
June wording is formally superseded; it must not be silently retained.

Closure representation remains the supported bounded Darband segment centered
on OSM node `3294759340`, implemented through its relevant contiguous directed
road edges. It is not a flood footprint or exact engineering failure polygon.

## Mandatory source-provenance gate

Before any accepted calculation:

1. Document the acquisition source, date, geographic extent, header metadata
   and SHA-256 of both source networks.
2. Establish that the January candidate represents the declared January 2024
   cutoff. Filename alone is insufficient.
3. Record that its hash differs from the unavailable original hash.
4. If historical validity cannot be established, return NO-GO.

## Mandatory paired reconstruction

Create a clean environment and record:

- operating system and architecture;
- Python version;
- exact dependency versions and lockfile;
- hashes of every executable script;
- complete commands and random-state statement;
- input and output hashes.

Run January and June through the same graph builder, road filter, one-way logic,
restriction treatment, distance weighting, closure rule and output serializer.
Do not accept existing candidate JSON files as final results. They may be used
only to diagnose discrepancies after the clean run.

Routes 230/240 remain excluded. Do not add travel time, traffic, congestion,
EO-derived edge removal, new gateways, new destinations or new metrics.

## Required comparison

For each of the nine OD units report:

- connectivity: CONNECTED / CONNECTED WITH DETOUR / DISCONNECTED / ABSTAIN;
- baseline distance at each historical cutoff;
- closure-scenario distance at each historical cutoff;
- detour ratio and distance increase;
- dominant physical corridor;
- percentage difference between the January and June paired reconstructions.

The former heading `Gate 1 vs Gate 2A` is prohibited. Use
`January retrospective reference vs June historical reconstruction`.

## Stability rules

Pass only if:

1. all nine connectivity classifications are stable;
2. no dominant physical corridor changes because of unresolved topology;
3. every main route differs by no more than 2%, unless a larger correction has
   a verified historical explanation and leaves the qualitative interpretation
   unchanged;
4. gateway sensitivity remains low for connectivity;
5. destination-node sensitivity does not determine the substantive result;
6. all routes pass manual topology and infrastructure-availability QA;
7. the run is deterministic from the frozen environment and inputs.

Any unresolved Haraz topology, post-event motorway use, restriction ambiguity,
graph artefact or materially different reasonable reconstruction triggers
NO-GO.

## Evidence labels

Final distances must be labelled:

`MODELLED FROM PAIRED RETROSPECTIVE HISTORICAL NETWORKS`

Never label them observed trajectories, recovered Gate 1 results or original
Gate 1 values.

## Authorized conclusion ceiling

The strongest permitted conclusion remains:

> Disruption of a documented transport corridor altered modelled
> gateway-specific access distance to the selected tourism destinations.

No claims about tourists, cancellations, demand, occupancy, revenue,
destination resilience or required infrastructure investment are authorized.

## Output and stop point

Produce the Gate 2A sections A–N adapted to the paired retrospective design,
plus a provenance statement explaining why strict Gate 2A was impossible.

Do not authorize EO or Gate 2B automatically. Stop after the Gate 2A-R verdict
and state the remaining unanswered scientific question.
