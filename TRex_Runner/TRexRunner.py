import pygame, sys
pygame.init()

from utilities.settings import *
from game_assets.game_over_screen import draw_game_over
from game_assets.background import draw_background
from game_assets.clouds import draw_clouds
from game_assets.ground import draw_ground
from game_assets.trex import draw_trex, get_trex_rect
from game_assets.obstacles import draw_cactus, get_cactus_rect, reset_cactus

# game window settings
SCREEN = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(GAMETITLE)
clock = pygame.time.Clock()
GAME_OVER = True


def main():
    # game loop
    while True:
        check_events()

        if GAME_OVER:
            draw_game_over(SCREEN)
        else:
            # draw mountains and sky
            draw_background(SCREEN)
            draw_clouds(SCREEN)

            # draw ground
            draw_ground(SCREEN)
            draw_cactus(SCREEN)

            # draw trex
            draw_trex(SCREEN)

            check_collisions()

        pygame.display.update()
        clock.tick(FPS)


def check_events():
    global GAME_OVER

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_game()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            close_game()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            reset_cactus()
            GAME_OVER = False


def check_collisions():
    global GAME_OVER

    trex_rect = get_trex_rect()
    cactus_rect = get_cactus_rect()

    if trex_rect.colliderect(cactus_rect):
        GAME_OVER = True


def close_game():
    pygame.quit()
    sys.exit()


main()
