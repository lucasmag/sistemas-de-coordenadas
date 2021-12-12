from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from utils import empurrar_solido


fig = plt.figure()


def criar_paralelepipedo(empurrar=(0, 0, 0)):
    v = np.array(
        [[0, 0, 0],
         [0, 5, 0],
         [1.5, 5, 0],
         [1.5, 0, 0],
         [0, 0, 2.5],
         [0, 5, 2.5],
         [1.5, 5, 2.5],
         [1.5, 0, 2.5]])

    if any(empurrar):
        v = empurrar_solido(v, empurrar)

    faces = [[v[0], v[1], v[2], v[3]],
             [v[0], v[1], v[5], v[4]],
             [v[1], v[2], v[6], v[5]],
             [v[2], v[3], v[7], v[6]],
             [v[3], v[0], v[4], v[7]],
             [v[4], v[5], v[6], v[7]]]

    return faces, v


if __name__ == '__main__':
    faces_paralelepipedo, vertices = criar_paralelepipedo()

    ax = fig.add_subplot(111, projection='3d')
    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])

    ax.add_collection3d(Poly3DCollection(
        faces_paralelepipedo,
        facecolors='cyan',
        linewidths=1,
        edgecolors='r',
        alpha=.25)
    )

    plt.setp(ax.get_xticklabels(), rotation=30, va="bottom", ha="center")
    plt.setp(ax.get_yticklabels(), rotation=-20, va="bottom", ha="center")

    ax.set_zlim(0, 5)
    plt.xlim([0, 5])
    plt.ylim([0, 5])
    plt.show()
