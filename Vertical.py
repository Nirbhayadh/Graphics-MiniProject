from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import sin, cos, pi
import time
import math
windowSize = (1200, 700)

UserVelocity = float(
    input("Enter the Velocity of the Ball (0 <= Velocity <= 26.5) :- "))
UserAngle = float(
    input("Enter the Projectile Angle of the Ball (0 < Angle < 180) :- "))


def Plot(x, y, g):
    if g == 'p':

        glColor3f(1.0, 1.0, 1.0)
        glPointSize(3.0)
    else:
        glColor3f(1.0, 0.0, 0.0)
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
    angle = 2*15*math.pi/180
    while theta <= 2*math.pi:
        x = radius*math.cos(theta)
        y = radius*math.sin(theta)
        theta = theta + angle
        Line((cx, cy+3.2), (x+cx, y+cy+3.2), "y")


def Line(p1, p2, c="g"):
    if c == "w":
        glColor3f(1, 1, 1)
    elif c == "y":
        glColor3f(1.0, 1.0, 0.0)
    elif c == "g":
        glColor3f(0, 1, 0)
    glPointSize(3.0)
    glBegin(GL_LINES)
    glVertex2f(p1[0], p1[1])
    glVertex2f(p2[0], p2[1])

    glEnd()


def TriangleArrow(p1, theta):
    p2 = (p1[0]+1.5*cos(135*pi/180+theta), p1[1]+1.5*sin(135*pi/180+theta))
    p3 = (p1[0]+1.5*cos(-135*pi/180+theta), p1[1]+1.5*sin(-135*pi/180+theta))
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)

    glVertex2f(p1[0], p1[1])
    glVertex2f(p2[0], p2[1])
    glVertex2f(p3[0], p3[1])

    glEnd()


def Projectile():
    p1 = (5, 5)
    p2 = (80, 5)
    t = 10
    s = 0
    v = UserVelocity
    theta = UserAngle
    if theta < 90:
        base = p1
    elif theta > 90:
        base = p2
    else:
        base = ((p1[0]+p2[0])/2, 5)
    ox = base[0]
    oy = base[1]
    theta = theta*math.pi / 180
    y = 0
    Ball(base[0], base[1], 3)
    R = pow(v, 2)*sin(2*theta)/9.8
    x = 0
    t = 2*v*sin(theta)/9.8
    dirx = ox+25*cos(theta)
    diry = oy+25*sin(theta)
    p = (dirx, diry)
    Container = []

    while s <= t:
        glClear(GL_COLOR_BUFFER_BIT)
        Line(p1, p2, "g")
        Line((ox, oy+3), (dirx, diry), "w")
        TriangleArrow(p, theta)
        Ball(ox, oy, 3)
        x = v*cos(theta)*s
        y = -v*sin(theta)*s+(1/2 * 9.8 * pow(s, 2))

        Container.append((x, y))
        for point in Container:
            Plot(base[0]+point[0], base[1]-point[1], "g")

        Plot(x+ox, -y+oy, "g")
        Ball(x+ox, -y+oy, 3)
        glutSwapBuffers()
        time.sleep(0.01)
        s = s+0.01


def VerticleProjectile():
    glClear(GL_COLOR_BUFFER_BIT)
    Projectile()
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(windowSize[0], windowSize[1])
    glutCreateWindow("Nirbhay Adhikari (02) Verticle Projectile")
    gluOrtho2D(0.0, 84.375, 0, 50)
    glutDisplayFunc(VerticleProjectile)
    glutMainLoop()


main()
