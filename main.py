import pygame as pg
import math
from pygame import display
from pygame import surface
from pygame.constants import K_ESCAPE
from pygame.draw import rect

#Variables#
Row = 10
Colom = 10

Window_height=1080
Window_width=1920

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

# Grid Create#
def Makegrid(Row, Colom):
	grid = []
	gap = Colom // rows
	for i in range(Row):
		grid.append([])
		for j in range(Row):
			spot = Spot(i, j, gap, Row)
			grid[i].append(spot)

	return grid

# run loop #
run=True
while run:
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if keys[K_ESCAPE]:
        run=False

  