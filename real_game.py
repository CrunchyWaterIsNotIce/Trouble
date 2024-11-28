import pygame
import random
# Display is 800 x 800
from real_events import events
from real_board import display_board
from real_players import display_player_pieces

class TroubleGame:
    def __init__(self, window, clock):

        self.window = window
        self.clock = clock
        # HOW ITS RUNNED
        self.running = True
        
        self.game_state = "Choosing Player"
        self.moves_of_players = {
            "Player 1": 0,
            "Player 2": 0,
            "Player 3": 0,
            "Player 4": 0
        }
        
        # 1 to 4 inclusive
        self.current_player_number = 1

    def next_player(self):
        self.current_player_number += 1
        if self.current_player_number > 4:
            self.current_player_number = 1
    
    def roll_dice(self):
        return random.randint(1, 6)

    # Game loop
    def run(self):
        while self.running:
            dt = self.clock.tick(60)
            
            self.handle_events()
            self.update_display()

    # Events
    def handle_events(self):
        event = events()
        if event == "CLOSE":
            self.running = False
        elif event == "MOUSERELEASE":
            if self.game_state == "Choosing Player":
                
                if self.moves_of_players["Player 4"] == 0:  # If not all players have rolled
                    self.moves_of_players[f"Player {self.current_player_number}"] = self.roll_dice()
                    self.next_player()
                    
                if self.moves_of_players["Player 4"] > 0:  # If all players have rolled
                    for i in range(1, 5): # Loops all players
                        if self.moves_of_players[f"Player {i}"] > self.moves_of_players[f"Player {self.current_player_number}"]:
                            self.current_player_number = i
                    # current_player_number should be the player who rolled the highest and should start
                    self.game_state = "sigma"
                    print(self.current_player_number, self.moves_of_players)

    # Display
    def update_display(self):
        self.window.fill("white")
        display_board(self.window)
        display_player_pieces(self.window)

        if self.game_state == "Choosing Player":
            font = pygame.font.Font(None, 36)
            text = font.render(f"Player {self.current_player_number}, Click to roll the dice!", True, (0, 0, 0))
            self.window.blit(text, (300, 20))

        pygame.display.flip()
