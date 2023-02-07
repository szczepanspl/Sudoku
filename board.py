import pygame
from constants import *
import numpy
import random

class Board:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.game_array = [[],[],[],
                        [],[],[],
                        [],[],[]]  
        self.draw_board()
        print(self.game_array)

    
    def draw_board(self):
        # Drawing squares
        for i in range(ROWS):
            for j in range(COLS):
                # Creating instance of Field class and appending to game_array list
                field = Field(self.screen, (i, j))
                self.game_array[i].append(field)
                # Establishing rect size and drawing it
                rect = (i * SQUARE, j * SQUARE, SQUARE, SQUARE)
                pygame.draw.rect(self.screen, BLACK, rect, 1)
                # Drawing vertical thick lines
                if i % 3 == 0:
                    pygame.draw.line(self.screen, BLACK, (i * SQUARE, 0), (i * SQUARE, HEIGHT), 7)
                # Drawing horizontal thick lines
                if j % 3 == 0:
                    pygame.draw.line(self.screen, BLACK, (0, j * SQUARE), (WIDTH, j * SQUARE), 7)

    def fill_board(self):
        # Minimum clues == 17
        for i in range(17):
            pass
        

class Field:
    def __init__(self, screen, position:tuple) -> None:
        self.screen = screen
        self.clicked = False
        self.filled = False
        self.value = 0
        self.position = position
        self.is_filled()

    def is_filled(self):
        if self.value != 0:
            self.filled = True

    def __repr__(self) -> str:
        return f"Field_{self.value}{self.position}"