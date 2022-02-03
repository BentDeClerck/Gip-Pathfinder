import pygame as pg
import math
from pygame import display
from pygame import surface
from pygame.constants import K_ESCAPE
from pygame.draw import rect

# Setup #
pg.init()

Window_height=1080
Window_width=1920
Window = pg.display.set_mode((Window_width,Window_height))
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

    keys = pg.key.get_pressed()
    if keys[K_ESCAPE]:
        run=False
