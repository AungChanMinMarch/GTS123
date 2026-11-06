import numpy as np
from pathlib import Path

# grades.tsv is in the same folder as this file
FILE = Path(__file__).parent / "grades.tsv"

# 1) Load the file: column 0 = student ID, columns 1-6 = grades
data = np.loadtxt(FILE, dtype=str)
ids = data[:, 0]
grades = data[:, 1:].astype(float)

# 2) Credits of the 6 courses
credits = np.array([3, 2, 1, 3, 3, 3])

# 3) GPA = sum(grade * credit) / sum(credit)   -- for every student at once
gpa = (grades @ credits) / credits.sum()

# 4) Print the table
print("Student ID\tGPA")
for i in range(len(ids)):
    print("%s\t%.2f" % (ids[i], gpa[i]))
