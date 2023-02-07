import pygame
from constants import *
import numpy

class Board:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.game_array = []
        for i in range(ROWS):
            self.game_array.append(numpy.zeros((9, 9)))
        self.draw_board()
    
    def draw_board(self):
        for i in range(ROWS):
            for j in range(COLS):
                rect = (i * SQUARE, j * SQUARE, SQUARE, SQUARE)
                pygame.draw.rect(self.screen, BLACK, rect, 1)
                if i % 3 == 0:
                    pygame.draw.line(self.screen, BLACK, (i * SQUARE, 0), (i * SQUARE, HEIGHT), 7)
                if j % 3 == 0:
                    pygame.draw.line(self.screen, BLACK, (0, j * SQUARE), (WIDTH, j * SQUARE), 7)
