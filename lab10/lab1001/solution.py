import numpy as np

# 1) Read the size of the square matrix
n = int(input("Input size of matrix: "))

# 2) Read every element, row by row
A = np.zeros((n, n))          # n x n matrix of floats
for i in range(n):
    for j in range(n):
        A[i, j] = float(input("Input element at row %d column %d: " % (i + 1, j + 1)))

# 3) Show the matrix and its determinant
print("Output:")
print("Matrix =")
print(A)

det = np.linalg.det(A)
if abs(det) < 1e-9:           # tiny rounding error -> treat as zero
    det = 0.0
print("Determinant = %.2f" % det)

# 4) Inverse exists only when determinant is not zero
if det == 0:
    print("No inverse exists")
else:
    print("Inverse matrix =")
    print(np.linalg.inv(A))
