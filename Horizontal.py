from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import math
windowSize = (1200, 700)

UserVelocity = float(
    input("Enter Horizontal Velocity of the Ball (-35 <= Vx <= 35) :- "))


def Plot(x, y, c):
    if c == "r":
        glColor3f(1.0, 0.0, 0.0)
    elif c == "p":
        glColor3f(1.0, 0.75, 0.8)
    else:
        pass
    glPointSize(3.0)
    glBegin(GL_POINTS)

    glVertex2f(x, y+3.2)
    glEnd()


def Ball(cx, cy, radius):
    glColor3f(0.0, 1.0, 1.0)
    glPointSize(3.0)
    angle = 1*math.pi/180
    theta = 0
    glBegin(GL_LINE_LOOP)
    while theta <= 2*math.pi:
        x = radius*math.cos(theta)
        y = radius*math.sin(theta)
        theta = theta+angle
        glVertex2f(cx+x, cy+y+3.2)
    glEnd()
    theta = 0
    angle = 30*math.pi/180
    while theta <= 2*math.pi:
        x = radius*math.cos(theta)
        y = radius*math.sin(theta)
        theta = theta + angle
        Line((cx, cy+3.2), (x+cx, y+cy+3.2), "y")


def Line(p1, p2, c):
    if c == "g":
        glColor3f(.0, 1.0, 0.0)
    elif c == "y":
        glColor3f(1, 1, 0)
    else:
        glColor3f(1.0, 1, 1.8)
    glPointSize(3.0)
    glBegin(GL_LINES)
    glVertex2f(p1[0], p1[1])
    glVertex2f(p2[0], p2[1])
    glEnd()


def Projectile():
    vx = UserVelocity
    p2 = (5, 5)
    p3 = (80, 5)

    if vx < 0:
        p1 = (80, 25)
        base = p3
    elif vx > 0:
        p1 = (5, 25)
        base = p2
    else:
        p1 = ((p2[0]+p3[0]/2), 25)
        base = ((p2[0]+p3[0]/2), 5)

    h = p2[1]-p1[1]
    h = abs(h)
    s = 0
    y = 0
    Ball(5, 25, 3)
    Container = []
    while y < h:
        glClear(GL_COLOR_BUFFER_BIT)
        Ball(p1[0], p1[1], 3)
        x = vx*s
        y = (1/2 * 9.8 * pow(s, 2))
        Container.append((x, y))
        for point in Container:
            Plot(p1[0]+point[0], p1[1]-point[1], "r")

        Line(p1, base, "g")
        Line(p2, p3, "g")
        Ball(x+p1[0], -y+p1[1], 3)
        glutSwapBuffers()
        time.sleep(0.01)
        s = s+0.01


def HorizontalProjectile():
    glClear(GL_COLOR_BUFFER_BIT)
    Projectile()
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(windowSize[0], windowSize[1])
    glutCreateWindow("Nirbhay Adhikari (02) Horizontal Projectile")
    gluOrtho2D(0.0, 84.375, 0, 50)
    glutDisplayFunc(HorizontalProjectile)
    glutMainLoop()


main()
