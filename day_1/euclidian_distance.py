import numpy as np

point1 = np.array((2, 3))
point2 = np.array((10, 8))

dist = np.linalg.norm(point1 - point2)

print(dist)