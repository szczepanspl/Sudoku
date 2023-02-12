import pygame
from constants import *
from random import randint
from pprint import pprint


class Board:
    """Class Board that basically manage the game board and individual fields. 
    It's responsible for drawing board, marking fields and all basic mechanics
    """
    def __init__(self, screen) -> None:
        """init method

        Args:
            screen (Surface): screen to operate on
        """
        self.screen = screen
        self.game_array = [[Field(self.screen, (j, i)) for i in range(COL)] for j in range(ROW)]
        
        
    def draw_tile(self, coordinates:tuple, color:tuple, thickness:int):
        """tile drawing method

        Args:
            coordinates (tuple): coordinates of block to draw
            color (tuple): color of the block, black if normal block, red if marked
            thickness (int): thickness of block, 1 if normal block, 4 if marked block
        """
        rect = (coordinates[0] * SQUARE, coordinates[1] * SQUARE, SQUARE, SQUARE)
        pygame.draw.rect(self.screen, color, rect, thickness)
     

    def fill_tile(self, position:tuple, number:int):
        """Method that takes position and number of field and fills it with text
        
        Args:
            position (tuple): position of the field
            number (int): value of the field to be added
        """
        field = self.game_array[position[0]][position[1]]
        field.value = number
        font = pygame.font.Font(None, 72)
        text = font.render(f"{field.value}", True, BLACK)
        self.screen.blit(text, (position[0] * SQUARE + SQUARE // 3, position[1] * SQUARE + SQUARE // 3))

    
    def clear_tile(self, position:tuple):
        """Method responsible for clearing field that is setting it's value to 0
        
        Args:
            position (tuple): position of the field to clear it's value
        """
        self.game_array[position[0]][position[1]].value = 0           


    def draw_board(self):
        """Drawing board method, handles tiles as well as vertical and horizontal lines on the board"""
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


    def fill_board(self):
        """Method responsible for filling game array"""
        for rows in self.game_array:
            for field in rows:
                if field.value != 0:
                    self.fill_tile(field.position, field.value)


    def update_board(self):
        """Game updating method (drawing and filling the board)"""
        self.draw_board()
        self.fill_board()
        
        
    def sample_board(self, num_of_fields:int, delete=False):
        """Method that samples (or delete form) board

        Args:
            num_of_fields (int): number of fields to be field with random values. 5 to 10 works best
            delete (bool, optional): If true then it delete values instead of putting them. Defaults to False:bool.
        """
        if not delete:
            placed_values = 0
            while placed_values <= num_of_fields:
                random_value = randint(1, 9)
                random_field = self.game_array[randint(0, 8)][randint(0, 8)]
                if self.is_possible(random_field.position[0], random_field.position[1], random_value) and random_field.value == 0:
                    random_field.value = random_value
                    placed_values += 1
        else:
            deleted_values = 0
            while deleted_values <= num_of_fields:
                random_field = self.game_array[randint(0, 8)][randint(0, 8)]
                if random_field.value != 0:
                    random_field.value = 0
                    deleted_values += 1            
            
        
    def is_possible(self, row:int, col:int, n:int) -> bool:
        """Method that checks if putting certain number (n) on some field is valid - it means that there is no same value across row, column and smaller box
        
        Args:
            row (int): row of field that need to be checked
            col (int): column of field that need to be checked
            n (int): number for check if it is valid to put on the board
        
        Returns:
            bool: returns True if is valid to put, False when not
        """
        values_grid = [[field.value for field in rows] for rows in self.game_array]
        # Check if not in row
        not_in_row = n not in values_grid[row]
        # Check if not in column
        not_in_col = n not in [values_grid[i][col] for i in range(9)]
        # Check if not in smaller box
        not_in_box = n not in [values_grid[i][j] for i in range(row//3*3, row//3*3 + 3) for j in range(col//3*3, col//3*3 + 3)]
        return not_in_row and not_in_col and not_in_box
        
        
    def solve(self, row=0, column=0) -> bool:
        """solving method using backtracking algorithm and recursion to solve all board

        Args:
            row (int, optional): Incremented by recursion. Defaults to 0.
            column (int, optional): Incremented by recursion. Defaults to 0.

        Returns:
            bool: returns True if done, return False if not
        """
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
        
    
    def start_game(self, level:int):
        """Starting method game, depends on level chosen by player in setup menu

        Args:
            level (int): Range from 0 to 2. 0 is the easy mode, 1 is the medium mode, 2 is the hard mode
        """
        self.sample_board(8)
        self.solve()
        # Easy mode
        if level == 0:
            self.sample_board(30, delete=True)
        # Medium mode
        elif level == 1:
            self.sample_board(45, delete=True)
        # Hard mode
        elif level == 2:
            self.sample_board(60, delete=True)                     
            
                            
  
class Field:
    """ Class Field with screen and position as input, used in Board class to manage single field properly"""
    def __init__(self, screen, position:tuple) -> None:
        self.screen = screen
        self.clicked = False
        self.value = 0
        self.position = position

    
    def __repr__(self) -> str:
        return f"Field_{self.value}{self.position}"



    

                
               
                
    