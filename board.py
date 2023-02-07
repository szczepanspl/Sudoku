import pygame
from constants import *
import numpy
from random import randint
from pprint import pprint

class Board:
    
    def __init__(self, screen) -> None:
        self.screen = screen
        self.game_array = [[],[],[],
                        [],[],[],
                        [],[],[]]  
        self.create_game_array()

    
    def create_game_array(self):
        # Creating instance of Field class and appending to game_array list
        for i in range(ROWS):
            for j in range(COLS):
                field = Field(self.screen, (i, j))
                self.game_array[i].append(field)


    def draw_tile(self, coordinates:tuple, color:tuple, thickness:int):
        rect = (coordinates[0] * SQUARE, coordinates[1] * SQUARE, SQUARE, SQUARE)
        pygame.draw.rect(self.screen, color, rect, thickness)


    def draw_board(self):
        # Drawing squares
        for i in range(ROWS):
            for j in range(COLS):
                # Drawing a tile
                self.draw_tile((i, j), BLACK, 1)
                # Drawing vertical thick lines
                if i % 3 == 0:
                    pygame.draw.line(self.screen, BLACK, (i * SQUARE, 0), (i * SQUARE, HEIGHT), 7)
                # Drawing horizontal thick lines
                if j % 3 == 0:
                    pygame.draw.line(self.screen, BLACK, (0, j * SQUARE), (WIDTH, j * SQUARE), 7)


    def fill_tile(self, position:tuple, number:int):
        field = self.game_array[position[0]][position[1]]
        field.value = number
        font = pygame.font.Font(None, 72)
        text = font.render(f"{field.value}", True, (0, 0, 0))
        self.screen.blit(text, (position[0] * SQUARE + SQUARE // 3, position[1] * SQUARE + SQUARE // 3))
        

    def fill_board(self):
        # Minimum clues == 17
        for i in range(18):
            random_field = self.game_array[randint(0, 8)][randint(0, 8)]
            if random_field.value == 0:
                self.fill_tile(random_field.position, randint(1, 9))


    def mark_tile(self, coordinates:tuple):
        self.draw_tile(coordinates, RED, 3)
        

class Field:
    def __init__(self, screen, position:tuple) -> None:
        self.screen = screen
        self.clicked = False
        self.value = 0
        self.position = position

    def __repr__(self) -> str:
        return f"Field_{self.value}{self.position}"