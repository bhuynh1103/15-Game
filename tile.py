from pygame.draw import *
from constants import *


class Tile:
    def __init__(self, i, j, num):
        self.i = i
        self.j = j
        self.w = screenSize // boardSide
        self.x = j * self.w
        self.y = i * self.w + self.w
        self.num = num

    def writeNum(self, window):
        writeText(window, str(self.num), black, self.x + self.w * .5, self.y + self.w * .5, self.w * .9)

    def draw(self, window):
        if self.num != 0:
            rect(window, white, (self.x, self.y, self.w, self.w))
            rect(window, gray(200), (self.x, self.y, self.w, self.w), 1)
            self.writeNum(window)
        else:
            rect(window, gray(200), (self.x, self.y, self.w, self.w))

    def has(self, mousePos):
        mouseX = mousePos[0]
        mouseY = mousePos[1]
        return (mouseX > self.x and mouseX < self.x + self.w and
                mouseY > self.y and mouseY < self.y + self.w)

    def movable(self, grid):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if abs(i) + abs(j) == 1:
                    x = self.i + i
                    y = self.j + j
                    if x >= 0 and x < boardSide and y >= 0 and y < boardSide and grid[x][y].num == 0:
                        return True
        return False
