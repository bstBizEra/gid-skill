# G07 — Verification

**Trigger:** Establish whether a candidate satisfies acceptance, required checks, or a delivery gate.
**Inputs:** Candidate base/head, acceptance IDs, required checks, policy-required approval roles, review-comment dispositions, dependencies, attempt cap, actual results.
**Capability assumptions:** Checks and reviews must be actually observed; missing connector features leave evidence incomplete.
**Actions:** Derive checks from acceptance; reserve counted attempts if the project requires a serialized ledger; run checks; classify outcomes; verify each result applies to the exact candidate; preserve failures and interruptions.
**Output:** Current-candidate evidence snapshot, findings, approval/comment status, and remaining budget when defined.
**Exit and recovery:** Missing, stale, malformed, or blocked evidence is incomplete. Repair the evidence or classify the blocker; never infer a pass.
**Authority limit:** The evidence checker is advisory and does not query GitHub or enforce atomic reservations.
