__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from random import choice
from src.colors import Game_color as color


class Food:

    screen :pygame.Surface
    table_size_position :dict
    food_position :list
    possible_food_positions :list
    snake_step : int
    food_rect :pygame.Rect

    def __init__(self, screen :pygame.Surface, table_size_position :dict, snake_step :int) -> None:
        self.screen = screen
        self.table_size_position = table_size_position
        self.snake_step = snake_step
        self.possible_food_positions = [[],[]]
        self.calculate_food_positions()
        self.generate_new_food()
        self.food_rect = None

    def calculate_food_positions(self):
        for pos in range(
            int(self.table_size_position["x_position"]), 
            int(self.table_size_position["x_position"]+self.table_size_position["widht"]), 
            self.snake_step
        ):
            self.possible_food_positions[0].append(pos)
        
        for pos in range(
            int(self.table_size_position["y_position"]), 
            int(self.table_size_position["y_position"]+self.table_size_position["height"]), 
            int(self.snake_step)
        ):
            self.possible_food_positions[1].append(pos)

    def generate_new_food(self) -> None:
        x_position = choice(self.possible_food_positions[0]) + 8
        y_position = choice(self.possible_food_positions[1]) + 8
        self.food_position = [x_position, y_position]
    
    def get_food_rect(self) -> dict:
        return self.food_rect

    def draw_food(self) -> None:
        self.food_rect = pygame.Rect(
            self.food_position[0]-5,
            self.food_position[1]-5, 
            10,10
        )
        pygame.draw.rect(
            self.screen, 
            color.green.value, 
            self.food_rect
        )
        pygame.draw.circle(
            self.screen, 
            color.red.value, 
            (self.food_position[0], self.food_position[1]), 
            4
        )
