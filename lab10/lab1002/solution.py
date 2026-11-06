import numpy as np

# 1) Read C1 ... C12
C = []
for i in range(1, 13):
    C.append(float(input("Input C%d: " % i)))

# 2) Build  A * X = B
#    A = coefficients (3x3), B = right-hand side (3 values)
A = np.array([[C[0], C[1], C[2]],
              [C[4], C[5], C[6]],
              [C[8], C[9], C[10]]])
B = np.array([C[3], C[7], C[11]])

# 3) X = inverse(A) * B   (only if A has an inverse)
if abs(np.linalg.det(A)) < 1e-9:
    print("Unable to find a solution")
else:
    X = np.linalg.inv(A) @ B
    print("Solution:")
    print("x = %.2f" % X[0])
    print("y = %.2f" % X[1])
    print("z = %.2f" % X[2])
