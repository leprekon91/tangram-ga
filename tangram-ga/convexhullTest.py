from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
import numpy as np
points = np.array([[0, 0], [10, 0],[10, 10], [0, 10], [5, 5]]
                  )   # 30 random points in 2-D
hull = ConvexHull(points)
print(points)
print(hull.vertices)

print(hull.volume)