# Evidence and Attempt Contract

Tie evidence to the exact project and candidate. Record task/acceptance IDs, repository, base/head SHA, actual command or run, result, environment, timestamp/timezone, links, limits, and next action when applicable.

Use the project's existing attempt ledger and counting rule. Preserve successful, failed, reserved, and interrupted attempts across agents/providers. A comment or JSON snapshot is evidence, not a distributed lock or proof of live GitHub state. The research-trigger counter reads the same task/criterion attempts and does not reset or replace a project cap.

An attempt qualifies for the research trigger only when a materially distinct corrective hypothesis/action was executed, the same acceptance criterion was checked, and it still failed on the same task/candidate. Duplicate logs, unchanged reruns, deliberate pre-fix reproduction, tool outages, missing access, and external blockers do not qualify.

The bundled evidence checker validates only the supplied snapshot. Its results are advisory; they do not establish live permissions, review provenance, branch protection, or runtime health.
# Evidence and attempts

The optional `check_evidence.py` accepts a JSON snapshot with this shape:

```json
{
  "candidate": {"repository": "owner/repo", "base_sha": "base", "head_sha": "head"},
  "required_checks": ["tests"],
  "checks": [{"name": "tests", "status": "success", "head_sha": "head"}],
  "acceptance": [{"id": "AC-1", "status": "passed", "head_sha": "head"}],
  "required_approval_roles": ["auditor", "reviewer"],
  "approvals": [
    {"reviewer": "auditor-login", "role": "auditor", "state": "APPROVED", "head_sha": "head"},
    {"reviewer": "reviewer-login", "role": "reviewer", "state": "APPROVED", "head_sha": "head"}
  ],
  "dependencies": [{"id": "ISSUE-1", "state": "closed"}],
  "attempt_cap": 5,
  "attempts": [{"id": "attempt-1", "state": "failed"}]
}
```

`required_approval_roles` is optional; when supplied, every role must have an approved entry for the current head, and one reviewer cannot fill multiple required roles. Omit it when the project has no role-specific approval gate. Role labels in a snapshot do not prove a person's authority.

`attempt_cap` is optional. Each entry in `attempts`, including reserved and interrupted entries, consumes one slot. The checker reports snapshot consistency only (`enforcement: false`); it does not verify reviewer eligibility, comment-thread state, provenance, live rules, or GitHub state. Exit 0 means no findings in the supplied snapshot, not that a change is authorized or accepted. Exit 1 means findings, and 2 means invalid input.
