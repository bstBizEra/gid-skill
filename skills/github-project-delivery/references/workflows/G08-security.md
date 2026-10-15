# G08 — Security

**Trigger:** The task or changed surface raises security, privacy, dependency, secret, or abuse risk.
**Inputs:** Threat surface, data classes, applicable policy, available scans/findings, dependencies, and acceptance criteria.
**Capability assumptions:** Scan results and security settings are limited to the tools and repositories actually accessible.
**Actions:** Map risks to controls; inspect available coverage and findings; triage with evidence; propose or implement scoped remediation under authority; verify the fix and record residual risk.
**Output:** Finding/control register with severity rationale, evidence, disposition, and owner for unresolved risks.
**Exit and recovery:** Escalate active exposure or missing containment authority. Preserve sensitive evidence in an approved location and exclude secrets from reports.
**Authority limit:** Tool output is evidence to assess, not permission to expose secrets or alter security policy.
