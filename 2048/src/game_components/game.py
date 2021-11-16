__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
import numpy as np
from random import randint
from time import sleep
from pygame import font
from pygame.draw import line
from src.support.font import Game_fonts as fonts
from src.support.colors import Game_color as color
from src.game_components.cube import Cube

class Game_loop:
    
    screen_size :tuple          # screen size info
    screen :pygame.Surface      # screen surface
    game_win :bool              # control if the game was won
    game_table :list            # store information about the game table
    game_events :pygame.event   # hold the current games events
    play_algorithm :str         # hold the current self playing algorithms
    cube_sizes :dict            # store all the information about the cubes
    game_cubes :list            # list of objets related to the cubes on th game

    def __init__(self, screen :pygame.Surface, screen_size :list, algorithm = None ) -> None:
        self.screen = screen
        self.screen_size = screen_size
        self.play_algorithm = algorithm
        self.game_cubes = []
        # starting cubes gaps info
        self.cube_sizes = {"cube_gap": 5}
        # starting the game table info
        self.game_table = {"width": 300, "heigth": 300}
        self.set_up_games_settings()
        self.start_cubes_display_info()
    
    def set_up_games_settings(self) -> None:
        # Ajustin the table position info
        self.game_table["x_position"] = self.screen_size[0]/2 - self.game_table["width"]/2
        self.game_table["y_position"] = self.screen_size[1]/2 - self.game_table["heigth"]/2
        # Aujusting the cubes information
        self.cube_sizes["width"] = self.game_table["width"]/4 - self.cube_sizes["cube_gap"]*1.22
        self.cube_sizes["heigth"] = self.game_table["heigth"]/4 - self.cube_sizes["cube_gap"]*1.22
        self.cube_sizes["x_start"] = self.game_table["x_position"] + self.cube_sizes["cube_gap"]
        self.cube_sizes["y_start"] = self.game_table["y_position"] + self.cube_sizes["cube_gap"]

    def start_cubes_display_info(self) -> None:
        x = self.cube_sizes["x_start"]
        y = self.cube_sizes["y_start"]
        # starting_position = [(randint(0, 1), randint(0, 1)), (randint(3, 2), randint(0, 3))]
        starting_position = [(3, 0), (1, 0)]
        for i in range(4):
            line = []
            for f in range(4):
                value = 0
                if((f, i) in starting_position):
                    value = 2
                cube_display_info = {
                    "x_position": x,
                    "y_position": y,
                    "width": self.cube_sizes["width"],
                    "heigth": self.cube_sizes["heigth"],
                    "value": value
                }
                line.append(Cube(self.screen, self.screen_size, cube_display_info))
                x += self.cube_sizes["cube_gap"] + self.cube_sizes["width"]
            x = self.cube_sizes["x_start"]
            self.game_cubes.append(line)
            y += self.cube_sizes["cube_gap"] + self.cube_sizes["heigth"]
        
        # for cubes in self.game_cubes:
        #     line = ""
        #     for cube in cubes:
        #         line += f" {cube.get_cube_value()}"

        #     print(line)
        # self.make_matrix_transpost()
        # exit()
    
    def make_matrix_transpost(self) -> list:
        return np.transpose(self.game_cubes)

        # print("\nmatrix_T")
        # for cubes in matrix_T:
        #     line = ""
        #     for cube in cubes:
        #         line += f" {cube.get_cube_value()}"

        #     print(line)


    def draw_game_table_and_cubes(self) -> None:
        pygame.draw.rect(
            self.screen, 
            color.blue.value, 
            pygame.Rect(self.game_table["x_position"], 
            self.game_table["y_position"], self.game_table["width"],
            self.game_table["heigth"] ), 2
        )
        [line[i].draw() for line in self.game_cubes  for i in range(4)]

    def get_starting_cube_object(self):
        pass

    def send_elements_to_a_side(self, line_cube :list) -> list:
        for i in range(len(line_cube)):
            if line_cube[i] == 0:
                line_cube.pop(i)
                line_cube.insert(0, 0)
        return line_cube

    def pass_position_till_end(self, line_of_cubes, line_index):
        line_cubes_values = [cube.get_cube_value() for cube in self.game_cubes[line_index]]
        # line_cubes_values = [32, 2, 2, 32]
        i = 0
        for current_value in line_cubes_values:
            if current_value != 0:
                j = i
                for next_value in line_cubes_values[i+1:len(line_cubes_values)]:
                    if next_value == current_value:
                        line_cubes_values[j+1] = line_cubes_values[i] * 2
                        line_cubes_values[i] = 0                        
                    if next_value != 0:
                        break
                    j += 1
            i+=1
        # print([cube.get_cube_value() for cube in self.game_cubes[line_index]])
        # line_cubes_values = self.send_elements_to_a_side(line_cubes_values)
        [cube.update_cube_value(new_value) for cube, new_value in zip(self.game_cubes[line_index], line_cubes_values)]
        # print([cube.get_cube_value() for cube in self.game_cubes[line_index]])
        # print("\n")
        # exit()
        


    def movin_right(self):
        for cubes in self.game_cubes:
            line = ""
            for cube in cubes:
                line += f" {cube.get_cube_value()}"
            print(line)
        print("\n")
        
        i = 0
        for cubes in self.game_cubes:
            self.pass_position_till_end(cubes, i)
            i += 1
                    
        for cubes in self.game_cubes:
            line = ""
            for cube in cubes:
                line += f" {cube.get_cube_value()}"
            print(line)

        # exit()
    
    def game_events_handler(self) -> None:
        for event in self.game_events:
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_UP]:
                    exit()
                elif pygame.key.get_pressed()[pygame.K_DOWN]:
                    pass
                elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                    self.movin_right()
                elif pygame.key.get_pressed()[pygame.K_LEFT]:
                    exit()
        pass

    def run_link(self, game_events :pygame.event) -> str:
        self.game_events = game_events
        self.pressed_keys = pygame.key.get_pressed()
        self.draw_game_table_and_cubes()
        self.game_events_handler()
        
        for event in game_events:
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    return "game_pause_menu"

        return "game_loop"
