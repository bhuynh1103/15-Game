import pygame, sys
from pygame.locals import *
from constants import *
from tile import *
from random import randint

pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize + screenSize // boardSide))

while True:
    # Setup functions
    
    # Generates grid array with Tiles
    grid = []
    num = 0
    for i in range(boardSide):
        grid.append([])
        for j in range(boardSide):
            num += 1
            if num == boardSide ** 2:
                num = 0
            grid[i].append(Tile(i, j, num))


    # Scrambles board
    count = 0    # \/ this number (the 50) MUST be even! Odd number will reseult in parity
    while count != 50:
        i = randint(0, boardSide - 1)
        j = randint(0, boardSide - 1)
        if grid[i][j].num != 0:
            store = grid[i][j].num
            a = randint(0, boardSide - 1)
            b = randint(0, boardSide - 1)
            if i != a and j != b and grid[a][b].num != 0:
                grid[i][j].num = grid[a][b].num
                grid[a][b].num = store
                count += 1


    # Creates a solved array that has solution of board
    solved = []
    for i in range(boardSide):
        solved.append([])
        for j in range(boardSide):
            num += 1
            if num == boardSide ** 2:
                num = 0
            solved[i].append(num)

    # Game control variables
    clicked = False
    gameover = False
    moves = 0

    setup = True

    while setup:
        # Game loop
        while not gameover:
            screen.fill(gray(200))

            for i in range(boardSide):
                for j in range(boardSide):
                    tile = grid[i][j]

                    tile.draw(screen)

                    mousePos = pygame.mouse.get_pos()
                    if tile.has(mousePos) and clicked and tile.movable(grid):
                        tile.swap(grid)
                        moves += 1

            writeText(screen, "Moves: " + str(moves), black, screenSize // 2, (screenSize // boardSide) * .5, screenSize // boardSide * .75)

            #  'current' array holds current number positions
            current = []
            for i in range(boardSide):
                current.append([])
                for j in range(boardSide):
                    current[i].append(grid[i][j].num)

            # Win condition
            if current == solved:
                gameover = True

            pygame.display.update()

            # Program end loop and input loop
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                mouseStates = pygame.mouse.get_pressed()

                if event.type == MOUSEBUTTONDOWN and mouseStates[0] == 1:
                    clicked = True
                else:
                    clicked = False

        # gameover loop

        screen.fill(gray(200))

        # Draws tiles
        for i in range(boardSide):
            for j in range(boardSide):
                grid[i][j].draw(screen)

        writeText(screen, "Moves: " + str(moves), black, screenSize // 2, screenSize // boardSide * .33, screenSize // boardSide * .25)
        writeText(screen, "You won! Press 'ENTER' to play again!", black, screenSize // 2, (screenSize // boardSide) * .66, screenSize // boardSide * .25)

        pygame.display.update()

        # end program and input loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_RETURN:
                setup = False
