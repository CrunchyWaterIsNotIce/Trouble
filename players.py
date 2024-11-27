import pygame
# Display is 800 x 800

players = {} # key-> Player n : value-> [color, position]
players["Player 1"] = ["#2acffc", pygame.Vector2(725, 25)]  # startin from upper right
players["Player 2"] = ["#fc3a2a", pygame.Vector2(725, 725)]
players["Player 3"] = ["#89e935", pygame.Vector2(25, 725)]
players["Player 4"] = ["#e9e135", pygame.Vector2(75, 75)]

def display_players(w):
    pygame.draw.circle(w, players["Player 1"][0], players["Player 1"][1], 10) # surface, color, center, radius
    pygame.draw.circle(w, players["Player 2"][0], players["Player 2"][1], 10)
    pygame.draw.circle(w, players["Player 3"][0], players["Player 3"][1], 10)
    pygame.draw.circle(w, players["Player 4"][0], players["Player 4"][1], 10)


