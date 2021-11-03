__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from pygame.constants import NOEVENT
from src.font import Game_fonts as fonts
from src.colors import Game_color as color
from src.buttons import verticalButtonsDisplay
from src.auxiliar_functions import draw_vertical_styled_lines

class Game_menu:

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
            "game_loop": "New Game", 
            "game_continue":"Continue", 
            "game_tutorial":"Tutorial", 
            "game_quit":"Quit"
        }
        self.algorithms_buttons = {
            "hamiltonian_choice":"Hamiltonian cycle", 
            "ai_game_play":"Simple AI"
        }
        self.menu_tittles = {
            "game_tittle": "Snake Game",
            "game_menu_tittle": "Game Menu",
            "self_play_menu": "Watch Snake Play"
        }
        self.menus_start_positions = {
            "game_menu":{
                "x":80,
                "y":190
            },
            "self_play_menu":{
                "x":400,
                "y":190
            }
        }
        self.buttons_size = {
            "x":220,
            "y":50
        }
    
    def game_play_buttons(self) -> None:

        font_size = pygame.font.Font.size(fonts.montserrat_subbig_font.value, self.menu_tittles["game_menu_tittle"])
        line = fonts.montserrat_subbig_font.value.render(self.menu_tittles["game_menu_tittle"], True, color.green_1.value)
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
            font = fonts.montserrat_small_font.value,
            button_clicked = self.button_clicked
        )
    
    def snake_self_play_buttons(self) -> None:

        font_size = pygame.font.Font.size(fonts.montserrat_subbig_font.value, self.menu_tittles["self_play_menu"])
        line = fonts.montserrat_subbig_font.value.render(self.menu_tittles["self_play_menu"], True, color.green_1.value)
        self.screen.blit(
            line, 
            (self.menus_start_positions["self_play_menu"]["x"]-(font_size[0]/2)+(self.buttons_size["x"]/2),
                self.menus_start_positions["self_play_menu"]["y"]-font_size[1]*2)
        )

        self.button_clicked = verticalButtonsDisplay(
            screen = self.screen,
            buttons = self.algorithms_buttons.values(),
            start_position = {
                "x":self.menus_start_positions["self_play_menu"]["x"],
                "y":self.menus_start_positions["self_play_menu"]["y"]
            },
            box_dim = self.buttons_size,
            mouse_pos = self.mouse_pos,
            font = fonts.montserrat_small_font.value,
            button_clicked = self.button_clicked
        )

    def run_link(self, game_events :pygame.event) -> str:
        del game_events
        self.mouse_pos = pygame.mouse.get_pos()

        font_size = pygame.font.Font.size(fonts.montserrat_big_font.value, self.menu_tittles["game_tittle"])
        line = fonts.montserrat_big_font.value.render(self.menu_tittles["game_tittle"], True, color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-(font_size[0]/2), 25))

        draw_vertical_styled_lines(self.screen, self.screen_size)

        self.game_play_buttons()
        
        self.snake_self_play_buttons()

        if (self.button_clicked != "" ):
            for key,value in self.game_buttons.items():
                if(self.button_clicked == value):
                    self.button_clicked = ""
                    return key
        
        return "game_menu"
        