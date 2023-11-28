
from pygame import *
from pygame.sprite import collide_rect
from pygame.transform import scale, flip
from pygame.image import load
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, rect_x, rect_y, playeer_speed):
        super().__init__()
        self.image = scale(load(player_image), (65, 65))
        self.speed = playeer_speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed


class Enemy(GameSprite):
    def __init__(self, player_image, rect_x, rect_y, playeer_speed, min_x, ):
        super().__init__(player_image, rect_x, rect_y, playeer_speed)
        self.min_x = min_x

        self.direction = "left"
    direction = "left"
    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        if self.rect.x <= 500:
        if self.rect.x <= self.min_x:
            self.direction = 'right'
        elif self.rect.x >= win_width - 80:
            self.direction = "left"
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
background = scale(load("background.jpg"), (win_width, win_height))


player = Player("hero.png", 5, win_height - 80, 5)
cyborg = Enemy("cyborg.png", win_width - 100, win_height - 300,  2)
cyborg = Enemy("cyborg.png", win_width - 100, win_height - 300,  2, 500)
final = GameSprite("treasure.png", win_width - 80, win_height - 80, 0)
cyborg2 = Enemy("cyborg.png", win_width - 150, win_height - 150,  2, 350)


game = True
finish = False
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        player.reset()
        cyborg.reset()
        final.reset()

        cyborg2.reset()
        cyborg2.update()
        cyborg.update()
        player.update()

    display.update()
    clock.tick(FPS)