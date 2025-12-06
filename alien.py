import pygame


class Alien:
    def __init__(self, image_path, screen_width, y_pos):
        
        # Load alien image
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        # Position alien near the top of the screen
        self.rect.centerx = screen_width // 2
        self.rect.y = y_pos

    def draw(self, screen):
        # Draw the alien
        screen.blit(self.image, self.rect)


