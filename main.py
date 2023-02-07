import pygame
import numpy as np
import sys
from pygame.locals import *
from constants import *
from board import Board
  
pygame.init()
 

fps_clock = pygame.time.Clock()
 

screen = pygame.display.set_mode((WIDTH + SIDE_BAR, HEIGHT))

# Game loop
while True:
  screen.fill(WHITE)
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # Update
  board = Board(screen)
  # Draw
  
  pygame.display.flip()
  fps_clock.tick(FPS)