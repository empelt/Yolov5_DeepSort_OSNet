import numpy as np

a = np.array([100, 0])
b = np.array([100, 100])
p = np.array([200, 50])

ab = b - a
ap = p - a
cross_product = np.cross(ap, ab)
print("cross product=", cross_product)
