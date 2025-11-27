import pygame
import sys
from ship import Ship

pygame.init()

# Set up the display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

COLOUR = (0, 0, 0)

# Create ship instance
ship = Ship("images/ship.bmp", SCREEN_WIDTH, SCREEN_HEIGHT)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # continuous movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.move_left()
    if keys[pygame.K_RIGHT]:
        ship.move_right()
    
    # Fill the screen
    screen.fill(COLOUR)
    
    # Draw the ship
    ship.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

