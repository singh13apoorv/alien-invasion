import sys
import pygame
from settings import Settings


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

    def run_game(self):
        """start the main loop for the game.
        """

        while True:

            # watch for keyboard and mouse entry.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redrawing the screen in each iteration of while loop
            self.screen.fill(self.settings.bg_color)

            # make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == "__main__":
    # make game instance
    ai = AlienInvasion()
    ai.run_game()
