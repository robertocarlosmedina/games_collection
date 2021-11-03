__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from src.game_links import Game_links as Link
from src.colors import Game_color as color

# variable declaration
screen_size :tuple
screen :pygame.Surface
current_link :str
game_events :pygame.event
keep_going :bool
game_links :dict
clock :pygame.time


screen_size = (700, 500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Snake')

links = Link()

game_links = {
    "game_start": links.start_game,
    "game_menu": links.game_main_menu,
    "game_loop": links.gameplay_loop,
    "game_quit": links.game_quit,
    "game_tutorial": links.game_tutorial,
    "game_continue": links.continue_game,
    "game_pause_menu": links.game_pause_menu,
    "game_lost": links.game_lost,
    "game_won": links.game_won,
}

current_link = "game_start"
game_events = None

keep_going = True

clock = pygame.time.Clock()

while keep_going:
    game_events = pygame.event.get()
    for event in game_events:
        if event.type == pygame.QUIT:
            current_link = "game_quit"
            
        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_KP_ENTER]:
                exit()

    clock.tick(30)
    screen.fill(color.black.value)

    current_link = game_links[current_link](screen, screen_size, game_events)
    
    pygame.display.update()
