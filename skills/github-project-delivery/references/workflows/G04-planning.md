# G04 — Planning

**Trigger:** A design or request needs executable tasks, dependencies, milestones, or a work queue.
**Inputs:** Accepted scope, existing issues, project fields, owners, dependencies, capacity, and completion criteria.
**Capability assumptions:** Issue and Project read/write support is connector-specific and must be verified separately.
**Actions:** Reuse or reconcile records; decompose by reviewable outcome; link dependencies; identify owner and acceptance evidence; map only confirmed project fields and views; prepare a branch plan when work is parallel, release-sensitive, or lacks a clear convention (see [branch strategy](../branch-strategy.md)); when preparing a PR, check sidebar metadata against [PR readiness](../contracts/pull-request-readiness.md); when establishing delivery governance, follow the [project runbook contract](../contracts/project-governance-runbook.md) and use its [template](../../templates/project-governance-runbook.md).
**Output:** Deduplicated backlog and ready task packets with explicit blockers, any needed branch plan, grounded PR metadata proposals, or an evidence-linked governance runbook and adoption backlog.
**Exit and recovery:** Keep blocked tasks out of the ready queue; preserve the decision needed to unblock them.
**Authority limit:** Create or edit GitHub records only when the request and project policy authorize the write.
