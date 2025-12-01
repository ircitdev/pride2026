import sys
import os
# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
import pygame
from player import Player
from enemy import Enemy
from key import Key
from platform import Platform
from settings import *

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.player = Player(100, 100)
        self.enemy = Enemy(100, 100)
        self.key = Key(200, 200)
        self.platform = Platform(100, 200, 100, 20)

    def test_player_jump(self):
        self.player.on_ground = True
        self.player.jump()
        self.assertEqual(self.player.velocity_y, PLAYER_JUMP_SPEED)
        self.assertFalse(self.player.on_ground)

    def test_player_move(self):
        initial_x = self.player.rect.x
        self.player.move(PLAYER_SPEED)
        self.assertEqual(self.player.rect.x, initial_x + PLAYER_SPEED)

    def test_player_enemy_collision(self):
        enemies = pygame.sprite.Group()
        enemies.add(self.enemy)
        self.assertTrue(pygame.sprite.spritecollide(self.player, enemies, False))

    def test_player_key_collection(self):
        keys = pygame.sprite.Group()
        keys.add(self.key)
        # Move player to the key's position to trigger a collision
        self.player.rect.x = self.key.rect.x
        self.player.rect.y = self.key.rect.y
        pygame.sprite.spritecollide(self.player, keys, True)
        self.assertEqual(len(keys), 0)

    def test_player_platform_collision(self):
        platforms = pygame.sprite.Group()
        platforms.add(self.platform)
        self.player.rect.y = 180
        self.player.velocity_y = 5
        self.player.update(platforms, pygame.sprite.Group(), pygame.sprite.Group())
        self.assertTrue(self.player.on_ground)
        self.assertEqual(self.player.rect.bottom, self.platform.rect.top)

if __name__ == '__main__':
    unittest.main()
