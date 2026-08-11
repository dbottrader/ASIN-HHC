# CP8 Physical-State Bridge v0.2

## Status

Experiment specification and result record supplied in the CP8/ASIN-HHC working corpus.

## State

`[x, vx, theta, omega]`

2-DOF cart-pole.

## HOS

`E_HOS = 1 / (1 + ||Delta x||_2)`

## Authority bound

`kappa = 0.85`

The declared bound is treated as physical authority, not as an arbitrary tuning knob.

## Experiment

- seed: 428
- dt: 0.01
- steps: 200
- profiles: gaussian, spike, bias_hf

## A-priori PASS criterion

Corrected MSE (full state and theta) must be lower than uncorrected MSE **and** the corrected trajectory must have zero constraint violations.

## Results

| Profile | Status | theta MSE uncorrected -> corrected | Improvement | Violations uncorrected / corrected | mean E_HOS |
|---|---|---:|---:|---:|---:|
| gaussian | PASS | 0.0871 -> 0.0001 | 785.8x | 1 / 0 | 0.546 |
| spike | FAIL | 0.1035 -> 0.0162 | 6.4x | 13 / 5 | 0.756 |
| bias_hf | PASS | 1.3319 -> 0.1003 | 13.3x | 163 / 0 | 0.348 |

## Interpretation

The spike profile is an intentional FAIL. The correction improves the metric but does not eliminate all constraint violations. The experiment records the residual violations instead of exceeding the declared correction authority. This is the intended safety/falsifiability behavior.

## Verified properties claimed by the experiment record

- `E_HOS` formula generalizes to the four-state cart-pole.
- `bounded_correction()` prevents runaway correction under impulse disturbance.
- Constraint violations are counted rather than hidden.
- SHA-256 receipts are deterministic and replayable.
- Merkle-chain verification is deterministic and replayable.
- The HOS API client can fall back to the local deterministic implementation.
- PASS/FAIL criteria are declared a priori and enforced.
- Failure is a valid experimental outcome.

## Expected artifacts

```text
cp8_psb_v02.py
cp8_psb_v02_output/
  EXPERIMENT_REPORT.md
  summary.json
  receipts_last.json
  merkle_root_last.txt
```

## API integration

Optional remote endpoint:

`POST /v1/harmonic-state`

The client uses standard-library `urllib` and falls back to the local deterministic HOS path on network or schema failure.

## Hardware bridge

The simulator state vector maps directly to encoder-based hardware or ROS/serial input:

```text
simulator
   -> serial.read() / ROS topic
   -> [x, vx, theta, omega]
   -> HOS
   -> bounded_correction()
   -> constraint checking
   -> receipt
   -> SHA-256
   -> Merkle chain
   -> PASS / FAIL
```

## Evidence boundary

This file records the supplied v0.2 experimental claims and results. It is not a substitute for the missing original `cp8_psb_v02.py` source or raw receipt files. Those should be added verbatim when the source artifact is available.
