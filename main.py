import pygame as pg
import math
import sys
from pygame import display
from pygame import surface
from pygame.constants import K_ESCAPE
from pygame.draw import rect

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
Colored_Block = BlockSize - 1

Window = pg.display.set_mode((Window_width, Window_height))
Window.fill (WHITE)
Surface = pg.display.set_mode((Window_height, Window_width))
Surface.fill(WHITE)

image = pg.display.get_surface()
pg.display.set_caption("Path Of Exile")

clock = pg.time.Clock()
clock.tick(FPS)

#Dweller of the deep end#
def drawGrid():
    for x in range(0, Window_width, BlockSize):
        for y in range(0, Window_height, BlockSize):
            rect = pg.Rect(x, y, BlockSize, BlockSize)
            pg.draw.rect(Window, BLACK, rect, 1)
            
#De burning man#
def ColorGrid (row, colom):
    Coord_x = (row - 1) * BlockSize
    Coord_y = (colom - 1) * BlockSize
    print("coord X:", Coord_x, "Coord Y:", Coord_y) 

    rect_green = pg.Rect(Coord_x, Coord_y, BlockSize, BlockSize)
    image.fill(GREEN, rect_green)

#The touch of innocence#
def resetGrid():
    Window.fill(WHITE)
    Surface.fill(WHITE)
    drawGrid()
    pg.display.update()

# run loop #
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

        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            row = (pos[0] // BlockSize) + 1
            colom = (pos[1] // BlockSize) + 1

            ColorGrid(row, colom)
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
