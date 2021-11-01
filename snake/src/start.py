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

class Game_start:
    def __init__(self, screen, screen_size) -> None:
        self.screen = screen
        self.screen_size = screen_size

    def run_link(self) -> str:
        pygame.draw.rect(self.screen, color.blue.value, pygame.Rect(20, 21, 30, 30))
        return "game_start"