import ast
import subprocess
import sys
from pathlib import Path
import pytest

SOLUTION = Path(__file__).resolve().parent / "solution.py"


def test_solution_defines_required_functions():
    tree = ast.parse(SOLUTION.read_text())
    function_names = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }

    assert {"SquareArea", "CircleArea"} <= function_names, (
        "This problem requires functions named SquareArea(x) and CircleArea(r)."
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
    result = run_solution("s\n10\n")
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize(
    ("user_input", "expected_output"),
    [
        pytest.param(
            "s\n10\n",
            "Do you want to find the area of a square (s) or a circle (c)?: "
            "Enter the length: The area of the square is 100.00.\n",
            id="square-sample"
        ),
        pytest.param(
            "c\n2\n",
            "Do you want to find the area of a square (s) or a circle (c)?: "
            "Enter the length: The area of the square is 12.57.\n",
            id="circle-sample"
        ),
        pytest.param(
            "a\n",
            "Do you want to find the area of a square (s) or a circle (c)?: Wrong Input\n",
            id="wrong-input"
        ),
        pytest.param(
            "S\n",
            "Do you want to find the area of a square (s) or a circle (c)?: Wrong Input\n",
            id="uppercase-wrong"
        ),
    ],
)
def test_solution_prints_expected_output(user_input, expected_output):
    """Test with exact output format."""
    result = run_solution(user_input)
    assert result.stdout == expected_output
    assert result.returncode == 0
