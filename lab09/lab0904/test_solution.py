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

    assert {"UserInput", "FindBMI", "ShowBMI"} <= function_names, (
        "This problem requires functions named UserInput(), FindBMI(hh, ww), "
        "and ShowBMI(MyBMI)."
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
    result = run_solution("45\n1.61\n")
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize(
    ("weight", "height", "expected_bmi"),
    [
        pytest.param("45", "1.61", "17.36", id="sample-1"),
        pytest.param("80", "1.75", "26.12", id="sample-2"),
        pytest.param("65", "1.80", "20.06", id="sample-3"),
        pytest.param("70", "1.75", "22.86", id="another-case"),
    ],
)
def test_solution_prints_expected_bmi(weight, height, expected_bmi):
    """Test BMI calculation with exact output format."""
    user_input = f"{weight}\n{height}\n"
    result = run_solution(user_input)
    
    expected_output = (
        f"Input your weight (kilogram): "
        f"Input your height (meter): "
        f"The user BMI is {expected_bmi}\n"
    )
    
    assert result.stdout == expected_output
    assert result.returncode == 0
