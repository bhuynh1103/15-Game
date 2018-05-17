from pygame.font import Font

# Function for drawing text
def writeText(window, written, color, cenX, cenY, size):
    font = Font(None, int(size))
    text = font.render(written, 1, color)
    textpos = text.get_rect()
    textpos.centerx = cenX
    textpos.centery = cenY
    window.blit(text, textpos)
    return (textpos)


def flip(array):
    flip = []
    for a in range(len(array)):
        flip.append([])
        for b in range(len(array)):
            flip[a].append(array[b][a])

    return flip


# Creates all gray-scale colors with one argument
def gray(x):
    return x, x, x


red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (127, 0, 255)
pink = (255, 0, 255)
black = gray(0)
white = gray(255)

# Constants
screenSize = 800
boardSide = 4


# Creates a solved array that has solution of board
solved = []
num = 0
for i in range(boardSide):
    solved.append([])
    for j in range(boardSide):
        num += 1
        if num == boardSide ** 2:
            num = 0
        solved[i].append(num)
