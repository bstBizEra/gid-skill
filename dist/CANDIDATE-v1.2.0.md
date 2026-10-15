# Candidate record — github-project-delivery v1.2.0

Status: **candidate only; release gates incomplete**. Do not install or treat as released until remaining fresh-context evaluations pass.

- Artifact: [`github-project-delivery-v1.2.0-candidate.zip`](github-project-delivery-v1.2.0-candidate.zip)
- SHA-256: `bdf38a8e6bb0472c5c67f70f150f7f3026d0d94d246871303799c00e47d746f0`
- Package source: `skills/github-project-delivery`
- Automated checks: 23 Python unit/package-contract tests passed on 2026-10-15; candidate ZIP integrity and source-file parity passed; installer preview/apply passed in a temporary directory.
- Independent behavior evidence: one read-only synthetic fixture run passed the scaled-branch and incomplete-review acceptance assertions; see `tests/skill-evals.md`.
- Open release gates: remaining independent fresh-context behavior scenarios, including small-scale branch choice, no-dual-gate negative, reviewer-comment handling, ordinary routing across G01–G12, and varied positive/negative prompts.
- Not verified: live GitHub rules/policy, reviewer eligibility, hosted enforcement, native host discovery, target repository adoption, and installation of this candidate.
- No installed copy, repository settings, remote, PR, branch, or release was changed.

The evidence checker is advisory. Its clean result applies only to the supplied snapshot and does not authorize a change.
