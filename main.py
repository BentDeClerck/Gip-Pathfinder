from shutil import move
from tkinter.font import ROMAN
from turtle import right, st
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
Row = 15
Colom = 15
BlockSize = 50

FPS = 60

# Colors #
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0) 
LIGHT_GREEN = (144,238,144)
LIGHT_BLUE = (173, 216, 230)
LIGHT_RED = (255, 204, 203)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
PURPLE = (165, 137, 193)

# Setup #
pg.init()

Window_height =  Colom * BlockSize
Window_width = Row * BlockSize

Window = pg.display.set_mode((Window_width, Window_height))
pg.display.set_caption("Path Of Exile")
           
# A* Class #
class Spot:
    def __init__ (self, rij, kolom, total_Rows, total_Col):
        self.rij = rij
        self.kolom = kolom
        self.x = rij * BlockSize 
        self.y =  kolom * BlockSize
        self.color = WHITE
        self.neighbors = []
        self.total_Rows = total_Rows
        self.total_Col = total_Col
    
    def get_pos(self):
        return  self.rij, self.kolom

    def is_closed(self):
        return self.color == LIGHT_GREEN

    def is_open(self):
        return self.color == LIGHT_RED

    def is_black(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == GREEN

    def is_end(self):
        return self.color == RED

    def reset(self): 
        self.color = WHITE

    def make_start(self):
        self.color = GREEN

    def make_closed(self):
        self.color = LIGHT_GREEN

    def make_open(self):
        self.color = LIGHT_RED

    def make_black(self):
        self.color = BLACK

    def make_end(self):
        self.color = RED
    
    def make_path(self):
        self.color = LIGHT_BLUE

    def draw(self):
        pg.draw.rect(Window, self.color, (self.x, self.y, BlockSize, BlockSize))

    def update_neighbors(self, grid):
        self.neighbors = []

        if self.rij < self.total_Rows - 1 and not grid[self.rij + 1][self.kolom].is_black(): #Onder
            self.neighbors.append(grid[self.rij + 1][self.kolom])

        if self.rij > 0 and not grid[self.rij - 1][self.kolom].is_black(): #Boven
            self.neighbors.append(grid[self.rij - 1][self.kolom])

        if self.kolom < self.total_Col - 1 and not grid[self.rij][self.kolom + 1].is_black(): #Rechts
            self.neighbors.append(grid[self.rij][self.kolom + 1])

        if self.kolom > 0 and not grid[self.rij][self.kolom - 1].is_black(): #Links
            self.neighbors.append(grid[self.rij][self.kolom - 1])

    def __Lt__(self, other):
        return False

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbor  in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

def make_grid():
    grid = []

    for i in range(Row):
        grid.append([])
        for j in range(Colom):
            spot = Spot(i, j, Row, Colom)
            grid[i].append(spot)

    return grid       

def draw_grid():

    for i in range(Colom):
        pg.draw.line(Window, GRAY, (0, i * BlockSize), (Window_width, i * BlockSize))
        for j in range(Row):
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

                if not start and spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start :
                    spot.make_black()

            elif pg.mouse.get_pressed()[2]:
                pos = pg.mouse.get_pos()
                rij, kolom = get_clicked_pos(pos)
                spot = grid[rij][kolom]
                spot.reset()

                if spot == start:
                    start = None

                elif spot == end:
                    end = None

            if event.type == pg.KEYDOWN:

                if event.key == pg.K_SPACE and start and end:
                    for rij in grid:
                        for spot in rij:
                            spot.update_neighbors(grid)

                    algorithm(lambda: draw(grid), grid, start, end)

                if event.key == pg.K_c:
                    start = None
                    end = None
                    grid = make_grid()
                
                if event.key == pg.K_ESCAPE:
                    run = False

    pg.quit()       

main()