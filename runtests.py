#!/usr/bin/env python3
"""Cross-platform test runner (Windows / macOS / Linux).

Usage: python runtests.py [PREFIX ...]
  With prefixes (e.g. lab09): runs pytest in every folder starting with each prefix.
  Without arguments: runs pytest in every folder (at any depth) containing solution.py.
Prints one summary line per folder (green = all passed, red = otherwise), then a total.

Requires pytest:  python -m pip install pytest
"""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()  # run from the folder containing the labs (works when piped via stdin too)
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache"}

if sys.stdout.isatty():
    os.system("")  # enables ANSI colours in Windows terminals
    GREEN, RED, RESET = "\033[32m", "\033[31m", "\033[0m"
else:
    GREEN = RED = RESET = ""


def find_solution_dirs():
    dirs = set()
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        if "solution.py" in filenames:
            dirs.add(Path(dirpath))
    return sorted(dirs)


def run(folder):
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "--import-mode=importlib",
         str(folder), "-q", "--tb=no", "-rN"],
        cwd=ROOT, capture_output=True, text=True, errors="replace",
    )
    lines = proc.stdout.strip().splitlines() or proc.stderr.strip().splitlines()
    last = lines[-1] if lines else "no output"
    if "No module named pytest" in proc.stderr + proc.stdout:
        last = "pytest not installed (run: python -m pip install pytest)"
    ok = proc.returncode == 0
    print(f"{GREEN if ok else RED}{folder.relative_to(ROOT).as_posix()} {last}{RESET}")
    return ok


def main(prefixes):
    results = []
    if not prefixes:
        folders = find_solution_dirs()
        if not folders:
            print(f"no solution.py found under {ROOT}")
        results = [run(f) for f in folders]
    else:
        for prefix in prefixes:
            matches = sorted(p for p in ROOT.glob(prefix + "*") if p.is_dir())
            if not matches:
                print(f"{prefix}: no matching folders")
            results += [run(f) for f in matches]
    passed = sum(results)
    failed = len(results) - passed
    print(f"checked {len(results)}, {GREEN}passed {passed}{RESET}, {RED}failed {failed}{RESET}")


if __name__ == "__main__":
    main(sys.argv[1:])
