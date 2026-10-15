# Pull request metadata and readiness

Use this checklist in G04 when preparing a pull request and in G09 when reviewing its readiness or integration state.

## Keep these states separate

- **Work state:** draft or explicitly incomplete work remains in progress.
- **Review state:** distinguish review requests from submitted reviews and their decisions. No submitted reviews means `awaiting_review`; it does not mean approved or prove that nobody was asked to review. A non-draft PR may be ready for review while still awaiting reviews.
- **Integration state:** unmerged remains unintegrated. Do not call a PR accepted or merge-ready until current-head reviews, required checks, blocking comments, and policy gates pass. Use the merge box for current merge blockers; a missing review alone does not establish the complete merge state.

When asked whether a PR is “still in progress,” inspect its authoritative PR state (`open`, `closed`, or merged), draft flag (`isDraft`), current diff/acceptance, review requests, submitted review decisions, checks, and merge box. A draft cannot be merged; a PR marked ready for review can still be open, unapproved, or blocked from merging. An empty sidebar or the phrase “Still in progress?” does not establish any of those states. Report unknown values as unknown.

## Inspect PR sidebar metadata

Check each field against repository conventions and the task's scope:

- **Reviewers:** identify required reviewers from confirmed policy, CODEOWNERS, or explicit direction. Request them only when authorized. Treat “No reviews” as literal sidebar wording; by itself, it establishes neither the review-request state nor the submitted-review state. Inspect review requests and submitted review decisions separately. Do not treat the wording as approval or as proof that nobody was asked to review.
- **Assignees:** use a confirmed accountable owner or explicit assignment. Do not assign the author or another person by default.
- **Labels:** apply only existing, relevant labels supported by repository conventions or explicit direction. Do not invent labels.
- **Projects:** link only the confirmed project and item when tracking is in scope and authorized.
- **Milestone:** select only an existing, confirmed milestone that matches the accepted plan. Do not infer one from a date or version.
- **Development / linked issues:** the explanatory text “Successfully merging this pull request may close these issues” is conditional. If the section says “None yet,” report that no linked issue is shown there; do not infer an issue will close. Use a closing keyword only when merging this PR into the default branch should close the confirmed issue. For partial work or related context, use a non-closing reference. Never invent issue links.

## Report and stop conditions

Return the observed draft/work state, review-request state, submitted-review state, integration state, and each metadata field as set, missing, or unknown. Record proposed values separately from values actually written. Leave optional fields unset when no grounded value exists; surface required missing metadata or reviews as blockers. A recommendation does not authorize a GitHub write.

## GitHub documentation

- [Pull requests](https://docs.github.com/en/pull-requests/reference/pull-requests) (draft and ready-for-review states; merge status)
- [Pull request reviews](https://docs.github.com/en/pull-requests/reference/pull-request-reviews), [requesting a review](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/requesting-a-pull-request-review), and [review-request API](https://docs.github.com/en/rest/pulls/review-requests) (review submissions and requests are distinct records)
- [Linking a pull request to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue) (issue linkage and closing behavior)
