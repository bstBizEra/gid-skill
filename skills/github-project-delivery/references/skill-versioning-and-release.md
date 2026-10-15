# Skill versioning and release

Use this procedure only when an owner accepts a task-local lesson as a candidate change to this shared skill. A successful task or research cycle alone does not authorize promotion.

## Promote a lesson

1. Keep the lesson in the originating task record first. Remove private/project-specific details and link the observed failures, research sources, and outcome.
2. Draft a change proposal stating the intended behavior, activation and non-activation conditions, affected workflow/contracts, compatibility impact, and evaluation cases. Preserve conflicting evidence.
3. Obtain explicit owner approval before editing shared skill files. If approval is absent, leave the proposal task-local.
4. Add or update evaluations before changing guidance. Include a positive activation case and a negative/non-activation case; retain earlier safety and routing evaluations.
5. Edit the smallest relevant reference. Do not change unrelated workflows, policy, or provider configuration.

## Choose the version

Use Semantic Versioning `MAJOR.MINOR.PATCH` for the package version in `registry.json`:

- **PATCH** (`1.0.0` → `1.0.1`): clarify wording, fix a documentation error, or repair packaging without changing expected behavior or contracts.
- **MINOR** (`1.0.0` → `1.1.0`): add backward-compatible guidance, workflow coverage, or optional fields while preserving existing triggers, authority limits, routes, and required outputs.
- **MAJOR** (`1.0.0` → `2.0.0`): change or remove an existing trigger, threshold, authority boundary, required evidence field, route, template contract, or behavior in a way that can invalidate existing consumers or records.

When uncertain whether a consumer must change, classify as MAJOR and document the migration. Never use a major bump to bypass owner review or failing evaluations. The version in `registry.json` is the package version; the parent framework/specification version is a separate document version.

## Validate and release

1. Run all existing and new evaluation cases against the candidate. For a major change, also run migration cases against an old-format record and confirm how it is handled.
2. Run package tests, metadata/registry/link/workflow checks, and installer preview/apply checks. Bind results to the exact candidate file set or archive checksum.
3. If any required evaluation or package check fails, do not release or advance the published version. Record the failed candidate and keep its proposed version distinct from the latest released version.
4. After all gates pass, update `registry.json` and add a dated entry to `CHANGELOG.md`. Include behavior changes, compatibility/migration notes, evaluation evidence, and known limits.
5. Build a version-named package artifact, inspect its contents, and record its SHA-256. Retain the prior artifact and changelog entry so consumers can recover or compare versions.
6. Report the release as **locally packaged** unless a repository, remote, and release authority are confirmed. Creating a Git commit/tag, GitHub release, or changing an installed skill is a separate action and requires the applicable project authority and explicit authorization.

Do not silently update installed copies. Provide the artifact/version and upgrade notes; consumers adopt it through their own authorized workflow.
