import pygame
from utilities.resources import get_resource

TREX_RUN = [
    pygame.image.load(get_resource("trex_run_01.png")),
    pygame.image.load(get_resource("trex_run_02.png")),
]

TREX_JUMP = pygame.image.load(get_resource("trex_jump.png"))

FRAME = 0
ANIM_SPEED = 0.2
GROUND_POS = 260
TREX_IMAGE = TREX_RUN[FRAME]
TREX_RECT = TREX_IMAGE.get_rect(y=GROUND_POS)


def draw_trex(screen):
    global FRAME, TREX_IMAGE

    FRAME += ANIM_SPEED
    if FRAME >= len(TREX_RUN):
        FRAME = 0

    TREX_IMAGE = TREX_RUN[int(FRAME)]

    screen.blit(TREX_IMAGE, TREX_RECT)
    pygame.draw.rect(screen, "blue", TREX_RECT, 3)


def get_trex_rect():
    return TREX_RECT