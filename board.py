import pygame
from constants import *
from random import randint
from pprint import pprint


class Board:
    """Class Board that basically manage the game board and individual fields. 
    It's responsible for drawing board, marking fields and all basic mechanics"""
    def __init__(self, screen) -> None:
        self.screen = screen
        self.game_array = [[Field(self.screen, (j, i)) for i in range(COL)] for j in range(ROW)]
        self.randomize_board(10)
        
     
    def draw_tile(self, coordinates:tuple, color:tuple, thickness:int):
        """Tile drawing method, takes coordinates, color and thickness of rectangle"""
        rect = (coordinates[0] * SQUARE, coordinates[1] * SQUARE, SQUARE, SQUARE)
        pygame.draw.rect(self.screen, color, rect, thickness)
     
     # Function that takes position and number of field and fills it with text
    def fill_tile(self, position:tuple, number:int):
        field = self.game_array[position[0]][position[1]]
        field.value = number
        font = pygame.font.Font(None, 72)
        text = font.render(f"{field.value}", True, BLACK)
        self.screen.blit(text, (position[0] * SQUARE + SQUARE // 3, position[1] * SQUARE + SQUARE // 3))

    
    def clear_tile(self, position:tuple):
        self.game_array[position[0]][position[1]].value = 0           


    def draw_board(self):
        # Drawing squares
        for rows in self.game_array:
            for field in rows:
                if field.clicked and field.value == 0:
                    self.draw_tile((field.position[0], field.position[1]), BLACK, 1)
                    self.draw_tile((field.position[0], field.position[1]), RED, 4)
                else:
                    self.draw_tile((field.position[0], field.position[1]), BLACK, 1)
                # Drawing vertical thick lines
                if field.position[0] % 3 == 0:
                    pygame.draw.line(self.screen, BLACK, (field.position[0] * SQUARE, 0), (field.position[0] * SQUARE, HEIGHT), 7)
                # Drawing horizontal thick lines
                if field.position[1] % 3 == 0:
                    pygame.draw.line(self.screen, BLACK, (0, field.position[1] * SQUARE), (WIDTH, field.position[1] * SQUARE), 7)


    # Filling game array
    def fill_board(self):
        for rows in self.game_array:
            for field in rows:
                if field.value != 0:
                    self.fill_tile(field.position, field.value)


    def update_board(self):
        """Game updating method (drawing and filling the board)"""
        self.draw_board()
        self.fill_board()
        
        
    # Temporary method just to check if everything works
    def randomize_board(self, num_of_fields):
        placed_values = 0
        while placed_values < num_of_fields:
            random_value = randint(1, 9)
            random_field = self.game_array[randint(0, 8)][randint(0, 8)]
            if self.is_possible(random_field.position[0], random_field.position[1], random_value) and random_field.value == 0:
                random_field.value = random_value
                placed_values += 1
                
        
    def is_possible(self, row, col, n) -> bool:
        values_grid = [[field.value for field in rows] for rows in self.game_array]
        # Check if not in row
        not_in_row = n not in values_grid[row]
        # Check if not in column
        not_in_col = n not in [values_grid[i][col] for i in range(9)]
        # Check if not in smaller box
        not_in_box = n not in [values_grid[i][j] for i in range(row//3*3, row//3*3 + 3) for j in range(col//3*3, col//3*3 + 3)]
        return not_in_row and not_in_col and not_in_box
        
        
    def solve(self, row=0, column=0):
        if row == 9:
            return True
        elif column == 9:
            return self.solve(row + 1, 0)
        elif self.game_array[row][column].value != 0:
            return self.solve(row, column + 1)
        else:
            for n in range(1, 10):
                if self.is_possible(row, column, n):
                    self.game_array[row][column].value = n
                    if self.solve(row, column + 1):
                        return True
                    self.game_array[row][column].value = 0
            return False
        
        
    
    def is_solved(self) -> bool:
        all_values = [tile.value
                      for rows in self.game_array
                      for tile in rows]
        if 0 in all_values:
            return False
        return True
                            

     

class Field:
    """ Class Field with screen and position as input, used in Board class to manage single field properly"""
    def __init__(self, screen, position:tuple) -> None:
        # TODO.2 AFTER GETTING PROPER VALUES IN FIELDS INSTEAD OF RANDOM VALUES, GIVE A FIELD CLASS VARIABLE CORE_POSITION TO PREVENT FROM CHANGING CORE VALUES
        self.screen = screen
        self.clicked = False
        self.value = 0
        self.position = position

    
    def __repr__(self) -> str:
        return f"Field_{self.value}{self.position}"



    

                
               
                
    