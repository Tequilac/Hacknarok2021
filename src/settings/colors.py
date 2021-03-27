from enum import Enum
import pygame


class Colors(Enum):
    SHADOW = pygame.color.Color((192, 192, 192))
    WHITE = pygame.color.Color((255, 255, 255))
    LIGHTGREEN = pygame.color.Color((0, 255, 0))
    GREEN = pygame.color.Color((0, 200, 0))
    BLUE = pygame.color.Color((0, 0, 128))
    LIGHTBLUE = pygame.color.Color((0, 0, 255))
    RED = pygame.color.Color((200, 0, 0))
    LIGHT_RED = pygame.color.Color((255, 100, 100))
    PURPLE = pygame.color.Color((102, 0, 102))
    LIGHT_PURPLE = pygame.color.Color((153, 0, 153))
    BLACK = pygame.color.Color((0, 0, 0))
    VERY_LIGHT_BLUE = pygame.color.Color((124, 210, 249, 100))

