from typing import Tuple

import pygame as pg
from OpenGL.GL import glBegin, glEnd
from OpenGL.raw.GL.VERSION.GL_1_0 import GL_LINES, glVertex3fv, glEnable, glPointSize, GL_POINT_SMOOTH, GL_POINTS, \
    glColor3d, glVertex3d, GL_QUADS, glLineWidth, glClearColor, glClear, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT
from OpenGL.raw.GLU import gluPerspective, gluLookAt
from pygame import DOUBLEBUF
from pygame.constants import OPENGL

from mundo import PARALELEPIPEDO, TRONCO
from utils import ponto_medio_solidos, BaseCamera

ORIGEM = [0, 0, 0]
CORES = [[0.2, 0.75, 0.33], [0.1, 0.4, 0.8]]  # verde e azul

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


def desenhar_ponto(ponto: Tuple, cor, tamanho=10):
    glEnable(GL_POINT_SMOOTH)
    glPointSize(tamanho)
    glColor3d(*cor)
    glBegin(GL_POINTS)
    glVertex3d(*ponto)
    glEnd()


def desenhar_solido(solido, cor):
    vertices = solido.vertices_opengl
    faces = solido.faces_opengl

    glBegin(GL_QUADS)
    glColor3d(*cor)
    for i_surface, surface in enumerate(faces):
        i = 0
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


def criar_camera(somente_arestas=False, visao_ortogonal=False, terceira_pessoa=False):
    pg.init()
    display = (1200, 900)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    glClearColor(0.8, 0.8, 0.8, 1)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # Calculando at
    x, y, z = ponto_medio_solidos([PARALELEPIPEDO, TRONCO])
    at = (x, y, z)
    eye = (x, -12, z)  # ponto escolhido em outro quadrante

    camera = BaseCamera(eye, at)

    TRONCO.mudar_para_camera(camera)
    PARALELEPIPEDO.mudar_para_camera(camera)

    if visao_ortogonal:
        TRONCO.projecao_ortogonal(1)
        PARALELEPIPEDO.projecao_ortogonal(1)

    # novo sistema de coordenadas da camera
    u, v, n = camera.base

    if terceira_pessoa:
        # Posicionaando camera na terceira pessoa
        gluLookAt(-8, -8, 0, *at, *u)
    else:
        # Posicionaando camera na origem com novo sistema de coordenadas
        gluLookAt(*ORIGEM, *n, *u)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for solido, cor in zip([TRONCO, PARALELEPIPEDO], CORES):
            if not somente_arestas and not visao_ortogonal:
                desenhar_solido(solido, cor)
            desenhar_linhas_solido(solido, (0, 0, 0) if not visao_ortogonal and not somente_arestas else cor)

        if terceira_pessoa:
            desenhar_camera(camera)

        pg.display.flip()
        pg.time.wait(20)


if __name__ == "__main__":
    criar_camera()
