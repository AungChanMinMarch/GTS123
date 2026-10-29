#!/usr/bin/env bash
# Usage: ./runtests.sh [PREFIX ...]
# With prefixes (e.g. lab09): runs pytest in every folder starting with each prefix.
# Without arguments: runs pytest in every folder (at any depth) that contains solution.py.
# Prints one summary line per folder.

cd "$(dirname "$0")" || exit 1

pytest=.venv/bin/pytest
[ -x "$pytest" ] || pytest=pytest

run() {
    printf "%s " "$1"
    "$pytest" --import-mode=importlib "$1" -q --tb=no -rN 2>&1 | tail -1
}

if [ $# -eq 0 ]; then
    found=0
    while IFS= read -r d; do
        found=1
        run "${d#./}"
    done < <(find . \( -name .git -o -name .venv -o -name venv -o -name node_modules \) -prune \
                -o -name solution.py -type f -printf '%h\n' | sort -u)
    [ $found -eq 1 ] || echo "no solution.py found under $(pwd)"
    exit 0
fi

for prefix in "$@"; do
    found=0
    for d in "$prefix"*/; do
        [ -d "$d" ] || continue
        found=1
        run "${d%/}"
    done
    [ $found -eq 1 ] || echo "$prefix: no matching folders"
done
