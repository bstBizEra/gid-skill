#!/usr/bin/env python3
"""Preview or copy this skill without overwriting a different destination."""
import argparse
import hashlib
import shutil
import sys
import tempfile
from pathlib import Path


def files(root):
    result = {}
    for path in root.rglob("*"):
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        if path.is_symlink():
            raise ValueError("source or destination contains a symlink")
        if path.is_file():
            result[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--apply", action="store_true", help="copy only when destination is absent")
    args = parser.parse_args()
    source = args.source.resolve()
    destination = args.destination.resolve()
    target = destination / source.name
    if not source.is_dir() or not (source / "SKILL.md").is_file():
        print("error: missing or invalid source skill")
        return 2
    if source == target or source in target.parents or target in source.parents:
        print("error: recursive source/destination overlap")
        return 2
    try:
        source_files = files(source)
        if target.exists():
            if not target.is_dir():
                print("error: destination exists and is not a directory")
                return 1
            if files(target) == source_files:
                print("identical: destination already matches source")
                return 0
            print("error: destination conflict; existing content preserved")
            return 1
        if not args.apply:
            print(f"preview: would copy {source} to {target}; pass --apply to create it")
            return 0
        destination.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=f".{source.name}.staging-", dir=destination) as temp:
            staged = Path(temp) / source.name
            shutil.copytree(source, staged, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            if files(staged) != source_files:
                print("error: staged bytes did not verify; final destination was not changed")
                return 1
            try:
                # copytree creates the final directory exclusively; never clean it up after a race or partial failure.
                shutil.copytree(staged, target)
            except FileExistsError:
                print("error: destination appeared before publish; existing content preserved")
                return 1
            except OSError as exc:
                print(f"error: publish failed; destination preserved for inspection and may be incomplete: {exc}")
                return 1
            if files(target) != source_files:
                print("error: copied bytes did not verify; destination preserved for inspection")
                return 1
        print(f"installed and verified: {target}")
        return 0
    except (OSError, ValueError) as exc:
        print(f"error: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
