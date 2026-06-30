# Witness Boundary

## Purpose

The witness layer exists to separate internal claims from externally reviewed claims.

## Witness categories

| Category | Meaning | Promotion effect |
|---|---|---|
| Internal note | creator or assistant statement | no independent promotion |
| Local run | result observed in local environment | E2 only |
| Independent reproduction | outside actor reproduces from instructions | E3 candidate |
| Signed witness | reviewer signs method/result | E4 candidate |
| Production audit | operational controls reviewed | E5 candidate |

## Template warning

A witness packet template is not a completed witness result.

Template-only files must be labeled:

`TEMPLATE_ONLY / NOT_INDEPENDENTLY_REPRODUCED`

## Required witness record

A completed witness record should include:

1. witness name or pseudonymous key
2. date/time
3. artifact ID
4. repository commit
5. environment
6. commands run
7. observed output
8. deviations
9. pass/fail verdict
10. signature or verifiable attestation method

## Current Codex witness status

`WITNESS_STATUS = PENDING`

The Codex is ready to receive witness packets. It does not yet globally claim independent witness confirmation.
