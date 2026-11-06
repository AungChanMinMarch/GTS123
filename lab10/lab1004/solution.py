import numpy as np
from pathlib import Path

# sales.tsv is in the same folder as this file
FILE = Path(__file__).parent / "sales.tsv"

# 1) Load the file: column 0 = branch, other columns = sales
data = np.loadtxt(FILE, dtype=int, ndmin=2)
branches = data[:, 0]
totals = data[:, 1:].sum(axis=1)      # total sales of each branch

# 2) np.argsort sorts small -> large, so sort by -totals to get large -> small
#    (kind="stable" keeps file order when two totals are equal)
order = np.argsort(-totals, kind="stable")

# 3) Print the table
print("Branch\tTotal Sales")
for i in order:
    print("%d\t%d" % (branches[i], totals[i]))
