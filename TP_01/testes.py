import pygame

available = pygame.font.get_fonts()

for font in available:
    print(font)
