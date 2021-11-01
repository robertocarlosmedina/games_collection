__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from src.colors import Game_color as color

class Snake_part:
    part_position :dict
    screen :pygame.Surface
    part_rect :pygame.Rect

    def __init__(self, screen :pygame.Surface, position: dict) -> None:
        self.screen = screen
        self.part_position = position
        self.part_rect = None
    
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
            14,14
        )

        pygame.draw.rect(
            self.screen, 
            color.green.value, 
            self.part_rect
        )
