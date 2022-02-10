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

    for event in pg.event.get():
		if event.type == pg.KEYDOWN:	     
		keys = pg.key.get_pressed()
        
    		if keys[K_ESCAPE]:
        		pg.quit()
				sys.exit()

    	if event.type == pg.QUIT:
			pg.quit()
			sys.exit()    

    pg.display.update()
  