__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.5"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from pygame.constants import NOEVENT
from src.support.font import Game_fonts as fonts
from src.support.colors import Game_color as color
from src.support.buttons import verticalButtonsDisplay
from src.support.auxiliar_functions import draw_header_styled_lines, \
    display_game_snake_info, read_from_file, get_screen_text

class Game_Credits:

    screen :pygame.Surface
    screen_size :tuple
    game_buttons :list
    button_clicked :str
    mouse_position :tuple
    menu_tittles :dict
    menus_start_positions :dict
    buttons_size :dict

    def __init__(self, screen, screen_size) -> None:
        self.screen = screen
        self.screen_size = screen_size
        self.button_clicked = ""
        self.game_buttons = {
            "game_menu": "Main Menu",
        }
        self.buttons_size = {
            "x":220,
            "y":50
        }
        self.menus_start_positions = {
            "game_menu":{
                "x": int(self.screen_size[0]/2 - self.buttons_size["x"]/2),
                "y":190
            }
        }
    
    def credits_content(self) -> None:

        font_size = pygame.font.Font.size(fonts.montserrat_size_22.value, get_screen_text("game_lost_text"))
        line = fonts.montserrat_size_22.value.render(get_screen_text("game_lost_text"), True, color.red.value)
        self.screen.blit(
            line, 
            (self.menus_start_positions["game_menu"]["x"]-(font_size[0]/2)+(self.buttons_size["x"]/2),
                self.menus_start_positions["game_menu"]["y"]-font_size[1]*2)
        )

    def run_link(self, game_events :pygame.event) -> str:
        del game_events
        self.mouse_pos = pygame.mouse.get_pos()

        font_size = pygame.font.Font.size(fonts.montserrat_size_30.value, get_screen_text("game_tittle"))
        line = fonts.montserrat_size_30.value.render(get_screen_text("game_tittle"), True, color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-(font_size[0]/2), 25))

        self.credits_content()
        
        if (self.button_clicked != "" ):
            for key,value in self.game_buttons.items():
                if(self.button_clicked == value):
                    self.button_clicked = ""
                    return key
        
        return "game_credits"
        