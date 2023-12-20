
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint


lost = 0
score = 0


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




class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x < win_widht-self.width-95:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
    def fire(self):
        pass

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(0, win_widht - 150)
            lost = lost + 1



win_widht = 700
win_height = 500
window = display.set_mode((win_widht,win_height))
background = scale(load('galaxy.jpg'), (win_widht, win_height))

ship = Player('rocket.png', 5, (win_height) - 160, 3, 100, 150)

monsters = sprite.Group()

for i in range(4):
    enemy = Enemy('ufo.png', randint(0, win_widht - 100), 0,randint(1,3),85,80)
    monsters.add(enemy)

for i in range(2):
    enemy = Enemy('asteroid.png', randint(0, win_widht - 50), 0,randint(1,3),60,45)
    monsters.add(enemy)

game = True
finish = False
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)
mixer.music.set_volume(0.03)

font.init()
font1 = font.SysFont('Aril', 36)



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        txt_score = font1.render(f'Тебе запушили стільки разів: {lost}', True, (255, 255, 255))
        window.blit(txt_score, (10, 50))
        ship.reset()
        monsters.draw(window)
        monsters.update()
        ship.update()
    display.update()
    clock.tick(FPS)