import pygame
import draw
import color
import kugel
import tisch
import math

def reset():
    whiteBall = kugel.Ball(color.WHITE, False, "0", 0.75, 0.5)
    balls = t.buildTriangle(0.5, 0.5)


t = tisch.Table()
t.createTable()
colors = [color.BLACK, color.WHITE, color.RED, color.BLUE, color.YELLOW, color.PINK]
numbers = [str(i) for i in range(16)]
whiteBall = kugel.Ball(color.WHITE, False, "0", 0.75, 0.5)
balls = t.buildTriangle(0.5, 0.5)
draw.show(1)
while True:
    draw.clear()
    t.createTable()
    whiteBall.drawBall()
    whiteBall.nextPosition()
    t.reflection(whiteBall)
    whiteBall.mouseMove()
    for elem in balls:
        elem.nextPosition()
        elem.drawBall()
        t.reflection(elem)
        elem.collision(whiteBall)
        for other in balls:
            if elem != other:
                elem.collision(other)
    if draw.hasNextKeyTyped():
        whiteBall = kugel.Ball(color.WHITE, False, "0", 0.75, 0.5)
        balls = t.buildTriangle(0.5, 0.5)







    draw.show(1)







