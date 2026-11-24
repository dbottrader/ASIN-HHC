# ASIN-HHC / CP8 — Recovered Formula Catalog (Batch 001)

**Status:** PUBLICATION CANDIDATE — SOURCE-BOUNDED, NOT COMPLETE  
**Catalog ID:** ASIN-MATH-CATALOG-001  
**Prepared:** 2026-11-24  
**Repository:** `dbottrader/ASIN-HHC`  
**Purpose:** Preserve mathematical expressions recovered from currently accessible ASIN-HHC/CP8 artifacts, distinguish source transcription from independent verification, and make unresolved arithmetic visible.

> **Completeness boundary:** This is the first recovered catalog, not a claim that every formula ever developed in conversation has been recovered. The original ChatGPT HTML exports and the complete September 2025 conversation bodies are not currently available in the accessible Library. The September 6–8, 2025 source threads (Conversations 120–122 and 157–161) therefore remain an open recovery gate. Do not assign these later formal expressions to those early conversations without original message receipts.

## 1. Evidence and attribution rules

Each entry is classified as one of:

- **SOURCE-TRANSCRIBED** — formula appears in an accessible artifact; transcription is preserved, but the formula is not thereby validated.
- **ALGEBRA-CHECKED** — elementary arithmetic or symbolic consistency was independently checked here.
- **STANDARD-MATHEMATICAL-FORM** — a conventional mathematical definition used as a comparison or reconstruction aid; not claimed as an original discovery.
- **PROVISIONAL-RECOVERED-NOTE** — expression is present in prior project summaries/context but its original source file or message receipt has not yet been recovered.
- **UNVERIFIED-CLAIM** — associated empirical or scientific claim lacks sufficient reproducible evidence.

Source artifact currently available:
- `1_5057967467335256237.pdf` — *ASIN-HHC / CP8 Harmonic Algebra: Formal Definition Document*, 6 pages, Library file record dated 2026-07-01. The PDF itself attributes its generation to Kimi.ai. This is evidence that the expressions were recorded in that document, not proof that every derivation or empirical assertion is correct.

## 2. HHC frequency ratios and thresholds

### 2.1 Frequency anchors

**SOURCE-TRANSCRIBED**

```text
f1 = 428 Hz
f2 = 528 Hz
f3 = 963 Hz
f2/f1 = 528/428 ≈ 1.23364486
f3/f1 = 963/428 = 2.25 = 9/4
```

The exact ratio (963/428=9/4) is **ALGEBRA-CHECKED**.

### 2.2 Threshold equations as printed

**SOURCE-TRANSCRIBED — INTERNAL INCONSISTENCY FOUND**

The formal definition document prints:

```text
tau_soft = (528/428) * sqrt(3)/4 = 0.70
tau_hard = (963/428) * tau_soft * (2/3) = 1.85
```

Direct arithmetic gives:

```text
(528/428) * sqrt(3)/4 ≈ 0.5339
(963/428) * 0.70 * (2/3) = 1.05
(963/428) * 0.5339 * (2/3) ≈ 0.801
```

Therefore the printed equalities to 0.70 and 1.85 do not follow from the printed expressions. The document also describes 0.70 as empirically calibrated, but the supporting dataset and calibration procedure are not included in this source. Treat both threshold values and their derivation as **UNVERIFIED** pending source-data recovery and a reproducible calibration.

### 2.3 Gate ordering

The source prints a piecewise FCG rule using:
- ALLOW if (Delta_{717}(t) geq 	au_{soft})
- AMBER if (	au_{soft} > Delta_{717}(t) geq 	au_{hard})
- VETO if (Delta_{717}(t) < 	au_{hard})

With the document's stated values (	au_{soft}=0.70) and (	au_{hard}=1.85), the AMBER interval is empty because (0.70 > Delta geq 1.85) cannot be true. This is a **SOURCE-LEVEL LOGIC CONFLICT**, not a corrected implementation. A corrected threshold ordering must not be guessed; it requires an explicit design decision and tests.

## 3. Harmonic field and phase-coupling expressions

**SOURCE-TRANSCRIBED**

The document defines a three-oscillator superposition:

```text
H(t) = sum(i=1..3) A_i * exp(i * (omega_i*t + phi_i(t)))
omega_1 = 2*pi*428
omega_2 = 2*pi*528
omega_3 = 2*pi*963
```

Here (A_i) are amplitude weights and (phi_i(t)) are phase functions.

The printed Kuramoto-style phase equation is:

```text
d(phi_i)/dt = omega_i + (K/N) * sum(j=1..N) sin(phi_j - phi_i)
```

The source document reports (K=0.15) as an empirical healthy-dialectic setting and (K>0.25) as a collusion-detection trigger. Those are **UNVERIFIED EMPIRICAL CLAIMS** until the experiment, data, sample size, controls, and implementation are recovered. The displayed equation also needs an explicit definition of whether the oscillator index (i) ranges over the same (N) oscillators as the summation.

## 4. Kuramoto order parameter and Delta-717

**SOURCE-TRANSCRIBED**

```text
R(t) = (1/N) * abs(sum(i=1..N) exp(i*phi_i(t)))
Delta_717(t) = EMA(1 - R(t), tau_ema)
```

The document associates the label “717” with a canonical test seed. That naming history is source-reported; independent validation of the claimed first-validation event is not included in the PDF.

The document states the intended bounds:
- (0 leq R(t) leq 1)
- (0 leq Delta_{717}(t) leq 1)

These bounds depend on the implementation and EMA initialization/convention; test them in code rather than treating the prose invariant as proof.

## 5. CP8 invariant register (33 entries)

The source document groups 33 invariants into seven categories. These are transcribed as specification statements, not certified implementation properties.

### Integrity
- **I1:** (sum_i |A_i|^2 = 	ext{constant}) (claimed amplitude/energy conservation).
- **I2:** (R(t) geq 0).
- **I3:** (|H(t)| leq sum_i |A_i|).
- **I4:** Phase unwrapping is continuous; no unlogged (2pi) jumps.
- **I5:** Gate output is immutable once emitted (CGIR BLOCK).

### Causality
- **I6:** (dphi_i/dt) exists almost everywhere (source calls this Lipschitz continuity).
- **I7:** (phi_i(t)) depends only on prior-time values (phi_j(s<t)).
- **I8:** No retroactive gate-state changes (WORM ledger).
- **I9:** Transition entropy monotonically increases under thrashing.
- **I10:** Failure records are retained through archive/deferred-node flow.

### Coherence
- **I11:** (0 leq Delta_{717}(t) leq 1).
- **I12:** (0 leq R(t) leq 1).
- **I13:** (K geq 0).
- **I14:** (	au_{ema} geq 1).
- **I15:** Anomalies are archived and confidence labels updated.

### Safety
- **I16:** (	au_{soft}=0.70) (source-stated; derivation unresolved; see §2).
- **I17:** (	au_{hard}=1.85) (source-stated; derivation unresolved; see §2).
- **I18:** (	ext{HYSTERESIS_ENTRY}=2) consecutive breaches.
- **I19:** (	ext{HYSTERESIS_RECOVERY}=9) consecutive recovery observations.
- **I20:** Hard VETO is permanent once triggered.

### Transparency
- **I21:** Missing PipelineTrace makes execution invalid.
- **I22:** Every state transition is logged with a SHA-256 hash.
- **I23:** Confidence scores are exposed.
- **I24:** Missing log probabilities are logged, never fabricated.

### Reproducibility
- **I25:** Same seed produces same synthetic output; canonical seed stated as 717.
- **I26:** EMA state is deterministic given initial conditions.
- **I27:** Gate transitions can be replayed from the delta trace.
- **I28:** Hash-chain tampering is detected.
- **I29:** Exact-chain replay is required, not approximate reconstruction.

### Service
- **I30:** Build for humanity; outputs must meet the stated safety requirements.
- **I31:** Verify for eternity; claims carry an evidence ladder.
- **I32:** Each iteration improves the invariant set.
- **I33:** Falsifiable claims only; belief is not a substitute for evidence.

## 6. Five ANU-28 operator definitions

**SOURCE-TRANSCRIBED**

### AFG — Alignment Field Generator

```text
AFG(H(t)) = normalize(sum(i=1..3) w_i * A_i * exp(i*phi_i))
```

The source says (w_i) are learned from historical coherence data and normalization should ensure (|AFG|leq1). The normalization function and training procedure are not specified in the PDF.

### NSG — Narrative Shape Gateway

```text
NSG(narrative) = SHA256(canonical(narrative))
```

The source claims semantic canonicalization makes equivalent meanings hash identically despite different wording. Ordinary canonical serialization does not establish semantic equivalence; the semantic canonicalizer is unspecified. Treat semantic equivalence as **UNVERIFIED**.

### LRG — Loom Recursor Generator

```text
x^(0) = x
x^(n+1) = f(x^(n))
LRG(x,n) = x^(n)
MAX_DEPTH = 28
DIVERGENCE_THRESHOLD = 0.10
AMBER if abs(x^(n+1) - x^(n)) > 0.10
```

For vector or structured (x), the distance/norm used in the divergence test is not specified and must be defined by implementation.

### BFG — Bridge Field Gate

```text
BFG(input) = I5(input) AND I16(input) AND I20(input)
```

The exact executable predicates for I5, I16, and I20 must be specified in code. This expression is a Boolean composition at the specification level.

### FCG — Frequency Coherence Gate

The source's piecewise rule is transcribed in §2.3. Its printed thresholds make the AMBER interval empty; no silent correction is applied in this catalog.

## 7. Evidence ladder and watchdog

**SOURCE-TRANSCRIBED**

The formal document defines:

- **E1 — CLAIM:** (c>0.35).
- **E2 — LOCAL TEST:** (P(	ext{fail})<0.05) per test.
- **E3 — REPRODUCED:** seeds ({717,42,123,999,2026}).
- **E4 — INDEPENDENT:** subsystem B confirms subsystem A.
- **E5 — ECOSYSTEM:** stated adversarial suites (SLOW_POISON, BURST, COORDINATED) all pass.

The criteria need operational definitions. In particular, (c), the statistical meaning of per-test failure probability, test-suite contents, and independence criteria are not defined in the PDF.

Watchdog target printed in the source:

```text
T_WATCHDOG = 666.67 microseconds
670 microseconds floor (as separately stated)
```

The document also reports simulation timing figures (449 ns mean, 803 ns maximum) and an FPGA target. These are **SOURCE-REPORTED RESULTS**, not independently reproduced by this catalog.

## 8. Geometric, recursive, and signal-processing formulas in the recovered project notes

The following expressions are present in prior recovered project summaries, but their exact originating source files/message receipts have not yet been attached to this catalog. They are therefore **PROVISIONAL-RECOVERED-NOTE**, not original-export verified.

### Hexagonal lattice / centered-hexagonal count

```text
N(k) = 3*k*(k+1) + 1
```

This is the centered-hexagonal number formula. The convention for (k) (starting at 0 or 1) must be stated whenever used.

### Complex-plane sixfold step construction

```text
z_(n+1) = z_n + c_n
c_n = R * exp(i*n*pi/3)
```

This describes a six-direction step sequence when (R) is fixed. It is not by itself a general spiral equation; ordering and step-length rules matter.

### Golden-ratio recursion

```text
T_(n+1) = phi * T_n
phi = (1 + sqrt(5))/2
```

This is a geometric progression with ratio (phi), not the Fibonacci recurrence. Do not conflate the two.

### Logarithmic spiral

```text
r = a * exp(b*theta)
```

A standard logarithmic-spiral form; the values and interpretation of (a,b) must come from measured data.

### Fourier / discrete frequency analysis

**STANDARD-MATHEMATICAL-FORM** (comparison/reconstruction aid; not claimed as a recovered original equation):

```text
X[k] = sum(n=0..N-1) x[n] * exp(-i*2*pi*k*n/N)
```

A frequency mapping pipeline must specify sampling, ordering, windowing, normalization, frequency units, and null/control comparisons.

### Phyllotaxis / golden-angle construction

**STANDARD-MATHEMATICAL-FORM** (candidate model for reconstructing the September 2025 phyllotaxis work):

```text
theta_n = n * alpha
alpha = 2*pi*(1 - 1/phi^2) ≈ 2.3999632297 radians
       ≈ 137.507764 degrees
r_n = c * sqrt(n)
z_n = r_n * exp(i*theta_n)
```

This is a common sunflower/phyllotaxis point model. Its presence here does not establish that this exact equation appeared in Conversations 157–161. The original thread bodies are required for that attribution.

### Physical-state bridge metric

**SOURCE-TRANSCRIBED FROM A LATER PROJECT NOTE**

```text
E_HOS = 1 / (1 + ||Delta_x||_2)
```

The exact definition of (Delta_x), normalization, state dimension, and tested operating range must be recovered from the implementation before treating this as a validated metric.

## 9. Image-to-binary-to-frequency workflow (method, not a standalone formula)

The recovered historical summary describes this sequence:

1. Capture a screenshot or spiral image.
2. Order elements from center outward.
3. Map colors to bits.
4. Produce a binary stream.
5. Map the stream to frequencies.
6. Test in CodePen/Harmonizer.
7. Correct and revise.

This is a documented experimental workflow in the recovered summary. It does **not** establish that a source image contains an objectively encoded message. A reproducible implementation must define segmentation, color quantization, traversal order, bit mapping, framing, sampling rate, transform, controls, and hash receipts.

## 10. Open mathematical recovery and verification work

1. Recover original ChatGPT exports and message bodies for Conversations 120–122 and 157–161.
2. Extract exact equations, timestamps, model outputs, code blocks, and attachments.
3. Compare those originals with the later geometric report, Harmonic Algebra PDF, and executable code.
4. Recompute every printed numerical equality and repair no inconsistency without a recorded design decision.
5. Add unit tests and property tests for each implementable expression.
6. Record source hashes, code commit, runtime, inputs, outputs, and independent replay receipts.
7. Separate exploratory fits from confirmatory tests; use held-out data and negative controls.
8. Promote formulas individually only after reproducible evidence exists.

## 11. Current conclusion

This catalog preserves a substantial set of mathematical expressions across harmonic oscillators, phase coupling, coherence metrics, recursive operators, geometric constructions, and signal processing. It also records real inconsistencies in the formal definition document.

**No claim is made here that ASIN-HHC independently derives the Riemann zeta functional equation, proves a new law of nature, or establishes encoded messages in natural or aerial imagery.** Those questions require separate mathematical derivations and reproducible tests.

**Publication state:** source-bounded catalog; original-export recovery remains OPEN; formula-by-formula verification remains PENDING.
