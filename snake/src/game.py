__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from time import sleep
from pygame import font
from src.font import Game_fonts as fonts
from src.colors import Game_color as color
from src.snake import Snake
from src.food import Food
from src.auxiliar_functions import display_game_snake_info, write_from_file

class Game_loop:
    
    table_size_position :dict
    snake :Snake
    screen_size :tuple
    screen :pygame.Surface 
    snake_is_alive :bool
    game_win :bool
    snake_step :int
    collected_foods :int
    game_events :pygame.event

    def __init__(self, screen :pygame.Surface, screen_size :list) -> None:
        self.screen = screen
        self.screen_size = screen_size
        self.table_size_position = {"widht": 420, "height": 420}
        self.table_size_position["x_position"] = self.screen_size[0]/2 - self.table_size_position["widht"]/2
        self.table_size_position["y_position"] = self.screen_size[1]/2 - self.table_size_position["height"]/2
        self.snake_step = 14
        self.collected_foods = 0
        self.snake = Snake(
            screen = self.screen, 
            start_position = {
                "x": self.table_size_position["x_position"]+1,
                "y": self.table_size_position["y_position"]+1
            },
            table_size_position = self.table_size_position,
            snake_step = self.snake_step
        )
        self.food = Food(self.screen, self.table_size_position, self.snake_step)

    def draw_table_lines(self) -> None:
        y = self.table_size_position["y_position"]
        for _ in range(31):
            pygame.draw.line(
                self.screen, 
                color.grey1.value,
                (self.table_size_position["x_position"], y), 
                (self.table_size_position["x_position"]+420, y), 
                2
            )
            y += 14
        x = self.table_size_position["x_position"]
        for _ in range(31):
            pygame.draw.line(
                self.screen, 
                color.grey1.value,
                (x, self.table_size_position["y_position"]), 
                (x, self.table_size_position["y_position"]+420), 
                2
            )
            x += 14
    
    def draw_game_elements(self) -> None:
        # To draw the table lines
        self.draw_table_lines()
        self.snake.control_speed_and_steps()

        # game table draw
        pygame.draw.rect(
            self.screen, 
            color.blue.value, 
            pygame.Rect(self.table_size_position["x_position"]-2, 
            self.table_size_position["y_position"]-2, 
            self.table_size_position["widht"]+5,self.table_size_position["height"]+6 ), 
            3
        )

        self.food.draw_food()

        self.snake_is_alive = self.snake.draw_snake(self.pressed_keys)
        display_game_snake_info(screen = self.screen, info_name = "Movements", value = self.snake.get_snake_moves(), 
            position = {"x":20, "y":190})

        display_game_snake_info(screen = self.screen, info_name = "Foods", value = self.collected_foods, 
            position = {"x":580, "y":190})
    
    def game_events_handler(self, snake_head_rect :pygame.Rect, food_rect :pygame.Rect) -> None:
        if(snake_head_rect.colliderect(food_rect)):
            self.food.generate_new_food()
            self.snake.add_snake_part()
            self.collected_foods += 1
        if(self.pressed_keys[pygame.K_f]):
            self.food.generate_new_food()
            
        for event in self.game_events:
            if (event.type == pygame.KEYDOWN):
                self.snake.snake_move_direction_controlers()  

    def run_link(self, game_events :pygame.event) -> str:
        food_rect : dict
        snake_head_rect : dict
        self.game_events = game_events
        self.pressed_keys = pygame.key.get_pressed()
        self.draw_game_elements()
        self.game_win = self.snake.check_game_end()
        food_rect  = self.food.get_food_rect()
        snake_head_rect = self.snake.get_snake_head_rect()
        self.game_events_handler(food_rect, snake_head_rect)

        if(not self.snake_is_alive and not self.game_win):
            write_from_file("data/end_game_values.txt", "w", 
                f"{self.collected_foods} {self.snake.get_snake_moves()}"
            )

            return "game_lost"
        
        for event in game_events:
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    return "game_pause_menu"

        return "game_loop"
