import pygame
from pygame import surface
from src.support.colors import Game_color as color

class Scale_animtion:
    def __init__(self, screen: pygame.Surface, surf_pos: list, end_size: int, img_url:str) -> None:
        self.screen = screen
        self.surf_pos = surf_pos
        self.display_surf = pygame.Surface(tuple(surf_pos))
        self.end_size = end_size
        self.img_size = [20, 20]
        self.animation = False

    def draw(self, draw_board, draw_rows):
        
        while not self.animation: 
            self.screen.fill(color.black.value)
            draw_board()
            draw_rows()
            
            pygame.draw.rect(
                self.screen, 
                color.red.value, 
                pygame.Rect(self.surf_pos[0]/2 - self.img_size[0]/2, \
                    self.surf_pos[1]/2 - self.img_size[1]/2, self.img_size[0], self.img_size[1]))
            
            if self.img_size[0] >= self.end_size:
                break

            self.img_size[0] += .6
            self.img_size[1] += .6 

            pygame.display.update()