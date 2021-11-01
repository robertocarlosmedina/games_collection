__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from src.font import Game_fonts as fonts
from src.buttons import verticalButtonsDisplay

class Game_menu:

    screen :pygame.Surface
    screen_size :tuple
    game_buttons :list

    def __init__(self, screen, screen_size) -> None:
        self.screen = screen
        self.screen_size = screen_size
        self.game_buttons = ["New Game", "Continue"]
        self.current_button = self.game_buttons[0]

    def run_link(self, game_events :pygame.event) -> str:
        mouse_pos = pygame.mouse.get_pos()

        self.current_button = verticalButtonsDisplay(
            screen = self.screen,
            buttons = self.game_buttons,
            start_position = {
                "x":100,
                "y":150
            },
            box_dim = {
                "x":220,
                "y":50
            },
            mouse_pos = mouse_pos,
            font = fonts.montserrat_normal_font.value
        )
        return "game_menu"