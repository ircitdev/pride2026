# player.py
# This file contains the Player class.

import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    """
    Represents the player character.
    """
    def __init__(self, x, y):
        """
        Initialize the player.
        Args:
            x (int): The x-coordinate of the player.
            y (int): The y-coordinate of the player.
        """
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_y = 0
        self.on_ground = False

    def update(self, platforms, enemies, keys):
        """
        Update the player's state.
        Args:
            platforms (pygame.sprite.Group): A group of platform sprites.
            enemies (pygame.sprite.Group): A group of enemy sprites.
            keys (pygame.sprite.Group): A group of key sprites.
        """
        # Apply gravity
        self.velocity_y += PLAYER_GRAVITY
        if self.velocity_y > 10:
            self.velocity_y = 10
        self.rect.y += self.velocity_y

        # Check for collisions with platforms
        self.on_ground = False
        hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for hit in hit_list:
            # If the player is falling, snap to the top of the platform
            if self.velocity_y > 0:
                self.rect.bottom = hit.rect.top
                self.on_ground = True
                self.velocity_y = 0

        # Check for collisions with keys (and remove them)
        pygame.sprite.spritecollide(self, keys, True)

    def move(self, dx):
        """
        Move the player horizontally.
        Args:
            dx (int): The change in the x-coordinate.
        """
        self.rect.x += dx

    def jump(self):
        """
        Make the player jump.
        """
        if self.on_ground:
            self.velocity_y = PLAYER_JUMP_SPEED
            self.on_ground = False

    def draw(self, screen):
        """
        Draw the player on the screen.
        Args:
            screen (pygame.Surface): The screen to draw on.
        """
        screen.blit(self.image, self.rect)
