# Pull request metadata and readiness

Use this checklist in G04 when preparing a pull request and in G09 when reviewing its readiness or integration state.

## Keep these states separate

- **Work state:** draft or explicitly incomplete work remains in progress.
- **Review state:** distinguish reviewers requested from review submissions received. No submitted reviews means `awaiting_review`; it does not mean approved. A non-draft PR may be ready for review while still awaiting reviews.
- **Integration state:** unmerged remains unintegrated. Do not call a PR accepted or merge-ready until current-head reviews, required checks, blocking comments, and policy gates pass.

Do not infer draft/readiness from an empty sidebar. Inspect the PR state and current diff. Report unknown values as unknown.

## Inspect PR sidebar metadata

Check each field against repository conventions and the task's scope:

- **Reviewers:** identify required reviewers from confirmed policy, CODEOWNERS, or explicit direction. Request them only when authorized. “No reviews” means no review submission is observed; it does not establish whether reviewers were requested.
- **Assignees:** use a confirmed accountable owner or explicit assignment. Do not assign the author or another person by default.
- **Labels:** apply only existing, relevant labels supported by repository conventions or explicit direction. Do not invent labels.
- **Projects:** link only the confirmed project and item when tracking is in scope and authorized.
- **Milestone:** select only an existing, confirmed milestone that matches the accepted plan. Do not infer one from a date or version.
- **Development / linked issues:** use closing keywords only when merging this PR should close that issue. For partial work or related context, use a non-closing reference. Never invent issue links.

## Report and stop conditions

Return the observed draft/work state, review-request state, submitted-review state, integration state, and each metadata field as set, missing, or unknown. Record proposed values separately from values actually written. Leave optional fields unset when no grounded value exists; surface required missing metadata or reviews as blockers. A recommendation does not authorize a GitHub write.
