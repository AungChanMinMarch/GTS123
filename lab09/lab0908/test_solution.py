import ast
import subprocess
import sys
from pathlib import Path
import pytest

SOLUTION = Path(__file__).resolve().parent / "solution.py"


def test_solution_defines_required_function():
    tree = ast.parse(SOLUTION.read_text())
    function_names = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }

    assert "myRange" in function_names, (
        "This problem requires a function named myRange(FirstVal, UpperBound, StepSize)."
    )


def run_solution(user_input: str):
    return subprocess.run(
        [sys.executable, str(SOLUTION)],
        input=user_input,
        capture_output=True,
        text=True,
        check=False,
    )


def test_solution_exits_successfully():
    """Test that the program runs without crashing."""
    result = run_solution("0\n10\n2\n")
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize(
    ("user_input", "expected_output"),
    [
        pytest.param(
            "0\n10\n2\n",
            "Enter the first number: Enter the upper bound: Enter the step: Range = [0, 2, 4, 6, 8]\n",
            id="sample-1"
        ),
        pytest.param(
            "5\n20\n4\n",
            "Enter the first number: Enter the upper bound: Enter the step: Range = [5, 9, 13, 17]\n",
            id="sample-2"
        ),
        pytest.param(
            "9\n8\n4\n",
            "Enter the first number: Enter the upper bound: Enter the step: First number should be less than upper bound.\n",
            id="first-greater-than-upper"
        ),
        pytest.param(
            "2.5\n2\n4\n",
            "Enter the first number: Please enter valid integers.\n",
            id="non-integer-input"
        ),
        pytest.param(
            "2\n9\n0\n",
            "Enter the first number: Enter the upper bound: Enter the step: Step size cannot be zero.\n",
            id="step-zero"
        ),
        pytest.param(
            "10\n0\n-2\n",
            "Enter the first number: Enter the upper bound: Enter the step: Range = [10, 8, 6, 4, 2]\n",
            id="negative-step"
        ),
    ],
)
def test_solution_prints_expected_output(user_input, expected_output):
    """Test all cases with exact output format."""
    result = run_solution(user_input)
    assert result.stdout == expected_output
    assert result.returncode == 0
