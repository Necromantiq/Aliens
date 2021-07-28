import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        # Флаг перемещения
        self.moving_right = False
        pygame.display.set_caption("Alien Invasion")

    
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    #sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.rect.x += 10
                    if event.key == pygame.K_LEFT:
                        self.ship.rect.x -= 10

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right:
            self.rect.x += 1


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


    def run_game(self):
        """Start the main loop for the game."""
        self.running = True
        while self.running:
            # Watch for keyboard and mouse events.
            self._check_events()

            # Redraw the screen during each pass through the loop.
            self._update_screen()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
