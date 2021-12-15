from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from utils import Solido


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect((1.0, 1.0, 1.0))
plt.setp(ax.get_xticklabels(), rotation=30, va="bottom", ha="center")
plt.setp(ax.get_yticklabels(), rotation=-20, va="bottom", ha="center")

ax.set_zlim(0, 5)
plt.xlim([0, 5])
plt.ylim([0, 5])


class Paralelepipedo(Solido):

    def __init__(cls, translacao=(0, 0, 0)):
        super().__init__(translacao)

    _vertices = [
        [0, 0, 0],
        [0, 5, 0],
        [1.5, 5, 0],
        [1.5, 0, 0],
        [0, 0, 2.5],
        [0, 5, 2.5],
        [1.5, 5, 2.5],
        [1.5, 0, 2.5]
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


def criar_paralelepipedo():
    paralelepipedo = Paralelepipedo()
    faces = paralelepipedo.faces_matplot
    vertices = paralelepipedo.vertices_matplot

    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])
    ax.add_collection3d(Poly3DCollection(faces, facecolors='b', linewidths=1, edgecolors='black', alpha=.25))
    plt.show()
