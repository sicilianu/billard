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
        abstand = math.sqrt((self.x - o.x)**2 + (self.y - o.y)**2)
        if abstand <= 2*self.r:
            self.v, o.v = o.v, self.v





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
            self.v[0] = (tupel[0] - self.x) * 0.01
            self.v[1] = (tupel[1] - self.y) * 0.01








