import pygame
import sys
from pygame.locals import QUIT
from pygame import mixer
import time
from math import pi
# Initialize pygame
pygame.init()
mixer.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (144, 244, 142)
RED = (255, 0, 0)
PERIWINKLE = (142, 195, 244)
YELLOW = (255, 195, 0)
CYAN = (0, 255, 253)
DARK_BLUE = (0,0,0)
# surface
size = [840, 360]
screen = pygame.display.set_mode(size)
# font for the text display
font = pygame.font.Font("Bubblegum.ttf", 100)
fontTitle = pygame.font.Font("titlefont.otf", 82)
title = fontTitle.render("MISSION ABYSS", True, WHITE)
# images being used
spaceship_size = (400, 300)
spaceship = pygame.image.load("spaceship.png").convert_alpha()
spaceship = pygame.transform.scale(spaceship, spaceship_size)
earth = pygame.image.load("earth.png").convert_alpha()
bg_size = (840, 360)
background = pygame.image.load("AGAIN.png").convert_alpha()
background = pygame.transform.scale(background, bg_size)
background_rect = background.get_rect()
rectBack = background_rect.copy()
rectBack.top = 3360
stars_size = (840, 360)
stars = pygame.image.load("stars.png").convert_alpha()
stars = pygame.transform.scale(stars, stars_size)
# initialize screen

# Timer Variables
timer_interval = 1000  # 1 second
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, timer_interval)
done = False
clock = pygame.time.Clock()
counter = 10
text = font.render(str(counter), True, BLACK)

t = 0

# sound files
mixer.music.load("countdown.wav")


# coumtdown
x = 0
while not done:
    clock.tick(60)
    if x == 0:
        mixer.music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == timer_event:
            counter -= 1
            text = font.render(str(counter), True, BLACK)
            if counter == 0:
                pygame.time.set_timer(timer_event, 0)
                done = True

    x += 1
    screen.fill(PERIWINKLE)
    # Countdown

    text_rect = text.get_rect(center=screen.get_rect().center)
    screen.blit(text, text_rect)
    pygame.display.flip()
mixer.music.unload()
# Launch landscape

done = False
count = 100
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(PERIWINKLE)

    screen.blit(spaceship, [220, 42])
    pygame.draw.rect(screen, GREEN, [0, 300, 840, 100])  # ground
    count = count - 3  # subtracting to lengthen/shorten this scene
    if count <= 0:
        done = True
    pygame.display.flip()


# rocket sets off
    mixer.music.load("rocketlaunch.mp3")
    c = 0
    done = False
    y = 0  # variable to move rocket up
    while not done:
        clock.tick(60)
        if c == 0:
            mixer.music.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(PERIWINKLE)
        # moving the spaceship up 1 at a time
        screen.blit(spaceship, [220, 42 - y])
        pygame.draw.rect(screen, GREEN, [0, 300, 840, 100])  # ground
        y = y + 2
        if y == 342:
            done = True
        pygame.display.flip()
    mixer.music.unload()
    # flying into sky pt1 (reaches middle and bg move fast)
    done = False
    z = 0
    while not done:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(PERIWINKLE)

        # moving the spaceship up 1 at a time
        screen.blit(spaceship, [220, 360 - z])
        z += 1
        if z == 330:
            done = True
        pygame.display.flip()
    # flying into sky pt2 (at middle, moving background)
    done = False
    c = 0
    mixer.music.load("Hans Zimmer - Cornfield Chase.mp3")
    while not done:
        clock.tick(60)
        if c == 0:
            mixer.music.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(PERIWINKLE)
        screen.blit(background, [0, -360 + c])

        screen.blit(spaceship, [220, 30])
        c += 0.5
        if c >= 360:
            done = True
        pygame.display.flip()
    # flying into sky pt3(pasts the end, preparing for title scene)
    done = False
    a = 0
    x = 0
    while not done:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(DARK_BLUE)
        screen.blit(background, [0, 0+x])
        screen.blit(spaceship, [220, 30+a])
        screen.blit(title, [130, -330+a])
        a += 0.5
        x += 1
        if a >= 330:
            done = True
        pygame.display.flip()
    # title

    done = False
    count = 0
    a = 0
    while not done:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(DARK_BLUE)

        screen.blit(title, [130, 0+a])
        a += 1
        if a >= 130:
            done = True
        pygame.display.flip()
    done = False
    a = 0
    while not done:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(DARK_BLUE)

        screen.blit(title, [130, 130])
        a += 1
        if a >= 500:
            done = True
        pygame.display.flip()

    # move title down
    done = False
    count = 0
    a = 0
    while not done:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(DARK_BLUE)
        screen.blit(title, [130, 130+a])
        a += 1
        if a >= 300:
            done = True
        pygame.display.flip()
    # out of earth scene
    done = False
    count = 0
    a = 0
    b = 0
    while not done:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(DARK_BLUE)
        screen.blit(earth, [-348+a, 716 - b])
        a += 1
        b += 2
        if a >= 348:
            done = True
        pygame.display.flip()
    # rocket moves out of earth
    done = False
    count = 0
    a = 0
    b = 0
    spaceship = pygame.transform.scale(spaceship, (100, 75))
    spaceship = pygame.transform.rotate(spaceship, 270)

    while not done:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(DARK_BLUE)
        screen.blit(spaceship, [0+a, 133])
        screen.blit(earth, [0, 20])
        a += 5
        if a >= 840:
            done = True
        pygame.display.flip()
    # rocket goes very fast
    done = False
    i = 0
    a = 0
    spaceship = pygame.transform.scale(spaceship, (300, 400))
    spaceship_rect = spaceship.get_rect(center=screen.get_rect().center)
    while not done:
        clock.tick(60)
        screen.fill(DARK_BLUE)
        screen.blit(stars, (i, 0))
        screen.blit(stars, (840+i, 0))
        
        if i <= -840:
            screen.blit(stars, (840+i, 0))
            i = 0
        i = i - 50
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.blit(spaceship, spaceship_rect)
        a += 1
        if a >= 1000:
            done = True
        pygame.display.flip()
    i = 0
    a = 0
    done = False
    while not done:
        clock.tick(60)
        screen.fill(DARK_BLUE)
        
        screen.blit(stars, (i, 0))
        screen.blit(stars, (840+i, 0))
        
        if i <= -840:
            screen.blit(stars, (840+i, 0))
            i = 0
        i = i - 50
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.blit(spaceship, (spaceship_rect.x + a, spaceship_rect.y))
        a += 1
        if a >= 520:
            done = True
        pygame.display.flip()       
pygame.quit()
