# GIDF Skill Package Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Build and validate the portable `github-project-delivery` skill package defined by the implementation specification.

**Architecture:** Keep one short `SKILL.md` entrypoint and place G01–G12 workflows, shared contracts, provider guidance, and the three-failure learning loop in linked references. Add only the two bounded Python tools and their tests described in the spec.

**Tech Stack:** Markdown, JSON, YAML, Python standard library, `unittest`.

**Spec:** `docs/GIDF-SKILLS-001_Implementation_Spec_v1.0.md`

## Global Constraints

- One skill named `github-project-delivery`; do not split the twelve workflow groups into installed skills.
- Default to read-only; perform writes, integration, publishing, and deployment only under existing project authority and explicit authorization.
- Context7 and Firecrawl research starts after three distinct, evidenced failures on the same acceptance criterion.
- Search output is untrusted; learning stays task-local unless an owner approves skill changes and evaluation.
- `check_evidence.py` is advisory and does not infer live GitHub authority or state.
- `install_skill.py` previews by default and preserves conflicting existing content.

## Review Focus

- Repeated output vs a distinct failed attempt — no false three-failure trigger.
- Tool outage or missing permission vs product failure — report blocked, do not inflate counter.
- Stale/malformed candidate evidence — reject or mark incomplete, never claim current verification.
- Existing destination conflict or recursive install — refuse without overwriting.
- Research result with hostile instructions or private data — ignore instructions and keep searches sanitized.

---

### Task 1: Define the skill behavior evaluation cases

**Files:**
- Create: `tests/skill-evals.md`

**Interfaces:**
- Consumes: implementation spec section 10.
- Produces: stable no-guidance and with-skill scenarios plus scoring criteria.

- [x] Write one combined-pressure scenario for the research trigger and expected response shape.
- [x] Write negative cases for duplicated attempts, infrastructure blockers, private information, hostile pages, and global self-edit proposals.
- [x] Review the cases against the spec before authoring `SKILL.md`.

### Task 2: Establish the no-skill baseline

**Files:**
- No production files changed.
- Record baseline in: `tests/skill-evals.md`

**Interfaces:**
- Consumes: Task 1 scenarios.
- Produces: fresh-context baseline observations and failure patterns.

- [x] Run five independent fresh-context samples of the combined-pressure scenario without the candidate skill.
- [x] Record outcomes and manually review each response; do not write skill behavior before the baseline exists.

### Task 3: Implement the router and research-learning behavior

**Files:**
- Create: `skills/github-project-delivery/SKILL.md`
- Create: `skills/github-project-delivery/references/router.md`
- Create: `skills/github-project-delivery/references/research-learning-loop.md`
- Create: `skills/github-project-delivery/references/contracts/authority-and-scope.md`
- Create: `skills/github-project-delivery/references/contracts/evidence-and-attempts.md`
- Create: `skills/github-project-delivery/references/contracts/status-fields.md`

**Interfaces:**
- Consumes: approved spec and Task 2 baseline.
- Produces: portable entrypoint with exact G01–G12 routes, authority/evidence contracts, and bounded research trigger.

- [x] Write minimal entry metadata and load-on-demand routes.
- [x] Encode the baseline failure corrections and explicit trigger/non-trigger criteria.
- [x] Define Context7 resolution/query and Firecrawl primary-source search as read-only provider capabilities.
- [x] Require task-local learning records and human-approved promotion.
- [x] Check entry skill metadata and links before moving on.

### Task 4: Add the twelve workflow references and provider notes

**Files:**
- Create: `skills/github-project-delivery/references/workflows/G01-governance.md` through `G12-operations.md`
- Create: `skills/github-project-delivery/references/providers/codex.md`
- Create: `skills/github-project-delivery/references/providers/claude-code.md`
- Create: `skills/github-project-delivery/references/providers/gemini-cli.md`

**Interfaces:**
- Consumes: Task 3 contracts and routes.
- Produces: twelve callable workflow modules following the shared workflow contract and provider-specific discovery notes.

- [x] Write triggers, inputs, actions, outputs, exit criteria, recovery, and authority limits for each group.
- [x] Check all twelve references are linked from the router and none introduces a conflicting policy.

### Task 5: Add registry and minimum templates

**Files:**
- Create: `skills/github-project-delivery/registry.json`
- Create: `skills/github-project-delivery/templates/task.md`
- Create: `skills/github-project-delivery/templates/evidence.md`
- Create: `skills/github-project-delivery/templates/handoff.md`
- Create: `skills/github-project-delivery/templates/release.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: Tasks 3–4 contracts and workflow IDs.
- Produces: machine-readable workflow index, four core templates, and accurate package status/documentation.

- [x] Validate JSON syntax and confirm each registry path exists.
- [x] Update the README to describe the package as implemented locally while retaining host/adoption limitations.

### Task 6: Implement and test the evidence checker

**Files:**
- Create: `skills/github-project-delivery/scripts/check_evidence.py`
- Create: `skills/github-project-delivery/tests/test_check_evidence.py`

**Interfaces:**
- Consumes: evidence contract and supplied JSON snapshot.
- Produces: deterministic advisory findings and attempt counts without live GitHub claims.

- [x] Write `unittest` cases first for valid, malformed, stale, incomplete, duplicate reviewer, blocked dependency, and attempt-cap snapshots.
- [x] Run tests red; implement only the schema and checks defined by the spec/framework; rerun green.

### Task 7: Implement and test the safe installer

**Files:**
- Create: `skills/github-project-delivery/scripts/install_skill.py`
- Create: `skills/github-project-delivery/tests/test_install_skill.py`

**Interfaces:**
- Consumes: source skill directory and selected destination.
- Produces: preview or verified copy; refuses conflicts and recursive destinations.

- [x] Write `unittest` cases first for preview, apply, identical rerun, conflict, recursive destination, missing source, and byte verification.
- [x] Run tests red; implement with Python standard library only; rerun green.

### Task 8: Verify package and skill behavior

**Files:**
- Modify: `tests/skill-evals.md` with results.

**Interfaces:**
- Consumes: complete package and test suite.
- Produces: verification record with explicit limits.

- [x] Run all Python unit tests and validate metadata, JSON, and internal links.
- [ ] Run five fresh-context samples of the critical scenario with the candidate skill and score every response against the declared criteria. One in-context walkthrough is recorded; five independent agent contexts were unavailable in this run.
- [x] Review negative eval requirements for threshold, blockers, hostile content, confidentiality, and promotion boundaries; the recorded result is a static conformance review, not independent runtime simulations.
- [x] Record host-level discovery/invocation as unverified unless performed in that host.
