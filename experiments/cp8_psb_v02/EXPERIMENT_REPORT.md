# CP8 Physical-State Bridge v0.2 — Experiment Report

Generated: 2026-08-11T14:17:46.350255+00:00
Version: CP8-PSB-v0.2
Seed: 428  |  dt: 0.01  |  κ: 0.85
Safety limits: {"x_max": 1.6, "vx_max": 4.5, "theta_max": 0.95, "omega_max": 6.0}
HOS endpoint: local only

## Pass / Fail Criterion (declared a priori)
- Metric improved: corrected MSE (full & θ) < uncorrected MSE
- Zero constraint violations on the corrected trajectory
- Both conditions required for PASS

## Results by Noise Profile

### Profile: `gaussian` → **PASS**
- uncorrected MSE (full / θ): 0.244224 / 0.087108
- corrected   MSE (full / θ): 0.014596 / 0.000111
- improvement ratio (full / θ): 16.7325× / 785.8394×
- mean E_HOS: 0.545592
- constraint violations (uncorrected / corrected): 1 / 0
- Merkle root: `1c90a670feae7ea2cf5dfa66775aaf031982d700d12ad33158f58643bfe71724`
- receipts: 200  |  eval source sample: local

### Profile: `spike` → **FAIL**
- uncorrected MSE (full / θ): 0.858035 / 0.10354
- corrected   MSE (full / θ): 0.562518 / 0.016236
- improvement ratio (full / θ): 1.5253× / 6.3773×
- mean E_HOS: 0.755531
- constraint violations (uncorrected / corrected): 13 / 5
- Merkle root: `9e8f8d4e141ffe647cf1f3f7b6daf8d671be53e65b5cc6bd81044b83e48a4dbc`
- receipts: 200  |  eval source sample: local

### Profile: `bias_hf` → **PASS**
- uncorrected MSE (full / θ): 0.882118 / 1.331885
- corrected   MSE (full / θ): 0.052255 / 0.100261
- improvement ratio (full / θ): 16.8811× / 13.2842×
- mean E_HOS: 0.348347
- constraint violations (uncorrected / corrected): 163 / 0
- Merkle root: `2fd882b431c7eabf860839f34624a0ccec87bbb10eb3494e33937d529d3515aa`
- receipts: 200  |  eval source sample: local

## Aggregate Outcome
One or more profiles recorded FAIL under the declared criterion.

Evidence is the set of Merkle-rooted receipts and the metrics above.
No monetary claims. No additional cryptography beyond the existing SHA-256 / Merkle layer.
