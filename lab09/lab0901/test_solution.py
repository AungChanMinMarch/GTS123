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

    assert {"CirArea", "SqArea"} <= function_names, (
        "This problem requires functions named CirArea(x) and SqArea(x)."
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
    result = run_solution("10\n5\n")

    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize(
    ("x", "circle_area", "square_area"),
    [
        pytest.param(5, 78.54, 25.00, id="sample-values-1"),
        pytest.param(10.5, 346.36, 110.25, id="sample-values-2"),
    ],
)
def test_solution_prints_expected_total_area(x, circle_area, square_area):
    result = run_solution(f"{x}\n")

    expected_output = (
        "Input a positive number: "
        f"The area of the circle is {circle_area:.2f} square units.\n"
        f"The area of the square is {square_area:.2f} square units.\n"
    )
    
    assert result.stdout == expected_output
def test_solution_handles_negative_input():
    result = run_solution("-5\n")
    
    expected_output = "Input a positive number: Wrong Input\n"
    
    assert result.stdout == expected_output

