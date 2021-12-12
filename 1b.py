from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

v = np.array(
    [[0, 0, 0],
     [0, 5, 0],
     [1.5, 5, 0],
     [1.5, 0, 0],
     [0, 0, 2.5],
     [0, 5, 2.5],
     [1.5, 5, 2.5],
     [1.5, 0, 2.5]])

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

verts = [[v[0], v[1], v[2], v[3]],
         [v[0], v[1], v[5], v[4]],
         [v[1], v[2], v[6], v[5]],
         [v[2], v[3], v[7], v[6]],
         [v[3], v[0], v[4], v[7]],
         [v[4], v[5], v[6], v[7]]]

ax.add_collection3d(Poly3DCollection(verts,
 facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))


ax.set_zlim(0, 5)
plt.xlim([0, 5])
plt.ylim([0, 5])
plt.show()
