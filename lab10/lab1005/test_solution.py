import subprocess
import sys
from pathlib import Path
from math import sqrt

import pytest

SOLUTION = Path(__file__).resolve().parent / "solution.py"


def run_solution(input_text: str):
    """Run the solution.py and return the result."""
    return subprocess.run(
        [sys.executable, str(SOLUTION)],
        input=input_text,
        capture_output=True,
        text=True,
        check=False,
    )


def distance(point_a, point_b):
    return sqrt(
        (point_a[0] - point_b[0]) ** 2
        + (point_a[1] - point_b[1]) ** 2
        + (point_a[2] - point_b[2]) ** 2
    )


def expected_output(p1_line, p2_line, p3_line):
    p1 = [float(value) for value in p1_line.split()]
    p2 = [float(value) for value in p2_line.split()]
    p3 = [float(value) for value in p3_line.split()]

    longest_distance = max(
        distance(p1, p2),
        distance(p2, p3),
        distance(p3, p1),
    )

    return (
        "Input coordinate of P1: "
        "Input coordinate of P2: "
        "Input coordinate of P3: "
        "Output:\n"
        f"The longest distance = {longest_distance:.2f}\n"
    )


def test_solution_prints_expected_longest_distance():
    """Test the exact output for the sample input."""
    result = run_solution("0 0 0\n1 0 1\n5 3 0\n")

    expected = expected_output("0 0 0", "1 0 1", "5 3 0")

    assert result.stdout == expected
    assert result.returncode == 0


@pytest.mark.parametrize(
    ("p1_line", "p2_line", "p3_line"),
    [
        pytest.param("0 0 0", "3 4 0", "1 1 1", id="longest-p1-p2"),
        pytest.param("1 1 1", "2 2 2", "8 2 2", id="longest-p1-p3"),
        pytest.param("-1 -2 -3", "4 0 0", "4 6 8", id="negative-coordinates"),
        pytest.param(
            "0.5 1.5 2.5",
            "3.5 1.5 2.5",
            "0.5 5.5 2.5",
            id="decimal-coordinates",
        ),
    ],
)
def test_solution_handles_more_coordinate_sets(p1_line, p2_line, p3_line):
    result = run_solution(f"{p1_line}\n{p2_line}\n{p3_line}\n")

    assert result.stdout == expected_output(p1_line, p2_line, p3_line)
    assert result.returncode == 0
