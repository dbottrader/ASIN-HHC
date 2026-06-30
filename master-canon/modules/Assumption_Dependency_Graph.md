# Assumption Dependency Graph + Decision Stability Monitor

**Module:** v8.3 Candidate Extension  
**Status:** E1 Architecture  
**Date:** 2026-06-30  
**Authority:** None (specification only)  
**Promotion Blockers:** Implementation, test vectors, replay receipts, contradiction propagation tests, governance review

---

## Purpose

Preserve and actively monitor the dependency structure beneath claims, decisions, recommendations, and authority grants.

The system must detect when changed reality invalidates, weakens, or destabilizes prior reasoning — turning institutional memory from a passive archive into a **living diagnostic system**.

---

## Core Insight

A decision is not only justified by evidence.  
It is justified by a **weighted dependency structure over assumptions about reality**.

Some assumptions are:
- Supporting conditions
- Load-bearing
- Catastrophic if contradicted

Therefore the system must distinguish:

- **Minor assumption changed** → Note / monitor
- **Important assumption changed** → Review recommended
- **Critical assumption changed** → Decision unstable
- **Fatal assumption contradicted** → Decision reopened or revoked

---

## Architectural Position

```
Judgment Reconstruction
        ↓
Assumption Dependency Graph          ← New Module
        ↓
Decision Stability Monitor           ← New Module
        ↓
Delta Engine
        ↓
ReopenTicketObject
```

This module sits between **Judgment Reconstruction** and the **Delta Engine**, providing the missing structure for ongoing validity monitoring.

---

## Assumption Object (Minimum Shape)

```json
{
  "assumption_id": "string",
  "decision_context_id": "string",
  "assumption_text": "string",
  "assumption_type": "regulatory | technical | financial | clinical | operational | security | market | model | vendor | recovery | other",
  "dependency_ids": ["assumption_id"],
  "supported_claim_ids": ["claim_id"],
  "supported_decision_ids": ["decision_id"],
  "criticality": "low | medium | high | critical | fatal",
  "weight": 0.0,
  "confidence": 0.0,
  "evidence_ids": ["evidence_id"],
  "contradiction_ids": ["contradiction_id"],
  "last_verified_at": "datetime",
  "verification_status": "unverified | current | stale | contradicted | retired",
  "decay_rule": "string",
  "reopen_threshold": "string",
  "owner": "string"
}
```

---

## DecisionContextObject Extension

Every `DecisionContextObject` should include:

```json
{
  "decision_context_id": "string",
  "assumption_graph_id": "string",
  "critical_assumptions": ["assumption_id"],
  "dependency_root_ids": ["assumption_id"],
  "instability_score": 0.0,
  "reopen_policy": "manual_review | automatic_reopen | automatic_suspend | automatic_revoke"
}
```

---

## Delta Engine Monitoring Triggers

The Delta Engine should monitor for events such as:

- New regulation contradicts assumption
- Risk model threshold changes
- Clinical validation remains C0
- Vendor dependency becomes unsupported
- Evidence expires
- Witness status expires
- Model performance degrades
- Recovery target is missing
- Business constraint changes
- New contradiction arrives
- Prediction fails

When triggered, instability is propagated:

```
Changed Observation
  → affected Assumption
    → affected Claim
      → affected Decision Context
        → affected Decision
          → ReopenTicketObject
```

---

## ReopenTicketObject

```json
{
  "reopen_ticket_id": "string",
  "trigger_type": "assumption_changed | contradiction_added | evidence_expired | regulation_changed | risk_changed | prediction_failed | dependency_missing",
  "triggering_object_id": "string",
  "affected_decision_ids": ["decision_id"],
  "affected_claim_ids": ["claim_id"],
  "criticality": "low | medium | high | critical | fatal",
  "instability_score": 0.0,
  "required_review": "none | analyst | governance | clinical | security | executive",
  "recommended_action": "monitor | review | suspend | revoke | revalidate",
  "created_at": "datetime",
  "status": "open | under_review | resolved | accepted_risk"
}
```

The `ReopenTicketObject` preserves **why** a decision was triggered for reopening.

---

## Evidence Status

| Dimension              | Status     |
|------------------------|------------|
| Architecture           | E1         |
| Implementation         | None       |
| Test Vectors           | None       |
| Replay Receipts        | None       |
| Contradiction Tests    | None       |
| Governance Review      | Pending    |

**Promotion Status:** Specification only. Not to be treated as implemented without code, logs, receipts, and tests.

---

## Integration Notes

- This module is fully coherent with the **Labyrinth Master Canon** (LMC) principles of provenance, evidence discipline, and human-governed decision systems.
- It extends the **Evidence Ladder** concept from static initial validation into **ongoing validity monitoring**.
- It pairs naturally with **ANU-28** symbolic packets and **ML-DSA** cryptographic signing for auditable, long-term decision integrity.

---

**This module is submitted as a v8.3 Candidate Extension to the Continuity Engineering / Judgment Reconstruction framework.**