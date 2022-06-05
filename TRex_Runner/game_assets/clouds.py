import pygame
from utilities.resources import get_resource


CLOUDS = pygame.image.load(get_resource("clouds.png"))


def draw_clouds(screen):
    screen.blit(CLOUDS, (0, 0))