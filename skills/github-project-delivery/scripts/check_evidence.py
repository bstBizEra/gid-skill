#!/usr/bin/env python3
"""Check a supplied evidence snapshot; this tool never queries GitHub."""
import json
import sys
from pathlib import Path


def check(data):
    if not isinstance(data, dict):
        raise ValueError("invalid_schema")
    required = {"candidate": dict, "required_checks": list, "checks": list, "acceptance": list,
                "approvals": list, "dependencies": list, "attempts": list}
    if any(key not in data or not isinstance(data[key], kind) for key, kind in required.items()):
        raise ValueError("invalid_schema")
    candidate = data["candidate"]
    if not all(isinstance(candidate.get(k), str) and candidate[k] for k in ("repository", "base_sha", "head_sha")):
        raise ValueError("invalid_schema")
    if any(not isinstance(item, dict) for key in ("checks", "acceptance", "approvals", "dependencies", "attempts") for item in data[key]):
        raise ValueError("invalid_schema")
    cap = data.get("attempt_cap")
    if cap is not None and (not isinstance(cap, int) or isinstance(cap, bool) or cap < 0):
        raise ValueError("invalid_schema")
    required_roles = data.get("required_approval_roles", [])
    if not isinstance(required_roles, list) or any(not isinstance(role, str) or not role for role in required_roles):
        raise ValueError("invalid_schema")
    normalized_roles = [role.casefold() for role in required_roles]
    if len(set(normalized_roles)) != len(normalized_roles):
        raise ValueError("invalid_schema")
    head = candidate["head_sha"]
    findings = []
    checks = data["checks"]
    for name in data["required_checks"]:
        if not isinstance(name, str) or not name:
            raise ValueError("invalid_schema")
        matching = [c for c in checks if c.get("name") == name]
        if not matching:
            findings.append({"code": "missing_check", "item": name})
        elif not any(c.get("status") == "success" and c.get("head_sha") == head for c in matching):
            code = "stale_check" if any(c.get("head_sha") != head for c in matching) else "failed_check"
            findings.append({"code": code, "item": name})
    for item in data["acceptance"]:
        if not all(isinstance(item.get(k), str) and item[k] for k in ("id", "status", "head_sha")):
            raise ValueError("invalid_schema")
        if item["status"] != "passed":
            findings.append({"code": "incomplete_acceptance", "item": item["id"]})
        elif item["head_sha"] != head:
            findings.append({"code": "stale_acceptance", "item": item["id"]})
    reviewers = set()
    approved_roles = {}
    for approval in data["approvals"]:
        name = approval.get("reviewer")
        if not isinstance(name, str) or not name:
            raise ValueError("invalid_schema")
        role = approval.get("role")
        if role is not None and (not isinstance(role, str) or not role):
            raise ValueError("invalid_schema")
        if name.casefold() in reviewers:
            findings.append({"code": "duplicate_reviewer", "item": name})
        reviewers.add(name.casefold())
        if approval.get("state") != "APPROVED" or approval.get("head_sha") != head:
            findings.append({"code": "stale_or_ineligible_approval", "item": name})
        if role is not None and role.casefold() in normalized_roles and approval.get("state") == "APPROVED" and approval.get("head_sha") == head:
            approved_roles.setdefault(role.casefold(), set()).add(name.casefold())
    reviewer_roles = {}
    for role in normalized_roles:
        eligible = approved_roles.get(role, set())
        if not eligible:
            findings.append({"code": "missing_approval_role", "item": role})
        for reviewer in eligible:
            reviewer_roles.setdefault(reviewer, set()).add(role)
    for reviewer, roles in reviewer_roles.items():
        if len(roles) > 1:
            findings.append({"code": "same_reviewer_multiple_required_roles", "item": reviewer})
    for dependency in data["dependencies"]:
        if not isinstance(dependency.get("id"), str) or not isinstance(dependency.get("state"), str):
            raise ValueError("invalid_schema")
        if dependency["state"].casefold() not in {"closed", "complete", "done"}:
            findings.append({"code": "blocked_dependency", "item": dependency["id"]})
    if any(not isinstance(attempt.get("id"), str) or not attempt["id"] or
           not isinstance(attempt.get("state"), str) or not attempt["state"] for attempt in data["attempts"]):
        raise ValueError("invalid_schema")
    remaining = None if cap is None else max(0, cap - len(data["attempts"]))
    if cap is not None and len(data["attempts"]) > cap:
        findings.append({"code": "attempt_cap_exceeded", "item": str(len(data["attempts"]))})
    return {"advisory": True, "enforcement": False,
            "snapshot_state": "consistent" if not findings else "has_findings",
            "repository": candidate["repository"], "head_sha": head,
            "attempt_count": len(data["attempts"]), "attempt_cap": cap,
            "remaining_attempts": remaining, "findings": findings}


def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": "usage: check_evidence.py SNAPSHOT.json"}))
        return 2
    try:
        result = check(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    except json.JSONDecodeError:
        print(json.dumps({"error": "invalid_json"}))
        return 2
    except OSError as exc:
        print(json.dumps({"error": "input_error", "detail": str(exc)}))
        return 2
    except ValueError as exc:
        print(json.dumps({"error": str(exc)}))
        return 2
    print(json.dumps(result, indent=2))
    return 1 if result["findings"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
