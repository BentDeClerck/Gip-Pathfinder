from shutil import move
from turtle import right
from numpy import blackman
import pygame as pg
import math
import sys
from queue import PriorityQueue
from pygame import display
from pygame import surface
from pygame.locals import *
from pygame.draw import rect
from pygame.constants import K_ESCAPE
from pygame.constants import K_r


# Variables #
Row = 10
Colom = 10
BlockSize = 50

FPS = 60

# Colors #
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
LIGHT_GREEN = (144,238,144)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
PURPLE = (165, 137, 193)

# Setup #
pg.init()

Window_height =  Colom * BlockSize
Window_width = Row * BlockSize

Window = pg.display.set_mode((Window_width, Window_height))
#Surface = pg.display.set_mode((Window_height, Window_width))
#Surface.fill(WHITE)

image = pg.display.get_surface()
pg.display.set_caption("Path Of Exile")

clock = pg.time.Clock()
clock.tick(FPS)

# Rechter / Linker muisknop #
#moving = False
#Left = 1
#Right = 3
#LEFT = False
#RIGHT = False
           
# A* Class #
class Spot:
    def __init__ (self, rij, kolom, total_Rows, total_Col):
        self.rij = rij
        self.kolom = kolom
        self.x = rij * BlockSize 
        self.y =  kolom * BlockSize
        self.color = WHITE
        self.neigbors = []
        self.total_Rows = total_Rows
        self.total_Col = total_Col
    
    def get_posision(self):
        return  self.rij, self.kolom

    def is_closed(self):
        return self.color == LIGHT_GREEN

    def is_open(self):
        return self.color == GRAY

    def is_black(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == GREEN

    def is_end(self):
        return self.color == RED

    def reset(self): 
        self.color == WHITE

    def make_closed(self):
        self.color = LIGHT_GREEN

    def make_open(self):
        self.color = GRAY

    def make_black(self):
        self.color = BLACK
    
    def make_start(self):
        self.color == GREEN

    def make_end(self):
        self.color = RED
    
    def make_path(self):
        self.color = PURPLE

    def draw(self, Window):
        rect = pg.Rect(self.x, self.y, BlockSize, BlockSize)
        pg.draw.rect(Window, self.color, rect, 1)

    def update_neighbors(self, grid):
        pass

    def __Lt__(self, other):
        return False

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def make_grid():
    grid = []

    for i in range(0, Window_width, BlockSize):
        grid.append([])
        for j in range(0, Window_height, BlockSize):
            rect = pg.Rect(i, j, BlockSize, BlockSize)
            pg.draw.rect(Window, BLACK, rect, 1)
            spot = Spot(i, j, Row, Colom)
            grid.append(spot)

    return grid       

def draw_grid():
    for i in range(0, Window_width, BlockSize):
        pg.draw.line(Window, GRAY, (0, i * BlockSize), (Window_width, i * BlockSize))
        for j in range(0, Window_height, BlockSize):
            pg.draw.line(Window, GRAY, (j * BlockSize, 0), (j * BlockSize, Window_height))

def draw(grid):
    Window.fill(WHITE)

    for rij in grid:
        for spot in rij:
            spot.draw()

    draw_grid()
    pg.display.update()

def get_clicked_pos(pos):
    y, x = pos

    row = y // BlockSize
    col = x // BlockSize

    return row, col

def main():
    grid = make_grid()

    start = None
    end = None
    run = True
    started = False

    while run:
        draw(grid)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            
            if started:
                continue

            if pg.mouse.get_pressed()[0]:
                pos = pg.mouse.get_pos()
                rij, kolom = get_clicked_pos(pos)
                spot = grid[rij][kolom]

                if not start :
                    start = spot
                    start.make_start()

                elif not end:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start :
                    spot.make_black()

            elif pg.mouse.get_pressed()[2]:
                pass

    pg.quit()       

main()