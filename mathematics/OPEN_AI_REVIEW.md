# Open AI Review Instructions — ASIN-HHC Mathematics Archive

The ASIN-HHC mathematical archive is published for adversarial review. This is an invitation to test, not an invitation to endorse.

## Review objective

Audit every formula, equation, algorithm, metric, empirical statement, and mathematical interpretation in:
- `mathematics/RECOVERED_FORMULA_CATALOG_001.md`
- `mathematics/FORMULA_CANDIDATES_002.md`
- `mathematics/AI_TRIAGE_REGISTER_001.md)
- Existing ASIN-HHC repository code and documents cited by those catalogs.

## Required output

For each item:
1. Quote the exact source expression and location.
2. Classify it: standard mathematics, source-transcribed formula, code-observed behavior, under-specified proposal, empirical claim, hypothesis, metaphor, or unsupported/AI-generated assertion.
3. Independently recompute the arithmetic.
4. Check dimensional consistency and definitions of every variable.
5. Determine whether the code implements the expression.
6. Run or propose tests, including negative controls.
7. Identify source dependence, circular reasoning, prompt contamination, and common-model agreement.
8. Return a correction proposal without overwriting the original expression.
9. State what evidence would change your conclusion.

## Do not

- Invent missing historical formulas.
- Claim a formula is novel because it is absent from this limited corpus.
- Treat multiple models repeating the same source as independent verification.
- Infer physical, biological, therapeutic, cryptographic, or cosmological effects from symbolic language.
- Call an experiment reproduced without publishing its inputs, environment, code revision, outputs, and receipts.
- Promote the Riemann zeta connection without a complete derivation.

## Response schema

Use the JSON schema in `AI_TRIAGE_REGISTER_001.md`. Include a human-readable summary of strongest results, failed claims, unresolved questions, and the three highest-value experiments.

## Historical boundary

The original ChatGPT HTML exports and the complete message bodies for September 6–8, 2025 (Conversations 120–122 and 157–161) are not in the accessible corpus used for this publication. Any statement about the exact equations in those conversations must remain provisional until the original records are recovered.

## Invitation

Open an issue or pull request with reproducible findings. Preserve dissent. Challenge the math, not the person. Publish corrections with provenance.
