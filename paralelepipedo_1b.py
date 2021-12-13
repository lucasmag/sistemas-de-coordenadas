from dataclasses import dataclass

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from utils import empurrar_solido


fig = plt.figure()


@dataclass
class Paralelepipedo:
    v = np.array(
        [[0, 0, 0],
         [0, 5, 0],
         [1.5, 5, 0],
         [1.5, 0, 0],
         [0, 0, 2.5],
         [0, 5, 2.5],
         [1.5, 5, 2.5],
         [1.5, 0, 2.5]])

    faces_matplot = [[v[0], v[1], v[2], v[3]],
                     [v[0], v[1], v[5], v[4]],
                     [v[1], v[2], v[6], v[5]],
                     [v[2], v[3], v[7], v[6]],
                     [v[3], v[0], v[4], v[7]],
                     [v[4], v[5], v[6], v[7]]]

    faces_opengl = (
        (0, 1, 2, 3),
        (0, 1, 5, 4),
        (1, 2, 6, 5),
        (2, 3, 7, 6),
        (3, 0, 4, 7),
        (4, 5, 6, 7)
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

def criar_paralelepipedo(empurrar=(0, 0, 0)):
    para = Paralelepipedo()
    v = para.v

    if any(empurrar):
        v = empurrar_solido(v, empurrar)

    faces = para.buscar_faces(v)
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
