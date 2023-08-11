import sys
import pygame
from settings import Settings
from ship import Ship
from ufo import Ufo


class AlienInvasion:
    """Overall class to manage game assets and behavior.
    """

    def __init__(self):
        """Initialize the game, and create resources.
        """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        # self.ufo = Ufo(self)

    def run_game(self):
        """start the main loop for the game.
        """

        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # watch for keyboard and mouse entry.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event=event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event=event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
            self.ship.moving_right = True
        elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key release."""
        if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
            self.ship.moving_right = False
        elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # redrawing the screen in each iteration of while loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # self.ufo.blitme()

        # make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    # make game instance
    ai = AlienInvasion()
    ai.run_game()
