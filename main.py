import pygame
import os
pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

from player import *
from loadmap import *
from camera import *

def change():
    map_sprites.empty()
    mapload(pytmx.load_pygame('map/testmap2.tmx'), map_sprites)
    all_sprites.empty()
    all_sprites.add(player, map_sprites)

all_sprites = object()
mapload(pytmx.load_pygame('map/testmap.tmx'), map_sprites)
player = player(map_sprites)
all_sprites.add(player)
all_sprites.add(map_sprites)
run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if player.rect.x > 400:
            change()
    screen.fill((255,255,255))
    all_sprites.update()
    all_sprites.camera_draw(player)
    pygame.display.update()
    clock.tick(60)