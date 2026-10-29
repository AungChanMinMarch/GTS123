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

    assert "myCylinder" in function_names, (
        "This problem requires a function named myCylinder(r, h)."
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
    result = run_solution("1\n3\n")
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize(
    ("radius", "height", "expected_output"),
    [
        pytest.param(
            "1", "3",
            "Enter the radius r of the cylinder: Enter the height h of the cylinder: "
            "The volume is 9.42 and the surface area is 25.13.\n",
            id="sample-1"
        ),
        pytest.param(
            "3.3", "4.5",
            "Enter the radius r of the cylinder: Enter the height h of the cylinder: "
            "The volume is 153.95 and the surface area is 161.73.\n",
            id="sample-2"
        ),
        pytest.param(
            "5", "10",
            "Enter the radius r of the cylinder: Enter the height h of the cylinder: "
            "The volume is 785.40 and the surface area is 471.24.\n",
            id="another-case"
        ),
        pytest.param(
            "-2", "4",
            "Enter the radius r of the cylinder: Enter the height h of the cylinder: "
            "Please enter positive values for both radius and height.\n",
            id="negative-radius"
        ),
        pytest.param(
            "5", "-1",
            "Enter the radius r of the cylinder: Enter the height h of the cylinder: "
            "Please enter positive values for both radius and height.\n",
            id="negative-height"
        ),
    ],
)
def test_solution_prints_expected_output(radius, height, expected_output):
    """Test with exact output format."""
    user_input = f"{radius}\n{height}\n"
    result = run_solution(user_input)
    assert result.stdout == expected_output
    assert result.returncode == 0
