# G10 — Release

**Trigger:** Package, publish, tag, deploy, or validate a released artifact/runtime.
**Inputs:** Authorized scope, artifact identity, environment policy, recovery plan, release checks, health criteria.
**Capability assumptions:** Release and environment access are independently verified; requested deploy is not observed deploy.
**Actions:** Pin artifact and provenance; prepare recovery; validate staging; publish/deploy only when authorized; run health checks; record exact environment, time, result, and recovery outcome. To release this skill package, follow [skill versioning and release](../skill-versioning-and-release.md), including its version, evaluation, checksum, and authority gates.
**Output:** Release/runtime evidence and recovery record.
**Exit and recovery:** Stop on missing approval, artifact mismatch, failed gate, or health regression; follow the approved recovery plan and record observed state.
**Authority limit:** A release note, tag, or deployment request is not proof that publishing or deployment occurred.
