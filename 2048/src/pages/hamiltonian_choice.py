__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from src.game_components.game import Game_loop
from src.support.font import Game_fonts as fonts
from src.support.colors import Game_color as color
from src.support.buttons import verticalButtonsDisplay
from src.support.auxiliar_functions import draw_header_styled_lines, get_screen_text

class Hamiltonian_Choice:

    screen :pygame.Surface
    screen_size :tuple
    game_buttons :list
    button_clicked :str
    mouse_position :tuple
    menu_tittles :dict
    menus_start_positions :dict
    buttons_size :dict
    on_game_play :bool
    game_object :object

    def __init__(self, screen, screen_size) -> None:
        self.screen = screen
        self.screen_size = screen_size
        self.button_clicked = ""
        self.on_game_play = False
        self.game_buttons = {
            "hamiltonian_horizontal": "Horizontal", 
            # "hamiltonian_vertical":"Vertical", 
            # "hamiltonian_spiral":"Spiral", 
            "game_menu":"Main Menu"
        }
        self.buttons_size = {
            "x":220,
            "y":50
        }
        self.menu_start_positions = {
            "x":int(self.screen_size[0]/2 - self.buttons_size["x"]/2),
            "y":190
        }
        
    
    def menu_buttons(self) -> None:

        font_size = pygame.font.Font.size(fonts.montserrat_size_22.value, get_screen_text("hamiltonian_choice_text"))
        line = fonts.montserrat_size_22.value.render(get_screen_text("hamiltonian_choice_text"), True, color.green_1.value)
        self.screen.blit(
            line, 
            (self.menu_start_positions["x"]-(font_size[0]/2)+(self.buttons_size["x"]/2),
                self.menu_start_positions["y"]-font_size[1]*2)
        )

        self.button_clicked = verticalButtonsDisplay(
            screen = self.screen,
            buttons = self.game_buttons.values(),
            start_position = {
                "x":self.menu_start_positions["x"],
                "y":self.menu_start_positions["y"]
            },
            box_dim = self.buttons_size,
            mouse_pos = self.mouse_pos,
            font = fonts.montserrat_size_16.value,
            button_clicked = self.button_clicked
        )

    def run_link(self, game_events :pygame.event) -> str:
        self.mouse_pos = pygame.mouse.get_pos()

        if(not self.on_game_play):
            font_size = pygame.font.Font.size(fonts.montserrat_size_30.value, get_screen_text("game_tittle"))
            line = fonts.montserrat_size_30.value.render(get_screen_text("game_tittle"), True, color.white.value)
            self.screen.blit(line, (self.screen_size[0]/2-(font_size[0]/2), 25))

            draw_header_styled_lines(self.screen, self.screen_size)
            self.menu_buttons()
        
        if (self.button_clicked != "" ):
            for key,value in self.game_buttons.items():
                if(self.button_clicked == value):
                    if(not self.on_game_play):
                        self.game_object = Game_loop(screen = self.screen, screen_size = self.screen_size, algorithm = key)
                        self.on_game_play = True

                    if(self.on_game_play):
                        go_to = self.game_object.run_link(game_events)
                        if (go_to == "game_won"):
                            return go_to
                        # return go_to
        
        return "game_self_play_hamiltoniano"
        