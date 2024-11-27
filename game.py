import pygame
import random

from board import display_board
from players import display_players

# Game variables
current_player = None
moves = {}  # "Player n" : 1-6


# Called by main to manage the game
def display_game(w, dt, state):  # w - window, dt - delta time, state - game state
    w.fill("white")

    # Renders board and players
    display_board(w)
    display_players(w)

    # # Game logic based on state
    # if state == "Choosing Player":
        
