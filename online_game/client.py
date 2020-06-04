import pygame
import random
import math

# initialize the pygame
pygame.init()
# creating the screen exists for a second
screen = pygame.display.set_mode((800, 600))  # (width,height)

# background image
back_img = pygame.image.load('1.jpg')
back_img = pygame.transform.scale(back_img, (800, 600))  # resizing image

# title and icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player

player_img = pygame.image.load('space-invaders.png')
player_img = pygame.transform.scale(player_img, (64, 64))  # resizing image
px = 370
py = 480
speed = 0

# Enemy
enemy_img = []
ex = []
ey = []
exch = []
eych = []
no_of_enemy = 6

for i in range(no_of_enemy):
    tt = pygame.image.load('pp.png')
    tt = pygame.transform.scale(tt, (64, 64))  # resizing image
    enemy_img.append(tt)
    #  randomizing the position of enemy
    ex.append(random.randint(0, 735))
    ey.append(random.randint(50, 150))
    exch.append(3)
    eych.append(40)

# player
# ready -> we can't see the bullet
# fire -> the bullet is currently moving
bullet_img = pygame.image.load('bull.png')
bullet_img = pygame.transform.scale(bullet_img, (30, 30))  # resizing image
bx = 0
by = 480
bxch = 0
bych = 7
bullet_state = "ready"
score = 0;

# score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
tx = 10
ty = 10

# game over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over():
    over_txt = over_font.render("Game Over :", True, (255, 255, 255))
    screen.blit(over_txt, (200, 250))


def player(x, y):
    screen.blit(player_img, (x, y))  # here we are drawing an image in our screen


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))  # here we are drawing an image in our screen


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def isCollision(ex, ey, bx, by):
    distance = math.sqrt(math.pow(ex - bx, 2) + math.pow(ey - by, 2))
    if distance < 30:
        return True
    return False


# game loop
run = True
while run:
    # RGB
    screen.fill((10, 50, 150))
    # add background image
    screen.blit(back_img, (0, 0))
    # px += 0.1
    # py -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # when we click on cross
            run = False

        # check if keystroke is being pressed whether its left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = -3
            if event.key == pygame.K_RIGHT:
                speed = 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bx = px
                fire_bullet(bx, by)
        # check if key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed = 0
    px += speed
    if px <= 0:
        px = 0
    elif px >= 736:
        px = 736

    # enemy moment
    for i in range(no_of_enemy):
        # game over
        if ey[i] > 200:
            for j in range(no_of_enemy):
                ey[j] = 2000
            game_over()
            break

        ex[i] += exch[i]
        if ex[i] <= 0:
            exch[i] = 3
            ey[i] += eych[i]
        elif ex[i] >= 736:
            exch[i] = -3
            ey[i] += eych[i]

        # collision
        coll = isCollision(ex[i], ey[i], bx, by)
        if coll:
            by = 480;
            bullet_state = "ready"
            score_value += 1
            # print(score)
            ex[i] = random.randint(0, 800)
            ey[i] = random.randint(50, 150)
        enemy(ex[i], ey[i], i)
    # bullet moment
    if by <= 0:
        by = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bx, by)
        by -= bych

    player(px, py)
    show_score(tx, ty)
    pygame.display.update()  # To update screen
