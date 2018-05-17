from pygame.draw import *
from constants import *


class Tile:
    def __init__(self, i, j):
        # Tile's index in grid array
        self.i = i
        self.j = j
        # Draw specifications
        self.w = screenSize // boardSide
        self.x = j * self.w
        self.y = i * self.w + self.w
        # Tile's number
        self.num = None

    def setNum(self, current):
        self.num = current[self.i][self.j]

    # Draws number in tile
    def writeNum(self, window):
        writeText(window, str(self.num), black, self.x + self.w * .5, self.y + self.w * .5, self.w * .9)

    # Draws tile according to its number
    def draw(self, window):
        if self.num != 0:
            rect(window, white, (self.x, self.y, self.w, self.w))
            rect(window, gray(200), (self.x, self.y, self.w, self.w), 1)
            self.writeNum(window)
        else:
            rect(window, gray(200), (self.x, self.y, self.w, self.w))

    # Method for checking if mouse is above tile
    def has(self, mousePos):
        mouseX = mousePos[0]
        mouseY = mousePos[1]
        return (mouseX > self.x and mouseX < self.x + self.w and
                mouseY > self.y and mouseY < self.y + self.w)

    # Checks if the tile with the moouse above it is able to be moved
    def movable(self, current):
        if 0 in current[self.i]:
            return True
        else:
            for x in range(len(current)):
                if current[x][self.j] == 0:
                    return True

        return False
