# Project governance and delivery runbook

Use this contract when a project needs a reusable operating model for planning, engineering, verification, integration, release, or operations. Route through G01 → G02 → G04; add other workflows only for accepted scope.

## Establish a trustworthy baseline first

1. Read repository and host instructions, then inventory the available repository, default/base branches, issue and PR records, Projects, templates, CI workflows, architecture/security documents, release procedures, and operational records that are in scope.
2. Record each finding as **observed**, **approved**, **proposed**, or **unknown/not inspected**, with its source, date/revision when available, and review limit. A repository snapshot does not establish hosted settings, permissions, owner decisions, or production state.
3. Map current issues and documents to the proposed outcome/capability structure. Identify duplicates and gaps before proposing new records. Do not create, relabel, assign, move, or close GitHub records without authorization.

## Build the smallest useful operating model

- Trace only the levels needed to connect a business or technical outcome to planned work, implementation, verification evidence, acceptance, and any release/operational record. A useful default is `outcome → initiative/epic (if needed) → issue/work item → PR/checks/evidence → acceptance → release/operations`.
- Reuse confirmed repository conventions and native GitHub fields. Propose new fields, views, labels, milestones, or hierarchy only when a demonstrated gap requires them; identify the canonical source of truth and avoid duplicate fields.
- For each SOP, define **trigger, inputs, actions, exit criteria, evidence, decision authority, and recovery/escalation**. Include only procedures needed by the requested scope.
- Define a project-specific **Definition of Ready** and **Definition of Done**. Keep implementation complete, verification passed, human/business acceptance, integration, deployment, and operational health as distinct states.
- Make quality gates risk-based. For each gate specify the risk controlled, required evidence, accountable decision-maker, failure response, and exception path. A written gate is not enforced policy; identify the repository rule, required check, or environment protection that would enforce it, if any.
- Separate executor roles from approvers. Agents may act only within explicit scope and capability; they do not acquire merge, business, security, production, or release authority from task assignment or passing CI.

## Plan adoption without turning proposals into facts

- Present phases, sequence, estimates, dates, staffing, owners, project fields, and thresholds as proposals until verified or explicitly approved. Mark schedule/capacity assumptions and preserve dependencies; parallelize only after dependency and resource checks.
- Define every KPI before setting a target: purpose, formula/denominator, source data, owner, reporting interval, baseline, target status, and limitations. Mark unavailable baselines and unapproved targets as unknown/proposed; never report targets as actual results.
- Produce a prioritized adoption backlog whose items include current evidence, gap/risk, proposed next action, dependency, decision/owner needed, and acceptance evidence. Reconcile against existing issues before recommending new ones.
- State what the runbook does not establish: approval, repository enforcement, hosted configuration, CI success, deployment, or production readiness without the corresponding current evidence and authority.

See the [reusable runbook template](../../templates/project-governance-runbook.md). Keep project-specific names, issue IDs, controls, numerical targets, and environment facts in the target project's approved documents, not in this shared contract.
