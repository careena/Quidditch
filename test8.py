# OOP and OOAD Assessment
# Karina Sudnicina
# 17.12.2020
# Quidditch v 8.0

from field import Field
from seeker import Seeker
from snitch import Snitch

# import the Pygame
import random, sys, copy, os, pygame
from pygame.locals import *

# create objects
field = Field()
s1 = Seeker('1', 4, 1)
s2 = Seeker('2', 5, 3)
sn = Snitch('@', 3, 2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FPS = 30                    # frames per second to update the screen
WINWIDTH = 800              # width and height of the program's window
WINHEIGHT = 600
HALF_WINWIDTH = int(WINWIDTH / 2)    # place things centrally
HALF_WINHEIGHT = int(WINHEIGHT / 2)

# The total width and height of each tile in pixels.
TILEWIDTH = 32
TILEHEIGHT = 32
TILEFLOORHEIGHT = 32

MEDIUMORCHID = (186,85,211)
DARKORCHID = (153,50,204)
WHITE = (255, 255, 255)
PLUM = (221,160,221)
BGCOLOR = MEDIUMORCHID
BGCOLOR1 = DARKORCHID
TEXTCOLOR = WHITE

# A dictionary of the images used.

IMAGESDICT = {'floor': pygame.image.load("Images/floor.png"),
              'wall': pygame.image.load("Images/wall.png"),
              'snitch': pygame.image.load("Images/snitch.png"),
              'seeker1': pygame.image.load("Images/seeker.png"),
              'seeker2': pygame.image.load("Images/seeker2.png")}

TILEMAPPING = { '#':IMAGESDICT['wall'],
                ' ':IMAGESDICT['floor'],
                '@':IMAGESDICT['snitch'],
                '1':IMAGESDICT['seeker1'],
                '2':IMAGESDICT['seeker2']}

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('Quidditch v 8.00')
font = pygame.font.Font('freesansbold.ttf', 18)
largeFont = pygame.font.Font('freesansbold.ttf', 30)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# functions to move 1st seeker
def moveSeek1Left():
    scoreIncrease = 0
    # Check if there is no wall
    if field.canMove(s1.row, s1.moveLeft()):
        # Clear the symbol
        field.clearAtPos(s1.row, s1.column)
        # Set column to a new column
        s1.column = s1.moveLeft()
        # Place seeker at a new position and check for the snitch
        if field.getCharAtPos(s1.row, s1.column) == '@':
            field.catchSnitch()
            field.placeSeeker1(s1.seek_char, s1.row, s1.column)
            scoreIncrease += 150
        else:
            # Place seeker at a new position
            field.placeSeeker1(s1.seek_char, s1.row, s1.column)
            print(field.toString())
    return scoreIncrease

def moveSeek1Right():
    scoreIncrease = 0
    if field.canMove(s1.row, s1.moveRight()):
        field.clearAtPos(s1.row, s1.column)
        s1.column = s1.moveRight()
        if field.getCharAtPos(s1.row, s1.column) == '@':
            field.catchSnitch()
            field.placeSeeker1(s1.seek_char, s1.row, s1.column)
            print(field.toString())
            scoreIncrease += 150
        else:
            field.placeSeeker1(s1.seek_char, s1.row, s1.column)
            print(field.toString())
    return scoreIncrease

def moveSeek1Up():
    scoreIncrease = 0
    if field.canMove(s1.moveUp(), s1.column):
        field.clearAtPos(s1.row, s1.column)
        s1.row = s1.moveUp()
        if field.getCharAtPos(s1.row, s1.column) == '@':
            field.catchSnitch()
            field.placeSeeker1(s1.seek_char, s1.row, s1.column)
            scoreIncrease += 150
        else:
            field.placeSeeker1(s1.seek_char, s1.row, s1.column)
            print(field.toString())
    return scoreIncrease

def moveSeek1Down():
    scoreIncrease = 0
    if field.canMove(s1.moveDown(), s1.column):
        field.clearAtPos(s1.row, s1.column)
        s1.row = s1.moveDown()
        if field.getCharAtPos(s1.row, s1.column) == '@':
            field.catchSnitch()
            field.placeSeeker1(s1.seek_char, s1.row, s1.column)
            scoreIncrease += 150
        else:
            field.placeSeeker1(s1.seek_char, s1.row, s1.column)
            print(field.toString())
    return scoreIncrease

# functions to move 2nd seeker
def moveSeek2Left():
    scoreIncrease = 0
    if field.canMove(s2.row, s2.moveLeft()):
        field.clearAtPos(s2.row, s2.column)
        s2.column = s2.moveLeft()
        if field.getCharAtPos(s2.row, s2.column) == '@':
            field.catchSnitch()
            field.placeSeeker2(s2.seek_char, s2.row, s2.column)
            scoreIncrease += 150
        else:
            field.placeSeeker1(s2.seek_char, s2.row, s2.column)
            print(field.toString())
    return scoreIncrease

def moveSeek2Right():
    scoreIncrease = 0
    if field.canMove(s2.row, s2.moveRight()):
        field.clearAtPos(s2.row, s2.column)
        s2.column = s2.moveRight()
        if field.getCharAtPos(s2.row, s2.column) == '@':
            field.catchSnitch()
            field.placeSeeker2(s2.seek_char, s2.row, s2.column)
            scoreIncrease += 150
        else:
            field.placeSeeker1(s2.seek_char, s2.row, s2.column)
            print(field.toString())
    return scoreIncrease

def moveSeek2Up():
    scoreIncrease = 0
    if field.canMove(s2.moveUp(), s2.column):
        field.clearAtPos(s2.row, s2.column)
        s2.row = s2.moveUp()
        if field.getCharAtPos(s2.row, s2.column) == '@':
            field.catchSnitch()
            field.placeSeeker2(s2.seek_char, s2.row, s2.column)
            scoreIncrease += 150
        else:
            field.placeSeeker1(s2.seek_char, s2.row, s2.column)
            print(field.toString())
    return scoreIncrease

def moveSeek2Down():
    scoreIncrease = 0
    if field.canMove(s2.moveDown(), s2.column):
        field.clearAtPos(s2.row, s2.column)
        s2.row = s2.moveDown()
        if field.getCharAtPos(s2.row, s2.column) == '@':
            field.catchSnitch()
            field.placeSeeker2(s2.seek_char, s2.row, s2.column)
            scoreIncrease += 150
        else:
            field.placeSeeker1(s2.seek_char, s2.row, s2.column)
            print(field.toString())
    return scoreIncrease

# function to move the Snitch on level2
def moveSnitch():
    # store randomly generated row and col so that it will be the same in if statement
    row = sn.moveSnitchRow()
    col = sn.moveSnitchCol()
    if field.canMove(row, col):
        field.clearAtPos(sn.row, sn.column)
        sn.row = row
        sn.column = col
        field.placeSnitch('@', row, col)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, BASICFONT, level, move1, move2, score1, score2
    #set up the moves and score count
    move1 = 0
    move2 = 0
    score1 = 0
    score2 = 0
    level = 1
    # place Seekers and Snitch
    field.placeSeeker1('1', 4, 1)
    field.placeSnitch('@', 3, 2)
    field.placeSeeker2('2', 5, 3)
    print (field.toString())
    print (sn.toString())
    print (s1.toString())
    print (s2.toString())
    drawMap(field)

    while True:
        #thread 1 - look for an action
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                # Player clicked the "X" at the corner of the window.
                terminate()
            elif event.type == KEYDOWN:
                # first seeker
                if event.key == K_RIGHT:
                    score1 += moveSeek1Right()
                    move1 += 1
                    if level == 2:
                        moveSnitch()
                elif event.key == K_UP:
                    score1 += moveSeek1Up()
                    move1 += 1
                    if level == 2:
                        moveSnitch()
                elif event.key == K_LEFT:
                    score1 += moveSeek1Left()
                    move1 += 1
                    if level == 2:
                        moveSnitch()
                elif event.key == K_DOWN:
                    score1 += moveSeek1Down()
                    move1 += 1
                    if level == 2:
                        moveSnitch()
                # second seeker
                elif event.key == K_d:
                    score2 += moveSeek2Right()
                    move2 += 1
                    if level == 2:
                        moveSnitch()
                elif event.key == K_w:
                    score2 += moveSeek2Up()
                    move2 += 1
                    if level == 2:
                        moveSnitch()
                elif event.key == K_a:
                    score2 += moveSeek2Left()
                    move2 += 1
                    if level == 2:
                        moveSnitch()
                elif event.key == K_s:
                    score2 += moveSeek2Down()
                    move2 += 1
                    if level == 2:
                        moveSnitch()
                else:
                    pass
            mapNeedsRedraw = True

            # go to level2
            if field.getSnitch() == 0:
                if level == 1:
                    field.goToLevel2()
                    level = 2
                    field.placeSeeker1('1', 4, 1)
                    field.placeSeeker2('2', 5, 3)
                    field.placeSnitch('@', 3, 2)
                    s1.setCol(1)
                    s1.setRow(4)
                    s2.setCol(3)
                    s2.setRow(5)
                    move1 = 0
                    move2 = 0
                    drawMap(field)
                elif level == 2:
                    endScreen(score1, score2)

        #thread 2: redraw the screen
        #draws the background
        DISPLAYSURF.fill(BGCOLOR)
        #if something has changed, redraw....
        if mapNeedsRedraw:
            mapSurf = drawMap(field)
            mapNeedsRedraw = False

        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

        # Draw the map on the DISPLAYSURF object.
        DISPLAYSURF.blit(mapSurf, mapSurfRect)
        # Print score
        text1 = font.render('First seeker moves: ' + str(move1), 1, (230,230,250))
        text2 = font.render('Second seeker moves: ' + str(move2), 1, (230,230,250))
        text3 = font.render('First seeker score: ' + str(score1), 1, (230,230,250))
        text4 = font.render('Second seeker score: ' + str(score2), 1, (230,230,250))
        DISPLAYSURF.blit(text1, (50,70))
        DISPLAYSURF.blit(text2, (50,100))
        DISPLAYSURF.blit(text3, (500,70))
        DISPLAYSURF.blit(text4, (500,100))

        pygame.display.update() # draw DISPLAYSURF to the screen.
        FPSCLOCK.tick()

def drawMap(field):
    #draw the tile sprites onto this surface.
    #this creates the visual map!
    mapSurfWidth = field.getWidth() * TILEWIDTH
    mapSurfHeight = field.getHeight() * TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(BGCOLOR)
    for h in range(field.getHeight()):
        for w in range(field.getWidth()):
            thisTile = pygame.Rect((w * TILEWIDTH, h * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
            if field.getCharAtPos(h, w) in TILEMAPPING:
                #checks in the TILEMAPPING directory above to see if there is a
                #matching picture, then renders it
                baseTile = TILEMAPPING[field.getCharAtPos(h,w)]

            # Draw the tiles for the map.
            mapSurf.blit(baseTile, thisTile)
    return mapSurf

def restart():
    global move1, move2, level, score1, score2
    field.__init__()
    s1.setRow(4)
    s1.setCol(1)
    s2.setRow(5)
    s2.setCol(3)
    sn.setCol(2)
    sn.setRow(3)
    level = 1
    move1 = 0
    move2 = 0
    score1 = 0
    score2 = 0
    field.placeSeeker1(s1.getChar(), s1.getRow(), s1.getCol())
    field.placeSeeker2(s2.getChar(), s2.getRow(), s2.getCol())
    field.placeSnitch('@', 3, 2)
    drawMap(field)

def endScreen(score1, score2):
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    # another game loop
    while True:
        pygame.time.delay(100)
        DISPLAYSURF.fill(BGCOLOR1)
        finish = largeFont.render('The game has finished! ', 1, PLUM)
        seek1 = largeFont.render('Seeker 1 got '+ str(score1) + ' points', 1, PLUM)
        seek2 = largeFont.render('Seeker 2 got '+ str(score2) + ' points', 1, PLUM)
        restartMessage = font.render('If you want to restart the game --> press SPACE button', 1, PLUM)
        if score1 > score2:
            score_Total = largeFont.render('SEEKER 1 is the WINNER!',1, WHITE)
        elif score1 < score2:
            score_Total = largeFont.render('SEEKER 2 is the WINNER!',1, WHITE)
        else:
            score_Total = largeFont.render('1 : 1 - NO WINNER',1, WHITE)
        DISPLAYSURF.blit(finish, (225,70))
        DISPLAYSURF.blit(seek1, (20, 200))
        DISPLAYSURF.blit(seek2, (450, 200))
        DISPLAYSURF.blit(score_Total, (225, 350))
        DISPLAYSURF.blit(restartMessage, (300, 500))
        pygame.display.update()
        FPSCLOCK.tick()
        # loop to exit or restart the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    restart()
                    return


def terminate():
    #shutdown routine
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()