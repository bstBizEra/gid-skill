# GIDF-SKILLS-001 — GitHub Project Delivery Skill Framework

- **Framework version:** 1.0.0
- **Skill package version:** 1.2.0 candidate
- **Status:** Release gates incomplete; host adoption not verified
- **Source document:** [docs/GIDF-SKILLS-001_Framework_v1.0.md](docs/GIDF-SKILLS-001_Framework_v1.0.md)

GIDF-SKILLS-001 describes a provider-neutral skill for guiding AI agents through GitHub project delivery. It routes a request to the smallest relevant workflow, uses repository policy as the authority for actions, and keeps verification, integration, runtime status, and business acceptance distinct.

The portable skill candidate v1.2.0 is under [`skills/github-project-delivery`](skills/github-project-delivery/SKILL.md). It adds scalable branch planning, review-comment disposition, and optional distinct auditor/reviewer checks in evidence snapshots. Its evidence checker remains advisory and cannot enforce GitHub policy. The installer stages and verifies a copy and preserves a destination that appears during a race. Package tests pass; fresh-context evaluation is incomplete, so this is not a release. The installed copy and target-repository adoption have not been updated.

Download the [v1.2.0 candidate package](dist/github-project-delivery-v1.2.0-candidate.zip) and review its [candidate record](dist/CANDIDATE-v1.2.0.md) for the SHA-256, validation status, and outstanding release gates.

## What the framework covers

The design groups project work into twelve workflows:

1. **Governance** — establish authority and inspect repository controls.
2. **Discovery** — inventory existing work and reconcile gaps.
3. **Design** — define outcomes, journeys, contracts, and acceptance.
4. **Planning** — organize issues, dependencies, milestones, and queues.
5. **Agents** — route work and prepare execution or handoff packets.
6. **Development** — make a scoped change and record behavior evidence.
7. **Verification** — run and classify checks against the current candidate.
8. **Security** — assess relevant risks, findings, and remediation.
9. **Integration** — review candidates and integrate under project authority.
10. **Release** — validate artifacts, environments, and deployment health.
11. **Knowledge** — maintain canonical documentation and decisions.
12. **Operations** — measure outcomes, handle incidents, and feed improvements back into planning.

These are workflow groups behind one intended entry skill, not twelve separately installed skills. Each workflow is designed to define its triggers, inputs, ordered actions, outputs, exit criteria, and recovery behavior.

## Operating principles

- Start with applicable instructions, authority, and a read-only inventory.
- Reconcile existing issues, decisions, and project records before adding duplicates.
- Keep evidence tied to the exact candidate revision and actual command or run result.
- Report task completion, verification, integration, runtime, and business acceptance separately.
- Treat connector access, account permissions, and feature availability as separate facts.
- Preserve attempt history and stopped work when handing work between agents or providers.
- Require project authority for configuration changes, integration, publication, and deployment.

## Typical routes

| Request | Workflow route |
|---|---|
| Adopt or upgrade the framework | Governance → Discovery → Planning → Agents |
| Deliver a feature | Design → Planning → Agents → Development → Verification → Integration |
| Fix a defect | Discovery → Development → Verification → Integration |
| Release and operate | Release → Operations, with measured improvements returned to Design and Planning |
| Resume work or switch providers | Agents, then continue the existing workflow and evidence history |

Routes are conditional. For example, include security review when the task or risk calls for it, and include release workflows only when release is in scope.

## Package and validation

The framework document describes the broader package and validation boundaries. This directory contains the local skill implementation; host discovery, runtime invocation, and adoption by a target repository remain separate validation steps.

Run the local standard-library test suite from this directory with:

```powershell
python -m unittest discover -s skills/github-project-delivery/tests -v
```

Native agent discovery, live GitHub configuration, and adoption by a target repository remain separate validation steps.

## References

See the [framework specification](docs/GIDF-SKILLS-001_Framework_v1.0.md) for the detailed workflow model, GitHub feature map, evidence controls, roadmap, and primary sources. The [implementation specification](docs/GIDF-SKILLS-001_Implementation_Spec_v1.0.md) records the package contract, including the bounded Context7/Firecrawl research loop.
