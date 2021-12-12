from math import pi
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from cubo_1a import criar_cubo
from paralelepipedo_1b import criar_paralelepipedo
from piramide_1c import criar_piramide
from tronco_1d import criar_tronco

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.setp(ax.get_yticklabels(), rotation=-20, va="bottom", ha="center")


def criar_universo():
    cubo, *_ = criar_cubo(empurrar=(5, 2, 0))
    piramide, *_ = criar_piramide(pi/4, (2, 2, 0))
    paralelepipedo, *_ = criar_paralelepipedo(empurrar=(-1.5, 0, 0))
    tronco, *_ = criar_tronco(empurrar=(-5.5, 0, 0))

    ax.add_collection3d(Poly3DCollection(cubo, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
    ax.add_collection3d(Poly3DCollection(piramide, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
    ax.add_collection3d(Poly3DCollection(paralelepipedo, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
    ax.add_collection3d(Poly3DCollection(tronco, facecolors="cyan", linewidths=1, edgecolors="r", alpha=0.25))

    plt.setp(ax.get_xticklabels(), rotation=45, va="bottom", ha="center")
    ax.view_init(elev=25., azim=280)
    ax.set_zlim(0, 15)
    plt.xlim([-8, 7])
    plt.ylim([-7, 8])

    plt.show()


if __name__ == '__main__':
    criar_universo()
