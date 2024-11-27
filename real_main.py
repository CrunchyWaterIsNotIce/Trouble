import pygame

from real_game import game

def main():
    pygame.init()
    
    window = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    
    game(window, clock)
    

    pygame.quit()


if __name__ == "__main__":
    main()