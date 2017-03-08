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
        # Draw upper and lower middle holes
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

        if o.x <= limitsx[0] :
            string = "left"
        if o.x >= limitsx[1] :
            string = "right"
        if o.y <= limitsy[0] and o.x < 0.52-self.edge:
            string = "lower"
        if o.y <= limitsy[0] and o.x > 0.48+self.edge:
            string = "lower"
        if o.y >= limitsy[1] and o.x > 0.52+self.edge:
            string = "upper"
        if o.y >= limitsy[1] and o.x < 0.48-self.edge:
            string = "upper"
        if string == "left" or string == "right":
            o.v = [o.v[0] * (-1), o.v[1]]
        if string == "lower" or string == "upper":
            o.v = [o.v[0], o.v[1] * (-1)]

    def triangleCoords(self,x0,y0,r, n = 6):#
        tmp = []
        for i in range(n,step=-1):
            tmp2 = []
            for j in range(i):
                tmp2.append(j)
            tmp.append(tmp2)
        







    def buildTriangle(self,x0, y0):
        numcol = { "1": (color.YELLOW, "1"), "2": (color.BLUE, "2"), "3": (color.RED, "3"), "4": (color.PINK, "4"), "5": (color.BLACK, "8"),
                  "6": (color.DARK_GREEN, "6"), "7": (color.BROWN, "7"), "8": (color.ORANGE, "5"), "9": (color.YELLOW, "9"), "10": (color.BLUE, "10"),
                  "11": (color.RED, "11"), "12": (color.PINK, "12"), "13": (color.ORANGE, "13"), "14": (color.DARK_GREEN, "14"), "15": (color.BROWN, "15")}
        triangle = [1, 1, 0, 1, 8, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0]
        xprev = x0
        yprev = y0

        tmp = []
        for i in range(1, len(triangle)+1):
            ball = kugel.Ball(numcol[str(i)][0], bool(triangle[i-1]),numcol[str(i)][1], xprev,yprev)
            #pos = self.calcPos(xprev, yprev, ball.r)
            pos = (xprev-ball.r, yprev-ball.r)
            tmp.append(ball)
            xprev, yprev = pos

        return tmp

    def ballInCorner(self,b):
        hit = False
        for k,v in self.corners.items():
            distsquare = ((b.x-v[0])**2 + (b.y-v[1])**2)
            if distsquare <= (b.r*2)**2:
                hit = True

        if b.y < 0.25 and b.y > 0.1:
            hit = True
        if b.y > 0.7 and b.y < 0.8:
            hit = True

        return hit
    def Holes(self,o):
        if self.ballInCorner(o):
            self.killBall(o)

    def killBall(self,o):
        o.v = [0, 0]
        if o.number == "0":
            o.x = 0.75
            o.y = 0.5
        else:
            o.x = o.Pos[0]
            o.y = o.Pos[1]







