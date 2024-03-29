import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from pygame.transform import scale, rotate
from pygame.image import load
import random
import math

pygame.init()

win_width = 700
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
background = scale(load('bg.jpg'), (win_width, win_height))
heart_image = scale(load('heart.png'), (30, 30))

# Font settings for score display
font = pygame.font.Font(None, 36)
score_color = (255, 255, 255)
hp = 5

class GameSprite(Sprite):
    def __init__(self, player_image, rect_x, rect_y, player_speed, player_width, player_height):
        super().__init__()
        self.original_image = scale(load(player_image), (player_width, player_height))
        self.image = self.original_image
        self.speed = player_speed
        self.width = player_width
        self.height = player_height
        self.rect = pygame.Rect(rect_x, rect_y, player_height, player_width)  # Modified line
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.jump_speed = -10
        self.gravity = 0.5
        self.on_ground = True
        self.jump_count = 0
        self.hp = 5



    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def jump(self):
        if self.on_ground:
            self.jump_speed = -10
            self.on_ground = False
            self.jump_count = 1
        elif self.jump_count < 2:
            self.jump_speed = -10
            self.jump_count += 1

    def apply_gravity(self):
        if not self.on_ground:
            self.jump_speed += self.gravity
            self.rect.y += self.jump_speed
            if self.rect.y >= win_height - self.height:
                self.rect.y = win_height - self.height
                self.on_ground = True
                self.jump_count = 0

    def draw_hp(self):
        for i in range(self.hp):
            if i < self.hp:
                window.blit(heart_image, (win_width - 30 - (i * 25), 10))

    def lose_hp(self):
        self.hp -= 1



class Enemy(GameSprite):
    def __init__(self, enemy_image, enemy_speed, enemy_width, enemy_height, disabled_time):
        super().__init__(enemy_image, win_width // 2, win_height - enemy_height, enemy_speed, enemy_width,
                         enemy_height)
        self.disabled_time = disabled_time
        self.disabled_timer = 0
        self.disabled = False
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, enemy_width, enemy_height)

    def move_to_middle(self):
        if self.rect.x < win_width // 2:
            self.rect.x += self.speed
        elif self.rect.x > win_width // 2:
            self.rect.x -= self.speed

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

        self.rect.y = win_height - self.height

    def attack(self, target_rect):
        new_enemy_slash = EnemySlash(self.rect, 'enemy_slash.png', 8, target_rect)
        enemy_slashes.add(new_enemy_slash)


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


class EnemySlash(GameSprite):
    def __init__(self, enemy_rect, slash_image, speed, target_rect):
        super().__init__(slash_image, enemy_rect.x, enemy_rect.y, speed, 25, 25)
        self.target_rect = target_rect
        self.direction = self.calculate_direction()

    def calculate_direction(self):
        dx = self.target_rect.centerx - self.rect.centerx
        dy = self.target_rect.centery - self.rect.centery
        dist = max(1, math.hypot(dx, dy))
        dx /= dist
        dy /= dist
        return dx, dy

    def update(self):
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed
        if self.rect.x <= 0:
            self.kill()


player = GameSprite('ver_idle.png', 100, 400, 5, 100, 100)
enemy = Enemy('enemy.png', 3, 100, 100, disabled_time=0)

slashes = pygame.sprite.Group()
enemy_slashes = pygame.sprite.Group()

score = 0
hit_count = 0
cooldown_time = 3000
cooldown_timer = 0
enemy_slash_delay = 5000
enemy_slash_timer = 0

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

    for i in range(player.hp):  # Placed the for loop here to draw hearts
        window.blit(heart_image, (win_width - 30 - (i * 35), 15))

    player.reset()
    enemy.reset()
    slashes.update()
    enemy_slashes.update()
    slashes.draw(window)
    enemy_slashes.draw(window)

    for slash in slashes:
        if slash.rect.colliderect(enemy.hitbox):
            if hit_count < 4:  # Check if hit count is less than 4
                enemy.disabled = True
                enemy.disabled_timer = pygame.time.get_ticks()
                slashes.remove(slash)
                score += 1
                hit_count += 1
            elif hit_count == 4:
                if pygame.time.get_ticks() - cooldown_timer >= cooldown_time:
                    hit_count = 0
                    cooldown_timer = pygame.time.get_ticks()

    enemy.move_to_middle()

    # Enemy slash logic
    if pygame.time.get_ticks() - enemy_slash_timer >= enemy_slash_delay:
        new_enemy_slash = EnemySlash(enemy.rect, 'enemy_slash.png', 8, player.rect)
        enemy_slashes.add(new_enemy_slash)
        enemy_slash_timer = pygame.time.get_ticks()

    for slash in enemy_slashes:
        if slash.rect.colliderect(player.rect):
            player.lose_hp()
            enemy_slashes.remove(slash)
            hp -= 1

    # Render and display the score on the screen
    score_text = font.render("Score: " + str(score), True, score_color)
    window.blit(score_text, (10, 10))

    # Cooldown logic
    if hit_count >= 4:
        if pygame.time.get_ticks() - cooldown_timer >= cooldown_time:
            hit_count = 0  # Reset hit count
            cooldown_timer = pygame.time.get_ticks()

    pygame.display.update()
    clock.tick(30)

    if score == 50:
        game = False
        print("Win")
    elif hp == 0:
        game = False
        print("Lose")

pygame.quit()
