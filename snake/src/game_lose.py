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

class Game_Lose:

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
            "new_game": "New Game",
            "game_menu": "Main Menu",
            "game_quit":"Quit"
        }

        self.menu_tittles = {
            "game_tittle": "Snake Game",
            "game_menu_tittle": "Game Menu",
            "self_play_menu": "Watch Snake Play"
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
        
    
    def draw_styled_lines(self) -> None:
        pygame.draw.line(
            self.screen, 
            color.green.value,
            (self.screen_size[0]/2 - 190, 100), 
            (self.screen_size[0]/2 + 190, 100), 
            3
        )
        pygame.draw.line(
            self.screen, 
            color.grey.value,
            (self.screen_size[0]/2 - 180, 95), 
            (self.screen_size[0]/2 + 180, 95),  
        )
        pygame.draw.line(
            self.screen, 
            color.grey.value,
            (self.screen_size[0]/2 - 180, 105), 
            (self.screen_size[0]/2 + 180, 105), 
            1
        )
    
    def pause_menu_buttons(self) -> None:

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

    def run_link(self, game_events :pygame.event) -> str:
        del game_events
        self.mouse_pos = pygame.mouse.get_pos()

        font_size = pygame.font.Font.size(fonts.montserrat_big_font.value, self.menu_tittles["game_tittle"])
        line = fonts.montserrat_big_font.value.render(self.menu_tittles["game_tittle"], True, color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-(font_size[0]/2), 25))

        self.draw_styled_lines()

        self.pause_menu_buttons()
        
        if (self.button_clicked != "" ):
            for key,value in self.game_buttons.items():
                if(self.button_clicked == value):
                    self.button_clicked = ""
                    return key
        
        return "game_lose"
        