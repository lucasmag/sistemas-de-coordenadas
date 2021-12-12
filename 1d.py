from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

v = np.array([
    [0, 0, 0],
    [0, 3, 0],
    [3, 0, 0],
    [3, 3, 0],
    [0.85, 0.85, 2.5],
    [0.85, 1.7, 2.5],
    [1.7, 0.85, 2.5],
    [1.7, 1.7, 2.5],
])

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

verts = [
    [v[0], v[1], v[3], v[2]],
    [v[0], v[1], v[5], v[4]],
    [v[1], v[3], v[7], v[5]],
    [v[0], v[2], v[6], v[4]],
    [v[2], v[3], v[7], v[6]],
    [v[4], v[5], v[7], v[6]],
]


plt.setp(ax.get_xticklabels(), rotation=45, va="bottom", ha="center")

ax.add_collection3d(
    Poly3DCollection(verts, facecolors="cyan", linewidths=1, edgecolors="r", alpha=0.25)
)

ax.set_zlim(0, 2.5)
plt.xlim([0, 3])
plt.ylim([0, 3])
plt.show()
