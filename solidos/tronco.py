from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from utils import Solido


def montar_ambiente():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    plt.setp(ax.get_xticklabels(), rotation=45, va="bottom", ha="center")
    plt.setp(ax.get_yticklabels(), rotation=-20, va="bottom", ha="center")
    ax.set_box_aspect((1.0, 1.0, 1.0))
    ax.set_zlim(0, 2.5)
    plt.xlim([0, 3])
    plt.ylim([0, 3])

    return ax

class Tronco(Solido):
    def __init__(self, translacao=(0, 0, 0)):
        super().__init__(translacao)

    _vertices = [
        [0, 0, 0],
        [0, 3, 0],
        [3, 3, 0],
        [3, 0, 0],
        [0.85, 0.85, 2.5],
        [0.85, 2.15, 2.5],
        [2.15, 2.15, 2.5],
        [2.15, 0.85, 2.5],
    ]

    arestas = (
        (0, 1),
        (1, 2),
        (2, 3),
        (0, 3),
        (4, 5),
        (5, 6),
        (6, 7),
        (4, 7),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7),
    )

    _faces = [
        [0, 1, 2, 3],
        [0, 1, 5, 4],
        [1, 2, 6, 5],
        [0, 3, 7, 4],
        [3, 2, 6, 7],
        [4, 5, 6, 7],
    ]


def criar_tronco():
    ax = montar_ambiente()
    tronco = Tronco()
    faces = tronco.faces_matplot
    vertices = tronco.vertices_matplot

    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])
    ax.add_collection3d(Poly3DCollection(faces, facecolors="y", linewidths=1, edgecolors="black", alpha=0.25))
    plt.show()
