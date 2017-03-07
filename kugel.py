import draw
import color
import pygame
import math
import tisch

class Ball():
    def __init__(self, color, marker, number, x=0.25, y=0.5):
        self.x = x
        self.y = y
        self.v = [0, 0]
        self.r = 0.02
        self.friction = 0.998
        self.color = color
        self.marker = marker
        self.number = number
        self.drawBall()
        self.collided = []
        self.timer = 0
        self.l = []
    def drawBall(self):
        draw.setPenColor(self.color)
        draw.filledCircle(self.x, self.y, self.r)
        if self.marker:
            draw.setPenColor(color.BLACK)
            draw.filledCircle(self.x, self.y, self.r/2)
        if self.number != 0:
            draw.setPenColor(color.WHITE)
            draw.text(self.x, self.y, self.number)

    def collision(self,o):
        dx = o.x-self.x
        dy = o.y-self.y
        abstand = dx**2+dy**2
        v1d = self.v[0]*dx + self.v[1]*dy
        v2d = o.v[0]*dx + o.v[1]*dy
        if abstand < (2*self.r)**2:
            self.v[0] = self.v[0] -dx * (v1d-v2d)/abstand
            self.v[1] = self.v[1] -dy* (v1d-v2d)/abstand
            o.v[0] = o.v[0] - dx * (v2d - v1d)/abstand
            o.v[1] = o.v[1] - dy * (v2d - v1d)/abstand


        self.l.append(abstand)


    def export(self):
        with open("./data.csv", "w") as f:
            for elem in self.l:
                f.write(str(elem)+"\n")







    def nextPosition(self):
        x = self.x + self.v[0]
        y = self.y + self.v[1]
        self.x = x
        self.y = y
        self._friction()

    def _friction(self):

        if math.sqrt(self.v[0]**2+ self.v[1]**2) > 0.0001:
            self.v[0] *= self.friction
            self.v[1] *= self.friction
        else:
            self.v[0] = 0
            self.v[1] = 0
    def mouseMove(self):
        if draw.mousePressed():
            tupel = list(draw.mousePosition())
            self.v[0] = (tupel[0] - self.x) * 0.015
            self.v[1] = (tupel[1] - self.y) * 0.015








