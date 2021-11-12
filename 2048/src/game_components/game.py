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
from src.support.font import Game_fonts as fonts
from src.support.colors import Game_color as color
from src.support.auxiliar_functions import display_game_snake_info, \
            get_screen_text, write_from_file

class Game_loop:
    
    table_size_position :dict
    screen_size :tuple
    screen :pygame.Surface 
    snake_is_alive :bool
    game_win :bool
    snake_step :int
    collected_foods :int
    game_events :pygame.event
    play_algorithm :str

    def __init__(self, screen :pygame.Surface, screen_size :list, algorithm = None ) -> None:
        self.screen = screen
        self.screen_size = screen_size
        self.play_algorithm = algorithm
        self.cubo_size = 20
        self.snake_step = 14
        self.table_size_position = {"widht": self.snake_step*self.cubo_size, "height": self.snake_step*self.cubo_size}
        self.table_size_position["x_position"] = int(self.screen_size[0]/2 - self.table_size_position["widht"]/2)
        self.table_size_position["y_position"] = int(self.screen_size[1]/2 - self.table_size_position["height"]/2)
        self.collected_foods = 3
        self.set_up_game_mode()
    
    def set_up_game_mode(self):
        pass

    def draw_table_lines(self) -> None:
        y = self.table_size_position["y_position"]
        for _ in range(int(self.table_size_position["widht"]/self.snake_step) + 1):
            pygame.draw.line(
                self.screen, 
                color.grey1.value,
                (self.table_size_position["x_position"], y), 
                (self.table_size_position["x_position"]+self.table_size_position["widht"], y), 
                2
            )
            y += 14
        x = self.table_size_position["x_position"]
        for _ in range(int(self.table_size_position["widht"]/self.snake_step) + 1):
            pygame.draw.line(
                self.screen, 
                color.grey1.value,
                (x, self.table_size_position["y_position"]), 
                (x, self.table_size_position["y_position"]+self.table_size_position["widht"]), 
                2
            )
            x += 14
    
    def draw_game_elements(self) -> None:
        # To draw the table lines
        self.draw_table_lines()

        # game table draw
        pygame.draw.rect(
            self.screen, 
            color.white.value, 
            pygame.Rect(self.table_size_position["x_position"]-2, 
            self.table_size_position["y_position"]-2, 
            self.table_size_position["widht"]+5,self.table_size_position["height"]+6 ), 
            3
        )

        display_game_snake_info(screen = self.screen, info_name = get_screen_text("data_movements"), value = 10, 
            position = {"x":40, "y":190})

        display_game_snake_info(screen = self.screen, info_name = get_screen_text("data_foods"), value = self.collected_foods, 
            position = {"x":560, "y":190})
    
    def game_events_handler(self, snake_head_rect :pygame.Rect, food_rect :pygame.Rect) -> None:
        pass

    def run_link(self, game_events :pygame.event) -> str:
        food_rect : dict
        snake_head_rect : dict
        self.game_events = game_events
        self.pressed_keys = pygame.key.get_pressed()
        self.draw_game_elements()
        # self.game_win = self.snake.check_game_end()
        # food_rect  = self.food.get_food_rect()
        # snake_head_rect = self.snake.get_snake_head_rect()
        # self.game_events_handler(food_rect, snake_head_rect)

        # if(not self.snake_is_alive):
        #     write_from_file("data/end_game_values.txt", "w", 
        #         f"{self.collected_foods} {self.snake.get_snake_moves()}"
        #     )
        #     sleep(2)
        #     return "game_lost"
        
        # if(self.game_win == self.cubo_size * self.cubo_size):
        #     write_from_file("data/end_game_values.txt", "w", 
        #         f"{self.collected_foods} {self.snake.get_snake_moves()}"
        #     )
        #     sleep(2)
        #     return "game_won"
        
        for event in game_events:
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    return "game_pause_menu"

        return "game_loop"
