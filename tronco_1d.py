from dataclasses import dataclass

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from utils import empurrar_solido



@dataclass
class Tronco:
    v = np.array([
        [0, 0, 0],
        [0, 3, 0],
        [3, 0, 0],
        [3, 3, 0],
        [0.85, 0.85, 2.5],
        [0.85, 2.15, 2.5],
        [2.15, 0.85, 2.5],
        [2.15, 2.15, 2.5],
    ])

    faces_matplot = [
        [v[0], v[1], v[3], v[2]],
        [v[0], v[1], v[5], v[4]],
        [v[1], v[3], v[7], v[5]],
        [v[0], v[2], v[6], v[4]],
        [v[2], v[3], v[7], v[6]],
        [v[4], v[5], v[7], v[6]],
    ]

    faces_opengl = (
        (0, 1, 3, 2),
        (0, 1, 5, 4),
        (1, 3, 7, 5),
        (0, 2, 6, 4),
        (2, 3, 7, 6),
        (4, 5, 7, 6)
    )

    v_opengl = tuple(tuple(x) for x in v)

    def buscar_faces(self, vertices):
        novas_faces = []

        for face in self.faces_opengl:
            novas_faces.append([
                vertices[face[0]],
                vertices[face[1]],
                vertices[face[2]],
                vertices[face[3]],
            ])

        return novas_faces



def criar_tronco(empurrar=(0, 0, 0)):
    tronco = Tronco()
    v = tronco.v

    if any(empurrar):
        v = empurrar_solido(v, empurrar)

    faces = tronco.buscar_faces(v)
    return faces, v


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    plt.setp(ax.get_xticklabels(), rotation=45, va="bottom", ha="center")
    plt.setp(ax.get_yticklabels(), rotation=-20, va="bottom", ha="center")

    faces_tronco, vertices = criar_tronco()
    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])

    ax.add_collection3d(Poly3DCollection(faces_tronco, facecolors="cyan", linewidths=1, edgecolors="r", alpha=0.25))

    ax.set_zlim(0, 2.5)
    plt.xlim([0, 3])
    plt.ylim([0, 3])
    plt.show()
