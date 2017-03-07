import pygame
import draw
import color
import kugel
import tisch


t = tisch.Table()
t.createTable()
colors = [color.BLACK, color.WHITE, color.RED, color.BLUE, color.YELLOW, color.PINK]
numbers = [str(i) for i in range(16)]
whiteBall = kugel.Ball(color.WHITE, False, "0", 0.75, 0.5)
draw.show(5)
balls = t.buildTriangle(0.5,0.5)
#balls = [kugel.Ball(color.BLACK, False, "3"),kugel.Ball(color.BLACK, False, "3",0.3,0.34),kugel.Ball(color.BLACK, False, "3",0.4,0.4),
         #kugel.Ball(color.BLACK, False, "3", 0.2, 0.2), kugel.Ball(color.BLACK, False, "3",0.35,0.35),
         #kugel.Ball(color.BLACK, False, "3", 0.45, 0.45)]
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
            if elem != other and other not in elem.collided:
                elem.collision(other)
                elem.collided.append(other)
                elem.export()
            elif other in elem.collided:
                elem.timer += 1
                if elem.timer == 4:
                    elem.collided.remove(other)
                    elem.timer = 0





    draw.show(1)







