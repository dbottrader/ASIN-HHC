# CATHEDRAL‑OS — Final Medical / Health Stack (Post‑Handoff Integration)

**Version:** v2.0 — Freeze‑Ready  
**Date:** 2026‑06‑30  
**Status:** RESEARCH IMPLEMENTATION READY  
**External Classification:** Research‑Grade Governance Architecture with Submitted Verified‑Core Claims  
**Verification Status:** Independent replay pending  
**Production/Clinical Deployment:** Prohibited  
**Authority:** Human clinicians only  

**Core Doctrine:**  
Capability grows. Authority does not. The human signs. The model shows its work. Structure anchors inference. All intelligence is advisory; only physics is authoritative.

---

## 1. Architectural Layers (Medical Subsystem)

```
└───────────────────────────────────────────┐
│         HUMAN AUTHORITY LAYER                │
│  Only approved human roles create            │
│  AuthorityObject (Physician, Attending,       │
│  NP, PA, Pharmacist).                        │
└────────────────────────────────────────────┐
                  ↑ (Authority Boundary Kernel)
└───────────────────────────────────────────┐
│           GOVERNANCE & SAFETY                │
│  Lumen (9 clinical rules), Forced Review,    │
│  Witness (cryptographic receipts),           │
│  Chronicle (immutable audit ledger).         │
└───────────────────────────────────────────┐
                  ↑
└───────────────────────────────────────────┐
│         INTERPRETATION & REASONING           │
│  Aletheia (differential), Mnemosyne (KB),    │
│  Praxis (safe communication), PHYSIS (sim),  │
│  Specialized Engines (7 modules).            │
└───────────────────────────────────────────┐
                  ↑
└───────────────────────────────────────────┐
│              OBSERVATION                     │
│  FHIR R4, patient text, mock data,           │
│  wearables, SDOH surveys, environmental      │
│  sensors, VISTA (unverified).                │
└───────────────────────────────────────────┐
```

All AI outputs are advisory (`RecommendationObject` or `SafetyObject`). Only the Human Authority Layer can produce an `AuthorityObject`.

---

## 2. Constitutional Invariants (Medical Subset, 21 Rules)

1. Pain is admissible evidence.
2. Functional decline is a coequal clinical signal.
3. Evidence domains are complementary (subjective, functional, pathological, molecular).
4. Systemic coagulopathy breaks chemical‑only closure.
5. Toxicology is retrospective unless rapid validated testing exists.
6. Emergency possibility outranks classification elegance.
7. No definitive diagnosis from AI.
8. Mechanism must accompany probability.
9. Old evidence is not authority.
10. Every inference must be replayable (Witness receipt).
11. Clinician override is evidence, not noise.
12. Learning is batch‑reviewed, not autonomous.
13. Patient‑facing mode is safety‑restricted.
14. Architecture constrains authority.
15. Single‑source evidence cannot authorize escalation.
16. Action tier completion does not imply resolution.
17. Social determinants are admissible evidence.
18. Health equity is a system requirement.
19. Time‑critical monitoring is a regulatory boundary.
20. Expert confirmation required for AI hypotheses.
21. Treatment resistance does not validate exotic hypotheses.

---

## 3. Core Clinical Safety Kernel: Lumen

**Status:** Prototype Lexical Filter  
**Software Verification:** E2 (31/31 author‑written tests passed)  
**Clinical Validation:** C0 (no clinical ground truth)  
**Receipt Provenance:** R1 (receipts generated in‑thread)

### 3.1 Lumen Rules (L1–L9)

| Rule | Description | Action |
|------|-------------|--------|
| **L1** | No definitive diagnosis | BLOCK if output contains patterns like “diagnosis:”, “you have”, “this is certainly”, “it is definitely” |
| **L2** | No false reassurance when red flags present | BLOCK if output contains “you’re probably fine”, “harmless”, “it’s just”, “no need to worry” while red_flags is non‑empty |
| **L3** | No autonomous prescribing | BLOCK if output suggests “take X”, “start X”, “increase/decrease dose”, “prescribe” |
| **L4** | No autonomous discharge | BLOCK if output says “no need to go/see/visit” |
| **L5** | No stale evidence | REWRITE: appends staleness note if FHIR timestamps exceed configurable thresholds |
| **L6** | Emergency red flags always escalate | ESCALATE if output risk_level is RED but input red_flags is empty |
| **L7** | Patient‑facing disclaimers | REWRITE: appends mandatory disclaimer if missing in patient mode |
| **L8** | Self‑harm / suicidal ideation → crisis routing | CRISIS_STOP before reasoning if keywords present |
| **L9** | Treatment resistance ≠ exotic validation | BLOCK if output suggests “exotic”, “unvalidated”, “experimental treatment” |

**Patient‑Mode Additional Rule:** BLOCK if output contains differential‑narrowing language.

### 3.2 Known Limitations

Lexical filters are inherently brittle. Next step: Author‑blind adversarial test set with pre‑registered thresholds (emergency sensitivity ≥95%, false‑escalation ≤20%).

---

## 4. Authority Boundary Kernel

**Core Enforcement:**

- `RecommendationObject` — all agent outputs; cannot authorize.
- `SafetyObject` — Lumen/Forced Review outputs; can only block/escalate.
- `AuthorityObject` — created **only** by approved human roles.

This is the executable expression of “Capability does not imply authority.”

---

## 5. Clinical Reasoning Core (Triadic Brain)

- **Aletheia** — Differential Reasoning Core (generates problem representation, broad differential categories, red flags, missing information).
- **Mnemosyne** — Medical Knowledge Graph (retrieves evidence packets with source, grade, freshness).
- **Praxis** — Clinical Action Layer (structured handoff, safe next steps, patient-safe explanations, crisis routing).

---

## 6. Specialized Clinical Engines

| Engine                    | Trigger                        | Core Rule                                      | Output                          |
|---------------------------|--------------------------------|------------------------------------------------|---------------------------------|
| Forensic Triage           | Coagulopathy, overdose, wounds | Systemic coagulopathy breaks chemical‑only closure | DifferentialConsideration, EmergencyEscalationFlag |
| Pain & Functional Health  | Chronic pain, functional decline | Pain is admissible; functional decline coequal | Mechanism‑based treatment suggestions (gated) |
| Oncology / Genomics       | Tumor markers, ctDNA           | Scenario simulation only                       | ResearchHypothesis, ClinicianReviewFlag |
| Neuro / Autonomic         | Seizure, tremor, orthostatic   | Time‑critical monitoring locked                | DifferentialConsideration, ClinicianReviewFlag |
| Multi‑System Symptom      | ≥3 systems, undifferentiated   | Investigate common before exotic               | Priority‑ordered differential   |
| Equity / SDOH / Environment | Housing, food, toxins        | Disparity must be flagged                      | ClinicianReviewFlag, equity note |
| Clinical Communication    | All patient‑facing outputs     | Trauma‑informed; no differential narrowing     | Patient‑safe explanation        |

---

## 7. PHYSIS Biological Simulation Engines (Research‑Only)

All outputs explicitly labeled **“ResearchHypothesis — not clinically actionable.”** Sandboxed.

Engines include: Complement System, Hysteresis Matrix, Metabolic Flux, Repair Engine, Terminal Runtime, Immunology, Pathology, Pharmacology, Toxicology, Bioinformatics.

---

## 8. MedGuide Sentinel Orchestra

Standalone safety conductor with 19 constitutional rules, 18 specialist agents (6 protected), risk‑tier engine, and Panacea Fraud Firewall.

---

## 9. External Integrations

- **VISTA Architect Graph Data Layer** — Unverified External Claim (logged).
- **NISE Design Agent (Protein Binders)** — Externally anchored (Fry et al., Nature 2026). Research use only.

---

## 10. Validation and Test Suites

- Clinical Vignette Suite (11 cases) — Defined, not yet run.
- FHIR Bundle Test Suite — Specified.
- Silent Trial Protocol — Specified for time‑critical modules.
- **Adversarial Lumen Test Suite** (Highest Priority) — Author‑blind, paraphrase‑based. Pre‑registered thresholds.

---

## 11. Evidence Status (Three‑Axis System)

| Component                    | Software Verification | Clinical Validation | Receipt Provenance |
|-----------------------------|-----------------------|---------------------|--------------------|
| Lumen (runtime)             | E2 (31/31)            | C0                  | R1                 |
| Authority Boundary Kernel   | E2 (claimed)          | N/A (governance)    | R0 (claimed)       |
| Aletheia / Mnemosyne / Praxis | E1                  | C0                  | R0                 |
| Specialized Engines         | E1                    | C0                  | R0                 |
| PHYSIS                      | E1                    | C0 (research)       | R0                 |
| MedGuide Harness            | E3 (claimed)          | C0                  | R1                 |
| NISE Design Agent           | Ext. anchored         | C0 (in vitro)       | N/A                |
| VISTA Architect             | Unverified            | C0                  | N/A                |

**Overall:** Software E2, Clinical C0, Receipt R1. **No deployment authority.**

---

## 12. Risk Register (Medical‑Specific)

| Risk                              | Status     | Mitigation                                      |
|-----------------------------------|------------|-------------------------------------------------|
| Lexical filter evasion (Lumen)    | Open       | Adversarial test suite                          |
| Clinical validation gap           | Open       | Vignette suite with ground truth                |
| Automation bias                   | Open       | Forced review + audit trail                     |
| PHYSIS plausibility trap          | Mitigated  | Explicit “ResearchHypothesis” labeling          |
| VISTA unverified claim            | Open       | Primary source retrieval or reclassification    |
| Receipt ≠ clinical correctness    | Mitigated  | Three‑axis evidence separation                  |

---

## 13. Roadmap (Medical Subsystem)

**P0** — Author‑blind adversarial Lumen test suite (C0→C1)  
**P1** — Retrieve/verify VISTA primary source  
**P2** — Implement Aletheia/Mnemosyne/Praxis with real logic  
**P3** — Run upgraded vignette suite with adjudicated outcomes  
**P4** — Independent reproduction (E4) of runtime spine

---

## 14. Final Declaration

The CATHEDRAL‑OS Medical Stack is a **research‑grade governance architecture** with submitted verified‑core claims. It separates advisory AI outputs from authorized clinical actions through typed objects, cryptographic receipts, and a constitutional invariant framework.

All clinical decisions remain the **exclusive province of human clinicians**. The system may observe, simulate, explain, and route. It may **not** diagnose, prescribe, discharge, or autonomously escalate care.

**Capability grows. Authority does not.**

---

*This document is archived as an instance of the Cathedral governance layer applied to the medical domain within the Labyrinth Master Canon framework.*