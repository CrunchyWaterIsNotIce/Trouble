import pygame
import random
# Display is 800 x 800
from board import display_board
from players import display_player_pieces, toggle_selectable_piece

class TroubleGame:
    def __init__(self, window, clock):

        self.window = window
        self.clock = clock
 
        self.running = True
        
        # Game States
        # -----------
        # > None
        # > Choosing Starting Player
        # > Player's Turn
        # >     Player Piece Moves(Out)
        
        self.game_state = "Choosing Starting Player"
        self.moves_of_players = {
            1 : [0, 0], # Player 1 - [Current Move, Total Moves]
            2 : [0, 0], # Player 2 - [Current Move, Total Moves]
            3 : [0, 0], # Player 3 - [Current Move, Total Moves]
            4 : [0, 0]  # Player 4 - [Current Move, Total Moves]
        }
        
        # 1 to 4 inclusive
        self.current_player_number = 1

    def next_player(self):
        self.current_player_number += 1
        if self.current_player_number > 4:
            self.current_player_number = 1
    
    def roll_dice(self):
        return random.randint(1, 6)
    
    def reset_players_moves(self):
        for i in range(1, 5):
            self.moves_of_players[i][0] = 0
            self.moves_of_players[i][1] = 0

    # Game loop
    def run(self):
        while self.running:
            dt = self.clock.tick(60)
            
            self.handle_events()
            self.update_display()

    # Events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONUP:

                mouse_x, mouse_y = event.pos
                
                if self.game_state == "Choosing Starting Player":
                    if self.moves_of_players[4][0] == 0:  # If not all players have rolled
                        self.moves_of_players[self.current_player_number][0] = self.roll_dice()
                        # ANIMATION ------------------------------------------
                        self.next_player()
                    elif self.moves_of_players[4][0] > 0:  # If all players have rolled
                        for i in range(1, 5): # Loops all players
                            if self.moves_of_players[i] > self.moves_of_players[self.current_player_number]:
                                self.current_player_number = i
                        
                        # !!!current_player_number should be the player who rolled the highest and should start!!!
                        # Sets game_state now to the current player's turn and resets the moves for all players
                        self.game_state = "Player's Turn"
                        
                        self.reset_players_moves()
                        
                elif self.game_state == "Player's Turn":
                    roll = 6
                    # Sets current moves
                    self.moves_of_players[self.current_player_number][0] = roll
                    # Adds to total moves
                    self.moves_of_players[self.current_player_number][1] += roll
                    # Toggles the latest piece at home to be selectable
                    if roll == 6:
                        toggle_selectable_piece(self.current_player_number)
                    # Moves pieces
                    # what if you dont move a piece out of home?
                    # what if there is already a piece
                    
                    
                    
                    
                        
                        
                        
                

    # Display
    def update_display(self):
        self.window.fill("white")
        display_board(self.window)
        display_player_pieces(self.window, self.current_player_number)

        if self.game_state == "Choosing Starting Player":
            if self.moves_of_players[4][0] == 0:
                message = f"Player {self.current_player_number}, Click to roll the dice!"
                center = (240, 20)
            elif self.moves_of_players[4][0] > 0:
                message = f"Player {self.current_player_number} will be going first, Click to continue."
                center = (150, 20)
            text = pygame.font.Font(None, 36).render(message, True, (0, 0, 0))
            self.window.blit(text, center)
        elif self.game_state == "Player's Turn":
            if self.moves_of_players[self.current_player_number][0] == 0:
                message = f"Player {self.current_player_number}'s Turn, Click to roll the dice!"
            else:
                message = f"Test"
            text = pygame.font.Font(None, 36).render(message, True, (0, 0, 0))
            self.window.blit(text, (250, 20))

        pygame.display.flip()
