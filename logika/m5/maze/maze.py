from pygame import *
from pygame.sprite import collide_rect
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, rect_x, rect_y, playeer_speed):
        super().__init__()
        self.image = scale(load(player_image), (30, 30))
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

        if self.rect.x <= self.min_x:
            self.direction = 'right'
        elif self.rect.x >= win_width - 80:
            self.direction = "left"

class Wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, wall_wight, wall_height):
        super().__init__()
        self.widht = wall_wight
        self.height = wall_height

        self.image = Surface((self.widht, self.height))
        self.image.fill((1,250,0))

        self.rect = self.image.get_rect()

        self.rect.x = wall_x

        self.rect.y = wall_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))

background = scale(load("background.jpg"), (win_width, win_height))
'''
wall_player1 = Wall(0, 0, 2500, 20)
wall_player2 = Wall(250, 0, 20, 350)
wall_player3 = Wall(120, 200, 20, 350)
wall_player4 = Wall(430, 200, 20, 350)
wall_player5 = Wall(430, 300, 120, 20)
wall_player6 = Wall(700, 0, 20, 2002)
wall_player6 = Wall(700, 700, 2000, 2)
'''

Wall_player1=Wall(0, 0, 2500, 20)
Wall_player2=Wall(250, 0, 20, 350)
Wall_player3=Wall(120, 200, 20, 350)
Wall_player4=Wall(430, 200, 20, 350)
Wall_player5=Wall(430, 300, 120, 20)
Wall_player6=Wall(700, 0, 20, 2002)
Wall_player7=Wall(700, 700, 2000, 2)
Wall_player8=Wall(200, 400, 150, 20)
Wall_player9=Wall(500, 100, 20, 200)
Wall_player10=Wall(600, 300, 100, 20)
Wall_player11=Wall(300, 150, 120, 20)
Wall_player12=Wall(450, 250, 20, 120)
Wall_player13=Wall(400, 400, 150, 20)
Wall_player13=Wall(100, 300, 20, 120)



gyborg1 = Enemy("cyborg.png", win_width - 100, win_height - 300, 2, 500),
gyborg2 = Enemy("cyborg.png", win_width - 150, win_height - 150, 2, 450),
gyborg3 = Enemy("cyborg.png", win_width - 200, win_height - 400, 2, 400),
gyborg4 = Enemy("cyborg.png", win_width - 300, win_height - 200, 2, 350),
gyborg5 = Enemy("cyborg.png", win_width - 400, win_height - 450, 2, 300),
gyborg6 = Enemy("cyborg.png", win_width - 500, win_height - 100, 2, 250)

player = Player("hero.png", 5, win_height - 80, 5)
final = GameSprite("treasure.png", win_width - 80, win_height - 80, 0)

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()

f = font.Font(None, 70)
win = f.render("You Win", True, (255, 215, 0))
lose = f.render("You lose", True, (255, 0, 0))

mixer.init()
mixer.music.load("jungles.ogg")

mixer.music.play()

money_sound = mixer.Sound("money.ogg")
kick_sound = mixer.Sound("kick.ogg")
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:

        window.blit(background, (0, 0))
        Wall_player1.reset()
        Wall_player2.reset()
        Wall_player3.reset()
        Wall_player4.reset()
        Wall_player5.reset()
        Wall_player6.reset()
        Wall_player7.reset()
        Wall_player8.reset()
        Wall_player9.reset()
        Wall_player10.reset()
        Wall_player11.reset()
        Wall_player12.reset()
        Wall_player13.reset()



        player.reset()
        #gyborg1.reset()
        #gyborg2.reset()
        #gyborg3.reset()
        #gyborg4.reset()
        #gyborg5.reset()
        #gyborg6.reset()
        final.reset()
        #gyborg2.reset()

        #gyborg1.update()
        #gyborg2.update()
        #gyborg3.update()
        #gyborg4.update()
        #gyborg5.update()
        #gyborg6.update()
        player.update()

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win,(200,200))
            money_sound.play()
        if sprite.collide_rect(player, Wall_player1) or sprite.collide_rect(player, Wall_player2) or sprite.collide_rect(player, Wall_player3) or sprite.collide_rect(player, Wall_player4) or sprite.collide_rect(player, Wall_player5) or sprite.collide_rect(player, Wall_player6) or sprite.collide_rect(player, Wall_player7) or sprite.collide_rect(player, Wall_player8) or sprite.collide_rect(player, Wall_player9) or sprite.collide_rect(player, Wall_player10) or sprite.collide_rect(player, Wall_player11) or sprite.collide_rect(player, Wall_player12) or sprite.collide_rect(player, Wall_player13):

            finish = True
            window.blit(lose,(200,200))
            kick_sound.play()


    display.update()

    clock.tick(FPS)