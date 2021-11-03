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

# class that control the initial painel 
class Game_start:

    pygame.init()

    def __init__(self, screen, screen_size):
        self.font = pygame.font.SysFont("arial", 50)
        self.font1 = pygame.font.SysFont("arial", 12)
        self.screen = screen
        self.screen_size = screen_size
        self.delay = self.highCircle  = self.count = 0
        self.menu_tittles = {
            "game_tittle": "Snake Game",
            "game_menu_tittle": "Game Menu",
            "self_play_menu": "Watch Snake Play"
        }
    
    def draw_screen_text(self) -> None:
        # drawing tittle
        size = pygame.font.Font.size(self.font, self.menu_tittles["game_tittle"])
        line = self.font.render(self.menu_tittles["game_tittle"], True, color.green.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, (self.screen_size[1]/2-size[1]/2)-40))
        # drawing sub tittle
        size = pygame.font.Font.size(self.font1, self.menu_tittles["game_tittle"])
        line = self.font1.render(self.menu_tittles["game_tittle"], True, color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, (self.screen_size[1]/2-size[1]/2)-10))

        # decrement the font1 size
        self.font1 = pygame.font.SysFont("arial", 9)

        # drawing tittle bottom info
        size = pygame.font.Font.size(self.font1, 'Made by Roberto Medina')
        line = self.font1.render('Made by Roberto Medina', True, color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 430))
        # drawing tittle bottom info
        size = pygame.font.Font.size(self.font1, 'Contact info:')
        line = self.font1.render('Contact info:', True, color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 440))
         # drawing tittle bottom info
        size = pygame.font.Font.size(self.font1, 'robertocarlosmedina.dev@gmail.com')
        line = self.font1.render('robertocarlosmedina.dev@gmail.com', True, color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 450))
         # drawing tittle bottom info
        size = pygame.font.Font.size(self.font1, 'https://robertocarlosmedina.github.io/rportfolio')
        line = self.font1.render('https://robertocarlosmedina.github.io/rportfolio', True, color.white.value)
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