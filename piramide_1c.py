from dataclasses import dataclass
from math import pi
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from utils import rotacionar_solido, empurrar_solido


@dataclass
class Piramide:
    v = np.array([[-1, -1, 0], [1, -1, 0], [1, 1, 0],  [-1, 1, 0], [0, 0, 3]])

    faces_matplot = [
        [v[0], v[1], v[4]],
        [v[0], v[3], v[4]],
        [v[2], v[1], v[4]],
        [v[2], v[3], v[4]],
        [v[0], v[1], v[2], v[3]]
    ]

    faces_opengl = (
        (0, 1, 4),
        (0, 3, 4),
        (2, 1, 4),
        (2, 3, 4),
        (0, 1, 2, 3),
    )

    v_opengl = tuple(tuple(x) for x in v)

    def buscar_faces(self, vertices):
        novas_faces = []

        for face in range(4):
            novas_faces.append([
                vertices[self.faces_opengl[face][0]],
                vertices[self.faces_opengl[face][1]],
                vertices[self.faces_opengl[face][2]],
            ])

        novas_faces.append([
            vertices[self.faces_opengl[-1][0]],
            vertices[self.faces_opengl[-1][1]],
            vertices[self.faces_opengl[-1][2]],
            vertices[self.faces_opengl[-1][3]],
        ])

        return novas_faces


def criar_piramide(rotacionar=0.0, empurrar=(0, 0, 0)):
    piramide = Piramide()
    v = piramide.v

    if rotacionar:
        v = rotacionar_solido(v, rotacionar)

    if any(empurrar):
        v = empurrar_solido(v, empurrar)

    faces = piramide.buscar_faces(v)
    return faces, v


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.setp(ax.get_xticklabels(), rotation=10, va="bottom", ha="center")
    plt.setp(ax.get_yticklabels(), rotation=-20, va="bottom", ha="center")

    # pi / 4 = 45 graus
    faces_piramide, vertices = criar_piramide(rotacionar=pi/4)
    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])

    ax.add_collection3d(Poly3DCollection(faces_piramide, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    ax.set_zlim(0, 3)
    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])

    plt.show()
