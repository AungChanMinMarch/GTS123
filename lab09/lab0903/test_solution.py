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

    assert {"UserInput", "SumOut", "MinOut", "MaxOut"} <= function_names, (
        "This problem requires functions named UserInput(), SumOut(), "
        "MinOut(), and MaxOut()."
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
    """Test that the program doesn't crash on valid input."""
    result = run_solution("1\n2\n3\nDone\n")
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize(
    ("user_input", "expected_output"),
    [
        pytest.param(
            "1\n2\n3\nDone\n",
            "Enter an input: Enter an input: Enter an input: Enter an input: "
            "The summation is 6\n"
            "The minimum is 1\n"
            "The maximum is 3\n",
            id="sample-1",
        ),
        pytest.param(
            "7\n5\n3\n0\n1\nDone\n",
            "Enter an input: Enter an input: Enter an input: Enter an input: "
            "Enter an input: Enter an input: "
            "The summation is 16\n"
            "The minimum is 0\n"
            "The maximum is 7\n",
            id="sample-2",
        ),
        pytest.param(
            "10\n20\n30\nDone\n",
            "Enter an input: Enter an input: Enter an input: Enter an input: "
            "The summation is 60\n"
            "The minimum is 10\n"
            "The maximum is 30\n",
            id="another-valid-case",
        ),
    ],
)
def test_solution_prints_expected_output(user_input, expected_output):
    """Test successful cases with exact output format."""
    result = run_solution(user_input)
    assert result.stdout == expected_output


def test_negative_number_error():
    """Test error when negative number is entered."""
    result = run_solution("1\n2\n-5\n")
    expected_output = "Enter an input: Enter an input: Enter an input: Error\n"
    assert result.stdout == expected_output


def test_non_integer_error():
    """Test error when non-integer (float) is entered."""
    result = run_solution("1\n2\n3\n4\n5.5\n")
    expected_output = (
        "Enter an input: Enter an input: Enter an input: Enter an input: "
        "Enter an input: Error\n"
    )
    assert result.stdout == expected_output


def test_invalid_text_error():
    """Test error when non-number text is entered."""
    result = run_solution("1\n2\nabc\n")
    expected_output = "Enter an input: Enter an input: Enter an input: Error\n"
    assert result.stdout == expected_output
