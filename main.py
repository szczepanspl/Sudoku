import pygame
import sys
from pygame.locals import *
from constants import *
from board import Board
from tkinter import *
from tkinter import ttk

pygame.init()
# Initializing the clock
fps_clock = pygame.time.Clock()
 

def setup() -> int:
    """Setup menu with tkinter

    Returns:
        int: returns level selected by player
    """
    global selected_value
    selected_value = None
    
    def button_click(value):
        global selected_value
        selected_value = value
        root.quit()

    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Welcome in Sudoku Game!", font=("Arial", 16, "bold")).grid(column=0, row=0, columnspan=3)
    ttk.Label(frm, text="LMB - mark the tile").grid(column=0, row=1, columnspan=3)
    ttk.Label(frm, text="RMB - delete the tile").grid(column=0, row=2, columnspan=3)
    ttk.Label(frm, text="Keys 1-9: fill the tile").grid(column=0, row=3, columnspan=3)
    ttk.Label(frm, text="Space: Solve Sudoku").grid(column=0, row=3, columnspan=3)
    ttk.Label(frm, text="Please Choose your difficulty level").grid(column=0, row=4, columnspan=3)
    ttk.Button(frm, text="Easy mode", command=lambda: button_click(0)).grid(column=0, row=5)
    ttk.Button(frm, text="Medium mode", command=lambda: button_click(1)).grid(column=1, row=5)
    ttk.Button(frm, text="Hard mode", command=lambda: button_click(2)).grid(column=2, row=5)

    root.mainloop()
    root.destroy()
    
    return selected_value

        
def main(level):
    """Main function responsible for handling all game mechanics using Board class"""
    
    # Screen setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Initializing Board class
    board = Board(screen)
    board.start_game(level)

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
main(setup())