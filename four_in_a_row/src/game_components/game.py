__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
    This is the class where all the game loop is controlled, and where all the action are
    controlled. And also all the cubes generated by the Cube class are controlled by here.
"""

from typing import Literal
import pygame
import numpy as np
from pygame import font
import numpy as np
from src.support.font import Game_fonts as fonts
from src.support.colors import Game_color as color
from src.game_components.faling_object import Falling_object
from src.game_components.Player import AI_player, Random_player, Human_player
from src.support.auxiliar_functions import write_from_file

def turn_worker(board, send_end, p_func):
    send_end.send(p_func(board))

class Game_loop:
    
    game_win: bool              # control if the game was won
    game_table: list            # store information about the game table
    game_events: pygame.event   # hold the current games events
    play_algorithm: str         # hold the current self playing algorithms
    cube_sizes: dict            # store all the information about the cubes
    game_cubes: list            # list of objets related to the cubes on th game
    nr_cubes: int               # to declare the number of cubes for the game
    players: list               # to store the configuration of the player 1
    current_player: bool        # current player to play
    falling_obj: Falling_object # store an object

    def __init__(self, screen: pygame.Surface, screen_size: list, game_mode = None ) -> None:
        self.screen = screen
        self.screen_size = screen_size
        self.board = np.zeros([6,7]).astype(np.uint8)
        self.game_cubes = []
        self.row_radius = 20
        self.row_distance = 30
        self.mouse_position = None
        self.slideArrows = []
        self.current_player = int(True)
        # starting the game table info
        self.game_table = {"width": 360, "heigth": 300}
        self.game_table["x_position"] = self.screen_size[0]/2 - self.game_table["width"]/2
        self.game_table["y_position"] = self.screen_size[1]/2 - self.game_table["heigth"]/2 + 30
        # falling down control
        self.falling_position = (0, 0)
        self.end_falling_effect = False
        self.start_position, self.end_position = None, None
        self.falling_obj = None
        self.algorithms = ""
        # starting methods
        self.initializing_game_mode(game_mode)
        self.make_arrows()

    def make_arrows(self) -> None:
        x = int(self.game_table["x_position"] + 15)
        for _ in range(7):
            self.slideArrows.append(((x, int(self.game_table["y_position"] - 20)), \
                (x + 15, int(self.game_table["y_position"] - 10)), (x + 30, int(self.game_table["y_position"] - 20))))
            x += 50

    def initializing_game_mode(self, game_mode: str) -> None:
        if game_mode == "human_player": 
             self.players = [Human_player(1), Human_player(2)]
        elif game_mode == "random_player":
            self.players = [Human_player(1), Random_player(2)]
        elif game_mode == "ai_player":
            self.algorithms = "alpha_prunning"
            self.players = [AI_player(2), Human_player(1)]
        else:
            self.players = [AI_player(1), AI_player(2)]
            if game_mode == "ai_vs_ai_exp":
                self.algorithms = "expectimax"
            else:
                self.algorithms = "alpha_prunning"

    def draw_game_board(self) -> None:
        pygame.draw.rect(
            self.screen, 
            color.blue_1.value, 
            pygame.Rect(self.game_table["x_position"], 
            self.game_table["y_position"], self.game_table["width"],
            self.game_table["heigth"] ),
            border_radius = 20
        )
        font_size = pygame.font.Font.size(fonts.montserrat_size_30.value, "Player: ")
        line = fonts.montserrat_size_30.value.render("Player: ", True, color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-(font_size[0]/2), 25))
        
        pygame.draw.circle(self.screen, color.red.value, (self.screen_size[0]/2 + font_size[0] - 10, 46), 20)\
            if int(self.current_player) == 0 else \
                pygame.draw.circle(self.screen, color.yellow.value, (self.screen_size[0]/2 + font_size[0] - 10, 46), 20)
    
    def draw_rows(self) -> None:
        x = self.game_table["x_position"] + self.row_distance 
        y = self.game_table["y_position"] + self.row_distance
        for line in self.board:
            for col in line:
                if col == 1:
                    pygame.draw.circle(self.screen, color.red.value, (x, y), self.row_radius)
                elif col == 2:
                    pygame.draw.circle(self.screen, color.yellow.value, (x, y), self.row_radius)
                else:
                    pygame.draw.circle(self.screen, color.dark_blue.value, (x, y), self.row_radius)
                    pygame.draw.circle(self.screen, color.black.value, (x, y), self.row_radius, 1)
                x += self.row_radius + self.row_distance
            x = self.game_table["x_position"] + self.row_distance 
            y += self.row_distance + 18
    
    def game_completed(self, player_num):
        player_win_str = '{0}{0}{0}{0}'.format(player_num)
        board = self.board
        to_str = lambda a: ''.join(a.astype(str))

        def check_horizontal(b):
            for row in b:
                if player_win_str in to_str(row):
                    return True
            return False

        def check_verticle(b):
            return check_horizontal(b.T)

        def check_diagonal(b):
            for op in [None, np.fliplr]:
                op_board = op(b) if op else b
                
                root_diag = np.diagonal(op_board, offset=0).astype(np.int)
                if player_win_str in to_str(root_diag):
                    return True

                for i in range(1, b.shape[1]-3):
                    for offset in [i, -i]:
                        diag = np.diagonal(op_board, offset=offset)
                        diag = to_str(diag.astype(np.int))
                        if player_win_str in diag:
                            return True

            return False

        return (check_horizontal(board) or
                check_verticle(board) or
                check_diagonal(board))

    def check_if_colum_is_filled(self, board_colum: int) -> None:
        if 0 in np.transpose(self.board)[board_colum]:
            return False

        return True

    def human_time(self) -> int:
        count = 0
        for arrow in self.slideArrows:
            if(not self.check_if_colum_is_filled(count)):
                if (self.mouse_position[0]in range(arrow[0][0], arrow[2][0]) and (self.mouse_position[1]in range(arrow[0][1], arrow[1][1])or\
                    self.mouse_position[1]in range(arrow[1][1], arrow[0][1]))): # checking if mouse is over them to draw them whit defferent color
                    # checking if the mouse is pressed to change the slide page
                    if pygame.mouse.get_pressed()[0]:
                        pygame.draw.polygon(self.screen, color.grey1.value, arrow)
                        pygame.draw.polygon(self.screen, color.black.value, arrow, 3)
                        return count
                        # check if it is not in the last page to increment the page
                    else:
                        pygame.draw.polygon(self.screen, color.grey.value, arrow)
                        pygame.draw.polygon(self.screen, color.grey.value, arrow, 3)
                else:
                    pygame.draw.polygon(self.screen, color.grey.value, arrow)
                    pygame.draw.polygon(self.screen, color.white.value, arrow, 3)
            count += 1

        return None

    def get_start_end_falling_position(self, play_position: int) -> int:
        x = self.game_table["x_position"] + self.row_distance 
        y = self.game_table["y_position"] + self.row_distance

        def get_start_position(x, y) -> list: 
            for _ in range(len(self.board[0])):
                for index_col in range(len(self.board[0])):
                    if index_col == play_position:
                        return [x, y]
                    x += self.row_radius + self.row_distance
                x = self.game_table["x_position"] + self.row_distance 
                y += self.row_distance + 18
        
        def get_end_position(y) -> int:
            auxiliar = np.transpose(self.board)[play_position]
            for index, value in enumerate(auxiliar):
                if value != 0:
                    return y - self.row_distance * 2 + 10

                if index == len(auxiliar) - 1:
                    return y
                y += self.row_distance + 18

        start_position = get_start_position(x, y)
        start_position[1] -= 50
        end_position = [start_position[0], get_end_position(y)]
        return start_position, end_position

    def falling_down_efect(self, play_position: int) -> int:
        self.start_position, self.end_position = self.get_start_end_falling_position(play_position)
        self.falling_obj = Falling_object(self.screen, self.start_position, self.end_position, int(self.current_player)+1, self.row_radius)

    def update_board(self, player_move: int, player: int) -> None:
        line_index = 0
        auxiliar = np.transpose(self.board)[player_move]
        for index, value in enumerate(auxiliar):
            if value != 0:
                line_index = index - 1
                break

            if index == len(auxiliar) - 1:
                line_index = index
                break

        self.board[line_index][player_move] = int(self.current_player) + 1

    def game_completed(self, player_num):
        player_win_str = '{0}{0}{0}{0}'.format(player_num)
        board = self.board
        to_str = lambda a: ''.join(a.astype(str))

        def check_horizontal(b):
            for row in b:
                if player_win_str in to_str(row):
                    return True
            return False

        def check_verticle(b):
            return check_horizontal(b.T)

        def check_diagonal(b):
            for op in [None, np.fliplr]:
                op_board = op(b) if op else b
                
                root_diag = np.diagonal(op_board, offset=0).astype(np.int)
                if player_win_str in to_str(root_diag):
                    return True

                for i in range(1, b.shape[1]-3):
                    for offset in [i, -i]:
                        diag = np.diagonal(op_board, offset=offset)
                        diag = to_str(diag.astype(np.int))
                        if player_win_str in diag:
                            return True

            return False

        return (check_horizontal(board) or
                check_verticle(board) or
                check_diagonal(board))   

    def game_over(self) -> Literal["game_over"]:
        write_from_file("./data/end_game_values.txt", "w",\
             f"{int(self.current_player) + 1} {self.players[int(self.current_player)].type}")
        return "game_over"
                
    # To run this page on the game
    def run_link(self, game_events :pygame.event) -> str:
        self.mouse_position = pygame.mouse.get_pos()
        self.draw_game_board()
        self.draw_rows()
        
        play = self.players[int(self.current_player)].get_move(self.algorithms, self.board, self.human_time)
        if play != None:
            self.falling_down_efect(play)
            self.falling_obj.draw(self.draw_game_board, self.draw_rows)
            self.update_board(play, 1)

            if self.game_completed(int(self.current_player) + 1):
                return self.game_over()
            else:
                self.current_player = not self.current_player
        
        return "game_loop"
