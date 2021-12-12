from math import cos, sin

import numpy as np


def empurrar_solido(vertices, valor=(0, 0, 0)):
    novos_pontos = []

    for ponto in vertices:
        novo_ponto = [ponto[0] + valor[0], ponto[1] + valor[1], ponto[2] + valor[2]]
        novos_pontos.append(novo_ponto)

    return np.array(novos_pontos)


def rotacionar_solido(vertices, angulo):
    novos_pontos = [
        [cos(angulo), -sin(angulo), 0],
        [sin(angulo), cos(angulo), 0],
        [0, 0, 1]
    ]

    return np.matmul(vertices, novos_pontos)
