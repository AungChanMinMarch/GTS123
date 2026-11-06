import numpy as np

# 1) Read 3 points, e.g. "0 0 0"  ->  array([0., 0., 0.])
p1 = np.array(input("Input coordinate of P1: ").split(), dtype=float)
p2 = np.array(input("Input coordinate of P2: ").split(), dtype=float)
p3 = np.array(input("Input coordinate of P3: ").split(), dtype=float)

# 2) Distance between two points = sqrt(sum of squared differences)
def distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# 3) Find the longest of the 3 distances
d = np.array([distance(p1, p2), distance(p2, p3), distance(p3, p1)])

print("Output:")
print("The longest distance = %.2f" % np.max(d))
