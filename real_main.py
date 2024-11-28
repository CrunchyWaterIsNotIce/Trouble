import pygame

from real_game import TroubleGame

def main():
    pygame.init()
    
    window = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    
    game = TroubleGame(window, clock)
    game.run()
    

    pygame.quit()


if __name__ == "__main__":
    main()