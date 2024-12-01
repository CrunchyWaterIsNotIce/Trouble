import pygame
import os
# Display is 800 x 800

# File Path for Assets
board_path = os.path.join("assets", "trouble_board.png")

# Loading Assets
board = pygame.transform.smoothscale_by(pygame.image.load(board_path), 2.95)

def display_board(window):
    window.blit(board, (48, 52))
    
def get_board_pos(x, y):
    return 