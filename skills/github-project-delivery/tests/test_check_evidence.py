import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "check_evidence.py"


def snapshot():
    return {
        "candidate": {"repository": "owner/repo", "base_sha": "base1", "head_sha": "head1"},
        "required_checks": ["tests"],
        "checks": [{"name": "tests", "status": "success", "head_sha": "head1"}],
        "acceptance": [{"id": "A-1", "status": "passed", "head_sha": "head1"}],
        "approvals": [{"reviewer": "alice", "state": "APPROVED", "head_sha": "head1"}],
        "dependencies": [{"id": "I-1", "state": "closed"}],
        "attempt_cap": 4,
        "attempts": [{"id": "a1", "state": "failed"}],
    }


class CheckEvidenceTests(unittest.TestCase):
    def run_checker(self, value):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "evidence.json"
            path.write_text(json.dumps(value), encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), str(path)], text=True, capture_output=True)

    def test_valid_snapshot_is_advisory_and_reports_remaining_attempts(self):
        result = self.run_checker(snapshot())
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn('"advisory": true', result.stdout)
        self.assertIn('"remaining_attempts": 3', result.stdout)

    def test_stale_check_and_acceptance_are_incomplete(self):
        data = snapshot()
        data["checks"][0]["head_sha"] = "old"
        data["acceptance"][0]["head_sha"] = "old"
        result = self.run_checker(data)
        self.assertEqual(result.returncode, 1)
        self.assertIn("stale_check", result.stdout)
        self.assertIn("stale_acceptance", result.stdout)

    def test_missing_required_check_is_reported(self):
        data = snapshot()
        data["checks"] = []
        result = self.run_checker(data)
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing_check", result.stdout)

    def test_duplicate_approvals_do_not_count_twice(self):
        data = snapshot()
        data["approvals"].append(dict(data["approvals"][0]))
        result = self.run_checker(data)
        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate_reviewer", result.stdout)

    def test_required_auditor_and_reviewer_roles_need_distinct_approvers(self):
        data = snapshot()
        data["required_approval_roles"] = ["auditor", "reviewer"]
        data["approvals"] = [
            {"reviewer": "alice", "role": "auditor", "state": "APPROVED", "head_sha": "head1"},
            {"reviewer": "bob", "role": "reviewer", "state": "APPROVED", "head_sha": "head1"},
        ]
        result = self.run_checker(data)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn('"enforcement": false', result.stdout)
        self.assertIn('"snapshot_state": "consistent"', result.stdout)

    def test_required_approval_role_missing_is_reported(self):
        data = snapshot()
        data["required_approval_roles"] = ["auditor", "reviewer"]
        data["approvals"] = [
            {"reviewer": "alice", "role": "reviewer", "state": "APPROVED", "head_sha": "head1"}
        ]
        result = self.run_checker(data)
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing_approval_role", result.stdout)

    def test_stale_role_approval_does_not_satisfy_required_role(self):
        data = snapshot()
        data["required_approval_roles"] = ["auditor", "reviewer"]
        data["approvals"] = [
            {"reviewer": "alice", "role": "auditor", "state": "APPROVED", "head_sha": "old"},
            {"reviewer": "bob", "role": "reviewer", "state": "APPROVED", "head_sha": "head1"},
        ]
        result = self.run_checker(data)
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing_approval_role", result.stdout)
        self.assertIn("stale_or_ineligible_approval", result.stdout)

    def test_duplicate_required_roles_are_invalid(self):
        data = snapshot()
        data["required_approval_roles"] = ["auditor", "AUDITOR"]
        result = self.run_checker(data)
        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid_schema", result.stdout)

    def test_one_person_cannot_fill_two_required_roles(self):
        data = snapshot()
        data["required_approval_roles"] = ["auditor", "reviewer"]
        data["approvals"] = [
            {"reviewer": "alice", "role": "auditor", "state": "APPROVED", "head_sha": "head1"},
            {"reviewer": "ALICE", "role": "reviewer", "state": "APPROVED", "head_sha": "head1"},
        ]
        result = self.run_checker(data)
        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate_reviewer", result.stdout)

    def test_blocked_dependency_and_incomplete_acceptance_report(self):
        data = snapshot()
        data["dependencies"][0]["state"] = "open"
        data["acceptance"].append({"id": "A-2", "status": "pending", "head_sha": "head1"})
        result = self.run_checker(data)
        self.assertEqual(result.returncode, 1)
        self.assertIn("blocked_dependency", result.stdout)
        self.assertIn("incomplete_acceptance", result.stdout)

    def test_attempts_include_reserved_and_interrupted_entries(self):
        data = snapshot()
        data["attempts"] += [{"id": "a2", "state": "reserved"}, {"id": "a3", "state": "interrupted"}]
        result = self.run_checker(data)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn('"remaining_attempts": 1', result.stdout)

    def test_attempt_cap_exceeded_is_reported(self):
        data = snapshot()
        data["attempts"] *= 5
        result = self.run_checker(data)
        self.assertEqual(result.returncode, 1)
        self.assertIn("attempt_cap_exceeded", result.stdout)

    def test_malformed_json_returns_input_error(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "bad.json"
            path.write_text("{", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], text=True, capture_output=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid_json", result.stdout)

    def test_invalid_schema_returns_input_error(self):
        result = self.run_checker({"candidate": {}})
        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid_schema", result.stdout)


if __name__ == "__main__":
    unittest.main()
