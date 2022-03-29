from shutil import move
from turtle import right
from numpy import blackman
import pygame as pg
import math
import sys
from pygame import display
from pygame import surface
from pygame.locals import *
from pygame.draw import rect
from pygame.constants import K_ESCAPE
from pygame.constants import K_r

#Variables#
Row = 10
Colom = 10
BlockSize = 50

FPS = 60

#Colors#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Setup #
pg.init()

Window_height =  Colom * BlockSize
Window_width = Row * BlockSize

Window = pg.display.set_mode((Window_width, Window_height))
Window.fill (WHITE)
Surface = pg.display.set_mode((Window_height, Window_width))
Surface.fill(WHITE)

image = pg.display.get_surface()
pg.display.set_caption("Path Of Exile")

clock = pg.time.Clock()
clock.tick(FPS)

moving = False
Left = 1
Right = 3
LEFT = False
RIGHT = False

# Draw Grid #
def drawGrid():
    for x in range(0, Window_width, BlockSize):
        for y in range(0, Window_height, BlockSize):
            rect = pg.Rect(x, y, BlockSize, BlockSize)
            pg.draw.rect(Window, BLACK, rect, 1)
            
# Color The Grid #
def ColorGrid (row, colom):
    Coord_x = (row - 1) * BlockSize
    Coord_y = (colom - 1) * BlockSize
    print("coord X:", Coord_x, "Coord Y:", Coord_y) 

    rect_green = pg.Rect(Coord_x, Coord_y, BlockSize, BlockSize)
    image.fill(BLACK, rect_green)

# Color White #
def WhiteGrid (row, colom):
    Coord_x = (row - 1) * BlockSize
    Coord_y = (colom - 1) * BlockSize
    print("coord X:", Coord_x, "Coord Y:", Coord_y) 

    rect_green = pg.Rect(Coord_x, Coord_y, BlockSize, BlockSize)
    image.fill(WHITE, rect_green)

# Reset Grid #
def resetGrid():
    Window.fill(WHITE)
    Surface.fill(WHITE)
    drawGrid()
    pg.display.update()

# Run Loop #
run=True

while run:
    drawGrid()
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
            sys.exit()
            pg.display.update()

        if event.type == pg.K_r:
            resetGrid()

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == Left:
            pos = pg.mouse.get_pos()
            row = (pos[0] // BlockSize) + 1
            colom = (pos[1] // BlockSize) + 1
            moving = True
            LEFT = True
            RIGHT = False

            ColorGrid(row, colom)
            print("Click ", pos, "Grid coordinates: ", row, colom)
            print(moving)

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == Right:
            pos = pg.mouse.get_pos()
            row = (pos[0] // BlockSize) + 1
            colom = (pos[1] // BlockSize) + 1
            moving = True
            LEFT = False
            RIGHT = True

            WhiteGrid(row, colom)
            print("Click ", pos, "Grid coordinates: ", row, colom)
            print(moving)

        elif event.type == pg.MOUSEBUTTONUP:
            moving = False
            print(moving)

        elif event.type == pg.MOUSEMOTION and moving and LEFT:
            pos = pg.mouse.get_pos()
            row = (pos[0] // BlockSize) + 1
            colom = (pos[1] // BlockSize) + 1

            ColorGrid(row, colom)
            print("Click ", pos, "Grid coordinates: ", row, colom)
        
        elif event.type == pg.MOUSEMOTION and moving and RIGHT:
            pos = pg.mouse.get_pos()
            row = (pos[0] // BlockSize) + 1
            colom = (pos[1] // BlockSize) + 1

            WhiteGrid(row, colom)
            print("Click ", pos, "Grid coordinates: ", row, colom)

    keys = pg.key.get_pressed()
    if keys[K_ESCAPE]:
        run=False
        pg.quit()
        sys.exit()
        pg.display.update()

    if keys[K_r]:
        resetGrid()

    pg.display.update()