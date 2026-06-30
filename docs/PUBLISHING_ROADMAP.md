# Publishing Roadmap

## Goal

Turn the scattered ASIN-HHC / CP8 / LOOM work into a clean public Codex that outsiders can read, review, cite, and reproduce.

## Phase 1 — Publication spine

Status: `IN_PROGRESS`

Tasks:

- Add Codex index.
- Add evidence boundary.
- Add artifact registry.
- Add CP8 protocol summary.
- Add witness boundary.
- Add manifest.
- Add license placeholder.

## Phase 2 — Artifact import

Status: `NEXT`

Tasks:

- Import master JSON bundles into `/artifacts/master-bundles/`.
- Import LOOM PDFs/HTML into `/loom/`.
- Import prototype HTML into `/public/`.
- Add SHA-256 hashes for each imported artifact.
- Add source repository and source date for each artifact.

## Phase 3 — Technical normalization

Status: `NEXT`

Tasks:

- Convert scattered prototype scripts into reproducible folders.
- Add dependency manifests.
- Add local run instructions.
- Add minimal tests.
- Add GitHub Actions verification.
- Add artifact hash check script.

## Phase 4 — Public documentation

Status: `NEXT`

Tasks:

- Write human-readable project overview.
- Write glossary.
- Write FAQ.
- Write contributor guide.
- Write claim-classification guide.
- Add diagrams and schematics where appropriate.

## Phase 5 — Witness packets

Status: `PENDING`

Tasks:

- Create witness packet template.
- Invite independent reviewers.
- Record reproduction attempts.
- Promote only artifacts that pass.

## Phase 6 — Release

Status: `PENDING`

Tasks:

- Tag `v0.1.0-codex-public`.
- Generate release notes.
- Attach artifact bundle.
- Publish README announcement.

## Immediate next actions

1. Merge this publication branch after review.
2. Create or rename a dedicated repo to `ASIN-HHC-CODEX` if desired.
3. Copy verified source artifacts into the Codex structure.
4. Run hash manifest generation.
5. Publish public release `v0.1.0-codex-public`.
