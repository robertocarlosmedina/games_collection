__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from src.support.colors import Game_color as color

class Snake_part:
    part_position :dict
    screen :pygame.Surface
    part_rect :pygame.Rect
    part_color :tuple
    snake_size :int

    def __init__(self, screen :pygame.Surface, position: dict, snake_size :int, part_color=color.green.value) -> None:
        self.screen = screen
        self.part_position = position
        self.part_rect = None
        self.part_color = part_color
        self.snake_size = snake_size
    
    def get_part_position(self) -> dict:
        return self.part_position

    def update_position(self, new_position :dict) -> None:
        self.part_position = new_position
    
    def get_part_rect(self) -> pygame.Rect:
        return self.part_rect

    def draw_part(self) -> None:
        self.part_rect = pygame.Rect(
            self.part_position["x"],
            self.part_position["y"], 
            self.snake_size,self.snake_size
        )

        pygame.draw.rect(
            self.screen, 
            self.part_color, 
            self.part_rect
        )
