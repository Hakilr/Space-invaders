import pygame
import sys

pygame.init()

# Set up the display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")


COLOUR = (0, 0, 0)

# Load ship image
ship_image = pygame.image.load("images/ship.bmp")
ship_rect = ship_image.get_rect()

# Position ship at the bottom center of the screen
ship_rect.centerx = SCREEN_WIDTH // 2
ship_rect.bottom = SCREEN_HEIGHT

# Main game loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen
    screen.fill(COLOUR)
    
    # Draw the ship
    screen.blit(ship_image, ship_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()

