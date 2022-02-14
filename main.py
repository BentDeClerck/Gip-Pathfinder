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

Window = pg.display.set_mode((Window_width,Window_height))
Window.fill (WHITE)
pg.display.set_caption("Pathfinding")

clock = pg.time.Clock()
clock.tick(FPS)

#Dweller of the deep end#
def drawGrid():
    for x in range(0, Window_width, BlockSize):
        for y in range(0, Window_height, BlockSize):
            rect = pg.Rect(x, y, BlockSize, BlockSize)
            pg.draw.rect(Window, BLACK, rect, 1)

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

        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()

            print("Click ", pos, "Grid coordinates: ", row, column)

    keys = pg.key.get_pressed()
    if keys[K_ESCAPE]:
        run=False
        pg.quit()
        sys.exit()
        pg.display.update()

    pg.display.update()
