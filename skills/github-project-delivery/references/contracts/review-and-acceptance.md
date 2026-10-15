# Review and acceptance contract

Use this contract in G09 when a candidate has reviewer comments, audit requirements, or an explicit request for separate auditor and reviewer acceptance.

## Distinct review responsibilities

- **Reviewer:** assess correctness, maintainability, tests, and the requested change against the current diff.
- **Auditor:** assess conformity to the accepted scope, authority, required controls, and evidence. Do not invent an auditor role when the project has not defined one.
- Treat these as separate people when policy or the requested gate requires independent sign-off. One identity cannot satisfy both required roles.

## Comment disposition

Track each material comment with its source/thread, candidate SHA, blocking status, and one disposition:

- `pending` — still needs a response or decision;
- `addressed` — code or documentation changed; link the new revision and the check that covers it;
- `accepted` — an authorized owner accepted the risk or requested behavior, with rationale and evidence;
- `deferred` — link follow-up work and identify the owner; if creating it is not authorized, draft the follow-up and name a proposed owner;
- `not_applicable` — explain why the comment does not apply to this candidate.

Do not call a comment resolved merely because a reply was posted or the author believes it is fixed. Confirm the disposition against the updated diff and relevant verification. Mark a hosted thread resolved only when the actor has authority and the user/project policy permits that write.

## Candidate acceptance

When project policy or the user explicitly requires both roles, accept the code change only when all of the following are observed for the exact current head SHA:

1. At least one eligible `auditor` approval and one eligible `reviewer` approval exist, from distinct identities.
2. Required checks and acceptance criteria pass on that same head.
3. Every blocking comment is addressed and verified, or explicitly accepted by an authorized owner with a recorded rationale. Deferred comments link to follow-up work.
4. No required approval or check became stale after a new commit.

Missing reviewer identity/eligibility evidence, unavailable live policy, stale approval, or unresolved blocking comments leaves acceptance `incomplete`. The evidence checker can flag a supplied snapshot; it cannot authenticate the people, comments, policy, or GitHub state. This contract does not authorize merge, thread-resolution writes, or release.

For GitHub-specific behavior, confirm the current [pull request review documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews) and [repository rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).
