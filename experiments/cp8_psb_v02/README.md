# CP8 Physical-State Bridge v0.2

This directory preserves the v0.2 experiment lineage in the ASIN-HHC repository.

## Source status

The experiment record was supplied in the CP8 working conversation. The original implementation file `cp8_psb_v02.py` and its raw output artifacts were not present in the connected GitHub search at the time of publication, so they are **not reconstructed or fabricated here**.

The supplied results and protocol are preserved in `EXPERIMENT_SPEC.md`.

## Result signature

- gaussian: PASS, 785.8x theta-MSE improvement, 1 -> 0 violations
- spike: FAIL, 6.4x theta-MSE improvement, 13 -> 5 violations
- bias_hf: PASS, 13.3x theta-MSE improvement, 163 -> 0 violations

The spike FAIL is retained as a valid falsifiable safety result.
