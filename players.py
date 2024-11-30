import pygame
import os
# Display is 800 x 800

# File Path for Assets
blue_piece_path = os.path.join("assets", "blue_piece.png")
hightlight_b_piece_path = os.path.join("assets", "highlighted_blue_piece.png")
green_piece_path = os.path.join("assets", "green_piece.png")
highlight_g_piece_path = os.path.join("assets", "highlighted_green_piece.png")
red_piece_path = os.path.join("assets", "red_piece.png")
highlight_r_piece_path = os.path.join("assets", "highlighted_red_piece.png")
yellow_piece_path = os.path.join("assets", "yellow_piece.png")
highlight_y_piece_path = os.path.join("assets", "highlighted_yellow_piece.png")

# Loading Assets
blue_piece = pygame.transform.scale_by(pygame.image.load(blue_piece_path), 1.2)
highlighted_blue_piece = pygame.image.load(hightlight_b_piece_path)
green_piece = pygame.image.load(green_piece_path)
highlighted_green_piece = pygame.image.load(highlight_g_piece_path)
red_piece = pygame.image.load(red_piece_path)
highlighted_red_piece = pygame.image.load(highlight_r_piece_path)
yellow_piece = pygame.image.load(yellow_piece_path)
highlighted_yellow_piece = pygame.image.load(highlight_y_piece_path)

players = {
    1 : [[blue_piece, highlighted_blue_piece], # Piece Image - Index 0
                [pygame.Vector2(640, 70), pygame.Vector2(640, 70), False], # Piece 1 - Index 1 -> [Current Position, Reset Position, selectable]
                [pygame.Vector2(660, 90), pygame.Vector2(660, 90), False], # Piece 2 - Index 2 etc.
                [pygame.Vector2(680, 110), pygame.Vector2(640, 110), False],
                [pygame.Vector2(700, 130), pygame.Vector2(700, 130), False]
                ],
    2 : [[red_piece, highlighted_red_piece],
                [pygame.Vector2(700, 630), pygame.Vector2(700, 630), False],
                [pygame.Vector2(680, 650), pygame.Vector2(680, 650), False],
                [pygame.Vector2(660, 670), pygame.Vector2(660, 670), False], 
                [pygame.Vector2(640, 690), pygame.Vector2(640, 690), False], 
                ],
    3 : [[green_piece, highlighted_green_piece],
                [pygame.Vector2(60, 630), pygame.Vector2(60, 630), False],
                [pygame.Vector2(80, 650), pygame.Vector2(80, 650), False],
                [pygame.Vector2(100, 670), pygame.Vector2(100, 670), False], 
                [pygame.Vector2(120, 690), pygame.Vector2(120, 690), False], 
                ],
    4 : [[yellow_piece, highlighted_yellow_piece],
                [pygame.Vector2(120, 70), pygame.Vector2(120, 70), False],
                [pygame.Vector2(100, 90), pygame.Vector2(100, 90), False],
                [pygame.Vector2(80, 110), pygame.Vector2(80, 110), False],
                [pygame.Vector2(60, 130), pygame.Vector2(60, 130), False]
                ]
}

# def get_pieces_on_field(player_num):
#     field_pieces = [] # piece numbers
    
#     for i in range(1, 5): # Going through pieces 1 to 4
#         piece = players[player_num][i]
#         if piece[0] != piece[1]: # Checks if piece's current position is not at the reset position
#             field_pieces.append(i) # Appends the piece

#     return field_pieces

def toggle_selectable_piece(current_player): # ONLY CALLED IF THEY ROLLED A 6
    # Goes through each piece of curent_player and toggles selectable (for the latest piece not on the board yet)
    for i in range(1,5):
        # Checks if the current position of piece is the same as its reset position, and if it isn't already selectable
        if players[current_player][i][0] == players[current_player][i][1]: 
            if players[current_player][i][2] == False:
                players[current_player][i][2] = True
            else: # Called if the player doesn't decide to move their piece from home when they roll a 6
                players[current_player][i][2] = False
            break

def move_piece(mouse_coords, current_player):
    raise NotImplementedError

def display_player_pieces(window, current_player = 0):
    for player_num in range(1, 5):
        for i in range(1, 5): # Going through pieces 1 to 4
            if players[player_num][i][2] and player_num == current_player: # Checks if piece is selectable for the current player
                # Draws the highlighted piece onto window
                window.blit(players[player_num][0][1], players[player_num][i][0])
            else: # Draws the rest of the pieces
                # Draws the regular piece onto window
                window.blit(players[player_num][0][0], players[player_num][i][0])