import pygame
import os
# Display is 800 x 800

# File Path for Assets
blue_piece_path = os.path.join("assets", "blue_piece.png")
green_piece_path = os.path.join("assets", "green_piece.png")
red_piece_path = os.path.join("assets", "red_piece.png")
yellow_piece_path = os.path.join("assets", "yellow_piece.png")

# Loading Assets
blue_piece = pygame.image.load(blue_piece_path)

green_piece = pygame.image.load(green_piece_path)
red_piece = pygame.image.load(red_piece_path)
yellow_piece = pygame.image.load(yellow_piece_path)

players = {
    1 : [[blue_piece, highlighted_blue_piece], # Piece Image - Index 0
                [pygame.Vector2(640, 70), pygame.Vector2(640, 70), False], # Piece 1 - Index 1 -> [Current Position, Reset Position, isOut]
                [pygame.Vector2(660, 90), pygame.Vector2(660, 90), False], # Piece 2 - Index 2 etc.
                [pygame.Vector2(680, 110), pygame.Vector2(640, 110), False],
                [pygame.Vector2(700, 130), pygame.Vector2(700, 130), False]
                ],
    2 : [[red_piece, highlighted_red_piece],
                [pygame.Vector2(700, 630), pygame.Vector2(620, 630), False],
                [pygame.Vector2(680, 650), pygame.Vector2(640, 650), False],
                [pygame.Vector2(660, 670), pygame.Vector2(660, 670), False], 
                [pygame.Vector2(640, 690), pygame.Vector2(640, 690), False], 
                ],
    3 : [[green_piece, highlighted_green_piece],
                [pygame.Vector2(60, 630), pygame.Vector2(60, 630), False],
                [pygame.Vector2(80, 650), pygame.Vector2(80, 650), False],
                [pygame.Vector2(100, 670), pygame.Vector2(100, 670), False], 
                [pygame.Vector2(120, 690), pygame.Vector2(120, 690), False], 
                ],
    4 : [[yellow_piece, highlighted_green_piece],
                [pygame.Vector2(120, 70), pygame.Vector2(120, 70), False],
                [pygame.Vector2(100, 90), pygame.Vector2(100, 90), False],
                [pygame.Vector2(80, 110), pygame.Vector2(80, 110), False],
                [pygame.Vector2(60, 130), pygame.Vector2(60, 130), False]
                ]
}

def get_isOut_pieces(player_num):
    isOut_pieces = [] # piece numbers
    
    for i in range(1, 5): # Going through pieces 1 to 4
        if players[player_num][i][2]: # If piece's isOut property is True
            isOut_pieces.append(i)
    return isOut_pieces

def move_piece(player, piece):
    raise NotImplementedError

def display_player_pieces(window):
    for player_num in range(1, 5):
        for i in range(1, 5): # Going through pieces 1 to 4
            if players[player_num][i][2]: # Checks if piece's isOut property is True 
                # Draws the highlighted piece onto window
                window.blit(players[player_num][0][1], players[player_num][i][0])
            else:
                # Draws the regular piece onto window
                window.blit(players[player_num][0][0], players[player_num][i][0])