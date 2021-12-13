from math import pi
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from utils import Solido


class Piramide(Solido):

    _vertices = np.array([[-1, -1, 0], [1, -1, 0], [1, 1, 0],  [-1, 1, 0], [0, 0, 3]])
    _faces = ((0, 1, 4), (0, 3, 4), (2, 1, 4), (2, 3, 4), (0, 1, 2, 3),)

    def __init__(cls, translacao=(0, 0, 0), rotacao=0):
        super().__init__(translacao, rotacao)


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.setp(ax.get_xticklabels(), rotation=10, va="bottom", ha="center")
    plt.setp(ax.get_yticklabels(), rotation=-20, va="bottom", ha="center")

    # pi / 4 = 45 graus
    piramide = Piramide(rotacao=pi/4)
    faces = piramide.faces_matplot
    vertices = piramide.vertices_matplot
    centro = piramide.centro

    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])
    ax.scatter3D(*centro)

    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    ax.set_zlim(0, 3)
    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])

    plt.show()
