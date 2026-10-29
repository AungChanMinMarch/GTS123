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

    assert "TriArea" in function_names, (
        "This problem requires a function named TriArea(h, b)."
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
    result = run_solution("2\n4\n")
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize(
    ("height", "base", "expected_output"),
    [
        pytest.param("2", "4", 
                    "Enter the height (h): Enter the base (b): The area of the triangle is 4.0\n",
                    id="sample-1"),
        pytest.param("15", "2", 
                    "Enter the height (h): Enter the base (b): The area of the triangle is 15.0\n",
                    id="sample-2"),
        pytest.param("7.5", "3.2", 
                    "Enter the height (h): Enter the base (b): The area of the triangle is 12.0\n",
                    id="decimal"),
        pytest.param("-2", "5", 
                    "Enter the height (h): Enter the base (b): Height and base must be non-negative.\n",
                    id="negative-height"),
        pytest.param("2", "-5", 
                    "Enter the height (h): Enter the base (b): Height and base must be non-negative.\n",
                    id="negative-base"),
    ],
)
def test_solution_prints_expected_output(height, base, expected_output):
    """Test with exact output format including error case."""
    user_input = f"{height}\n{base}\n"
    result = run_solution(user_input)
    assert result.stdout == expected_output
    assert result.returncode == 0
