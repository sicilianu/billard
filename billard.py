import pygame
import draw
import color
import kugel
import tisch
import math


def reset():
    whiteBall = kugel.Ball(color.WHITE, False, "0", 0.75, 0.5)
    balls = t.buildTriangle(0.5, 0.5)


def mouseMove(o):
    if draw.mousePressed():
        tupel = list(draw.mousePosition())
        force = 0
        vabsx = (tupel[0] - o.x)
        vabsy = (tupel[1] - o.y)
        lengthv = math.sqrt(vabsx**2 + vabsy**2)
        vabsxnorm = vabsx / lengthv
        vabsynorm = vabsy / lengthv
        pygame.event.get()
        while pygame.mouse.get_pressed() != (0, 0, 0):
            force += 0.0000001
            pygame.event.get()
        o.v[0] = -vabsxnorm * force
        o.v[1] = -vabsynorm * force


t = tisch.Table()
t.createTable()
whiteBall = kugel.Ball(color.WHITE, False, "0", 0.75, 0.5)
balls = t.buildTriangle(0.5, 0.5)
heaven = 0.05
hell = 0.05
for b in balls:
    if b.marker:
        b.Pos = [heaven, 0.9]
        heaven += 4 * b.r
    else:
        b.Pos = [hell, 0.1]
        hell += 4 * b.r
draw.show(1)
while True:
    draw.clear()
    t.createTable()
    whiteBall.drawBall()
    whiteBall.nextPosition()
    t.reflection(whiteBall)
    mouseMove(whiteBall)
    t.Holes(whiteBall)
    for elem in balls:
        elem.nextPosition()
        elem.drawBall()
        t.reflection(elem)
        elem.collision(whiteBall)
        t.Holes(elem)
        for other in balls:
            if elem != other:
                elem.collision(other)
    # if draw.hasNextKeyTyped():
    #     whiteBall = kugel.Ball(color.WHITE, False, "0", 0.75, 0.5)
    #     balls = t.buildTriangle(0.5, 0.5)
    draw.show(1)
