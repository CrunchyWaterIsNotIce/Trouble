import pygame
import os
# Display is 800 x 800

green_piece_path = os.path.join("assets", "green_piece.png")
piece = pygame.image.load(green_piece_path)


def display_player_pieces(w):
    w.blit(piece, (125, 125))