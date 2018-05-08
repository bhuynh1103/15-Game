import pygame, sys
from pygame.locals import *
from tile import *
from random import randint

pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize))

numbers = []
for num in range(boardSide ** 2):
    numbers.append(num)

grid = []
for i in range(boardSide):
    grid.append([])
    for j in range(boardSide):
        randnum = randint(0, len(numbers) - 1)
        grid[i].append(Tile(i, j, numbers[randnum]))
        del numbers[randnum]

clicked = False

while True:
    pygame.time.wait(1000 // 60)
    screen.fill(white)

    for i in range(boardSide):
        for j in range(boardSide):
            tile = grid[i][j]
            tile.draw(screen)

            mousePos = pygame.mouse.get_pos()

            if tile.clicked(mousePos, clicked): # and tile.movable(grid):
                print(tile.movable(grid))
                '''
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if abs(a) + abs(b) == 1:
                            x = tile.i + a
                            y = tile.j + b
                            if x > 0 and x < boardSide and y > 0 and y < boardSide:
                                grid[x][y] = grid[i][j]
                                grid[i][j] = Tile(i, j, 0)
                '''

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        mouseStates = pygame.mouse.get_pressed()

        if event.type == MOUSEBUTTONDOWN and mouseStates[0] == 1:
            clicked = True
        else:
            clicked = False
