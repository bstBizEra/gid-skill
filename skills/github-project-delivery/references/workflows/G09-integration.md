# G09 — Integration

**Trigger:** Review, merge, or otherwise integrate a proposed candidate.
**Inputs:** Exact base/head, raw diff, review comments and dispositions, policy-required auditor/reviewer roles, approvals, required checks, ownership, merge policy, dependencies.
**Capability assumptions:** A connector may lack review, policy, or merge access; unavailable live gates cannot be inferred.
**Actions:** Follow the [review and acceptance contract](../contracts/review-and-acceptance.md) and [PR metadata/readiness checklist](../contracts/pull-request-readiness.md); inspect the candidate and sidebar fields; classify and verify every material comment; distinguish requested reviewers from submitted reviews; refresh checks and approvals against current head; verify live policy and authority; integrate only if authorized; record the actual result.
**Output:** Comment dispositions, PR work/review/integration states, observed or missing metadata fields, role-specific acceptance state, and evidence links.
**Exit and recovery:** Any stale gate, unresolved blocking comment, changed candidate, missing required role/reviewer, or unknown authority returns to review/verification. No reviews means review is pending, not approved. Record a failed integration attempt without claiming success.
**Authority limit:** Approval of a review or passing old checks does not authorize or prove a merge.
