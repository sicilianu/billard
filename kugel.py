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
        self.Pos = None

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
        f = (-0.0001)
        while abstand < (2*self.r)**2:
            self.x += f * self.v[0]
            self.y += f * self.v[1]
            o.x += f * o.v[0]
            o.y += f * o.v[1]
            abstand = ((self.x - o.x)**2 + (self.y - o.y)**2)
        if abstand < (2*self.r)**2 + 0.0001:
            self.v[0] = self.v[0] -dx * (v1d-v2d)/abstand
            self.v[1] = self.v[1] -dy* (v1d-v2d)/abstand
            o.v[0] = o.v[0] - dx * (v2d - v1d)/abstand
            o.v[1] = o.v[1] - dy * (v2d - v1d)/abstand






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















