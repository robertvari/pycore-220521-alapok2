import pygame, sys
pygame.init()

from utilities.settings import *

# game window settings
SCREEN = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(GAMETITLE)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)