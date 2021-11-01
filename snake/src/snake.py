__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from random import randint
from src.colors import Game_color as color
from src.snake_parts import Snake_part


class Snake:

    screen :pygame.Surface # screen surface
    table_size_position :dict #information about the game table
    snake_parts :list # List of al the parts of the snake
    pressed_keys :pygame.key # all the pressed keys
    snake_step :int # Snake step size
    speed_couter :int # to control the snake speed
    snake_speed :int # this is the speed of the snake
    make_step :bool # to make the speep acordding to the speed
    snake_self_collision :bool
    dead_delay :int # timer to control the snake dead
    dead_counter :int # to control the dead_delay
    snake_step : int # the number of pixel that takes to make a step
    start_position :dict # initial position of the snake

    def __init__(self, screen :pygame.Surface, start_position : dict, table_size_position :dict, snake_step :int) -> None:
        self.screen = screen
        self.snake_step = snake_step
        self.table_size_position = table_size_position
        self.start_position = start_position
        self.pressed_keys = None 
        self.speed_couter = 0 
        self.snake_speed = 6 
        self.make_step = False 
        self.snake_self_collision = False 
        self.dead_delay = 3 
        self.dead_counter = 0

        self.start_snake_controlers_and_parts()

    def start_snake_controlers_and_parts(self) -> None:
        self.snake_move_direction = {
            pygame.K_UP: {
                "state": False, 
                "action": self.snake_moving_up, 
                "oposite_action": pygame.K_DOWN,
                "orientation": "vertical",
                "move_to": "up"
            },
            pygame.K_DOWN: {
                "state": False, 
                "action": self.snake_moving_down, 
                "oposite_action": pygame.K_UP,
                "orientation": "vertical",
                "move_to": "down"
            },
            pygame.K_RIGHT: {
                "state": True, 
                "action": self.snake_moving_right, 
                "oposite_action": pygame.K_LEFT,
                "orientation": "horizontal",
                "move_to": "right"
            }, 
            pygame.K_LEFT: {
                "state": False, 
                "action": self.snake_moving_left, 
                "oposite_action": pygame.K_RIGHT,
                "orientation": "horizontal",
                "move_to": "left"
            }
        }
        self.current_orientation = "horizontal"
        self.current_move_direction = "right"
        x_position = self.start_position["x"] + 14*randint(5,16)
        y_position = self.start_position["y"] + 14*randint(5,25)
        self.snake_parts = [
            Snake_part(
                screen=self.screen, 
                position={
                    "x": x_position,
                    "y": y_position,
                }
            ),
            Snake_part(
                screen=self.screen, 
                position={
                    "x": x_position - 14,
                    "y": y_position,
                }
            )
            ,
            Snake_part(screen=self.screen, 
                position={
                "x": x_position - 28,
                "y": y_position,
                }
            )
            ,
            Snake_part(screen=self.screen, 
                position={
                "x": x_position - 42,
                "y": y_position,
                }
            )
        ]

    # to change the snake speed
    def change_snake_speed(self, new_speed :int) -> None:
        self.snake_speed = new_speed

    # To control the snake move direction
    def snake_move_direction_controlers(self) -> None:
        there_is_changes = False

        for key, values in self.snake_move_direction.items():
            if self.pressed_keys[key]:
                if ((values["orientation"] != self.current_orientation and key != values["oposite_action"]) or
                    (self.current_move_direction == values["move_to"])):
                    values["state"] = True
                    self.current_orientation = values["orientation"]
                    self.current_move_direction = values["move_to"]
                    there_is_changes = True
            else:
                values["state"] = False

            self.snake_move_direction[key] = values
        
        if not there_is_changes:
            for key, values in self.snake_move_direction.items():
                if values["move_to"] == self.current_move_direction:
                    values["state"] = True
                    self.current_orientation = values["orientation"]
                    self.current_move_direction = values["move_to"]

                

        # for values in self.snake_move_direction.values():
            # print(values.values())

    def snake_moving_up(self) -> None:
        if(self.snake_parts[0].part_position["y"] > self.table_size_position["y_position"]+14):
            self.snake_parts[0].part_position["y"] -= self.snake_step
        else:
            self.dead_counter += 1
    
    def snake_moving_down(self) -> None:
        if(self.snake_parts[0].part_position["y"] < self.table_size_position["y_position"]+
                    self.table_size_position["height"]-14):
            self.snake_parts[0].part_position["y"] += self.snake_step
        else:
            self.dead_counter += 1

    def snake_moving_right(self) -> None:
        if(self.snake_parts[0].part_position["x"] < self.table_size_position["x_position"]+
                    self.table_size_position["widht"]-14):
            self.snake_parts[0].part_position["x"] += self.snake_step
        else:
            self.dead_counter += 1

    def snake_moving_left(self) -> None:
        if(self.snake_parts[0].part_position["x"] > self.table_size_position["x_position"]+14):
            self.snake_parts[0].part_position["x"] -= self.snake_step
        else:
            self.dead_counter += 1

    def control_speed_and_steps(self) -> None:
        if (self.speed_couter == self.snake_speed):
            self.make_step = True
            self.speed_couter = 0
        else:
            self.speed_couter += 1

    def check_game_end(self) -> bool:
        return False

    def update_parts_position(self, last_head_position :dict) -> None:
        for part in self.snake_parts[1:len(self.snake_parts)]:
            part_position = part.get_part_position()
            position = {"x": last_head_position["x"],
                        "y": last_head_position["y"]}
            part.update_position(position)
            last_head_position = part_position

    def get_snake_head_rect(self) -> dict:
        return self.snake_parts[0].get_part_rect()
    
    def snake_self_collision_controler(self) -> None:
        snake_head = self.snake_parts[0].get_part_rect()
        for part in self.snake_parts[1:len(self.snake_parts)]:
            if snake_head.colliderect(part.get_part_rect()):
                self.snake_self_collision = True

    def add_snake_part (self) -> None:
        last_part_position = self.snake_parts[len(self.snake_parts)-1].get_part_position()

        self.snake_parts.append(
            Snake_part(
                screen=self.screen, 
                position=last_part_position
            )
        )
    
    def draw_snake(self, presssed_keys :pygame.key) -> bool:
        head_position :dict

        self.pressed_keys = presssed_keys

        self.control_speed_and_steps()

        # snake draw
        for part in self.snake_parts:
            part.draw_part()       

        self.snake_self_collision_controler() 
    
        if(self.dead_counter == self.dead_delay or self.snake_self_collision):
            self.dead_counter = 0
            return False
        else:
            # to make the move in the selected direction
            for values in self.snake_move_direction.values():
                if(values["state"] and self.make_step):
                    head_position = self.snake_parts[0].get_part_position()
                    self.update_parts_position(head_position)
                    values["action"]()
                    self.make_step = False
                
        return True
