import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices= (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
    (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)
)

edges = (
    (0,1), (0,3), (0,4), (2,1), (2,3), (2,7),
    (6,3), (6,4), (6,7), (5,1), (5,4), (5,7)
)

colors = (
    (1,0,0), (0,1,0), (0,0,1), (0,1,0), (1,1,1), (0,1,1),
    (1,0,0), (0,1,0), (0,0,1), (1,0,0), (1,1,1), (0,1,1),
)

surfaces = (
    (0,1,2,3), (3,2,7,6), (6,7,5,4),
    (4,5,1,0), (1,5,7,2), (4,0,3,6)
)

class Cube(object):
    def __init__(self, vertices, edges, surfaces, colors):
        # Set up cube properties
        self.vertices = vertices
        self.edges = edges
        self.surfaces = surfaces
        self.colors = colors

        # Initialize PyGame configuration
        pygame.init()
        pygame.display.set_caption("OpenGL Cube Render")

    def __generate_hollow(self):
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

    def __generate_colored(self):
        glBegin(GL_QUADS)
        for surface in surfaces:
            x = 0
            for vertex in surface:
                x+=1
                glColor3fv(colors[x])
                glVertex3fv(self.vertices[vertex])
        glEnd()

        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def draw(self, mode:int = 0):
        try:
            # Setup
            display = (800,600)
            pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
            gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
            glTranslatef(0.0,0.0, -5)

            # Loop to continuously maintain execution
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                glRotatef(1, 3, 1, 1)
                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

                if mode == 0:
                    self.__generate_hollow()
                elif mode == 1:
                    self.__generate_colored()
                else:
                    raise Exception("Invalid mode selected.")
                pygame.display.flip()
                pygame.time.wait(10)

        except Exception as e:
            print(f'Error during drawing: {e}')

    def motion_render(self):
        try:
            display = (800,600)
            pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

            gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

            glTranslatef(0,0, -10)

            glRotatef(25, 2, 1, 0)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            glTranslatef(-0.5,0,0)
                        if event.key == pygame.K_RIGHT:
                            glTranslatef(0.5,0,0)

                        if event.key == pygame.K_UP:
                            glTranslatef(0,1,0)
                        if event.key == pygame.K_DOWN:
                            glTranslatef(0,-1,0)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 4:
                            glTranslatef(0,0,1.0)

                        if event.button == 5:
                            glTranslatef(0,0,-1.0)

                #glRotatef(1, 3, 1, 1)
                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                self.__generate_hollow()
                pygame.display.flip()
                pygame.time.wait(10)

        except Exception as e:
            print(f'Error during render: {e}')


if __name__ == "__main__":
    cube = Cube(vertices=vertices, colors=colors, edges=edges, surfaces=surfaces)
    cube.draw(mode=0)
