import pygame
from pygame import surface
from src.support.colors import Game_color as color

class Scale_animtion:
    def __init__(self, screen: pygame.Surface, surf_pos: list, end_size: int, img_url:str) -> None:
        self.screen = screen
        self.surf_pos = surf_pos
        self.display_surf = pygame.Surface((100, 100))
        self.display_surf.fill(color.grey.value)
        self.end_size = end_size
        self.img_size = [10, 10]
        self.img_url = img_url

    def draw(self, draw_board, draw_rows):
        
        while True: 
            self.screen.fill(color.black.value)
            draw_board()
            draw_rows()
            image = pygame.image.load(self.img_url)
            image = pygame.transform.scale(image, (self.img_size[0], self.img_size[1]))
            self.display_surf.blit(image, (int(50 - self.img_size[0]/2), \
                    int(50 - self.img_size[1]/2)))
            
            self.screen.blit(self.display_surf, tuple(self.surf_pos))
            if self.img_size[0] >= self.end_size:
                break

            self.img_size[0] += .6
            self.img_size[1] += .6 

            pygame.display.update()


            # picture = pygame.image.load(filename)
# 