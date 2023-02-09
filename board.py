import pygame
from constants import *
from random import randint
from pprint import pprint
from collections import deque

class Board:
    """Class Board that basically manage the game board and individual fields. 
    It's responsible for drawing board, marking fields and all basic mechanics"""
    def __init__(self, screen) -> None:
        self.screen = screen
        self.game_array = [[],[],[],
                        [],[],[],
                        [],[],[]]  
        self.create_game_array()
        self.randomize_board()


    def update_board(self):
        """Game updating method (drawing and filling the board)"""
        self.draw_board()
        self.fill_board()
    
    def clear_field(self, position:tuple):
        self.game_array[position[0]][position[1]].value = 0
        
        
    def create_game_array(self):
        """Creating instance of Field class and appending to game_array list"""
        for i in range(ROWS):
            for j in range(COLS):
                field = Field(self.screen, (i, j))
                self.game_array[i].append(field)


    def draw_tile(self, coordinates:tuple, color:tuple, thickness:int):
        """Tile drawing method, takes coordinates, color and thickness of rectangle"""
        rect = (coordinates[0] * SQUARE, coordinates[1] * SQUARE, SQUARE, SQUARE)
        pygame.draw.rect(self.screen, color, rect, thickness)
            

    def draw_board(self):
        # Drawing squares
        for i in range(ROWS):
            for j in range(COLS):
                # Drawing a tile
                if self.game_array[i][j].clicked and self.game_array[i][j].value == 0:
                    self.draw_tile((i, j), BLACK, 1)
                    self.draw_tile((i, j), RED, 4)
                else:
                    self.draw_tile((i, j), BLACK, 1)
                # Drawing vertical thick lines
                if i % 3 == 0:
                    pygame.draw.line(self.screen, BLACK, (i * SQUARE, 0), (i * SQUARE, HEIGHT), 7)
                # Drawing horizontal thick lines
                if j % 3 == 0:
                    pygame.draw.line(self.screen, BLACK, (0, j * SQUARE), (WIDTH, j * SQUARE), 7)

    # Function that takes position and number of field and fills it with text
    def fill_tile(self, position:tuple, number:int):
        field = self.game_array[position[0]][position[1]]
        field.value = number
        font = pygame.font.Font(None, 72)
        text = font.render(f"{field.value}", True, (0, 0, 0))
        self.screen.blit(text, (position[0] * SQUARE + SQUARE // 3, position[1] * SQUARE + SQUARE // 3))
        
    # Filling game array
    def fill_board(self):
        for row in self.game_array:
            for field in row:
                if field.value != 0:
                    self.fill_tile(field.position, field.value)

    # Temporary method just to check if everything works
    def randomize_board(self):
        # Minimum clues == 17
        for i in range(18):
            random_field = self.game_array[randint(0, 8)][randint(0, 8)]
            if random_field.value == 0:
                random_field.value = randint(1, 9)

     

class Field:
    """ Class Field with screen and position as input, used in Board class to manage single field properly"""
    def __init__(self, screen, position:tuple) -> None:
        self.screen = screen
        self.clicked = False
        self.value = 0
        self.position = position

    
    def __repr__(self) -> str:
        return f"Field_{self.value}{self.position}"

