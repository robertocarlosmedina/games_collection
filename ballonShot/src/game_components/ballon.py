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
from random import randint, choice

from torch import seed
from src.support.colors import Game_color as color


class Ballon:
    def __init__(self, game_obj: object, speed) -> None:
        self.game_object = game_obj
        self.radius = randint(40, 80)
        self.oval_value = self.radius + randint(10, 20)
        self.position = None
        self.arrow = None
        self.y_move_pos = speed*-1
        self.x_move_pos = 0
        self.color = choice(
            [color.blue_1.value, color.red.value, color.green_1.value, color.yellow.value])
        self.start_ballon_config()

    def start_ballon_config(self) -> None:
        x_start_pos = randint(10, self.game_object.screen_size[0]-30)  # 20
        y_start_pos = randint(
            self.game_object.screen_size[1], self.game_object.screen_size[1]+10)  # 30 #10
        self.position = {"x": x_start_pos, "y": y_start_pos}
        self.arrow = ((50, 100), (100, 50), (150, 100))
        self.arrow1 = ((x_start_pos-self.radius, y_start_pos), (int(x_start_pos +
                       self.radius/2), y_start_pos+30), (x_start_pos+self.radius, y_start_pos))

    def draw_ballon(self) -> None:
        """
            The main goal here is to make the animation on a loop an then when it finish continue to the game.
        """
        # pygame.draw.polygon(self.game_object.screen, color.grey_1.value, self.arrow)
        # pygame.draw.polygon(self.game_object.screen, color.grey_1.value, self.arrow1)
        pygame.draw.line(self.game_object.screen, color.grey_1.value, (
            self.position["x"]+self.radius/2, self.position["y"]+self.radius), (self.position["x"]+self.radius/2, self.position["y"]+self.radius*2), 2)
        pygame.draw.ellipse(self.game_object.screen, self.color,
                            (self.position["x"], self.position["y"], self.radius, self.oval_value))
        pygame.draw.ellipse(self.game_object.screen, color.grey_1.value,
                            (self.position["x"], self.position["y"], self.radius, self.oval_value), 1)
        self.position["x"] += self.x_move_pos
        self.position["y"] += self.y_move_pos

    def get_position(self) -> None:
        return (self.position["x"], self.position["y"])
