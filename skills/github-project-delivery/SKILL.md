---
name: github-project-delivery
description: Use when creating, planning, implementing, verifying, integrating, releasing, or operating GitHub projects and repository work needs authority-aware workflow routing and current evidence.
---

# GitHub Project Delivery

Route the request to the smallest relevant G01–G12 workflow. First read applicable project instructions, identify the repository and completion boundary, and inspect existing work read-only. Project policy controls actions; GitHub records work and evidence. Load only the selected [router](references/router.md), its [workflow](references/workflows/), and required [contracts](references/contracts/).

Do not infer write permission from read access. Do not report completion, integration, runtime health, or business acceptance without the matching evidence. Report `task_state`, `verification_state`, `integration_state`, `runtime_state`, and `business_acceptance` separately.

For the full lifecycle, skill package, provider, and script contracts, use the linked references. When one acceptance criterion fails in three distinct, executed attempts, pause edits and follow the [research and learning loop](references/research-learning-loop.md) before another implementation attempt. Respect an explicit user waiver and record it. Promote task-local lessons only with owner approval; use [skill versioning and release](references/skill-versioning-and-release.md) for compatible minor or breaking major changes and package release.
