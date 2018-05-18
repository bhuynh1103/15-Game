import pygame, sys
from pygame.locals import *
from constants import *
from tile import *
from random import randint

pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize + screenSize // boardSide))
pygame.display.set_caption("15 Game")

while True:
    # Setup functions

    # Generates grid array with Tiles
    grid = []
    num = 0
    for i in range(boardSide):
        grid.append([])
        for j in range(boardSide):
            # num += 1
            # if num == boardSide ** 2:
            #     num = 0
            grid[i].append(Tile(i, j))

    current = []
    num = 0
    for i in range(boardSide):
        current.append([])
        for j in range(boardSide):
            num += 1
            if num == boardSide ** 2:
                num = 0
            current[i].append(num)

    # Scrambles board
    if (boardSide ** 2) % 2 != 0:
        scramble = (boardSide ** 2) - 1
    else:
        scramble = (boardSide ** 2)
        
    count = 0
        
    while count != scramble:
        i = randint(0, boardSide - 1)
        j = randint(0, boardSide - 1)
        if current[i][j] != 0:
            store = current[i][j]
            a = randint(0, boardSide - 1)
            b = randint(0, boardSide - 1)
            if i != a and j != b and current[a][b] != 0:
                current[i][j] = current[a][b]
                current[a][b] = store
                count += 1


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

                    tile.setNum(current)
                    tile.draw(screen)

                    # Checks if tile is clicked and can be moved, if so, then moves tiles
                    mousePos = pygame.mouse.get_pos()
                    if tile.has(mousePos) and clicked and tile.movable(current):
                        # Shifts tiles
                        if 0 in current[i]:
                            current[i].remove(0)
                            current[i].insert(tile.j ,0)
                        else:
                            current = flip(current)
                            current[j].remove(0)
                            current[j].insert(tile.i ,0)
                            current = flip(current)

                        # Adds one to the move count for each shift made
                        if tile.num != 0:
                            moves += 1

            writeText(screen, "Moves: " + str(moves), black, screenSize // 2, (screenSize // boardSide) * .5, screenSize // boardSide * .75)


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
                grid[i][j].setNum(current)
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
