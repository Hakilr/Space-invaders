import pygame


class Ship:
    def __init__(self, image_path, screen_width, screen_height):
        """Initialize the ship and set its starting position."""
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        
        # Position ship at the bottom center of the screen
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height
        
        self.screen_width = screen_width
    
    def move_left(self):
        """Move the ship to the left."""
        # Check if ship would go beyond left boundary
        if self.rect.left > 0:
            self.rect.centerx -= 5
    
    def move_right(self):
        """Move the ship to the right."""
        # Check if ship would go beyond right boundary
        if self.rect.right < self.screen_width:
            self.rect.centerx += 5
    
    def draw(self, screen):
        """Draw the ship on the screen."""
        screen.blit(self.image, self.rect)

