from math import pi
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from utils import rotacionar_solido, empurrar_solido


def criar_piramide(rotacionar=0.0, empurrar=(0, 0, 0)):

    v = np.array([[-1, -1, 0], [1, -1, 0], [1, 1, 0],  [-1, 1, 0], [0, 0, 3]])

    if rotacionar:
        v = rotacionar_solido(v, rotacionar)

    if any(empurrar):
        v = empurrar_solido(v, empurrar)

    pontos = [
        [v[0], v[1], v[4]],
        [v[0], v[3], v[4]],
        [v[2], v[1], v[4]],
        [v[2], v[3], v[4]],
        [v[0], v[1], v[2], v[3]]
    ]

    return pontos, v


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.setp(ax.get_yticklabels(), rotation=-20, va="bottom", ha="center")

    # pi / 4 = 45 graus
    faces_piramide, vertices = criar_piramide(rotacionar=pi/4)
    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])

    ax.add_collection3d(Poly3DCollection(faces_piramide, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    ax.set_zlim(0, 3)
    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])

    plt.show()
