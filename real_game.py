import pygame
# Display is 800 x 800
from real_events import events
from real_board import display_board
from real_players import display_player_pieces

# Game States
# -----------
# > None
# > Choosing Player
game_state = ""

def game(w, c): # w - window, c - clock
    
    running = True
    
    while running:
        event = events()
        if event == "CLOSE":
            running = False
        # if event == "MOUSERELEASE" and game_state == "Choosing Player":
            
        w.fill("white")
        display_board(w)
        display_player_pieces(w)
    
    
        # Delta Time
        dt = c.tick(60)
        
        pygame.display.flip()

    
    
    
    