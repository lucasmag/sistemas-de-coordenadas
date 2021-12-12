from math import sin, cos, pi
import numpy
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


def rotacionar(original, angulo):
    matrix = [
        [cos(angulo), -sin(angulo), 0],
        [sin(angulo), cos(angulo), 0],
        [0, 0, 1]
    ]

    return numpy.matmul(original, matrix)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.setp(ax.get_yticklabels(), rotation=-20, va="bottom", ha="center")

v = np.array([[-1, -1, 0], [1, -1, 0], [1, 1, 0],  [-1, 1, 0], [0, 0, 3]])

# pi / 4 = 45 graus
v = rotacionar(v, pi / 4)

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

verts = [[v[0], v[1], v[4]],
         [v[0], v[3], v[4]],
         [v[2], v[1], v[4]],
         [v[2], v[3], v[4]],
         [v[0], v[1], v[2], v[3]]]

ax.add_collection3d(Poly3DCollection(verts,
 facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

ax.set_zlim(0, 3)
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])

plt.show()
