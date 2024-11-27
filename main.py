import pygame

from game import display_game
from events import game_events

def main():
    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption("Trouble Game")
    
    # Initialize Window and Clock
    window = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    running = True

    # Game state
    game_state = "Choosing Player"

    while running:
        # Handle events
        event_result = game_events(game_state)
        if event_result == "quit":
            running = False
        elif event_result == "mouse_click" and game_state == "Choosing Player":
            # Handle dice roll logic
            print("Dice rolled! Transitioning to Player Turn")
            game_state = "Player Turn"

        # Render the game
        dt = clock.tick(60)  # Delta time
        display_game(window, dt, game_state)

        # Update display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()