import pygame
from utilities.resources import get_resource


CLOUDS_1 = pygame.image.load(get_resource("clouds.png"))
CLOUDS_1_RECT = CLOUDS_1.get_rect()

CLOUDS_2 = pygame.image.load(get_resource("clouds.png"))
CLOUDS_2_RECT = CLOUDS_2.get_rect(midleft=CLOUDS_1_RECT.midright)

CLOUD_SPEED = 1


def draw_clouds(screen):
    # draw CLOUDS_1
    screen.blit(CLOUDS_1, CLOUDS_1_RECT)
    CLOUDS_1_RECT.x -= CLOUD_SPEED

    if CLOUDS_1_RECT.right <= 0:
        CLOUDS_1_RECT.left = CLOUDS_2_RECT.right

    # debug rect
    # pygame.draw.rect(screen, "red", CLOUDS_1_RECT, 3)

    # draw CLOUDS_2
    screen.blit(CLOUDS_2, CLOUDS_2_RECT)
    CLOUDS_2_RECT.x -= CLOUD_SPEED

    if CLOUDS_2_RECT.right <= 0:
        CLOUDS_2_RECT.left = CLOUDS_1_RECT.right

    # pygame.draw.rect(screen, "blue", CLOUDS_2_RECT, 3)