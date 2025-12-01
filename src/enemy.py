# enemy.py
# This file contains the Enemy class.

import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    """
    Represents an enemy character that patrols back and forth.
    """
    def __init__(self, x, y):
        """
        Initialize the enemy.
        Args:
            x (int): The x-coordinate of the enemy.
            y (int): The y-coordinate of the enemy.
        """
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.speed = ENEMY_SPEED

    def update(self, *args):
        """
        Update the enemy's position.
        """
        self.rect.x += self.direction * self.speed
        # Reverse direction if the enemy reaches the edge of the screen
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.direction *= -1
