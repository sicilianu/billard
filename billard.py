import pygame
import draw
import color
import kugel
import tisch
import math

def reset():
    whiteBall = kugel.Ball(color.WHITE, False, "0", 0.75, 0.5)
    balls = t.buildTriangle(0.5, 0.5)


def quiet(balls,whiteBall):
    """Returns true if the balls dont move now."""
    stehen = 0
    for i in balls:
        if i.v == [0, 0]:
            stehen += 1
    if whiteBall.v == [0,0]:
        stehen += 1
    return stehen == len(balls) +1





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


def lap(player,other):
    """Play one round player vs. other.

    - Text is written on the screen to indicate which player's turn it is
    - The functions responsible for mouse interaction and movement of objects are called
    - At the end of the loop that implements movement/collision of all balls, another loop checks whether
      there are still balls moving. If this is not the case, the state of the player variable hashit is checked
    - If player has not hit any balls, it is the other player's turn
    - [Not implemented]If player has hit the white ball, after movement the white ball's position is reset and it is the other player's turn."""
    if player.isPlaying:
        player.talk()
        whiteBall.nextPosition()
        t.reflection(whiteBall)
        mouseMove(whiteBall, balls)
        t.Holes(whiteBall)

        if whiteBall.v != [0, 0]:
            player.hashit = True
        if quiet(balls,whiteBall) and player.hashit:
            print("hier")
            q.setPosition()
            q.drawQueue()
            player.isPlaying = False
            other.isPlaying = True

            if whiteBall.dead:
                t.reviveWhite(whiteBall)
                whiteBall.dead = False



        for elem in balls:
            elem.nextPosition()
            elem.drawBall()
            t.reflection(elem)
            elem.collision(whiteBall)
            player.hashit = t.Holes(elem)
            for other in balls:
                if elem != other:
                    elem.collision(other)

movingBefore = False
t = tisch.Table()
t.createTable()
whiteBall = kugel.Ball(color.WHITE, False, "0", 0.75, 0.5)
balls = t.buildTriangle(0.5, 0.5)
player1 = tisch.Player("Aaron")
player2 = tisch.Player("Andrea")
q = t.queue(whiteBall)
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
player1.isPlaying=True
while True:
    draw.clear()
    t.createTable()
    whiteBall.drawBall()
    ##############################
    lap(player1,player2)
    lap(player2,player1)










    ##############################
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








    draw.show(0.25)







