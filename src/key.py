# key.py
# This file contains the Key class.

import pygame
from settings import *

class Key(pygame.sprite.Sprite):
    """
    Represents a collectible key.
    """
    def __init__(self, x, y):
        """
        Initialize the key.
        Args:
            x (int): The x-coordinate of the key.
            y (int): The y-coordinate of the key.
        """
        super().__init__()
        self.image = pygame.Surface((16, 16))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        """
        The key doesn't move, so its update method is empty.
        """
        pass
