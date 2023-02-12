import pygame
import sys
from pygame.locals import *
from constants import *
from board import Board
from setup import Setup
 
pygame.init()
# Initializing the clock
fps_clock = pygame.time.Clock()
 
def setup():
    """setup function responsible for gathering data from the user about difficulty level and explaining basic keywords"""

    # Screen setup
    setup_screen = pygame.display.set_mode((SETUP_WIDTH, SETUP_HEIGHT))

    # Setup class
    setup = Setup(setup_screen)
    
    done = False
    # Setup loop
    while not done:
        for event in pygame.event.get():
            # Handling quit
            if event.type == QUIT:
                done = True
                # pygame.quit()
                # sys.exit()
            # Handling mouse coordinates
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                x_cor = mouse_x // SQUARE
                y_cor = mouse_y // SQUARE
        
        # Reseting the screen                    
        setup_screen.fill(WHITE)

        # Updating and fps settings
        pygame.display.update()
        fps_clock.tick(FPS)
     

def main():
    """Main function responsible for handling all game mechanics using Board class"""
    
    # Screen setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Initializing Board class
    board = Board(screen)
    board.start_game(1)

    # Game loop
    while True:
        for event in pygame.event.get():
            # Handling quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Handling mouse events
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                x_cor = mouse_x // SQUARE
                y_cor = mouse_y // SQUARE
                # Marking tile on left click button
                if event.button == 1:
                    try:
                        board.game_array[x_cor][y_cor].clicked = True
                    except IndexError:
                        continue
                # Clearing tile on right click button
                elif event.button == 3:
                    board.clear_tile((x_cor, y_cor))
            # Handling user's number input on key press         
            if event.type == pygame.KEYDOWN:
                for fields in board.game_array:
                    for field in fields:
                        if field.clicked and field.value == 0:
                            if 49 <= event.key <= 57:
                                number = int(event.key) - 48
                                board.fill_tile(field.position, number)
                # Automatically solve the board on space key press
                if event.key == K_SPACE:
                    board.solve()
        
        # Reseting screen and updating the board                    
        screen.fill(WHITE)
        board.update_board()

        # Updating the game and fps settings
        pygame.display.update()
        fps_clock.tick(FPS)

# Calling functions
setup()
main()