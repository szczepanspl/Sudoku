import pygame
from constants import *

class Board:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.board_array = [[],[],[],
                            [],[],[],
                            [],[],[]]
        self.draw_board()
        print(self.board_array)
    
    def draw_board(self):
        for i in range(ROWS):
            for j in range(COLS):
                rect = (i * SQUARE, j * SQUARE, SQUARE, SQUARE)
                field = pygame.draw.rect(self.screen, BLACK, rect, 1)
                self.board_array[i].append((field[0] // 100, field[1] // 100))
                if i % 3 == 0:
                    pygame.draw.line(self.screen, BLACK, (i * SQUARE, 0), (i * SQUARE, HEIGHT), 7)
                if j % 3 == 0:
                    pygame.draw.line(self.screen, BLACK, (0, j * SQUARE), (WIDTH, j * SQUARE), 7)

