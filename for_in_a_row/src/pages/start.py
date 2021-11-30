__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"
__file__ = "start.py"
__path__ = "https://github.com/robertocarlosmedina/AI_games"

"""
"""
import pygame
from src.support.colors import Game_color as color
from src.support.auxiliar_functions import get_screen_text

# class that control the initial painel 
class Game_start:

    pygame.init()

    def __init__(self, screen, screen_size):
        self.font = pygame.font.SysFont("arial", 50)
        self.font1 = pygame.font.SysFont("arial", 12)
        self.screen = screen
        self.screen_size = screen_size
        self.delay = self.highCircle  = self.count = 0
    
    def draw_screen_text(self) -> None:
        # drawing tittle
        size = pygame.font.Font.size(self.font, get_screen_text("game_tittle"))
        line = self.font.render(get_screen_text("game_tittle"), True, color.blue.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, (self.screen_size[1]/2-size[1]/2)-40))
        # drawing sub tittle
        size = pygame.font.Font.size(self.font1, get_screen_text("game_subtittle"))
        line = self.font1.render(get_screen_text("game_subtittle"), True, color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, (self.screen_size[1]/2-size[1]/2)-10))

        # decrement the font1 size
        self.font1 = pygame.font.SysFont("arial", 9)

        # drawing tittle bottom info
        size = pygame.font.Font.size(self.font1, f'Made by {__author__}')
        line = self.font1.render(f'Made by {__author__}', True, color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 440))
        # drawing tittle bottom info
        size = pygame.font.Font.size(self.font1, f'{__email__}')
        line = self.font1.render(f'{__email__}', True, color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 450))
         # drawing tittle bottom info
        size = pygame.font.Font.size(self.font1, f'{__path__}')
        line = self.font1.render(f'{__path__}', True, color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 460))

    # Method that control this class
    def run_link(self, game_events :pygame.event):
        del game_events
        
        self.draw_screen_text()
        self.animation()
        
        # Controling if the process of drawing runned 6 times to pass this start page
        if self.count >= 3:    
            return "game_menu"
        return "game_start"

    # Method that control the circle animation display and the time 
    def animation(self):
        pos_x, pos_y = int(self.screen_size[0]/2), int(self.screen_size[1]/2)+20
        for i in range(0, 7):
            if i == self.highCircle:
                pygame.draw.circle(self.screen, color.red.value, (pos_x-60, pos_y), 6)
            elif i == self.highCircle + 1:
                pygame.draw.circle(self.screen, color.red_1.value, (pos_x-60, pos_y), 3)
            elif i == self.highCircle - 1:
                pygame.draw.circle(self.screen, color.red_1.value, (pos_x-60, pos_y), 3)
            else:
                pygame.draw.circle(self.screen, color.red_1.value, (pos_x-60, pos_y), 2)
            pos_x +=20

        # Controling the delay to change the higher circle
        if self.delay >= 3:
            self.highCircle += 1
            self.delay = 0
        self.delay += 1

        # COntroling the if the higher  circle is in the end to return it to the start
        if self.highCircle > 7:
            self.highCircle = 0
            self.count += 1
