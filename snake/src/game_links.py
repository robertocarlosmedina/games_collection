__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from src.game import Game_loop
from src.start import Game_start
from src.menu import Game_menu
from src.quit import Game_quit
from src.tutorial import Game_Turorial 
from src.continue_game import Game_Continue

def start_game(screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
    obje = Game_start(screen, screen_size)
    return obje.run_link(game_event)

def game_main_menu(screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
    obje = Game_menu(screen, screen_size)
    return obje.run_link(game_event)

def continue_game(screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
    obje = Game_Continue(screen, screen_size)
    return obje.run_link(game_event)

def gameplay_loop(screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
    obje = Game_loop(screen, screen_size)
    return obje.run_link(game_event)

def game_tutorial(screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
    obje = Game_Turorial(screen, screen_size)
    return obje.run_link(game_event)

def game_quit(screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
    obje = Game_quit(screen, screen_size)
    return obje.run_link(game_event)
