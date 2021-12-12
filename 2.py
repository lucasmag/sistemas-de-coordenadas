from math import sin, cos
import numpy
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


def empurra(solido, x=0, y=0, z=0):
    nova_lista = []
    for ponto in solido:
        novo_ponto = [ponto[0] + x, ponto[1] + y, ponto[2] + z]
        nova_lista.append(novo_ponto)

    return np.array(nova_lista)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.setp(ax.get_yticklabels(), rotation=-20, va="bottom", ha="center")

# cubo

v = np.array([[-0.75, 0.75, 0], [-0.75, -0.75, 0], [0.75, -0.75, 0],  [0.75, 0.75, 0],
              [-0.75, 0.75, 1.5], [-0.75, -0.75, 1.5], [0.75, -0.75, 1.5],  [0.75, 0.75, 1.5]])

v = empurra(v, x=5, y=2)

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

verts = [[v[0], v[1], v[2], v[3]],
         [v[0], v[1], v[5], v[4]],
         [v[1], v[2], v[6], v[5]],
         [v[2], v[3], v[7], v[6]],
         [v[3], v[0], v[4], v[7]],
         [v[4], v[5], v[6], v[7]]]

ax.add_collection3d(Poly3DCollection(verts,
 facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))


def rotate(lista, angulo):
    nova_lista = [lista[0]]

    for ponto in lista[1:]:
        x = ponto[0] * sin(angulo) - ponto[1] * sin(angulo)
        y = ponto[0] * sin(angulo) + ponto[1] * cos(angulo)
        z = ponto[2]
        nova_lista.append([x, y, z])

    return np.array(nova_lista)


def rotacionar(original, angulo):
    matrix = [
        [cos(angulo), -sin(angulo), 0],
        [sin(angulo), cos(angulo), 0],
        [0, 0, 1]
    ]

    return numpy.matmul(original, matrix)

# piramide
v = np.array([[-1, -1, 0], [1, -1, 0], [1, 1, 0], [-1, 1, 0], [0, 0, 3]])

v = rotacionar(v, 45)
v = empurra(v, x=2, y=2)

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

verts2 = [ [v[0],v[1],v[4]], [v[0],v[3],v[4]],
 [v[2],v[1],v[4]], [v[2],v[3],v[4]], [v[0],v[1],v[2],v[3]]]

ax.add_collection3d(Poly3DCollection(verts2,
 facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))


# paralelepipedo

v = np.array(
    [[0, 0, 0],
     [0, 5, 0],
     [1.5, 5, 0],
     [1.5, 0, 0],
     [0, 0, 2.5],
     [0, 5, 2.5],
     [1.5, 5, 2.5],
     [1.5, 0, 2.5]])

v = empurra(v, x=-1.5)
ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

verts = [[v[0], v[1], v[2], v[3]],
         [v[0], v[1], v[5], v[4]],
         [v[1], v[2], v[6], v[5]],
         [v[2], v[3], v[7], v[6]],
         [v[3], v[0], v[4], v[7]],
         [v[4], v[5], v[6], v[7]]]

ax.add_collection3d(Poly3DCollection(verts,
 facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))


# tronco

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
v = empurra(v, x=-5.5)

# v = rotate(v, 45)

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
ax.view_init(elev=25., azim=280)
ax.set_zlim(0, 15)
plt.xlim([-8, 7])
plt.ylim([-7, 8])

plt.show()
