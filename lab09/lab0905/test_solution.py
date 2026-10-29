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

    assert {"SeatType", "MovieType", "TicketPrice"} <= function_names, (
        "This problem requires functions named SeatType(), MovieType(), "
        "and TicketPrice()."
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
    result = run_solution("D\n2\n")
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize(
    ("user_input", "expected_output"),
    [
        pytest.param(
            "D\n2\n",
            "Select the seat type (P or D or H): Select the movie type (1 or 2): "
            "The ticket price is 200\n",
            id="sample-1",
        ),
        pytest.param(
            "H\n1\n",
            "Select the seat type (P or D or H): Select the movie type (1 or 2): "
            "The ticket price is 400\n",
            id="sample-2",
        ),
        pytest.param(
            "A\nB\nP\n1\n",
            "Select the seat type (P or D or H): Wrong seat type! Please select again.\n"
            "Select the seat type (P or D or H): Wrong seat type! Please select again.\n"
            "Select the seat type (P or D or H): Select the movie type (1 or 2): "
            "The ticket price is 100\n",
            id="wrong-seat-twice",
        ),
        pytest.param(
            "H\n4\n5\n2\n",
            "Select the seat type (P or D or H): Select the movie type (1 or 2): "
            "Wrong movie type! Please select again.\n"
            "Select the movie type (1 or 2): Wrong movie type! Please select again.\n"
            "Select the movie type (1 or 2): The ticket price is 500\n",
            id="wrong-movie-twice",
        ),
    ],
)
def test_solution_prints_expected_output(user_input, expected_output):
    """Test with exact output format including error messages."""
    result = run_solution(user_input)
    assert result.stdout == expected_output
    assert result.returncode == 0
