# Candidate record — github-project-delivery v1.3.0

Status: **candidate only; release gates incomplete**. Do not install or treat as released until remaining fresh-context evaluations pass.

- Artifact: [`github-project-delivery-v1.3.0-candidate.zip`](github-project-delivery-v1.3.0-candidate.zip)
- SHA-256: `b71b8ad6f1da2087c3e25214834febb74f5638340d1b89ecf1cf49861f7bf3c3`
- Package source: `skills/github-project-delivery`
- Automated checks: 24 Python unit/package-contract tests passed on 2026-10-15.
- Archive: 35 files; ZIP integrity and source-file parity verified. Installer preview/apply passed in a temporary directory.
- Behavior evidence: one read-only synthetic fixture run exercised v1.2.0 scaled branch planning and incomplete review acceptance. One live same-context read-only trial passed preservation of the existing About description on `bstBizEra/gid-skill`; it did not test repository creation or writing a missing description.
- Open release gates: independent fresh-context positive and negative tests for repository creation/description behavior, remaining branch/reviewer cases, and ordinary routing across G01–G12.
- Not verified: live GitHub rules/policy, reviewer eligibility, hosted enforcement, native host discovery, target repository adoption, and installation of this candidate.
- No installed copy, repository settings, remote, PR, branch, or release was changed by packaging.

The evidence checker is advisory. Its clean result applies only to the supplied snapshot and does not authorize a change.
