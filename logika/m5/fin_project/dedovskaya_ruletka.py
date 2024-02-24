import random

import pygame.display
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, rect_x, rect_y, player_speed, player_width, player_heigh):
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_heigh))
        self.speed = player_speed

        self.width = rect_x
        self.height = rect_y

        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
background = scale(load('bg.jpg'), (win_width, win_height))
class Slash(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
                self.kill()
game = True
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x < win_width - self.width - 95:
            self.rect.x += self.speed
        if keys[K_d] and self.rect.x > 5:
            self.rect.x -= self.speed

player = Player('ver_idle.png', 350, 40, 5, 100, 100)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False
    window.blit(background, (0, 0))
    player.reset()
    pygame.display.update()