# Changelog

## 1.4.0 — 2026-10-15 (candidate)

Backward-compatible PR metadata and readiness guidance.

- Added a G04/G09 contract for reviewer requests and submissions, draft/work/review/integration states, assignees, labels, Projects, milestones, and issue-closing links.
- Clarified that no reviews means awaiting review, not approved; a ready-for-review PR can still await review, while draft work remains in progress.
- Require repository conventions and authority for metadata changes; preserve unknown or optional fields instead of inventing values.
- Added package contract coverage and user-provided sidebar evaluation cases.
- Release status: candidate only; behavior evaluations remain incomplete.

## 1.3.0 — 2026-10-15 (candidate)

Backward-compatible repository-setup guidance.

- For every GitHub repository creation, derive a concise About description from the requested purpose and include it during creation; if the available creation path cannot set it, set it afterward when authorized.
- For existing repositories, preserve nonempty descriptions and add a description only when it is missing and the requested, authorized setup scope permits the metadata write.
- Added a repository-creation route and positive/negative behavior evaluation cases.
- Release status: candidate only; fresh-context evaluation and release gates remain incomplete.

## 1.2.0 — 2026-10-15

Backward-compatible branch planning and review-acceptance controls, plus installer race safety.

- Added a scale-aware branch strategy reference for short-lived task branches, parallel work, stacked changes, supported release lines, and monorepos.
- Added reviewer-comment dispositions and optional policy-required distinct auditor/reviewer sign-off tied to the current candidate head.
- Extended the advisory evidence checker to detect missing role approvals and reused identities; output now explicitly reports that it does not enforce policy.
- Changed installation to stage and verify before copying. A raced or partially published destination is preserved for inspection rather than recursively deleted.
- Synchronized the implementation/framework status, release/evaluation limits, and optional role evidence contract.
- Added regression tests for the publish race and role approvals, plus repeatable registry-path and Markdown-link checks. Fresh-context behavior trials for these new skill instructions remain pending.
- Release status: local package candidate only; installed v1.1.0 and hosted GitHub state were not changed.

## 1.1.1 — 2026-10-14

Documentation clarification linking the research loop to the existing external-query privacy contract.

- The learning-loop procedure now points directly to the existing authority and scope contract before preparing Context7 or Firecrawl queries.
- Evaluation: five no-skill and five v1.1.0 skill-on trigger samples passed. The behavior matched baseline; this patch makes the existing policy easier to find at the point of use and does not claim a measured behavior improvement.
- Release status: locally packaged only; installed v1.1.0 copy was not changed.

## 1.1.0 — 2026-10-14

Backward-compatible addition of a governed lesson-promotion and skill-release workflow.

- Added patch/minor/major classification and migration guidance for breaking changes.
- Added owner approval, positive and negative regression evaluations, package validation, changelog, checksum, and release gates.
- Clarified that local packaging is not a Git commit, tag, hosted GitHub release, or installation update.
- Evaluation status: four promotion/release cases reviewed against the procedure; review was static, not an independent fresh-context run. Existing Python suite: 14 tests pass. Native host discovery remains unverified.
- Release status: locally packaged; no repository remote was available for a hosted release.
