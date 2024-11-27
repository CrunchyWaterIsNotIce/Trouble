import pygame
import os
# Display is 800 x 800

blue_piece_path = os.path.join("assets", "blue_piece.png")
green_piece_path = os.path.join("assets", "green_piece.png")
red_piece_path = os.path.join("assets", "red_piece.png")
yellow_piece_path = os.path.join("assets", "yellow_piece.png")

blue_piece = pygame.image.load(blue_piece_path)
green_piece = pygame.image.load(green_piece_path)
red_piece = pygame.image.load(red_piece_path)
yellow_piece = pygame.image.load(yellow_piece_path)


players = {
    "Player 1" : [blue_piece, # Piece Image
                [pygame.Vector2(640, 70), pygame.Vector2(640, 70)], # Piece 1 : Current Position - 0, Reset Position
                [pygame.Vector2(660, 90), pygame.Vector2(660, 90)], # Piece 2 etc
                [pygame.Vector2(680, 110), pygame.Vector2(640, 110)],
                [pygame.Vector2(700, 130), pygame.Vector2(700, 130)]
                ],
    "Player 2" : [red_piece, # Piece Image
                [pygame.Vector2(700, 630), pygame.Vector2(620, 630)], # Piece 1 : Current Position - 0, Reset Position
                [pygame.Vector2(680, 650), pygame.Vector2(640, 650)], # Piece 2 etc
                [pygame.Vector2(660, 670), pygame.Vector2(660, 670)], 
                [pygame.Vector2(640, 690), pygame.Vector2(640, 690)], 
                ],
    "Player 3" : [green_piece, # Piece Image
                [pygame.Vector2(60, 630), pygame.Vector2(60, 630)], # Piece 1 : Current Position - 0, Reset Position
                [pygame.Vector2(80, 650), pygame.Vector2(80, 650)], # Piece 2 etc
                [pygame.Vector2(100, 670), pygame.Vector2(100, 670)], 
                [pygame.Vector2(120, 690), pygame.Vector2(120, 690)], 
                ],
    "Player 4" : [yellow_piece, # Piece Image
                [pygame.Vector2(120, 70), pygame.Vector2(120, 70)], # Piece 1 : Current Position - 0, Reset Position - 1
                [pygame.Vector2(100, 90), pygame.Vector2(100, 90)], # Piece 2 etc
                [pygame.Vector2(80, 110), pygame.Vector2(80, 110)],
                [pygame.Vector2(60, 130), pygame.Vector2(60, 130)]
                ]
}


def display_player_pieces(w):
    for player in players:
        for i in range(1, 5): # Going through pieces 1 to 4
            w.blit(players[player][0], players[player][i][0])