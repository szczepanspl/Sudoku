import pygame
import numpy as np
import sys
from pygame.locals import *
from constants import *
from board import Board
  
pygame.init()
 
# Initializing the clock
fps_clock = pygame.time.Clock()

# Screen setup
screen = pygame.display.set_mode((WIDTH + SIDE_BAR, HEIGHT))
screen.fill(WHITE)

# Initializing Board class
board = Board(screen)
board.fill_board()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x_cor = mouse_x // SQUARE
            y_cor = mouse_y // SQUARE
            board.game_array[x_cor][y_cor].clicked = True
            board.mark_tile((x_cor, y_cor))
        if event.type == pygame.KEYDOWN:
            for fields in board.game_array:
                for field in fields:
                    if field.clicked and field.value == 0:
                        if 48 <= event.key <= 57:
                            number = int(event.key) - 48
                            board.fill_tile(field.position, number)
                        



 
    
    
    board.draw_board()

    pygame.display.update()
    fps_clock.tick(FPS)
