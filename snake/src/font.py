from enum import Enum
import pygame

class Game_fonts(Enum):
    pygame.init()
    
    montserrat_big_font = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 30)
    montserrat_subbig_font = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 22)
    montserrat_normal_font = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 18)
    montserrat_small_font = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 16)
    montserrat_super_small_font = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 14)
    