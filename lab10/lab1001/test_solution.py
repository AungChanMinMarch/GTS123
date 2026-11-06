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


def input_prompts(size: int) -> str:
    prompts = ["Input size of matrix: "]
    for row in range(1, size + 1):
        for col in range(1, size + 1):
            prompts.append(f"Input element at row {row} column {col}: ")
    return "".join(prompts)


def test_solution_exits_successfully():
    result = run_solution("3\n1\n0\n0\n0\n1\n0\n0\n0\n1\n")

    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize(
    ("user_input", "expected_output"),
    [
        pytest.param(
            "3\n1\n0\n0\n0\n1\n0\n0\n0\n1\n",
            input_prompts(3)
            + "Output:\n"
            + "Matrix =\n"
            + "[[1. 0. 0.]\n"
            + " [0. 1. 0.]\n"
            + " [0. 0. 1.]]\n"
            + "Determinant = 1.00\n"
            + "Inverse matrix =\n"
            + "[[1. 0. 0.]\n"
            + " [0. 1. 0.]\n"
            + " [0. 0. 1.]]\n",
            id="identity-matrix",
        ),
        pytest.param(
            "2\n4\n7\n2\n6\n",
            input_prompts(2)
            + "Output:\n"
            + "Matrix =\n"
            + "[[4. 7.]\n"
            + " [2. 6.]]\n"
            + "Determinant = 10.00\n"
            + "Inverse matrix =\n"
            + "[[ 0.6 -0.7]\n"
            + " [-0.2  0.4]]\n",
            id="invertible-2x2-matrix",
        ),
        pytest.param(
            "2\n1\n2\n2\n4\n",
            input_prompts(2)
            + "Output:\n"
            + "Matrix =\n"
            + "[[1. 2.]\n"
            + " [2. 4.]]\n"
            + "Determinant = 0.00\n"
            + "No inverse exists\n",
            id="singular-2x2-matrix",
        ),
    ],
)
def test_solution_prints_expected_output(user_input, expected_output):
    result = run_solution(user_input)

    assert result.returncode == 0, result.stderr
    assert result.stdout == expected_output
