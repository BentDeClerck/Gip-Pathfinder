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
Window.fill (WHITE)
Surface = pg.display.set_mode((Window_height, Window_width))
Surface.fill(WHITE)

image = pg.display.get_surface()
pg.display.set_caption("Path Of Exile")

clock = pg.time.Clock()
clock.tick(FPS)

# Rechter / Linker muisknop #
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
    print("Coord X:", Coord_x, "Coord Y:", Coord_y) 

    rect_green = pg.Rect(Coord_x, Coord_y, BlockSize, BlockSize)
    image.fill(BLACK, rect_green)

# Color White #
def WhiteGrid (row, colom):
    Coord_x = (row - 1) * BlockSize
    Coord_y = (colom - 1) * BlockSize
    print("C             oord X:", Coord_x, "Coord Y:", Coord_y) 

    rect_green = pg.Rect(Coord_x, Coord_y, BlockSize, BlockSize)
    image.fill(WHITE, rect_green)

# Reset Grid #
def resetGrid():
    Window.fill(WHITE)
    Surface.fill(WHITE)
    drawGrid()
    pg.display.update()

# A* Class #
class Node:
    def__init__(self, rij, kolom, hoogte, breete, total_Rows):
        self.rij = rij
        self.kolom = kolom
        self.x = rij * breete 
        self.y =  kolom * hoogte
        self.color = WHITE
        self.neigbors = []
        self.hoogte = hoogte
        self.breete = breete
        self.total_Rows = total_Rows
    
    def get_posision(self):
        return  self.rij, self.kolom

    def is_closed(self):
        return self.color == RED

    def is_open(self):
<<<<<<< HEAD
        return self.color == GRAY
=======
        return self.color == GREEN
>>>>>>> parent of 640120c (Update main.py)

    def is_black(self):
        return self.color == BLACK

<<<<<<< HEAD
    def is_strat(self):
        return self.color == GREEN
=======
    def is_start(self):
        return self.color == LIGHT_GREEN
>>>>>>> parent of 640120c (Update main.py)

    def is_end(self):
        return self.color == GRAY

    def reset(self): 
<<<<<<< HEAD
        self.color == WHITE

    def make_closed(self):
=======
        self.color = WHITE

    def make_start(self):
>>>>>>> parent of 640120c (Update main.py)
        self.color = LIGHT_GREEN

    def make_closed(self):
        self.color = RED

    def make_open(self):
<<<<<<< HEAD
        self.color = GRAY
=======
        self.color = GREEN
>>>>>>> parent of 640120c (Update main.py)

    def make_black(self):
        self.color = BLACK

    def make_end(self):
        self.color = PURPLE
    
    def make_path(self):
        self.color = PURPLE
<<<<<<< HEAD
    
=======
>>>>>>> parent of 640120c (Update main.py)

# Run Loop #
run=True

<<<<<<< HEAD
while run:
    drawGrid()
=======
    def update_neighbors(self, grid):
        self.neigbors = []

        if self.rij < self.total_Rows - 1 and not grid[self.rij + 1][self.kolom].is_black(): #Onder
            self.neigbors.append(grid[self.rij + 1][self.kolom])

        if self.rij > 0 and not grid[self.rij - 1][self.kolom].is_black(): #Boven
            self.neigbors.append(grid[self.rij - 1][self.kolom])

        if self.kolom < self.total_Rows - 1 and not grid[self.rij][self.kolom + 1].is_black(): #Rechts
            self.neigbors.append(grid[self.rij][self.kolom + 1])

        if self.kolom > 0 and not grid[self.rij][self.kolom - 1].is_black(): #Links
            self.neigbors.append(grid[self.rij][self.kolom - 1])

    def __Lt__(self, other):
        return False

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

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
>>>>>>> parent of 640120c (Update main.py)
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

<<<<<<< HEAD
    pg.display.update()
=======
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
                
                if event.key == pg.K_ESCAPE:
                    run = False

    pg.quit()       

main()
>>>>>>> parent of 640120c (Update main.py)
