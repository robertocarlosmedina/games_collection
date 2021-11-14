__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from src.support.colors import Game_color as color
from src.support.font import Game_fonts as fonts

class Cube:

    cube_surface :pygame.Surface     # store information about the cube rect
    surface_colors :dict             # store information about color and their values

    def __init__(self, screen :pygame.Surface, screen_size :tuple, cube_display_info :dict) -> None:
        self.screen = screen
        self.screen_size = screen_size
        self.cube_display_info = cube_display_info
        self.cube_surface = pygame.Surface((self.cube_display_info["width"], self.cube_display_info["heigth"]))
        self.construing_sruface_colors()

    def construing_sruface_colors(self):
        self.surface_colors = {
            0: color.grey1.value, 
            2: color.white1.value, 
            4: color.white.value,
            8: color.darck_green.value, 
            16: color.red.value,
            32: color.darck_green.value,
            64: color.red_1.value,
            128: color.yellow.value,
            256: color.green_1.value,
            512: color.green_2.value,
            1024: color.green_3.value,
            2048: color.green.value
        }

    def update_cube_position(self) -> None:
        pass

    def update_surface_value(self) -> None:
        pass

    def get_cube_value(self) -> int:
        return self.cube_display_info["value"]

    def update_surface_color(self) -> None:
        [self.cube_surface.fill(col) for key, col in self.surface_colors.items() if key == self.cube_display_info["value"]]

    def draw(self) -> None:
        self.update_surface_color()
        cube_value = self.cube_display_info["value"]
        font_size = pygame.font.Font.size(fonts.montserrat_size_22.value, f"{cube_value}")
        line = fonts.montserrat_size_22.value.render(f"{cube_value}", True, color.grey.value)
        self.cube_surface.blit(line, (self.cube_display_info["width"]/2 - font_size[0]/2, self.cube_display_info["heigth"]/2 - font_size[1]/2))
        self.screen.blit(self.cube_surface, (self.cube_display_info["x_position"], self.cube_display_info["y_position"]))
