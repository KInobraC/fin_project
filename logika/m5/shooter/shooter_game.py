from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint
from time import time as timer



lost = 0
score = 0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, rect_x, rect_y, player_speed, player_width, player_heigh):
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_heigh))
        self.speed = player_speed
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
        if keys[K_d] and self.rect.x < win_width-self.widht-95:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
    def fire(self):
        pass

        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 10, 15,20)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(0, win_width - 150)
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
                self.kill()



win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
background = scale(load('galaxy.jpg'), (win_width, win_height))

ship = Player('rocket.png', 5, (win_height) - 160, 3, 100, 150)

bullets = sprite.Group()

monsters = sprite.Group()

for i in range(4):
    enemy = Enemy('ufo.png', randint(0, win_width - 100), 0,randint(1,3),85,80)
    monsters.add(enemy)
for i in range(2):
    enemy = Enemy('asteroid.png', randint(0, win_width - 50), 0,randint(1,3),60,45)
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
font2 = font.SysFont('Aril', 36)


ammo = 5
reload = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False

        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if ammo>0 and reload == False:
                    ship.fire()
                    ammo-=1
                if ammo == 0 and reload == False:
                    reload = True
                    start_reload = timer()



    if not finish:

        window.blit(background, (0 ,0))
        txt_lose = font1.render(f'скільки тебе запушили: {lost}', True, (255, 255, 255))
        txt_win = font2.render(f'РОзстріляно: {score}', True, (255, 255, 255))
        window.blit(txt_lose, (10, 50))
        window.blit(txt_win, (10, 25))
        ship.reset()


        if reload:
            now_time = timer()

            delta = now_time - start_reload
            if delta < 3:
                txt_reload = font1.render('Reload', True,[150, 50, 0])
                window.blit(txt_reload, (200, 400))
            else:
                ammo = 5
                reload = False

        monsters.draw(window)
        bullets.draw(window)

        bullets.update()
        monsters.update()

        ship.update()
    display.update()
    clock.tick(FPS)
