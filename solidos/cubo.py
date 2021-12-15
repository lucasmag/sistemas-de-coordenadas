from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from utils import Solido


class Cubo(Solido):

    def __init__(self, translacao=(0, 0, 0)):
        super().__init__(translacao)

    _vertices = [
        [-0.75, 0.75, 0],
        [-0.75, -0.75, 0],
        [0.75, -0.75, 0],
        [0.75, 0.75, 0],
        [-0.75, 0.75, 1.5],
        [-0.75, -0.75, 1.5],
        [0.75, -0.75, 1.5],
        [0.75, 0.75, 1.5]
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
        [2, 3, 7, 6],
        [3, 0, 4, 7],
        [4, 5, 6, 7],
    ]


def criar_cubo():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.setp(ax.get_xticklabels(), rotation=30, va="bottom", ha="center")
    plt.setp(ax.get_yticklabels(), rotation=-20, va="bottom", ha="center")
    ax.set_box_aspect((1.0, 1.0, 1.0))
    ax.set_zlim(0, 2)
    plt.xlim([-1, 1])
    plt.ylim([-1, 1])


    cubo = Cubo()
    faces_cubo = cubo.faces_matplot
    vertices = cubo.vertices_matplot

    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])
    ax.add_collection3d(Poly3DCollection(faces_cubo, facecolors='g', linewidths=1, edgecolors='black', alpha=.25))
    plt.show()
