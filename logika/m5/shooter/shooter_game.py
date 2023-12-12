from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, rect_x, rect_y, playeer_speed, player_widht, player_heigh):
        super().__init__()
        self.image = scale(load(player_image), (player_widht, player_heigh))
        self.speed = playeer_speed

        self.widht = rect_x
        self.height = rect_y

        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x < win_widht-self.widht-95:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
    def fire(self):
        pass

win_widht = 700
win_height = 500
window = display.set_mode((win_widht,win_height))
background = scale(load('galaxy.jpg'), (win_widht, win_height))

ship = Player('rocket.png', 5, (win_height) - 160, 6, 100, 150)


game = True
finish = False
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)
mixer.music.set_volume(0.03)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:

        window.blit(background, (0 ,0))
        ship.reset()
        ship.update()
    display.update()
    clock.tick(FPS)