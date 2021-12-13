import pygame
import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from universo_2 import CUBO, PARALELEPIPEDO, PIRAMIDE, TRONCO

glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

glEnable(GL_DEPTH_TEST)


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


def pontos_eixos():
    glEnable(GL_POINT_SMOOTH)
    glPointSize(10)

    glBegin(GL_POINTS)
    glColor3d(1, 1, 1)
    glVertex3d(10, 0, 0)
    glVertex3d(0, 10, 0)
    glVertex3d(0, 0, 10)
    glEnd()


def desenhar_solido(solido):
    vertices = solido.vertices_opengl
    faces = solido.faces_opengl

    glBegin(GL_QUADS)
    for i_surface, surface in enumerate(faces):
        i = 0
        # glNormal3fv(normals[i_surface])
        for vertex in surface:
            i += 1
            glColor3fv((0.8, 0.8, 0.8))
            glVertex3fv(vertices[vertex])
    glEnd()

    # glColor3fv(colors[0])


def main():
    pg.init()
    display = (1200, 900)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    glClearColor(0.8, 0.8, 0.8, 1)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)
    gluLookAt(10, -15, 15, 0, 0, 0, 0, 0, 1)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()


        # glRotatef(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for solido in [CUBO, PARALELEPIPEDO, PIRAMIDE, TRONCO]:
            desenhar_solido(solido)

        for eixo in [X, Y, Z]:
            desenhar_eixo(eixo)

        pontos_eixos()

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        pg.display.flip()
        pg.time.wait(20)


if __name__ == "__main__":
    main()
