# G01 — Governance

**Trigger:** The request changes or depends on repository authority, roles, protections, environments, or policy.
**Inputs:** Applicable instructions, repository identity, requested actions, access actually available.
**Capability assumptions:** Settings and rule access are confirmed only when directly observed; unavailable controls remain unknown.
**Actions:** Read governing files; inspect accessible settings, rulesets, CODEOWNERS, roles, and environments; map each requested action to its authority; identify any policy-required auditor/reviewer roles and who can satisfy them; separate confirmed facts, proposals, and unknowns.
**Output:** Authority matrix with source, scope, evidence, and permitted next action.
**Exit and recovery:** Stop before a write when authority or required access is unknown. Offer a read-only finding or a proposed change for the owner.
**Authority limit:** A connector's access does not prove account permission or policy approval.
