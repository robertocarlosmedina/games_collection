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


class Disk:
    def __init__(self, game_obj: object) -> None:
        self.game_object = game_obj

    def draw_disk_animation(self, x_pos: int, y_end: int,  draw_board, draw_disk, page_tittle, scale: int, size: int) -> None:
        """
            The main goal here is to make the animation on a loop an then when it finish continue to the game.
        """
        y = -10
        while True:
            self.game_object.screen_fill_bg()
            draw_board() 
            draw_disk()
            page_tittle()

            pygame.draw.rect(
                self.game_object.screen, 
                color.brown.value, pygame.Rect(
                    x_pos[0] - (size*scale)/2, 
                    y, 
                    size * scale, 
                    20
                ), 
                border_radius = 3,
            )
            y += .7
            if y >= y_end:
                break          

            pygame.display.update()
