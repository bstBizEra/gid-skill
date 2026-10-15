# G01 — Governance

**Trigger:** The request changes or depends on repository authority, roles, protections, environments, or policy.
**Inputs:** Applicable instructions, repository identity and metadata (including its About description), requested actions, access actually available.
**Capability assumptions:** Settings and rule access are confirmed only when directly observed; unavailable controls remain unknown.
**Actions:** Read governing files; inspect accessible settings, rulesets, CODEOWNERS, roles, and environments; map each requested action to its authority; identify any policy-required auditor/reviewer roles and who can satisfy them; separate confirmed facts, proposals, and unknowns. Whenever creating a GitHub repository, derive a concise About description from the stated purpose and include it in creation; if the creation path cannot set it, add it immediately afterward when authorized. For an existing repository, preserve a nonempty description; if it is missing, propose and set one only when repository metadata changes are in scope and authorized.
**Output:** Authority matrix with source, scope, evidence, permitted next action, and the proposed/observed repository description when repository setup is in scope.
**Exit and recovery:** Stop before a write when authority or required access is unknown. Offer a read-only finding or a proposed change for the owner.
**Authority limit:** A connector's access does not prove account permission or policy approval.
