# ASIN-HHC / CP8 / Labyrinth Implementation Index — 2026-06-30

**Repository:** `dbottrader/ASIN-HHC`  
**Publication path:** `publications/ASIN_HHC_CP8_LABYRINTH_IMPLEMENTATION_INDEX_2026-06-30.md`  
**Status:** Implementation/code publication index

## Purpose

This index maps the available code and implementation-facing files in the vault to their role in the ASIN-HHC / CP8 / Labyrinth cascade.

The source manifest already records byte sizes, line counts, and SHA-256 hashes. This file explains how the code-facing artifacts should be interpreted.

## Implementation-Facing Files

### Labeling / Evidence Gate

- `epistemic_labeler.py`
- `label_schema.py`
- `label_validator.py`
- `labeling_tests.py`
- `test_labeling_to_reality_gate.py`
- `LABELING.md`

**Role:** Evidence classification, validation, and reality-gate discipline.

**Evidence classification:** Implemented locally / test-candidate, pending confirmed CI receipts.

### Forge

- `forge_semantic.py`
- `forge_graph.py`
- `forge.json`
- `forge_graph.toml`
- `forge_semantic.toml`
- `forge_rules.md`
- `forge_process.md`
- `forge_overview.md`
- `forge_at_scale.md`
- `backforge_protocol.md`
- `FORGE_FINDINGS_2026-05-02.md`
- `miniforge_prompt.md`
- `ForgeConsole.jsx.txt`

**Role:** Semantic transformation, graph reasoning, findings, process documentation, console interface, and scale protocol.

**Evidence classification:** Architecture/specification plus local implementation artifacts; public runnable status requires committed source, dependency manifest, tests, and receipt.

### Labyrinth OS

- `Labyrinth-OS.txt`
- `Labyrinth-OS-Core-v8.txt`
- `Labyrinth-OS-Agent-v5.txt`
- `Labyrinth-OS-Full-Contents_20260606_201407.txt`
- `weaver_quillan_labyrinth_registry.html`

**Role:** Executive HQ, project routing, canonical governance, portfolio status, and registry interface.

**Evidence classification:** Architecture/reference corpus; not itself proof of operational deployment.

## Required Promotion Path

For any file to move beyond reference/artifact status:

1. Commit exact source bytes.
2. Attach dependency/environment manifest.
3. Run tests.
4. Publish raw test logs.
5. Generate receipt.
6. Bind receipt to commit SHA.
7. Reproduce from clean clone.
8. Obtain independent witness if claiming E4.

## Current Boundary

This index is a public repository artifact. It does not claim that every listed code file has been fully published as source in this repository yet. It points to the vault source manifest and defines the path for complete code import and promotion.

## Canonical Status

```json
{
  "artifact": "ASIN_HHC_CP8_LABYRINTH_IMPLEMENTATION_INDEX_2026-06-30.md",
  "classification": "IMPLEMENTATION_INDEX",
  "evidence_level": "E1/E2_REFERENCE_ARTIFACT",
  "not_promoted_to": [
    "public runnable artifact",
    "independent reproduction",
    "operational deployment"
  ]
}
```
