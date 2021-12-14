from typing import Tuple

import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from mundo import CUBO, PARALELEPIPEDO, PIRAMIDE, TRONCO
from utils import ponto_medio_solidos, BaseCamera

ORIGEM = [0, 0, 0]

colors = (
    (1, 1, 1),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 1),
    (0, 1, 0),
    (1, 0, 1),
    (0, 1, 0),
    (0, 0, 1),
)

normals = [
    (0,  0, -1),
    (-1, 0,  0),
    (0,  0,  1),
    (1,  0,  0),
    (0,  1,  0),
    (0, -1,  0),
]

X = ((-10, 0, 0), (10, 0, 0))
Y = ((0, -10, 0), (0, 10, 0))
Z = ((0, 0, -10), (0, 0, 10))

ligar_arestas = ((0, 1),)


def desenhar_eixo(eixo):
    glBegin(GL_LINES)
    for aresta in ligar_arestas:
        for vertice in aresta:
            glVertex3fv(eixo[vertice])
    glEnd()


def pontos_camera(camera, cor):
    glEnable(GL_POINT_SMOOTH)
    glPointSize(10)

    glBegin(GL_POINTS)
    glColor3d(*cor)
    glVertex3d(*camera)
    glEnd()


def desenhar_camera(camera):
    eixos = list(map(lambda eixo: [[0, 0, 0], eixo], camera.base))

    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    for eixo in eixos:
        for aresta in ligar_arestas:
            for vertice in aresta:
                glVertex3fv(eixo[vertice])
    glEnd()

    cores_eixos = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    glEnable(GL_POINT_SMOOTH)
    glPointSize(10)
    glBegin(GL_POINTS)

    for eixo, cor in zip(camera.base, cores_eixos):
        glColor3d(*cor)
        glVertex3d(*eixo)
    glEnd()

    desenhar_ponto((0, 0, 0), [1, 1, 1], 20)


def desenhar_ponto(ponto: Tuple[float], cor, tamanho=10):
    glEnable(GL_POINT_SMOOTH)
    glPointSize(tamanho)
    glColor3d(*cor)
    glBegin(GL_POINTS)
    glVertex3d(*ponto)
    glEnd()


def desenhar_solido(solido):
    vertices = solido.vertices_opengl
    faces = solido.faces_opengl

    glBegin(GL_QUADS)
    # glColor3f(0.2, 0.8, 0.5)
    for i_surface, surface in enumerate(faces):
        i = 0
        # glNormal3fv(normals[i_surface])
        for vertex in surface:
            i += 1
            glVertex3fv(vertices[vertex])
    glEnd()


def desenhar_linhas_solido(solido, cor):
    arestas = solido.arestas
    vertices = solido.vertices_opengl

    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3d(*cor)
    for edge in arestas:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pg.init()
    display = (1200, 900)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)
    # glMatrixMode(GL_PROJECTION)
    # glLoadIdentity()
    # glOrtho(0.0, 1200, 900, 0.0, 0.0, 1.0)
    glClearColor(0.8, 0.8, 0.8, 1)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    # glTranslatef(0, 0, -5)
    # gluLookAt(10, -15, 15, 0, 0, 0, 0, 0, 1)

    # Calculando at
    x, y, z = ponto_medio_solidos([PARALELEPIPEDO, TRONCO])
    at = (x, y, z)
    eye = (x, -12, z)  # ponto escolhido em outro quadrante

    camera = BaseCamera(eye, at)

    TRONCO.mudar_para_camera(camera)
    PARALELEPIPEDO.mudar_para_camera(camera)

    TRONCO.projecao_ortogonal(1)
    PARALELEPIPEDO.projecao_ortogonal(1)

    # Gerando visualizacao a partir no novo sistema de coordenadas da camera
    u, v, n = camera.base
    print(camera.base)

    x, y, z = ponto_medio_solidos([PARALELEPIPEDO, TRONCO])
    at = (x, y, z)
    print(at)
    # up = (0, 0, 1)
    # glFrustum(-5, 5, -5, 5, 8, 12)
    gluLookAt(*ORIGEM, *n, *u)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for solido, cor in zip([TRONCO, PARALELEPIPEDO], [[0.2, 0.75, 0.33], [0.1, 0.4, 0.8]]):
            # desenhar_solido(solido)
            desenhar_linhas_solido(solido, cor)

        # for eixo in [X, Y, Z]:
        #     desenhar_eixo(eixo)

        # desenhar_camera(camera)
        # pontos_eixos()
        # desenhar_ponto(at, (0, 0, 0))

        # desenhar_ponto(eye)

        pg.display.flip()
        pg.time.wait(20)


if __name__ == "__main__":
    main()
