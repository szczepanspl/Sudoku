import pygame
import numpy as np
import sys
from pygame.locals import *
from constants import *
  
pygame.init()
 

fps_clock = pygame.time.Clock()
 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
 
# Game loop
while True:
  screen.fill(WHITE)
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # Update
  
  # Draw
  
  pygame.display.flip()
  fps_clock.tick(FPS)