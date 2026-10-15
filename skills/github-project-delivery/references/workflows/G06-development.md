# G06 — Development

**Trigger:** Implement an authorized code, configuration, or documentation change.
**Inputs:** Baseline, scoped acceptance criteria, candidate location, dependencies, constraints, and counted-attempt policy.
**Capability assumptions:** The candidate environment and checks must be accessible; tool failures are blockers, not failed fixes.
**Actions:** Follow the accepted branch plan; inspect baseline; reproduce behavior when useful; specify the smallest change; implement one reviewable slice; run relevant checks; record exact candidate and results. Keep one writer per branch/file scope and stop if the base or ownership plan has drifted.
**Output:** Scoped candidate with behavior proof, changed-file list, limitations, and next action.
**Exit and recovery:** After three distinct evidenced failed corrective actions against the same criterion on the same task/candidate, pause and invoke `../research-learning-loop.md`. Revert or isolate only with authority and recoverable evidence.
**Authority limit:** Do not broaden scope, alter production data, or publish changes without authorization.
