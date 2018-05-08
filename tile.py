import pygame
from constants import *

class Tile:
    def __init__(self, i, j, num):
        self.i = i
        self.j = j
        self.x = i * (screenSize // boardSide)
        self.y = j * (screenSize // boardSide)
        self.w = screenSize // boardSide
        self.num = num

    def draw(self, window):
        if self.num != 0:
            pygame.draw.rect(window, white, (self.x, self.y, self.w, self.w))
            pygame.draw.rect(window, gray(100), (self.x, self.y, self.w, self.w), 2)
            self.writeNum(window)
        else:
            pygame.draw.rect(window, gray(100), (self.x, self.y, self.w, self.w))

    def writeNum(self, window):
        font = pygame.font.Font(None, int((screenSize // boardSide) * .9))
        text = font.render(str(self.num), 1, black)
        textpos = text.get_rect()
        textpos.centerx = self.x + self.w * .5
        textpos.centery = self.y + self.w * .5
        window.blit(text, textpos)
        return (textpos)

    def clicked(self, mousePos, clicked):
        mouseX = mousePos[0]
        mouseY = mousePos[1]
        return ((mouseX > self.x and mouseX < self.x + self.w and
        mouseY > self.y and mouseY < self.y + self.w) and clicked)

    def movable(self, grid):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if abs(i) + abs(j) == 1:
                    a = self.i + i
                    b = self.j + j
                    print(a, b)
                    '''
                    if a > 0 and a < boardSide and b > 0 and b < boardSide:
                        if grid[a][b].num == 0:
                            return True

        return False'''
