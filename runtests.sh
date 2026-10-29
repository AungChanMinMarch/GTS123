#!/usr/bin/env bash
# Usage: ./runtests.sh [PREFIX ...]
# With prefixes (e.g. lab09): runs pytest in every folder starting with each prefix.
# Without arguments: runs pytest in every folder (at any depth) that contains solution.py.
# Prints one summary line per folder (green = all passed, red = otherwise), then a total.

cd "$(dirname "$0")" || exit 1

pytest=.venv/bin/pytest
[ -x "$pytest" ] || pytest=pytest

if [ -t 1 ]; then green=$'\e[32m' red=$'\e[31m' reset=$'\e[0m'; else green= red= reset=; fi
checked=0 passed=0 failed=0

run() {
    local out
    out=$("$pytest" --import-mode=importlib "$1" -q --tb=no -rN 2>&1)
    if [ $? -eq 0 ]; then
        passed=$((passed + 1)); color=$green
    else
        failed=$((failed + 1)); color=$red
    fi
    checked=$((checked + 1))
    printf "%s%s %s%s\n" "$color" "$1" "$(tail -1 <<<"$out")" "$reset"
}

summary() {
    echo "checked $checked, ${green}passed $passed${reset}, ${red}failed $failed${reset}"
}

if [ $# -eq 0 ]; then
    found=0
    while IFS= read -r d; do
        found=1
        run "${d#./}"
    done < <(find . \( -name .git -o -name .venv -o -name venv -o -name node_modules \) -prune \
                -o -name solution.py -type f -printf '%h\n' | sort -u)
    [ $found -eq 1 ] || echo "no solution.py found under $(pwd)"
    summary
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
summary
