import pygame
# Display is 800 x 800


def display_board(window):
    pygame.draw.rect(window, "#dedcdc", (50, 50, 700, 700))
    
def get_board_pos(x, y):
    return 