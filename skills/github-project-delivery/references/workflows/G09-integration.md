# G09 — Integration

**Trigger:** Review, merge, or otherwise integrate a proposed candidate.
**Inputs:** Exact base/head, raw diff, review comments and dispositions, policy-required auditor/reviewer roles, approvals, required checks, ownership, merge policy, dependencies.
**Capability assumptions:** A connector may lack review, policy, or merge access; unavailable live gates cannot be inferred.
**Actions:** Follow the [review and acceptance contract](../contracts/review-and-acceptance.md); inspect the candidate; classify and verify every material comment; refresh checks and approvals against current head; verify live policy and authority; integrate only if authorized; record the actual result.
**Output:** Comment dispositions, role-specific acceptance state, and observed integration state, with evidence links.
**Exit and recovery:** Any stale gate, unresolved blocking comment, changed candidate, missing required role, or unknown authority returns to review/verification. Record a failed integration attempt without claiming success.
**Authority limit:** Approval of a review or passing old checks does not authorize or prove a merge.
