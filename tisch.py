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
        self.corners = {"Upperleft": (0.05,0.95), "Lowerleft": (0.05,0.25), "Upperright": (0.95,0.7), "Lowerright": (0.95,0.25)}
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

        self.upperrightx = [0.95 - self.edge, 0.95, 0.95 + self.edge, 0.95 + self.edge, 0.95]
        self.upperrighty = [0.7, 0.7 - self.edge, 0.7, 0.7 + self.edge, 0.7 + self.edge]

        self.lowerrightx = [0.95 - self.edge, 0.95, 0.95 + self.edge, 0.95 + self.edge, 0.95]
        self.lowerrighty = [0.25, 0.25 + self.edge, 0.25, 0.25 - self.edge, 0.25 - self.edge]

        self.upperleftx = [0.05, 0.05 + self.edge, 0.05, 0.05 - self.edge, 0.05 - self.edge]
        self.upperlefty = [0.7 - self.edge, 0.7, 0.7 + self.edge, 0.7 + self.edge, 0.7]

        self.lowerleftx = [0.05, 0.05 + self.edge, 0.05, 0.05 - self.edge, 0.05 - self.edge]
        self.lowerlefty = [0.25 + self.edge, 0.25, 0.25 - self.edge, 0.25 - self.edge, 0.25]
        draw.filledPolygon(self.upperrightx, self.upperrighty)
        draw.filledPolygon(self.lowerrightx, self.lowerrighty)
        draw.filledPolygon(self.upperleftx, self.upperlefty)
        draw.filledPolygon(self.lowerleftx, self.lowerlefty)

    def reflection(self,o):
        string = ""
        limitsx = (0.05+o.r, 0.95-o.r)
        limitsy = (0.25+o.r, 0.7-o.r)
        if o.x <= limitsx[0]:
            string = "left"

        if o.x >= limitsx[1]:
            string = "right"
        if o.y <= limitsy[0]:
            string = "lower"
        if o.y >= limitsy[1]:
            string = "upper"
        if string == "left" or string == "right":
            o.v = [o.v[0] * (-1), o.v[1]]
        if string == "lower" or string == "upper":
            o.v = [o.v[0], o.v[1] * (-1)]

    def calcPos(self, i,x0,y0,r):
        if i == 1 or i == 6:
            return (x0 - r*2),(y0 - r)
        if i == 4 or i > 10 or i == 5:
            return x0, (y0 - r*2) - 0.005
        if i == 2 or 7 <= i <= 9:
            return x0, (y0 + r*2) + 0.005
        if i == 3 or i == 10:
            return (x0 - r*2), (y0 + r)




    def buildTriangle(self,x0, y0):
        numcol = { "1": color.YELLOW, "2": color.BLUE, "3": color.RED, "4": color.PINK, "5": color.ORANGE,
                  "6": color.DARK_GREEN, "7": color.BROWN, "8": color.BLACK, "9": color.YELLOW, "10": color.BLUE,
                  "11": color.RED, "12": color.PINK, "13": color.ORANGE, "14": color.DARK_GREEN, "15": color.BROWN}
        triangle = [1, 1, 0, 1, 8, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
        xprev = x0
        yprev = y0


        tmp = []
        for i in range(1, len(triangle)+1):

            ball = kugel.Ball(numcol[str(i)], bool(triangle[i-1]),str(i), xprev,yprev)
            pos = self.calcPos(i, xprev, yprev, ball.r)
            tmp.append(ball)
            xprev, yprev = pos

        return tmp

    def ballInCorner(self,b):
        hit = False
        for k,v in self.corners.items():
            distsquare = ((b.x-v[0])**2 + (b.y-v[1])**2)
            if distsquare <= (b.r*2)**2:
                hit = True

        return hit
    def Holes(self,o):
        if self.ballInCorner(o):
            o.kill()





