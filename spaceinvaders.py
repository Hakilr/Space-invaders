import pygame
import sys
from ship import Ship

class Space_Invaders:
    def __init__(self):
        pygame.init()
        
        # Set up the display
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Space Invaders")
        
        self.COLOUR = (0, 0, 0)
        
        # Create ship instance
        self.ship = Ship("images/ship.bmp", self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        
        self.clock = pygame.time.Clock()
        self.running = True
    
    def run(self):
        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # continuous movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.ship.move_left()
            if keys[pygame.K_RIGHT]:
                self.ship.move_right()
            
            # Fill the screen
            self.screen.fill(self.COLOUR)
            
            # Draw the ship
            self.ship.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

si = Space_Invaders()
si.run()
