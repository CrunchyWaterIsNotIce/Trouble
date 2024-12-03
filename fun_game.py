# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Lorenzo Viray
#               Nathan Francis 
#               Dev Mistry
#               Tadd Pasipanodya
# Section:      521
# Assignment:   Lab Topic 13 Game
# Date:         12/1/24

import pygame, os, random

# ---Initializing Pygame---
pygame.init()

# ---Required Properties---
window = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

# ---File Path for Images---
blue_piece_path = os.path.join("assets", "blue_piece.png")
hightlight_b_piece_path = os.path.join("assets", "highlighted_blue_piece.png")
green_piece_path = os.path.join("assets", "green_piece.png")
highlight_g_piece_path = os.path.join("assets", "highlighted_green_piece.png")
red_piece_path = os.path.join("assets", "red_piece.png")
highlight_r_piece_path = os.path.join("assets", "highlighted_red_piece.png")
yellow_piece_path = os.path.join("assets", "yellow_piece.png")
highlight_y_piece_path = os.path.join("assets", "highlighted_yellow_piece.png")

dice_one_path = os.path.join("assets", "dice_one.png")
dice_two_path = os.path.join("assets", "dice_two.png")
dice_three_path = os.path.join("assets", "dice_three.png")
dice_four_path = os.path.join("assets", "dice_four.png")
dice_five_path = os.path.join("assets", "dice_five.png")
dice_six_path = os.path.join("assets", "dice_six.png")

board_path = os.path.join("assets", "trouble_board.png")

# ---Image Assets---
blue_piece = pygame.image.load(blue_piece_path).convert_alpha()
highlighted_blue_piece = pygame.image.load(hightlight_b_piece_path).convert_alpha()
green_piece = pygame.image.load(green_piece_path).convert_alpha()
highlighted_green_piece = pygame.image.load(highlight_g_piece_path).convert_alpha()
red_piece = pygame.image.load(red_piece_path).convert_alpha()
highlighted_red_piece = pygame.image.load(highlight_r_piece_path).convert_alpha()
yellow_piece = pygame.image.load(yellow_piece_path).convert_alpha()
highlighted_yellow_piece = pygame.image.load(highlight_y_piece_path).convert_alpha()

dice_one = pygame.image.load(dice_one_path).convert_alpha()
dice_two = pygame.image.load(dice_two_path).convert_alpha()
dice_three = pygame.image.load(dice_three_path).convert_alpha()
dice_four = pygame.image.load(dice_four_path).convert_alpha()
dice_five = pygame.image.load(dice_five_path).convert_alpha()
dice_six = pygame.image.load(dice_six_path).convert_alpha()

board = pygame.transform.scale_by(pygame.image.load(board_path), 2.95).convert_alpha()

# ---Game Properties---
players = {
    1 : [[blue_piece, highlighted_blue_piece], #0 [Piece Image, Highlighted Piece Image]
                [pygame.Vector2(640, 60), pygame.Vector2(640, 60), False, 0], #1 Piece 1 - [Current Position, Reset Position, Selectable, Moves]
                [pygame.Vector2(660, 80), pygame.Vector2(660, 80), False, 0], #2 Piece 2 - etc.
                [pygame.Vector2(680, 100), pygame.Vector2(680, 100), False, 0], #3 Piece 3 - etc.
                [pygame.Vector2(700, 120), pygame.Vector2(700, 120), False, 0], #4 Piece 4 - etc.
                0 #5 Current Move
                ],
    2 : [[red_piece, highlighted_red_piece],
                [pygame.Vector2(700, 630), pygame.Vector2(700, 630), False, 0],
                [pygame.Vector2(680, 650), pygame.Vector2(680, 650), False, 0],
                [pygame.Vector2(660, 670), pygame.Vector2(660, 670), False, 0], 
                [pygame.Vector2(640, 690), pygame.Vector2(640, 690), False, 0], 
                0
                ],
    3 : [[green_piece, highlighted_green_piece],
                [pygame.Vector2(60, 630), pygame.Vector2(60, 630), False, 0],
                [pygame.Vector2(80, 650), pygame.Vector2(80, 650), False, 0],
                [pygame.Vector2(100, 670), pygame.Vector2(100, 670), False, 0], 
                [pygame.Vector2(120, 690), pygame.Vector2(120, 690), False, 0], 
                0
                ],
    4 : [[yellow_piece, highlighted_yellow_piece],
                [pygame.Vector2(120, 60), pygame.Vector2(120, 60), False, 0],
                [pygame.Vector2(100, 80), pygame.Vector2(100, 80), False, 0],
                [pygame.Vector2(80, 100), pygame.Vector2(80, 100), False, 0],
                [pygame.Vector2(60, 120), pygame.Vector2(60, 120), False, 0],
                0
                ]
}

dice = [dice_one, dice_two, dice_three, dice_four, dice_five, dice_six]

board_coords = [
    pygame.Vector2(379, 56), pygame.Vector2(478, 60), pygame.Vector2(556, 77), pygame.Vector2(618, 92), 
    pygame.Vector2(650, 125), pygame.Vector2(668, 188), pygame.Vector2(685, 265), pygame.Vector2(685, 364),
    pygame.Vector2(685, 464), pygame.Vector2(667, 541), pygame.Vector2(650, 604), pygame.Vector2(617, 635),
    pygame.Vector2(555, 652), pygame.Vector2(479, 671), pygame.Vector2(378, 674), pygame.Vector2(278, 670),
    pygame.Vector2(202, 653), pygame.Vector2(139, 634), pygame.Vector2(107, 602), pygame.Vector2(90, 541),
    pygame.Vector2(72, 464), pygame.Vector2(72, 364), pygame.Vector2(72, 264), pygame.Vector2(90, 186),
    pygame.Vector2(107, 125), pygame.Vector2(140, 92), pygame.Vector2(201, 73), pygame.Vector2(278, 55)
]
home_coords = {
    1 : [pygame.Vector2(478, 275), pygame.Vector2(515, 239), pygame.Vector2(550, 205), pygame.Vector2(584, 169)], # Blue - First coords is starting FROM the middle going OUT
    2 : [pygame.Vector2(479, 475), pygame.Vector2(515, 511), pygame.Vector2(551, 547), pygame.Vector2(585, 581)], # Red
    3 : [pygame.Vector2(278, 475), pygame.Vector2(243, 510), pygame.Vector2(208, 546), pygame.Vector2(172, 583)], # Green
    4 : [pygame.Vector2(278, 277), pygame.Vector2(243, 241), pygame.Vector2(207, 205), pygame.Vector2(173, 170)], # Yellow
}
game_state = "Choosing Starting Player"
current_player = 1
toggle_instructions = False

# ---Game Functions---
## Game Methods
def roll_dice():
    """ Gets a random number between 1 and 6 (inclusive)

    Returns:
        _Integer_: _A dice roll_
    """
    return random.randint(1, 6)

def display_instructions(w):
    if toggle_instructions:
        w.fill("white")

## Board Methods
def display_board(w):
    """ Draws game board on screen

    Args:
        w (_pygame.display_): _Window_
    """
    w.blit(board, (48, 52))
    
def display_dice(w):
    if players[current_player][5] > 0:  # Check if a dice roll exists for the current player
        dice_index = players[current_player][5] - 1
        w.blit(dice[dice_index], (350, 300))  # Display dice at the center

## Player Methods
def display_players(w): # w -> Window
    for player_num in players:
        for piece_num in range(1, 5): # Going through Pieces 1-4
            if players[player_num][piece_num][2] and current_player == player_num and players[current_player][5] > 0: # If piece is selectable and is the current player
                choosen_piece_image = players[player_num][0][1] # Gets Highlighted Piece
            else:
                choosen_piece_image = players[player_num][0][0] # Gets Regular Piece
            
            w.blit(choosen_piece_image, players[player_num][piece_num][0]) # Draws piece onto window at current piece's position vector
            
def check_player_collisions(pos, curr): # pos -> Position, curr -> Current Player
    """ Goes through all player pieces and finds if the 
    current_player's piece collides with another.

    Args:
        pos (_pygame.Vector2_): _(new) position of current_player_
        curr (_Integer_): _essentially current_player_

    Returns:
        _Boolean_: _If collision occurs_
        _Tuple_: _Player and piece number of collided_
    """
    for player_num in players:
        for piece_num in range(1, 5):
            if players[player_num][piece_num][0] == pos:
                return True, (player_num, piece_num)
    return False, None
    
def next_player(curr): # curr -> Current Player
    if curr == 4:
        return 1
    return curr + 1

# ---Game Loop---
while running:
    # ---Event Handling---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
            # players[current_player][1][0] = mouse_pos
            # print(mouse_pos)
            if game_state == "Choosing Starting Player":
                
                    
                if players[4][5] == 0: # Checking if every player hasn't rolled yet(If player 4's current move is 0)
                    if players[current_player][5] == 0:
                        players[current_player][5] = roll_dice() # Then assign their current move from rolling a dice
                    else:
                        current_player = next_player(current_player) # Increment current_player
                else: # Checking if every player HAS rolled (If player 4's current move is not 0, meaning all players have rolled)
                    for player_num in players:
                        players[player_num][5] = 0 # Resets current moves of all players to start the game
                    
                    game_state = "Player's Turn"
                
                if players[4][5] > 0: # AUTOMATICALLY CHECK
                    for player_num in players: # Loops through all current moves(roll) of players and finds the player with the largest roll
                        if players[player_num][5] > players[current_player][5]: # If it(looping player) is higher than the current_player, then replace
                            current_player = player_num
                    
            if game_state == "Player's Turn":
                if players[current_player][5] == 0: # If players current move is 0
                    roll = roll_dice()
                    players[current_player][5] = roll
                    
                    if roll == 6:
                        for piece_num in range(1, 5):  # Check for pieces at home
                            if players[current_player][piece_num][0] == players[current_player][piece_num][1]:
                                players[current_player][piece_num][2] = True  # Make a home piece selectable
                                break
                else:
                    all_pieces_at_home = all(players[current_player][piece_num][0] == players[current_player][piece_num][1] for piece_num in range(1, 5))  
                        
                    if all_pieces_at_home and roll != 6: # Beginning of Game
                        players[current_player][5] = 0  # Reset current move
                        current_player = next_player(current_player)
                    else:
                        for piece_num in range(1, 5):
                            piece_pos = players[current_player][piece_num][0]
                            reset_pos = players[current_player][piece_num][1]
                            selectable = players[current_player][piece_num][2]
                            

                            if selectable and mouse_pos.distance_to(piece_pos) < 40:  # Check if a selectable piece was clicked
                                current_roll = players[current_player][5]
                                

                                if piece_pos == reset_pos:  # Move piece out of home base
                                    new_pos = board_coords[(4 + (current_player - 1) * 7) % len(board_coords)] # Starting position
                                    players[current_player][piece_num][3] += 1 # Adds to Total Moves  
                                else: 
                                    if players[current_player][piece_num][3] + current_roll > 28: # Checks if piece does a full loop
                                        potential_home_index = players[current_player][piece_num][3] % 28
                                        occupied_home_index = -1
                                        
                                        for other_piece_num in range(1, 5): # Finds the latest occupied spot in finish line
                                            if other_piece_num != piece_num:
                                                for coord in range(4):
                                                    if players[current_player][other_piece_num][0] == home_coords[current_player][coord]:
                                                        occupied_home_index = coord
                                                        
                                        if occupied_home_index != -1: # If there ARE spots occupied in finish line
                                            # Go to the next spot
                                            occupied_home_index += 1
                                        else:
                                            # Start spot
                                            occupied_home_index = 0
                                        
                                        if potential_home_index == occupied_home_index: # Check if the potential index rolled is exactly in the finish line
                                            new_pos = home_coords[current_player][occupied_home_index] # Piece goes into finish line
                                            players[current_player][piece_num][2] = False
                                        else:
                                            new_pos = piece_pos # Piece can't move

                                            
                                    else: # Checks if piece is just moving
                                        next_index = (board_coords.index(piece_pos) + current_roll) % len(board_coords)
                                        new_pos = board_coords[next_index] # Gets New Position
                                        players[current_player][piece_num][3] += current_roll # Adds to Total Moves
                                    
                                    
                                # Not needed? v
                                if current_roll == 6: ## EDGE CASE - If a player chooses to move a piece on board instead of a piece out of home, deselect all pieces at home
                                    for other_piece_num in range(1, 5):  # Check for pieces at home
                                        if players[current_player][other_piece_num][0] == players[current_player][other_piece_num][1] and other_piece_num != piece_num:
                                            players[current_player][other_piece_num][2] = False
                                    
                                    
                                collided, piece = check_player_collisions(new_pos, current_player) # Checks if position on board is occupied and is selectable(to not touch finish line pieces)
                                if collided: # If so, the initial piece at the position goes back home
                                    if piece[0] == current_player:
                                        players[current_player][piece_num][2] = False
                                    else:
                                        players[piece[0]][piece[1]][0] = players[piece[0]][piece[1]][1] # Resets Position
                                        players[piece[0]][piece[1]][2] = False # Unselected
                                        players[piece[0]][piece[1]][3] = 0 # Total moves is now 0
                                         # Update piece position and reset selectable
                                        players[current_player][piece_num][0] = new_pos
                                        players[current_player][5] = 0  # Reset current move
                                        current_player = next_player(current_player)
                                        break  # Only move one piece per click
                                else:

                                    # Update piece position and reset selectable
                                    players[current_player][piece_num][0] = new_pos
                                    players[current_player][5] = 0  # Reset current move
                                    current_player = next_player(current_player)
                                    break  # Only move one piece per click
                            
                            
                                    
                       
                    
    
    
    # ---Display Handling---
    window.fill("grey")
    display_board(window)
    display_dice(window)
    display_players(window)
    
    if game_state == "Choosing Starting Player":
        if players[4][5] == 0:  # If not all players have rolled
            if players[current_player][5] == 0:
                message = f"Player {current_player}, Click to roll the dice!"
            else:
                message = f"Next player's turn!"
        else:
            message = f"Player {current_player} rolled a {players[current_player][5]}! They are going first, click to start!"
        text = pygame.font.Font(None, 36).render(message, True, (0, 0, 0))
        window.blit(text, (100, 25))
    elif game_state == "Player's Turn":
        if players[current_player][5] == 0:  # Player needs to roll
            message = f"Player {current_player}'s turn!"
            message_two = "Click to roll the dice."
        else:
            message = f"Player {current_player} rolled a {players[current_player][5]}!"
            message_two = "Click on the highlighted piece to move. If they are none, next!"
        text = pygame.font.Font(None, 36).render(message, True, (0, 0, 0))
        text_two = pygame.font.Font(None, 36).render(message_two, True, (0, 0, 0))
        window.blit(text, (100, 0))
        window.blit(text_two, (50, 25))

    
    pygame.display.flip()
        
        
pygame.quit()