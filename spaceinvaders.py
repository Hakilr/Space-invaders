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

def move_ship_left():
    # Check if ship would go beyond left boundary
    if ship_rect.left > 0:
        ship_rect.centerx -= 5

def move_ship_right():
    # Check if ship would go beyond right boundary
    if ship_rect.right < SCREEN_WIDTH:
        ship_rect.centerx += 5

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
        move_ship_left()
    if keys[pygame.K_RIGHT]:
        move_ship_right()
    
    # Fill the screen
    screen.fill(COLOUR)
    
    # Draw the ship
    screen.blit(ship_image, ship_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

