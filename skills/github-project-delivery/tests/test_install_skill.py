import subprocess
import sys
import tempfile
import unittest
import importlib.util
import io
from contextlib import redirect_stdout
from unittest.mock import patch
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "install_skill.py"
SOURCE = Path(__file__).parents[1]
SPEC = importlib.util.spec_from_file_location("install_skill", SCRIPT)
INSTALLER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INSTALLER)


class InstallSkillTests(unittest.TestCase):
    def run_installer(self, destination, *extra):
        return subprocess.run([sys.executable, str(SCRIPT), "--destination", str(destination), *extra], text=True, capture_output=True)

    def test_preview_does_not_create_destination(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "skills"
            result = self.run_installer(destination)
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            self.assertFalse((destination / SOURCE.name).exists())
            self.assertIn("preview", result.stdout.lower())

    def test_apply_copies_and_identical_rerun_is_safe(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "skills"
            result = self.run_installer(destination, "--apply")
            target = destination / SOURCE.name
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            self.assertEqual((target / "SKILL.md").read_bytes(), (SOURCE / "SKILL.md").read_bytes())
            repeated = self.run_installer(destination, "--apply")
            self.assertEqual(repeated.returncode, 0, repeated.stderr + repeated.stdout)
            self.assertIn("identical", repeated.stdout.lower())

    def test_conflicting_destination_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "skills"
            target = destination / SOURCE.name
            target.mkdir(parents=True)
            (target / "SKILL.md").write_text("owner content", encoding="utf-8")
            result = self.run_installer(destination, "--apply")
            self.assertEqual(result.returncode, 1)
            self.assertEqual((target / "SKILL.md").read_text(encoding="utf-8"), "owner content")

    def test_recursive_destination_is_refused(self):
        result = self.run_installer(SOURCE / "nested")
        self.assertEqual(result.returncode, 2)

    def test_missing_source_is_refused(self):
        result = subprocess.run([sys.executable, str(SCRIPT), "--source", str(SOURCE / "missing"), "--destination", str(SOURCE.parent / "out")], text=True, capture_output=True)
        self.assertEqual(result.returncode, 2)

    def test_destination_created_during_publish_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "skills"
            destination.mkdir()
            target = destination / SOURCE.name
            real_copytree = INSTALLER.shutil.copytree
            calls = 0

            def create_racing_destination(source, dest, *args, **kwargs):
                nonlocal calls
                calls += 1
                if Path(dest) == target:
                    target.mkdir()
                    (target / "owner.txt").write_text("keep", encoding="utf-8")
                    raise FileExistsError(str(target))
                return real_copytree(source, dest, *args, **kwargs)

            output = io.StringIO()
            with patch.object(INSTALLER.shutil, "copytree", side_effect=create_racing_destination), \
                 patch.object(sys, "argv", [str(SCRIPT), "--destination", str(destination), "--apply"]), \
                 redirect_stdout(output):
                result = INSTALLER.main()

            self.assertEqual(result, 1)
            self.assertEqual((target / "owner.txt").read_text(encoding="utf-8"), "keep")
            self.assertIn("preserved", output.getvalue().lower())
            self.assertEqual([p.name for p in destination.iterdir()], [SOURCE.name])

    def test_partial_publish_failure_is_left_for_inspection(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "skills"
            destination.mkdir()
            target = destination / SOURCE.name
            real_copytree = INSTALLER.shutil.copytree

            def fail_during_publish(source, dest, *args, **kwargs):
                if Path(dest) == target:
                    target.mkdir()
                    (target / "copied-before-failure.txt").write_text("preserve", encoding="utf-8")
                    raise OSError("simulated disk error")
                return real_copytree(source, dest, *args, **kwargs)

            output = io.StringIO()
            with patch.object(INSTALLER.shutil, "copytree", side_effect=fail_during_publish), \
                 patch.object(sys, "argv", [str(SCRIPT), "--destination", str(destination), "--apply"]), \
                 redirect_stdout(output):
                result = INSTALLER.main()

            self.assertEqual(result, 1)
            self.assertEqual((target / "copied-before-failure.txt").read_text(encoding="utf-8"), "preserve")
            self.assertIn("preserved for inspection", output.getvalue().lower())
            self.assertEqual([p.name for p in destination.iterdir()], [SOURCE.name])


if __name__ == "__main__":
    unittest.main()
