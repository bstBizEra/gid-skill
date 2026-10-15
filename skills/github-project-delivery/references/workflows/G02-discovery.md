# G02 — Discovery

**Trigger:** Start, resume, upgrade, or reconcile project work.
**Inputs:** Repository and task identity, existing instructions, issues, PRs, projects, actions, docs, and accessible evidence.
**Capability assumptions:** GitHub and file access vary by connector; report the actual sources inspected.
**Actions:** Inventory relevant sources; pin revision and timestamps; reconcile requested outcomes with current records; mark gaps, conflicts, and unknowns; select the smallest route.
**Output:** Reconciliation matrix and scoped next-step list with source links.
**Exit and recovery:** If a source is unavailable, record that limitation and continue only with independent evidence. Do not create duplicate records until reconciliation is complete.
**Authority limit:** Read-only discovery is the default; inventory does not authorize repository changes.
