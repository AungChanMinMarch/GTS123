import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SOLUTION = BASE_DIR / "solution.py"
GRADES_FILE = BASE_DIR / "grades.tsv"
CREDITS = [3, 2, 1, 3, 3, 3]


def run_solution():
    return subprocess.run(
        [sys.executable, str(SOLUTION)],
        input="",
        capture_output=True,
        text=True,
        check=False,
    )


def expected_output():
    lines = ["Student ID\tGPA"]

    for line in GRADES_FILE.read_text().splitlines():
        parts = line.split()
        student_id = parts[0]
        grades = [float(value) for value in parts[1:]]
        gpa = sum(grade * credit for grade, credit in zip(grades, CREDITS)) / sum(
            CREDITS
        )
        lines.append(f"{student_id}\t{gpa:.2f}")

    return "\n".join(lines) + "\n"


def test_solution_exits_successfully():
    result = run_solution()

    assert result.returncode == 0, result.stderr


def test_solution_prints_gpa_for_all_students():
    result = run_solution()

    assert result.stdout == expected_output()


def test_solution_prints_sample_students_correctly():
    result = run_solution()
    lines = result.stdout.splitlines()

    assert lines[0] == "Student ID\tGPA"
    assert lines[1] == "6322882296\t2.77"
    assert lines[2] == "6322881601\t2.67"
    assert len(lines) == 21
