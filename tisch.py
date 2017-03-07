import pygame
import draw
import color
import kugel
import time

class Table():
    def __init__(self, edge=0.03):
        draw.setCanvasSize(600, 600)
        self.edge = edge
        self.limitsx = (0.05, 0.95)
        self.limitsy = (0.25, 0.7)

    def createTable(self):
        draw.setPenColor(color.GREEN)
        draw.filledRectangle(0.05, 0.25, 0.9, 0.45)
        draw.setPenColor(color.DARK_GRAY)
        # Draw the bumper of the billard table as a rectangle
        draw.filledRectangle(0.05 - self.edge, 0.25, self.edge, 0.45)
        draw.filledRectangle(0.05, 0.25 - self.edge, 0.9, self.edge)
        draw.filledRectangle(0.05, 0.7, 0.9, self.edge)
        draw.filledRectangle(0.95, 0.25, self.edge, 0.45)
        # Draw Holes on the bumper as polygons and rectangles.
        draw.setPenColor(color.BLACK)
        draw.setPenRadius()
        draw.filledRectangle(0.5 - (self.edge), 0.25 - self.edge, self.edge * 2, self.edge)
        draw.filledRectangle(0.5 - (self.edge), 0.25 + 0.45, self.edge * 2, self.edge)

        upperrightx = [0.95 - self.edge, 0.95, 0.95 + self.edge, 0.95 + self.edge, 0.95]
        upperrighty = [0.7, 0.7 - self.edge, 0.7, 0.7 + self.edge, 0.7 + self.edge]

        lowerrightx = [0.95 - self.edge, 0.95, 0.95 + self.edge, 0.95 + self.edge, 0.95]
        lowerrighty = [0.25, 0.25 + self.edge, 0.25, 0.25 - self.edge, 0.25 - self.edge]

        upperleftx = [0.05, 0.05 + self.edge, 0.05, 0.05 - self.edge, 0.05 - self.edge]
        upperlefty = [0.7 - self.edge, 0.7, 0.7 + self.edge, 0.7 + self.edge, 0.7]

        lowerleftx = [0.05, 0.05 + self.edge, 0.05, 0.05 - self.edge, 0.05 - self.edge]
        lowerlefty = [0.25 + self.edge, 0.25, 0.25 - self.edge, 0.25 - self.edge, 0.25]
        draw.filledPolygon(upperrightx, upperrighty)
        draw.filledPolygon(lowerrightx, lowerrighty)
        draw.filledPolygon(upperleftx, upperlefty)
        draw.filledPolygon(lowerleftx, lowerlefty)

    def reflection(self,o):
        string = ""
        limitsx = (0.05+o.r, 0.95-o.r)
        limitsy = (0.25+o.r, 0.7-o.r)
        if o.x <= limitsx[0]:
            string = "left"

        elif o.x >= limitsx[1]:
            string = "right"
        elif o.y <= limitsy[0]:
            string = "lower"
        elif o.y >= limitsy[1]:
            string = "upper"
        if string == "left" or string == "right":
            o.v = [o.v[0] * (-1), o.v[1]]
        elif string == "lower" or string == "upper":
            o.v = [o.v[0], o.v[1] * (-1)]

    def calcPos(self, i,x0,y0,f):
        if i == 1 or i == 6:
            return (x0 - f.r),(y0 - f.r/2)
        if i == 4 or i > 10 or i == 5:
            return x0, (y0 - f.r*2)
        if i == 2 or 7 <= i <= 9:
            return x0, (y0 + f.r*2)
        if i == 3 or i == 10:
            return (x0 - f.r), (y0 + f.r / 2)


    triangle = [1, 0, 1, 1, 8, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0]

    def buildTriangle(self,x0, y0):
        xprev = x0
        yprev = y0
        f = kugel.Ball(color.WHITE, xprev,yprev)
        tmp = [f]
        for i in range(1, len(triangle)-1):
            pos = calcPos(i,xprev,yprev)
            ball = kugel.Ball(color.WHITE, bool(triangle[i]), *pos)
            tmp.append(ball)
            xprev, yprev = pos

        return tmp

        return tmp

