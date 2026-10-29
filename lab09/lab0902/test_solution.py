import ast
import subprocess
import sys
from pathlib import Path
import pytest
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

    assert {"LeftRotate", "RightRotate"} <= function_names, (
        "This problem requires functions named LeftRotate() and RightRotate()."
    )


def run_solution(user_input: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SOLUTION)],
        input=user_input,
        capture_output=True,
        text=True,
        check=False,
    )


def test_solution_exits_successfully():
    """Test that the program doesn't crash on valid input."""
    result = run_solution("a b c 1 2\n1\n")
    assert result.returncode == 0, f"Program crashed: {result.stderr}"


@pytest.mark.parametrize(
    ("inputs", "n", "expected_left", "expected_right"),
    [
        pytest.param(
            "a b c 1 2",
            "1",
            "['b', 'c', '1', '2', 'a']",
            "['2', 'a', 'b', 'c', '1']",
            id="sample-1",
        ),
        pytest.param(
            "w x y z 5",
            "4",
            "['5', 'w', 'x', 'y', 'z']",
            "['x', 'y', 'z', '5', 'w']",
            id="sample-2",
        ),
        pytest.param(
            "hello world python 42 99",
            "0",
            "['hello', 'world', 'python', '42', '99']",
            "['hello', 'world', 'python', '42', '99']",
            id="zero-rotations",
        ),
    ],
)
def test_successful_rotations(inputs, n, expected_left, expected_right):
    """Test successful left and right rotations with exact output format."""
    user_input = f"{inputs}\n{n}\n"
    
    result = run_solution(user_input)
    
    expected_output = (
        f"Enter 5 inputs: Enter an integer number of rotations (0-4): "
        f"The left-rotated list: {expected_left}\n"
        f"The right-rotated list: {expected_right}\n"
    )
    
    assert result.stdout == expected_output
    assert result.returncode == 0


def test_out_of_range_integer():
    """Test error when n is integer but outside 0-4."""
    user_input = "a b c 1 2\n6\n"
    result = run_solution(user_input)
    
    expected_output = (
        "Enter 5 inputs: Enter an integer number of rotations (0-4): Error!\n"
    )
    
    assert result.stdout == expected_output
    assert result.returncode == 0


def test_non_integer_input():
    """Test error when n is not an integer (e.g. 2.5)."""
    user_input = "w x y z 5\n2.5\n"
    result = run_solution(user_input)
    
    expected_output = (
        "Enter 5 inputs: Enter an integer number of rotations (0-4): Error!\n"
    )
    
    assert result.stdout == expected_output
    assert result.returncode == 0


def test_negative_number():
    """Test error when n is negative."""
    user_input = "a b c d e\n-1\n"
    result = run_solution(user_input)
    
    expected_output = (
        "Enter 5 inputs: Enter an integer number of rotations (0-4): Error!\n"
    )
    
    assert result.stdout == expected_output
    assert result.returncode == 0

    
