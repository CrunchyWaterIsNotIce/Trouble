import pygame

def game_events(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "quit"
        

        if state == "Choosing Player":
            if event.type == pygame.MOUSEBUTTONUP:
                print("Mouse click detected in Choosing Player state")
                return "mouse_click"

        if state == "Player Turn":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Example: Roll dice
                    print("Space key pressed during Player Turn")
                    return "roll_dice"

    return None 
