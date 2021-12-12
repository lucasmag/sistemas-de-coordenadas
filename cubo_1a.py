from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from utils import empurrar_solido


def criar_cubo(empurrar=(0, 0, 0)):
    v = np.array(
        [[-0.75, 0.75, 0],
         [-0.75, -0.75, 0],
         [0.75, -0.75, 0],
         [0.75, 0.75, 0],
         [-0.75, 0.75, 1.5],
         [-0.75, -0.75, 1.5],
         [0.75, -0.75, 1.5],
         [0.75, 0.75, 1.5]])

    if any(empurrar):
        v = empurrar_solido(v, empurrar)

    faces = [
        [v[0], v[1], v[2], v[3]],
        [v[0], v[1], v[5], v[4]],
        [v[1], v[2], v[6], v[5]],
        [v[2], v[3], v[7], v[6]],
        [v[3], v[0], v[4], v[7]],
        [v[4], v[5], v[6], v[7]]
    ]

    return faces, v


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.setp(ax.get_xticklabels(), rotation=30, va="bottom", ha="center")
    plt.setp(ax.get_yticklabels(), rotation=-20, va="bottom", ha="center")

    faces_cubo, vertices= criar_cubo()
    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])

    ax.add_collection3d(Poly3DCollection(faces_cubo, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    ax.set_zlim(0, 2)
    plt.xlim([-1, 1])
    plt.ylim([-1, 1])

    ax.set_box_aspect((1.0, 1.0, 1.0))
    plt.show()
