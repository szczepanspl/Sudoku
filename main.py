import pygame
import sys
from pygame.locals import *
from constants import *
from board import Board
from pprint import pprint
  
pygame.init()
 
# Initializing the clock
fps_clock = pygame.time.Clock()

# Screen setup
screen = pygame.display.set_mode((WIDTH + SIDE_BAR, HEIGHT))


# Initializing Board class
board = Board(screen)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pprint(board.game_array)
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x_cor = mouse_x // SQUARE
            y_cor = mouse_y // SQUARE
            # Marking tile on left click button
            if event.button == 1:
                try:
                    # TODO.1 FIX THE BUG WITH CLEANING FIELD AND MARKING THE FIELD
                    board.game_array[x_cor][y_cor].clicked = True
                    print(board.game_array[y_cor][x_cor])
                except IndexError:
                    continue
            # Clearing tile on right click button
            elif event.button == 3:
                board.clear_tile((x_cor, y_cor))
                print(board.game_array[x_cor][y_cor])
        # Handling user's number input on key press         
        if event.type == pygame.KEYDOWN:
            for fields in board.game_array:
                for field in fields:
                    if field.clicked and field.value == 0:
                        if 49 <= event.key <= 57:
                            number = int(event.key) - 48
                            board.fill_tile(field.position, number)
            if event.key == K_SPACE:
                board.solve()
                        


 
 
    
    screen.fill(WHITE)
    board.update_board()


    pygame.display.update()
    fps_clock.tick(FPS)
