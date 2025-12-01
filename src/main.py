# main.py
# This file contains the main game loop and initializes the game.

import pygame
from player import Player
from platform import Platform
from enemy import Enemy
from key import Key
from settings import *

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Game")

# Font
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

# Game variables
score = 0
start_time = pygame.time.get_ticks()
game_over = False
game_won = False

# Create sprite groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()
keys_group = pygame.sprite.Group()

# Create the player
player = Player(100, SCREEN_HEIGHT - 100)
all_sprites.add(player)

# Create platforms
level = [
    (0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40),
    (200, SCREEN_HEIGHT - 150, 200, 20),
    (500, SCREEN_HEIGHT - 250, 150, 20),
]
for plat in level:
    p = Platform(*plat)
    all_sprites.add(p)
    platforms.add(p)

# Create enemies
enemy = Enemy(300, SCREEN_HEIGHT - 80)
all_sprites.add(enemy)
enemies.add(enemy)

# Create keys
key = Key(600, SCREEN_HEIGHT - 300)
all_sprites.add(key)
keys_group.add(key)
total_keys = 1

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic update
    if not game_over and not game_won:
        # Get pressed keys
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            player.move(-PLAYER_SPEED)
        if keys_pressed[pygame.K_RIGHT]:
            player.move(PLAYER_SPEED)
        if keys_pressed[pygame.K_SPACE]:
            player.jump()

        # Update all sprites
        keys_before_update = len(keys_group)
        all_sprites.update(platforms, enemies, keys_group)
        # Check if a key was collected
        if len(keys_group) < keys_before_update:
            score += 10
            # Check for win condition
            if score >= total_keys * 10:
                game_won = True

        # Check for player collision with enemies
        if pygame.sprite.spritecollide(player, enemies, False):
            game_over = True

        # Drawing
        screen.fill(WHITE)
        all_sprites.draw(screen)

        # Display score and time
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        score_text = font.render(f"Score: {score}", True, BLACK)
        time_text = font.render(f"Time: {elapsed_time}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 50))

    else:
        # Game over or game won screen
        screen.fill(WHITE)
        if game_over:
            message = "Game Over"
        else:
            message = "You Win!"
        text = game_over_font.render(message, True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
