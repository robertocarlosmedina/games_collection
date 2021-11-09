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
from src.support.colors import Game_color as color


class Food:

    screen :pygame.Surface
    table_size_position :dict
    food_position :list
    possible_food_positions :list
    snake_step : int
    food_rect :pygame.Rect

    def __init__(self, screen :pygame.Surface, table_size_position :dict, snake_step :int, snake_positions :list) -> None:
        self.screen = screen
        self.table_size_position = table_size_position
        self.snake_step = snake_step
        self.possible_food_positions = []
        self.snake_positions = snake_positions
        self.food_rect = None
        self.all_possible_position = []
        self.start_variables()
        self.calculate_possible_food_positions()
        self.generate_new_food(snake_positions)
        
        
    def start_variables(self) -> None:
        self.all_possible_position = [
            (pos_x, pos_y) 
            for pos_x in range(
                int(self.table_size_position["x_position"]), 
                int(self.table_size_position["x_position"]+self.table_size_position["widht"]), 
                self.snake_step
            ) for pos_y in range(
                    int(self.table_size_position["y_position"]), 
                    int(self.table_size_position["y_position"]+self.table_size_position["height"]), 
                    int(self.snake_step)
            )
        ]

    def calculate_possible_food_positions(self) -> None:
        self.possible_food_positions = []
        snakes_parts_positions = [(pos.x-1, pos.y-1) for pos in self.snake_positions]
        for pos in self.all_possible_position:
            for snake_pos in snakes_parts_positions:
                if (pos != snake_pos):
                    self.possible_food_positions.append(pos)                

    def generate_new_food(self, snake_parts_rects :int) -> None:
        self.snake_positions = snake_parts_rects
        self.calculate_possible_food_positions()
        random_pos = choice(self.possible_food_positions)
        self.food_position = [random_pos[0]+8, random_pos[1]+8]
    
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
