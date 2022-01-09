import pygame as pg
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

background = pg.image.load("track1.png")


# Class auto #
class Car(pg.sprite.Sprite):
    def __init__(self):
        super(Car, self).__init__()
        self.image = pg.image.load(("auto1.png"))
        self.rect = self.image.get_rect()
        self.rect.centery = Window_height /2
        self.rect.centerx = Window_width / 2

    def moveRight(self, pixels):
        self.rect.x += pixels
  
    def moveLeft(self, pixels):
        self.rect.x -= pixels
  
    def moveForward(self, speed):
        self.rect.y += speed * speed/10
  
    def moveBack(self, speed):
        self.rect.y -= speed * speed/10


# list sprites #
all_sprites = pg.sprite.Group()
Car1 = Car()
all_sprites.add(Car1)


# run loop #
run=True
while run:
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    Window.blit(background, [0,0])

    all_sprites.draw(Window)

    keys = pg.key.get_pressed()
    if keys[K_ESCAPE]:
        run=False
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        Car.moveLeft(10)
    if keys[pg.K_RIGHT]:
        Car.moveRight(10)
    if keys[pg.K_DOWN]:
        Car.moveForward(10)
    if keys[pg.K_UP]:
        Car.moveBack(10)    