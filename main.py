import pygame
import numpy as np
import sys
from pygame.locals import *
from constants import *
from board import Board
  
pygame.init()
 

fps_clock = pygame.time.Clock()
 

screen = pygame.display.set_mode((WIDTH + SIDE_BAR, HEIGHT))
screen.fill(WHITE)

board = Board(screen)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    
    
  # Update
 
  # Draw
  
    pygame.display.update()
    fps_clock.tick(FPS)
