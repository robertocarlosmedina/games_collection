import pygame
from src.support.colors import Game_color as color
from src.support.font import Game_fonts as fonts

file :object                 # Store the file object to be open
file_data :str               # Store the file content's
surface :pygame.Surface      # Surface to bee use in the information display
screen_texts :dict           # Dict of all the display text of the game

surface = pygame.Surface((100, 100))
screen_texts = {
    "game_tittle": " Tower of Hanoi",
    "game_subtittle": "Case study",
    "game_main_menu_text": "Game Menu",
    "game_mode_menu": "Chose game mode",
    "game_tower_disk_nr": "Chose the number of disk",
    "self_play_menu_text": "Play game",
    "game_result_text": "Game Over",
    "game_lost_text": "You lose!",
    "game_win_text": "You Win!",
    "game_credits_tittle": "Game credits",
    "game_quit_text": "Do you really want to finish the game?",
    "data_movements": "Movements",
    "data_foods": "Points",
    "pause_menu_title":"Pause Menu",
    "game_mode_choice_text": "Chose game mode",
    "author_text": ['"This project is for educational use, feel free to use', "and share it. And if you find it useful,", "don't forget to support the project by", 'making your contribution."']
}


def draw_header_styled_lines(screen :pygame.Surface, screen_size :tuple) -> None:
    """
        Draw the styled line on top of the menus pages.
    """
    pygame.draw.line(
        screen, 
        color.brown.value,
        (screen_size[0]/2 - 190, 100), 
        (screen_size[0]/2 + 190, 100), 
        3
    )
    pygame.draw.line(
        screen, 
        color.grey.value,
        (screen_size[0]/2 - 180, 95), 
        (screen_size[0]/2 + 180, 95),  
    )
    pygame.draw.line(
        screen, 
        color.grey.value,
        (screen_size[0]/2 - 180, 105), 
        (screen_size[0]/2 + 180, 105), 
        1
    )

def draw_vertical_styled_lines(screen :pygame.Surface, screen_size :tuple) -> None:
    """
        Draw a vertical line on the middle of the screen.
    """
    pygame.draw.line(
        screen, 
        color.green.value,
        (screen_size[0]/2 , 140), 
        (screen_size[0]/2, 430), 
        3
    )
    pygame.draw.line(
        screen, 
        color.grey.value,
        (screen_size[0]/2 - 7 , 150), 
        (screen_size[0]/2 - 7, 420), 
        
    )
    pygame.draw.line(
        screen, 
        color.grey.value,
        (screen_size[0]/2 + 7, 150), 
        (screen_size[0]/2 + 7, 420), 
        1
    )

def display_game_result_info(screen :pygame.Surface, info_name :str, value :int, position :dict) -> None:
    """
        Display a surface whit the game result.
    """
    font_size :int
    surface.fill(color.black.value)
    pygame.draw.rect(
        surface , 
        color.grey_1.value, 
        pygame.Rect(1,1, 98,98),
        1
    )
    font_size = pygame.font.Font.size(fonts.montserrat_size_16.value, f"{value}")
    line = fonts.montserrat_size_16.value.render(f"{value.capitalize()}", True, color.white.value)
    surface.blit(line, (50-font_size[0] / 2, 25))
    font_size = pygame.font.Font.size(fonts.montserrat_size_14.value, f"{info_name}")
    line = fonts.montserrat_size_14.value.render(f"{info_name}", True, color.white.value)
    surface.blit(line, (50-font_size[0]/2, 60))
    screen.blit(surface, (position["x"], position["y"]))

def display_game_result_winning_color_info(screen :pygame.Surface, info_name :str, value :int, position :dict) -> None:
    font_size :int
    surface.fill(color.black.value)
    pygame.draw.rect(
        surface , 
        color.grey_1.value, 
        pygame.Rect(1,1, 98,98),
        1
    )
    pygame.draw.circle(surface, color.yellow.value, (50, 30), 10) if int(value) == 2 else \
        pygame.draw.circle(surface, color.red.value, (50, 30), 10)

    font_size = pygame.font.Font.size(fonts.montserrat_size_14.value, f"{info_name}")
    line = fonts.montserrat_size_14.value.render(f"{info_name}", True, color.white.value)
    surface.blit(line, (50-font_size[0]/2, 60))
    screen.blit(surface, (position["x"], position["y"]))

def read_from_file(file_path :str, mode :str, clean_data = False) -> list:
    """
        function the read data from a txt file.
    """
    file = open(file_path, mode)
    file_data = file.readlines()
    file.close()
    
    if clean_data:
        file = open(file_path, "w")
        file.close()

    return file_data

def write_from_file(file_path :str, mode :str, value :str) -> None:
    """
        Function to write on a txt file.
    """
    file = open(file_path, mode)
    file.write(value)
    file.close()

def get_screen_text(text_name :str):
    """
        Getting a screen text according the his id.
    """
    return screen_texts[text_name]
