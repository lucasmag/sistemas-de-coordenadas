from math import cos, sin, atan2
from statistics import mean
from typing import List, Tuple

import numpy as np


np.seterr(divide='ignore', invalid='ignore')


class BaseCamera:
    n: List
    u: List
    v: List
    txr: List

    def __init__(self, eye: List, at: List):
        n = np.divide(np.subtract(at, eye), abs(np.subtract(at, eye)))
        # checa se divide por 0
        self.n = self.normalizar(n)

        aux = self.gerar_vetor_aux()
        aux_normalizado = self.normalizar(aux)

        # Cria vetores u e v
        u = np.cross(self.n, aux_normalizado)
        self.u = self.normalizar(u)

        v = np.cross(self.u, self.n)
        self.v = self.normalizar(v)

        self.txr = np.matmul(self.matriz_r, self.matriz_t(eye))

    def normalizar(self, vetor):
        vetor_normalizado = np.divide(vetor, abs(np.array(vetor)))
        return list(map(lambda i: 0 if np.isnan(i) else int(i), vetor_normalizado))

    def gerar_vetor_aux(self):
        return list(map(lambda num: 1 + int(num * 5), np.random.rand(3, 1)))

    @property
    def base(self):
        return self.u[::-1], self.v, self.n

    def matriz_t(self, x):
        return [
            [1, 0, 0, -x[0]],
            [0, 1, 0, -x[1]],
            [0, 0, 1, -x[2]],
            [0, 0, 0, 1],
        ]

    @property
    def matriz_r(self):
        return [
            [self.u[0], self.u[1], self.u[2], 0],
            [self.n[0], self.n[1], self.n[2], 0],
            [self.v[0], self.v[1], self.v[2], 0],
            [0, 0, 0, 1],
        ]

    def transformar_vertice_camera(self, vertice):
        return np.matmul(self.txr, vertice + (1,))[0:3]


class Solido:
    _vertices: List[List]
    _faces: Tuple[Tuple]
    arestas: Tuple[Tuple]

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
    def centro(self):  # Centro de massa do sólido
        todos_os_x = [vertice[0] for vertice in self._vertices]
        todos_os_y = [vertice[1] for vertice in self._vertices]
        todos_os_z = [vertice[2] for vertice in self._vertices]

        centro_x = (max(todos_os_x) + min(todos_os_x)) / 2
        centro_y = (max(todos_os_y) + min(todos_os_y)) / 2
        centro_z = (max(todos_os_z) + min(todos_os_z)) / 2

        return centro_x, centro_y, centro_z

    def mudar_para_camera(self, camera: BaseCamera):
        vertices_solido_na_camera = []

        for vertice in self.vertices_opengl:
            novo_vertice = camera.transformar_vertice_camera(vertice)
            vertices_solido_na_camera.append(novo_vertice)

        self._vertices = vertices_solido_na_camera
        return vertices_solido_na_camera

    def projecao_ortogonal(self, eixo):
        # Busca média do eixo a ser achatado
        media_eixo = mean(map(lambda v: v[eixo], self._vertices))

        # Aplica média em todos os vértices do eixo
        for vertice in self._vertices:
            vertice[eixo] = media_eixo

        # Remove vértices duplicados
        self._vertices = [list(tupl) for tupl in {tuple(item) for item in self._vertices}]

        # Ordena vértices do polígono a ser recriado em 2d
        centro = (
            sum([p[0] for p in self._vertices])/len(self._vertices),
            sum([p[2] for p in self._vertices])/len(self._vertices)
        )
        self._vertices.sort(key=lambda p: atan2(p[2]-centro[1], p[0]-centro[0]))

        # Recria arestas
        novas_arestas = []
        for i in range(len(self._vertices)-1):
            novas_arestas.append([i, i+1])
        novas_arestas.append([len(self._vertices)-1, 0])

        self.arestas = novas_arestas
        print(self._vertices)


def ponto_medio_solidos(solidos: List[Solido]):
    centros_solidos = map(lambda s: s.centro, solidos)
    lista_x, lista_y, lista_z = tuple(zip(*centros_solidos))

    media_x = round(mean(lista_x), 2)
    media_y = round(mean(lista_y), 2)
    media_z = round(mean(lista_z), 2)

    return media_x, media_y, media_z
