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

Window_height=600
Window_width=600

BlockSize = 10

#Colors#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Setup #
pg.init()

Window = pg.display.set_mode((Window_width,Window_height))
Window.fill (WHITE)
pg.display.set_caption("Pathfinding")

clock = pg.time.Clock()
clock.tick(60)
	
# run loop #
run=True

while run:
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
            sys.exit()
            pg.display.update()

    keys = pg.key.get_pressed()
    if keys[K_ESCAPE]:
        run=False
        pg.quit()
        sys.exit()
        pg.display.update()

    pg.display.update()
  