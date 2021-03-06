import pygame
from src.support.colors import Game_color as Color
from src.support.font import Game_fonts as fonts

file :object
file_data :str
surface :pygame.Surface
screen_texts :dict

surface = pygame.Surface((100, 100))
screen_texts = {
    "game_tittle": "Snake Game",
    "game_subtittle": "Case study",
    "game_main_menu_text": "Game Menu",
    "self_play_menu_text": "Watch Snake Play",
    "game_won_text": "You Won !!",
    "game_lost_text": "You Lost !!",
    "game_credits_tittle": "Game credits",
    "game_quit_text": "Do you really want to finish the game?",
    "data_movements": "Movements",
    "data_foods": "Collected",
    "hamiltonian_choice_text": "Choice the Hamiltonian version",
    "author_text": ['"This project is for educational use, feel free to use', "and share it. And if you find it useful,", "don't forget to support the project by", 'making your contribution."']
}

def draw_header_styled_lines(screen :pygame.Surface, screen_size :tuple) -> None:
    pygame.draw.line(
        screen,
        Color.green.value,
        (screen_size[0]/2 - 190, 100),
        (screen_size[0]/2 + 190, 100),
        3
    )
    pygame.draw.line(
        screen,
        Color.grey.value,
        (screen_size[0]/2 - 180, 95),
        (screen_size[0]/2 + 180, 95),
    )
    pygame.draw.line(
        screen,
        Color.grey.value,
        (screen_size[0]/2 - 180, 105),
        (screen_size[0]/2 + 180, 105),
        1
    )

def draw_vertical_styled_lines(screen :pygame.Surface, screen_size :tuple) -> None:
    pygame.draw.line(
        screen,
        Color.green.value,
        (screen_size[0]/2 , 140),
        (screen_size[0]/2, 430),
        3
    )
    pygame.draw.line(
        screen,
        Color.grey.value,
        (screen_size[0]/2 - 7 , 150),
        (screen_size[0]/2 - 7, 420),

    )
    pygame.draw.line(
        screen,
        Color.grey.value,
        (screen_size[0]/2 + 7, 150),
        (screen_size[0]/2 + 7, 420),
        1
    )

def display_game_snake_info(screen :pygame.Surface, info_name :str, value :int, position :dict) -> None:
    font_size :int
    surface.fill(Color.black.value)
    pygame.draw.rect(
        surface ,
        Color.green.value,
        pygame.Rect(1,1, 98,98),
        1
    )
    font_size = pygame.font.Font.size(fonts.montserrat_size_16.value, f"{value}")
    line = fonts.montserrat_size_16.value.render(f"{value}", True, Color.white.value)
    surface.blit(line, (50-font_size[0] / 2, 30))
    font_size = pygame.font.Font.size(fonts.montserrat_super_small_font.value, f"{info_name}")
    line = fonts.montserrat_super_small_font.value.render(f"{info_name}", True, Color.white.value)
    surface.blit(line, (50-font_size[0]/2, 60))
    screen.blit(surface, (position["x"], position["y"]))

def read_from_file(file_path :str, mode :str, clean_data :bool) -> list:
    file = open(file_path, mode)
    file_data = file.readlines()
    file.close()

    if clean_data:
        file = open(file_path, "w")
        file.close()

    return file_data

def write_from_file(file_path :str, mode :str, value :str) -> None:
    file = open(file_path, mode)
    file.write(value)
    file.close()

def get_screen_text(text_name :str):
    return screen_texts[text_name]
