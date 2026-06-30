# CP8 Protocol

## Purpose

CP8 is the Codex promotion discipline. It prevents symbolic, speculative, prototype, and evidence-bearing claims from being collapsed into one authority layer.

## Core doctrine

**No claim outruns its evidence.**

## Promotion pipeline

```text
Seed → Artifact → Local Demo → Reproduction → Witness → Production
 E0      E1          E2             E3          E4        E5
```

## CP8 operators

| Operator | Working meaning | Role |
|---|---|---|
| AFG | artifact formation gate | define artifact identity and boundary |
| NSG | narrative separation gate | separate story from evidence |
| LRG | local reproduction gate | require commands, files, and local output |
| BFG | benchmark/falsification gate | require tests that can fail |
| FCG | final claim gate | only publish supported claim level |

## Required packet for technical promotion

A technical artifact seeking E3 or above should include:

1. artifact ID
2. source files
3. version
4. dependency list
5. deterministic run command
6. expected output
7. failure modes
8. hash or checksum
9. local run log
10. independent reproduction log

## Anti-theater tests

A CP8 artifact should be rejected or demoted if it relies on:

- vague claims without source files
- screenshots without runnable procedure
- AI-generated success narratives without logs
- unverifiable external events
- private keys or secrets inside repositories
- symbolic language presented as engineering proof
- template-only witness packets presented as completed reviews

## Current Codex-wide status

`CP8_GLOBAL_STATUS = PUBLICATION_READY / E3_PENDING_PER_ARTIFACT`

The Codex can be published as a bounded research and symbolic archive. Individual technical claims require per-artifact promotion.
