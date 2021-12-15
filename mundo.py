from math import pi
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from solidos.cubo import Cubo
from solidos.paralelepipedo import Paralelepipedo
from solidos.piramide import Piramide
from solidos.tronco import Tronco

mundo = {
    "translacao":{
        "cubo": (4, 2, 0),
        "paralelepipedo": (-2, 0.5, 0),
        "piramide": (1.5, 2, 0),
        "tronco": (-5.5, 1, 0)
    },
    "rotacao": {
        "piramide": pi/4
    }
}

CUBO = Cubo(translacao=mundo["translacao"]["cubo"])
PARALELEPIPEDO = Paralelepipedo(translacao=mundo["translacao"]["paralelepipedo"])
PIRAMIDE = Piramide(translacao=mundo["translacao"]["piramide"], rotacao=mundo["rotacao"]["piramide"])
TRONCO = Tronco(translacao=mundo["translacao"]["tronco"])


def criar_mundo():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.setp(ax.get_yticklabels(), rotation=-20, va="bottom", ha="center")
    plt.setp(ax.get_xticklabels(), rotation=45, va="bottom", ha="center")
    ax.set_box_aspect((1.0, 1.0, 1.0))
    ax.view_init(elev=25., azim=280)
    ax.set_zlim(0, 15)
    plt.xlim([-8, 7])
    plt.ylim([-7, 8])

    cubo = Poly3DCollection(CUBO.faces_matplot, facecolors='g', linewidths=1, edgecolors='black', alpha=.3)
    paralel = Poly3DCollection(PARALELEPIPEDO.faces_matplot, facecolors='b', linewidths=1, edgecolors='black', alpha=.3)
    piramide = Poly3DCollection(PIRAMIDE.faces_matplot, facecolors='r', linewidths=1, edgecolors='black', alpha=.3)
    tronco = Poly3DCollection(TRONCO.faces_matplot, facecolors='y', linewidths=1, edgecolors="black", alpha=.3)

    for solido in [cubo, paralel, piramide, tronco]:
        ax.add_collection3d(solido)

    plt.show()


if __name__ == '__main__':
    criar_mundo()
