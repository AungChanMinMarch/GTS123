import subprocess
import sys
from pathlib import Path

import pytest


SOLUTION = Path(__file__).resolve().parent / "solution.py"


def run_solution(user_input: str):
    return subprocess.run(
        [sys.executable, str(SOLUTION)],
        input=user_input,
        capture_output=True,
        text=True,
        check=False,
    )


def input_prompts():
    return "".join(f"Input C{i}: " for i in range(1, 13))


def solution_output(x, y, z):
    return (
        input_prompts()
        + "Solution:\n"
        + f"x = {x:.2f}\n"
        + f"y = {y:.2f}\n"
        + f"z = {z:.2f}\n"
    )


def no_solution_output():
    return input_prompts() + "Unable to find a solution\n"


def test_solution_exits_successfully():
    result = run_solution(
        "5\n-2\n3\n20\n"
        "2\n-4\n-3\n-9\n"
        "1\n6\n-8\n21\n"
    )

    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize(
    ("user_input", "expected_output"),
    [
        pytest.param(
            "5\n-2\n3\n20\n"
            "2\n-4\n-3\n-9\n"
            "1\n6\n-8\n21\n",
            solution_output(5, 4, 1),
            id="sample-unique-solution",
        ),
        pytest.param(
            "1\n2\n3\n6\n"
            "4\n5\n6\n15\n"
            "7\n8\n9\n24\n",
            no_solution_output(),
            id="sample-singular-matrix",
        ),
        pytest.param(
            "1\n0\n0\n2\n"
            "0\n1\n0\n-3\n"
            "0\n0\n1\n4.5\n",
            solution_output(2, -3, 4.5),
            id="identity-coefficient-matrix",
        ),
        pytest.param(
            "2\n1\n-1\n8\n"
            "-3\n-1\n2\n-11\n"
            "-2\n1\n2\n-3\n",
            solution_output(2, 3, -1),
            id="mixed-sign-coefficients",
        ),
    ],
)
def test_solution_prints_expected_output(user_input, expected_output):
    result = run_solution(user_input)

    assert result.returncode == 0, result.stderr
    assert result.stdout == expected_output
