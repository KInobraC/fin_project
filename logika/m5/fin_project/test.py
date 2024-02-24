import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from pygame.transform import scale, rotate
from pygame.image import load
import random

pygame.init()

win_width = 700
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
background = scale(load('bg.jpg'), (win_width, win_height))


class GameSprite(Sprite):
    def __init__(self, player_image, rect_x, rect_y, player_speed, player_width, player_height):
        super().__init__()
        self.original_image = scale(load(player_image), (player_width, player_height))
        self.image = self.original_image
        self.speed = player_speed
        self.width = player_width
        self.height = player_height
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.jump_speed = -10
        self.gravity = 0.5
        self.on_ground = True
        self.jump_count = 0

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def jump(self):
        if self.on_ground:
            self.jump_speed = -15  # Increase jump height
            self.on_ground = False
            self.jump_count = 1
        elif self.jump_count < 2:
            self.jump_speed = -15  # Increase jump height
            self.jump_count += 1

    def apply_gravity(self):
        if not self.on_ground:
            self.jump_speed += self.gravity
            self.rect.y += self.jump_speed
            if self.rect.y >= win_height - self.height:
                self.rect.y = win_height - self.height
                self.on_ground = True
                self.jump_count = 0


class Enemy(GameSprite):
    def __init__(self, enemy_image, rect_x, rect_y, enemy_speed, enemy_width, enemy_height, disabled_time):
        super().__init__(enemy_image, rect_x, rect_y, enemy_speed, enemy_width, enemy_height)
        self.disabled_time = disabled_time
        self.disabled_timer = 0
        self.disabled = False
        self.hitbox = pygame.Rect(rect_x, rect_y, enemy_width, enemy_height)

    def update(self):
        if not self.disabled:
            self.rect.x -= self.speed
            self.hitbox.x = self.rect.x
            if self.rect.x <= 0:
                self.rect.x = win_width
        else:
            if pygame.time.get_ticks() - self.disabled_timer >= self.disabled_time:
                self.disabled = False
                self.disabled_timer = 0


class Slash(GameSprite):
    def __init__(self, player_rect, slash_image, direction):
        super().__init__(slash_image, player_rect.x, player_rect.y, 0, 50, 50)
        self.direction = direction
        self.timer = pygame.time.get_ticks()

        if self.direction == 'up':
            self.rect.x = player_rect.x + 25
            self.rect.y = player_rect.y - 43
        elif self.direction == 'down':
            self.rect.x = player_rect.x + 24
            self.rect.y = player_rect.y + 93
        elif self.direction == 'left':
            self.rect.x = player_rect.x - 25
            self.rect.y = player_rect.y + 21
        elif self.direction == 'right':
            self.rect.x = player_rect.x + 70
            self.rect.y = player_rect.y + 20

        if self.direction == 'up':
            self.image = rotate(self.original_image, 90)
        elif self.direction == 'down':
            self.image = rotate(self.original_image, 270)
        elif self.direction == 'left':
            self.image = rotate(self.original_image, 180)
        elif self.direction == 'right':
            self.image = self.original_image

    def update(self):
        if pygame.time.get_ticks() - self.timer >= 400:
            self.kill()


class Tidehunter(GameSprite):
    def __init__(self, stand_image, rect_x, rect_y, stand_width, stand_height):
        super().__init__(stand_image, rect_x, rect_y, 0, stand_width, stand_height)
        self.hitbox = pygame.Rect(rect_x, rect_y, stand_width, stand_height)

    def increase_jump(self):
        self.jump_speed -= 10  # Increase jump speed


player = GameSprite('ver_idle.png', 100, 400, 5, 100, 100)
enemy = Enemy('enemy.png', win_width - 100, 400, 3, 100, 100, disabled_time=3000)

slashes = pygame.sprite.Group()
tidehunter = Tidehunter('tidehunter.png', 100, 425, 30, 80)

game = True
clock = pygame.time.Clock()

while game:
    for event in pygame.event.get():
        if event.type == QUIT:
            game = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game = False

            if event.key == K_SPACE:
                player.jump()

            if event.key == K_UP:
                new_slash = Slash(player.rect, 'slash.png', 'up')
                slashes.add(new_slash)
            elif event.key == K_DOWN and not player.on_ground:
                new_slash = Slash(player.rect, 'slash.png', 'down')
                slashes.add(new_slash)
            elif event.key == K_LEFT:
                new_slash = Slash(player.rect, 'slash.png', 'left')
                slashes.add(new_slash)
            elif event.key == K_RIGHT:
                new_slash = Slash(player.rect, 'slash.png', 'right')
                slashes.add(new_slash)

    keys = pygame.key.get_pressed()
    if keys[K_a] and player.rect.x > 5:
        player.rect.x -= player.speed
    if keys[K_d] and player.rect.x < win_width - player.width:
        player.rect.x += player.speed

    player.apply_gravity()

    window.blit(background, (0, 0))

    player.reset()
    enemy.reset()
    slashes.update()
    slashes.draw(window)
    tidehunter.reset()

    for slash in slashes:
        if slash.rect.colliderect(enemy.hitbox):
            enemy.disabled = True
            enemy.disabled_timer = pygame.time.get_ticks()
            slashes.remove(slash)
            if slash.direction == 'down':
                player.jump_speed -= 10
                tidehunter.increase_jump()

    pygame.display.update()
    clock.tick(30)

pygame.quit()
