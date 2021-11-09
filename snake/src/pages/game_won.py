__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
import os
from src.support.font import Game_fonts as fonts
from src.support.colors import Game_color as color
from src.support.buttons import verticalButtonsDisplay
from src.support.auxiliar_functions import draw_header_styled_lines, \
    display_game_snake_info, read_from_file, get_screen_text

class Game_won:

    screen :pygame.Surface
    screen_size :tuple
    game_buttons :list
    button_clicked :str
    mouse_position :tuple
    menu_tittles :dict
    menus_start_positions :dict
    buttons_size :dict
    game_data :list

    def __init__(self, screen, screen_size) -> None:
        self.screen = screen
        self.screen_size = screen_size
        self.button_clicked = ""
        self.game_data = read_from_file("data/end_game_values.txt", "r", True)[0].split(" ")
        self.game_buttons = {
            "game_loop": "New Game",
            "game_menu": "Main Menu",
            "game_quit":"Quit"
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
    
    def pause_menu_buttons(self) -> None:
        font_size = pygame.font.Font.size(fonts.montserrat_size_22.value, get_screen_text("game_won_text"))
        line = fonts.montserrat_size_22.value.render(get_screen_text("game_won_text"), True, color.green_1.value)
        self.screen.blit(
            line, 
            (self.menus_start_positions["game_menu"]["x"]-(font_size[0]/2)+(self.buttons_size["x"]/2),
                self.menus_start_positions["game_menu"]["y"]-font_size[1]*2)
        )

        self.button_clicked = verticalButtonsDisplay(
            screen = self.screen,
            buttons = self.game_buttons.values(),
            start_position = {
                "x":self.menus_start_positions["game_menu"]["x"],
                "y":self.menus_start_positions["game_menu"]["y"]
            },
            box_dim = self.buttons_size,
            mouse_pos = self.mouse_pos,
            font = fonts.montserrat_size_16.value,
            button_clicked = self.button_clicked
        )

    def run_link(self, game_events :pygame.event) -> str:
        del game_events
        self.mouse_pos = pygame.mouse.get_pos()

        font_size = pygame.font.Font.size(fonts.montserrat_size_30.value, get_screen_text("game_tittle"))
        line = fonts.montserrat_size_30.value.render(get_screen_text("game_tittle"), True, color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-(font_size[0]/2), 25))

        draw_header_styled_lines(self.screen, self.screen_size)

        display_game_snake_info(screen = self.screen, info_name = "Foods", value = self.game_data[0], 
            position = {"x":self.menus_start_positions["game_menu"]["x"] + 250, "y":225})

        display_game_snake_info(screen = self.screen, info_name = "Movements", value = self.game_data[1], 
            position = {"x":self.menus_start_positions["game_menu"]["x"] - 130, "y":225})

        self.pause_menu_buttons()
        
        if (self.button_clicked != "" ):
            for key,value in self.game_buttons.items():
                if(self.button_clicked == value):
                    self.button_clicked = ""
                    return key
        
        return "game_won"