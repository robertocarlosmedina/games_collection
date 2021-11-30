import pygame
from src.support.colors import Game_color as color

class Falling_object:
    def __init__(self, screen: pygame.Surface, start_position: list, end_position: list, player: int, radius: int) -> None:
        self.screen, self.radius = screen, radius
        self.start_position, self.end_position, self.player = start_position, end_position, player
        self.end_falling = False

    def check_end_falling(self) -> bool:
        return self.start_position[1] == self.end_position[1]

    def draw(self, draw_board, draw_rows) -> None:
        
        while not self.end_falling: 
            self.screen.fill(color.black.value)
            draw_board()
            draw_rows()
            if self.player == 1:
                pygame.draw.circle(self.screen, color.red.value, (self.start_position[0], self.start_position[1]), self.radius)
            else:
                pygame.draw.circle(self.screen, color.yellow.value, (self.start_position[0], self.start_position[1]), self.radius)
            
            if self.check_end_falling():
                return None
            self.start_position[1] += 1


            pygame.display.update()
