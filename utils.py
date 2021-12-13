from math import cos, sin
import numpy as np


class Solido:
    _vertices = []
    _faces = []

    def __init__(self, translacao=(0, 0, 0), rotacao=0):
        if rotacao:
            self.rotacionar(rotacao)

        if any(translacao):
            self.empurrar(translacao)

    @property
    def faces_matplot(self):
        faces_em_lista = []
        for face in self._faces:
            linha = []
            for ordem in face:
                linha.append(self._vertices[ordem])
            faces_em_lista.append(linha)

        return faces_em_lista

    @property
    def faces_opengl(self):
        return self._faces

    @property
    def vertices_opengl(self):
        return tuple(tuple(x) for x in self._vertices)

    @property
    def vertices_matplot(self):
        return np.array(self._vertices)

    def empurrar(self, valor=(0, 0, 0)):
        novos_pontos = []

        for ponto in self._vertices:
            novo_ponto = [ponto[0] + valor[0], ponto[1] + valor[1], ponto[2] + valor[2]]
            novos_pontos.append(novo_ponto)

        self._vertices = novos_pontos

    def rotacionar(self, angulo):
        novos_pontos = [
            [cos(angulo), -sin(angulo), 0],
            [sin(angulo), cos(angulo), 0],
            [0, 0, 1]
        ]

        self._vertices = np.matmul(self._vertices, novos_pontos)

    @property
    def centro(self):
        todos_os_x = [vertice[0] for vertice in self._vertices]
        todos_os_y = [vertice[1] for vertice in self._vertices]
        todos_os_z = [vertice[2] for vertice in self._vertices]

        centro_x = (max(todos_os_x) + min(todos_os_x)) / 2
        centro_y = (max(todos_os_y) + min(todos_os_y)) / 2
        centro_z = (max(todos_os_z) + min(todos_os_z)) / 2

        return centro_x, centro_y, centro_z
