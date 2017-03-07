import pygame
import draw
import color
import kugel
import tisch


t = tisch.Table()
t.createTable()
colors = [color.BLACK, color.WHITE, color.RED, color.BLUE, color.YELLOW, color.PINK]
numbers = [str(i) for i in range(16)]
a = kugel.Ball(color.WHITE,False,"0")
b = kugel.Ball(color.BLUE,True,"3",0.75,0.5)
draw.show(5)
t.buildTriangle(0.5,0.5)

while True:
    t.createTable()
    a.mouseMove()
    b.mouseMove()
    t.reflection(a)
    t.reflection(b)
    a.collision(b)
    a.nextPosition()
    b.nextPosition()
    a.drawBall()
    b.drawBall()
    draw.show(5)







