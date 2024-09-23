import pygame

pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

WIDTH, HEIGHT = 1200, 700

ROWS = 50
COLS = 100

TOOLBAR_HEIGHT = 100

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("calibri", size)