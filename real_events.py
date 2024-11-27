import pygame

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "CLOSE"
        if event.type == pygame.MOUSEBUTTONUP:
            return "MOUSERELEASE"

    return None