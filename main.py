import pygame, sys
from pygame.locals import QUIT
from pygame import mixer
import time
from math import pi
#Initialize pygame
pygame.init()
mixer.init()

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (144, 244, 142)
RED = (255, 0, 0)
PERIWINKLE = (142, 195, 244)
YELLOW = (255, 195, 0)
CYAN = (0, 255, 253)
DARK_BLUE = (27, 25, 127)
#surface
size = [840, 360]
screen = pygame.display.set_mode(size)
#font for the text display
font = pygame.font.Font("Bubblegum.ttf", 100)
fontTitle = pygame.font.Font("titlefont.otf",82)
title = fontTitle.render("MISSION ABYSS", True, WHITE)
#images being used
spaceship_size = (400, 300)
spaceship = pygame.image.load("spaceship.png").convert_alpha()
spaceship = pygame.transform.scale(spaceship, spaceship_size)

bg_size = (840,360)
background = pygame.image.load("AGAIN.png").convert_alpha()
background = pygame.transform.scale(background,bg_size)
background_rect = background.get_rect()
rectBack = background_rect.copy()
rectBack.top = 3360

#initialize screen

#Timer Variables
timer_interval = 1000  # 1 second
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, timer_interval)
done = False
clock = pygame.time.Clock()
counter = 10
text = font.render(str(counter), True, BLACK)

t = 0

#sound files
mixer.music.load("countdown.wav")


#coumtdown
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
  #Countdown

  text_rect = text.get_rect(center=screen.get_rect().center)
  screen.blit(text, text_rect)
  pygame.display.flip()
mixer.music.unload()
#Launch landscape
  
done = False
count = 100
while not done:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  screen.fill(PERIWINKLE)
  
  screen.blit(spaceship, [220, 42])
  pygame.draw.rect(screen, GREEN, [0, 300, 840, 100])  #ground
  count = count - 3#subtracting to lengthen/shorten this scene
  if count <= 0:
    done = True
  pygame.display.flip()
  

#rocket sets off
  done = False
  y = 0  #variable to move rocket up
  while not done:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
    screen.fill(PERIWINKLE) 
    screen.blit(spaceship, [220, 42 - y])  #moving the spaceship up 1 at a time
    pygame.draw.rect(screen, GREEN, [0, 300, 840, 100])  #ground
    y = y + 2
    if  y == 342:
      done = True
    pygame.display.flip()

  #flying into sky pt1 (reaches middle and bg move fast)
  done = False
  z = 0
  while not done:
    clock.tick(60)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
    screen.fill(PERIWINKLE)

    screen.blit(spaceship, [220, 360 -z])  #moving the spaceship up 1 at a time
    z += 1
    if z == 330:
      done = True
    pygame.display.flip()
  #flying into sky pt2 (at middle, moving background)
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
    screen.blit(background,[0,-360 +c])

    screen.blit(spaceship, [220, 30])  
    c+=0.5
    if c >= 360:
      done = True
    pygame.display.flip()
  #flying into sky pt3(pasts the end, preparing for title scene)
  done = False
  a = 0
  x = 0
  while not done:
    clock.tick(60)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
    screen.fill(DARK_BLUE)
    screen.blit(background,[0,0+x])
    screen.blit(spaceship,[220,30+a]) 
    
    a += 0.5
    x += 1
    if a >= 330:
      done = True
    pygame.display.flip()
  #title
  
  done = False
  count = 0
  a = 0
  while not done:
    clock.tick(60)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
    screen.fill(DARK_BLUE)
    title_rect = title.get_rect(center=screen.get_rect().center)
    screen.blit(title,title_rect)
    a += 1
    if a >= 500:
      done = True
    pygame.display.flip() 
    
  #out of earth
  done = False
  count = 0
  a = 0
  while not done:
    clock.tick(60)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
    screen.fill(DARK_BLUE)
    title_rect = title.get_rect(center=screen.get_rect().center)
    screen.blit(title,title_rect)
    a += 1
    if a >= 500:
      done = True
    pygame.display.flip() 
   
pygame.quit()
