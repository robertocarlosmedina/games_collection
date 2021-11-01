__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from src.colors import Game_color as color
from src.game import Game_loop
from src.start import Game_start
from src.menu import Game_menu
from src.quit import Game_quit

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

game_links = {
    "game_start": Game_start(screen, screen_size),
    "game_menu": Game_menu(screen, screen_size),
    "game_loop": Game_loop(screen, screen_size),
    "game_quit": Game_quit(screen, screen_size)
}

current_link = "game_menu"
game_events = None

keep_going = True

clock = pygame.time.Clock()

while keep_going:
    game_events = pygame.event.get()
    for event in game_events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_KP_ENTER]:
                exit()

    clock.tick(30)

    screen.fill(color.black.value)
    current_link = game_links[current_link].run_link(game_events)
    
    pygame.display.update()
