import pygame
import draw
import color
import kugel
import tisch
import math

def reset():
    whiteBall = kugel.Ball(color.WHITE, False, "0", 0.75, 0.5)
    balls = t.buildTriangle(0.5, 0.5)

def mouseMove(o,b):


    if draw.mousePressed():
        stehen = 0
        for i in balls:
            if i.v == [0, 0]:
                stehen += 1
        if stehen == len(balls):
            tupel = list(draw.mousePosition())
            force = 0
            vabsx = (tupel[0] - o.x)
            vabsy = (tupel[1] - o.y)
            lengthv = math.sqrt(vabsx**2+vabsy**2)
            vabsxnorm = vabsx/lengthv
            vabsynorm = vabsy/lengthv
            pygame.event.get()
            while pygame.mouse.get_pressed() != (0,0,0):
                force += 0.00000001
                pygame.event.get()
                if force > 0.01:
                    break
            o.v[0] = -vabsxnorm * force
            o.v[1] = -vabsynorm * force


t = tisch.Table()
t.createTable()
colors = [color.BLACK, color.WHITE, color.RED, color.BLUE, color.YELLOW, color.PINK]
numbers = [str(i) for i in range(16)]
whiteBall = kugel.Ball(color.WHITE, False, "0", 0.75, 0.5)
balls = t.buildTriangle(0.5, 0.5)
heaven = 0.05
hell = 0.05
for b in balls:

    if b.marker == True:
        b.Pos = [heaven,0.9]
        heaven += 4*b.r
    else:
        b.Pos = [hell,0.1]
        hell += 4*b.r
draw.show(1)
while True:
    draw.clear()
    t.createTable()
    whiteBall.drawBall()
    whiteBall.nextPosition()
    t.reflection(whiteBall)
    mouseMove(whiteBall,balls)
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
    if draw.hasNextKeyTyped():
        whiteBall = kugel.Ball(color.WHITE, False, "0", 0.75, 0.5)
        balls = t.buildTriangle(0.5, 0.5)







    draw.show(0.25)







