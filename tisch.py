import pygame
import draw
import color
import kugel
import time
import math


class Table():

    def __init__(self, edge=0.03):
        draw.setCanvasSize(600, 600)
        self.edge = edge
        self.limitsx = (0.05, 0.95)
        self.limitsy = (0.25, 0.7)
        self.corners = {"Upperleft": (0.05, 0.95), "Lowerleft": (
            0.05, 0.25), "Upperright": (0.95, 0.7), "Lowerright": (0.95, 0.25)}

    def createTable(self):
        """Draw all the entities on the table."""
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
        draw.filledRectangle(0.5 - (self.edge), 0.25 -
                             self.edge, self.edge * 2, self.edge)
        draw.filledRectangle(0.5 - (self.edge), 0.25 +
                             0.45, self.edge * 2, self.edge)
        # Define lists of coordinates to make drawing the corner holes
        # easier.
        self.upperrightx = [0.95 - self.edge, 0.95,
                            0.95 + self.edge, 0.95 + self.edge, 0.95]
        self.upperrighty = [0.7, 0.7 - self.edge,
                            0.7, 0.7 + self.edge, 0.7 + self.edge]

        self.lowerrightx = [0.95 - self.edge, 0.95,
                            0.95 + self.edge, 0.95 + self.edge, 0.95]
        self.lowerrighty = [0.25, 0.25 + self.edge,
                            0.25, 0.25 - self.edge, 0.25 - self.edge]

        self.upperleftx = [0.05, 0.05 + self.edge,
                           0.05, 0.05 - self.edge, 0.05 - self.edge]
        self.upperlefty = [0.7 - self.edge, 0.7,
                           0.7 + self.edge, 0.7 + self.edge, 0.7]

        self.lowerleftx = [0.05, 0.05 + self.edge,
                           0.05, 0.05 - self.edge, 0.05 - self.edge]
        self.lowerlefty = [0.25 + self.edge, 0.25,
                           0.25 - self.edge, 0.25 - self.edge, 0.25]
        draw.filledPolygon(self.upperrightx, self.upperrighty)
        draw.filledPolygon(self.lowerrightx, self.lowerrighty)
        draw.filledPolygon(self.upperleftx, self.upperlefty)
        draw.filledPolygon(self.lowerleftx, self.lowerlefty)

    def reflection(self, o):
        """Make the bumpers reflect any balls hitting them by
        inverting their velocity vector whenever a ball reaches the
        limits.


        Parts of the bumpers in the middle of the upper and lower
        bumper are excluded to allow using them as holes."""
        string = ""
        limitsx = (0.05 + o.r, 0.95 - o.r)
        limitsy = (0.25 + o.r, 0.7 - o.r)

        if o.x <= limitsx[0]:
            string = "left"
        if o.x >= limitsx[1]:
            string = "right"
        if o.y <= limitsy[0] and o.x < 0.52 - self.edge:
            string = "lower"
        if o.y <= limitsy[0] and o.x > 0.48 + self.edge:
            string = "lower"
        if o.y >= limitsy[1] and o.x > 0.52 + self.edge:
            string = "upper"
        if o.y >= limitsy[1] and o.x < 0.48 - self.edge:
            string = "upper"
        if string == "left" or string == "right":
            o.v = [o.v[0] * (-1), o.v[1]]
        if string == "lower" or string == "upper":
            o.v = [o.v[0], o.v[1] * (-1)]

    def triangleCoords(self, x0, y0, n=6):
        """Returns an array of the proper coordinate pairs for the initial
        position of the balls on the board."""
        tmp = []
        x = x0
        y = y0
        yup = y0
        ydown = y0
        diagonal = math.sqrt((kugel.radius * 2)**2 + kugel.radius**2) / 2

        for i in range(n):
            for j in range(i):
                if j == 0:
                    y = y0 + i * diagonal
                    x -= 2 * kugel.radius
                else:
                    y -= 2 * kugel.radius
                tmp.append((x, y))
        return tmp

    def buildTriangle(self, x0, y0, n=6):
        """Initiates the balls required to play the game.


        Associate colors with numbers and boolean values to
        identify balls and initiates balls with these values and the
        proper initial positions. Returns a list of ball objects. This
        list is the one that is supposed to bo used throughout the game."""
        numcol = [(color.YELLOW, "1"), (color.BLUE, "2"), (color.RED, "3"),
                  (color.PINK, "4"),  (color.BLACK, "8"), (color.DARK_GREEN, "6"),
                  (color.BROWN, "7"), (color.ORANGE, "5"), (color.YELLOW, "9"),
                  (color.BLUE, "10"), (color.RED, "11"), (color.PINK, "12"),
                  (color.ORANGE, "13"), (color.DARK_GREEN, "14"),
                  (color.BROWN, "15")]
        triangle = [1, 1, 0, 1, 8, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0]
        tmp = []

        coords = self.triangleCoords(0.5, 0.5)
        for i, pair in enumerate(numcol):
            x, y = coords[i]
            ball = kugel.Ball(pair[0], triangle[i], pair[1], x, y)
            tmp.append(ball)
        return tmp

    def ballInHole(self, b):
        """Check whether a ball rolls into a hole. Returns true if it
        has, False otherwise.


        The corner holes are checked using the coordinates of the
        corners of the table, the side-holes are checked using their
        property of being actual holes.
        """
        hit = False
        for k, v in self.corners.items():
            distsquare = ((b.x - v[0])**2 + (b.y - v[1])**2)
            if distsquare <= (b.r * 2)**2:
                hit = True
        if b.y < 0.25 and b.y > 0.1:
            hit = True
        if b.y > 0.7 and b.y < 0.8:
            hit = True

        return hit

    def Holes(self, o):
        """Remove a ball from the table if it has hit a hole."""
        if self.ballInHole(o):
            self.killBall(o)

    def killBall(self, o):
        """Remove a ball from the table."""
        o.v = [0, 0]
        if o.number == "0":
            o.x = 0.75
            o.y = 0.5
        else:
            o.x = o.Pos[0]
            o.y = o.Pos[1]
