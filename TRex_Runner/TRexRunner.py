import pygame, sys
pygame.init()

from utilities.settings import *
from utilities.resources import get_resource
from game_assets.background import draw_background
from game_assets.clouds import draw_clouds

# game window settings
SCREEN = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(GAMETITLE)
clock = pygame.time.Clock()


def main():
    # game loop
    while True:
        check_events()

        # graphics, sounds stb...
        SCREEN.fill(SKYCOLOR)

        # draw mountains and sky
        draw_background(SCREEN)
        draw_clouds(SCREEN)


        pygame.display.update()
        clock.tick(FPS)


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_game()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            close_game()


def close_game():
    pygame.quit()
    sys.exit()


main()
