# platform.py
# This file contains the Platform class.

import pygame
from settings import *

class Platform(pygame.sprite.Sprite):
    """
    Represents a stationary platform.
    """
    def __init__(self, x, y, width, height):
        """
        Initialize the platform.
        Args:
            x (int): The x-coordinate of the platform.
            y (int): The y-coordinate of the platform.
            width (int): The width of the platform.
            height (int): The height of the platform.
        """
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        """
        Platforms don't move, so their update method is empty.
        """
        pass
