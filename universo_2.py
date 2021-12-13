from math import pi
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from cubo_1a import Cubo
from paralelepipedo_1b import Paralelepipedo
from piramide_1c import Piramide
from tronco_1d import Tronco

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# ax.set_proj_type('ortho')

plt.setp(ax.get_yticklabels(), rotation=-20, va="bottom", ha="center")

mundo = {
    "translacao":{
        "cubo": (5, 2, 0),
        "paralelepipedo": (-1.5, 0, 0),
        "piramide": (2, 2, 0),
        "tronco": (-5.5, 0, 0)
    },
    "rotacao": {
        "piramide": pi/4
    }
}

CUBO = Cubo(translacao=mundo["translacao"]["cubo"])
PARALELEPIPEDO = Paralelepipedo(translacao=mundo["translacao"]["paralelepipedo"])
PIRAMIDE = Piramide(translacao=mundo["translacao"]["piramide"], rotacao=mundo["rotacao"]["piramide"])
TRONCO = Tronco(translacao=mundo["translacao"]["tronco"])


def criar_universo():
    ax.add_collection3d(Poly3DCollection(CUBO.faces_matplot, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
    ax.add_collection3d(Poly3DCollection(PARALELEPIPEDO.faces_matplot, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
    ax.add_collection3d(Poly3DCollection(PIRAMIDE.faces_matplot, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
    ax.add_collection3d(Poly3DCollection(TRONCO.faces_matplot, facecolors="cyan", linewidths=1, edgecolors="r", alpha=0.25))

    plt.setp(ax.get_xticklabels(), rotation=45, va="bottom", ha="center")
    ax.view_init(elev=25., azim=280)
    ax.set_zlim(0, 15)
    plt.xlim([-8, 7])
    plt.ylim([-7, 8])

    plt.show()


if __name__ == '__main__':
    criar_universo()
