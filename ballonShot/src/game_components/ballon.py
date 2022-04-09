__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.1.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
    This class if just to control the animation of the disk.
"""

import pygame
from src.support.colors import Game_color as color


class Ballon:
    def __init__(self, game_obj: object) -> None:
        self.game_object = game_obj

    def draw_disk_animation(self) -> None:
        """
            The main goal here is to make the animation on a loop an then when it finish continue to the game.
        """
        
    def move(self) -> None:
        pass
