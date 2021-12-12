from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from utils import empurrar_solido


def criar_tronco(empurrar=(0, 0, 0)):
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

    if any(empurrar):
        v = empurrar_solido(v, empurrar)

    pontos = [
        [v[0], v[1], v[3], v[2]],
        [v[0], v[1], v[5], v[4]],
        [v[1], v[3], v[7], v[5]],
        [v[0], v[2], v[6], v[4]],
        [v[2], v[3], v[7], v[6]],
        [v[4], v[5], v[7], v[6]],
    ]

    return pontos, v


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    plt.setp(ax.get_xticklabels(), rotation=45, va="bottom", ha="center")

    faces_tronco, vertices = criar_tronco()
    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])

    ax.add_collection3d(Poly3DCollection(faces_tronco, facecolors="cyan", linewidths=1, edgecolors="r", alpha=0.25))

    ax.set_zlim(0, 2.5)
    plt.xlim([0, 3])
    plt.ylim([0, 3])
    plt.show()
