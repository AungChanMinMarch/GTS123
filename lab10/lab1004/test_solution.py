import subprocess
import sys
from pathlib import Path

SOLUTION = Path(__file__).resolve().parent / "solution.py"
SALES_FILE = Path(__file__).resolve().parent / "sales.tsv"


def run_solution():
    """Run the solution.py and return the result."""
    return subprocess.run(
        [sys.executable, str(SOLUTION)],
        input="",
        capture_output=True,
        text=True,
        check=False,
        cwd=SOLUTION.parent,
    )


def expected_output_from_sales(data_text):
    rows = []
    for line in data_text.strip().splitlines():
        values = [int(value) for value in line.split()]
        branch = values[0]
        total = sum(values[1:])
        rows.append((branch, total))

    rows.sort(key=lambda row: row[1], reverse=True)

    output = ["Branch\tTotal Sales"]
    output.extend(f"{branch}\t{total}" for branch, total in rows)
    return "\n".join(output) + "\n"


def test_solution_exits_successfully():
    """Test that the program runs without crashing."""
    result = run_solution()
    assert result.returncode == 0


def test_solution_prints_expected_branch_sales():
    """Test the exact branch totals output from sales.tsv."""
    result = run_solution()

    assert result.stdout == expected_output_from_sales(SALES_FILE.read_text())
    assert result.returncode == 0


def test_solution_calculates_from_sales_file_instead_of_hardcoding():
    """Use different sales data so hard-coded sample output cannot pass."""
    original_data = SALES_FILE.read_text()
    alternate_data = (
        "2001\t10\t20\t30\n"
        "2002\t100\t5\t5\n"
        "2003\t1\t2\t3\n"
        "2004\t50\t50\t50\n"
    )

    try:
        SALES_FILE.write_text(alternate_data)
        result = run_solution()
    finally:
        SALES_FILE.write_text(original_data)

    assert result.stdout == expected_output_from_sales(alternate_data)
    assert result.returncode == 0
