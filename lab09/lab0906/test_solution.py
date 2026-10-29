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

    assert "CelsiusToFahrenheit" in function_names, (
        "This problem requires a function named CelsiusToFahrenheit(c)."
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
    result = run_solution("25\n")
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize(
    ("celsius", "expected_fahrenheit"),
    [
        pytest.param("25", "77.00", id="sample-1"),
        pytest.param("39", "102.20", id="sample-2"),
        pytest.param("0", "32.00", id="zero"),
        pytest.param("100", "212.00", id="boiling-point"),
    ],
)
def test_solution_prints_expected_output(celsius, expected_fahrenheit):
    """Test conversion with exact output format."""
    user_input = f"{celsius}\n"
    result = run_solution(user_input)
    
    expected_output = (
        "Input temperature in degree Celcius: "
        f"The degree in Farenheit is {expected_fahrenheit}\n"
    )
    
    assert result.stdout == expected_output
    assert result.returncode == 0
