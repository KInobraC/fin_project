from pygame import *


window = display.set_mode((700, 500))

img = image.load("background.png")
background = transform.scale(img, (700, 500))

clock = time.Clock()
FPS = 60

speed = 10

sprite1 = transform.scale(image.load("sprite1.png"), (100, 100))
sprite2 = transform.scale(image.load("sprite2.png"), (100, 100))

s1_posx = 200
s2_posx = 400
s1_posy = 100
s2_posy = 50

game = True
while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (s1_posx, s1_posy))
    window.blit(sprite2, (s2_posx, s2_posy))
    for e in event.get():
        if e.type == QUIT:
            game = False

    key_pressed = key.get_pressed()

    if key_pressed[K_LEFT] and s2_posx > 0:
        s2_posx -= speed

    if key_pressed[K_UP] and s2_posy > 0 :
        s2_posy -= speed

    if key_pressed[K_RIGHT] and s2_posx < 600:
        s2_posx += speed

    if key_pressed[K_DOWN] and s2_posy < 410:
        s2_posy += speed

    if key_pressed[K_a] and s1_posx > 0:
        s1_posx -= speed

    if key_pressed[K_w] and s1_posy > 0 :
        s1_posy -= speed

    if key_pressed[K_d] and s1_posx < 600:
        s1_posx += speed

    if key_pressed[K_s] and s1_posy < 410:
        s1_posy += speed

    display.update()
    clock.tick(FPS)