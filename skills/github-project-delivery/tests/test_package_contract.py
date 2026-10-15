import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).parents[1]


class PackageContractTests(unittest.TestCase):
    def test_registry_references_existing_package_files_and_all_workflows(self):
        registry = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
        paths = [registry["entry"], registry["router"], *registry["contracts"],
                 *registry["providers"], *registry["templates"], *registry["tools"],
                 *registry.get("references", [])]
        paths.extend(workflow["path"] for workflow in registry["workflows"])
        self.assertEqual({workflow["id"] for workflow in registry["workflows"]},
                         {f"G{i:02}" for i in range(1, 13)})
        self.assertTrue(all((ROOT / path).is_file() for path in paths))

    def test_relative_markdown_links_resolve_inside_the_package(self):
        broken = []
        for markdown in ROOT.rglob("*.md"):
            content = markdown.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
                target = target.strip().strip("<>")
                parsed = urlsplit(target)
                if parsed.scheme or target.startswith("#"):
                    continue
                path = unquote(parsed.path)
                if path and not (markdown.parent / path).exists():
                    broken.append(f"{markdown.relative_to(ROOT)} -> {target}")
        self.assertEqual(broken, [])

    def test_repository_setup_route_includes_description_governance(self):
        registry = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
        self.assertEqual(registry["conditional_routes"]["repository_setup"], ["G01", "G02"])
        governance = (ROOT / "references/workflows/G01-governance.md").read_text(encoding="utf-8")
        self.assertIn("concise About description", governance)
        self.assertIn("preserve a nonempty description", governance)

    def test_pr_readiness_contract_is_registered_and_separates_statuses(self):
        registry = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
        self.assertIn("references/contracts/pull-request-readiness.md", registry["contracts"])
        self.assertEqual(registry["conditional_routes"]["pull_request_readiness"], ["G04", "G09"])
        contract = (ROOT / "references/contracts/pull-request-readiness.md").read_text(encoding="utf-8")
        for expected in ("awaiting_review", "Assignees", "Labels", "Projects", "Milestone", "Development"):
            self.assertIn(expected, contract)

    def test_pr_progress_question_requires_authoritative_state_checks(self):
        contract = (ROOT / "references/contracts/pull-request-readiness.md").read_text(encoding="utf-8")
        for expected in ("isDraft", "review requests", "submitted reviews", "merge box", "linked issue"):
            self.assertIn(expected, contract)


if __name__ == "__main__":
    unittest.main()
