import sys
import pygame


class AlienInvasion:
    """Overall class to manage game assets and behavior.
    """

    def __init__(self):
        """Initialize the game, and create resources.
        """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # setting the background color
        self.bg_color = (120, 131, 75)

    def run_game(self):
        """start the main loop for the game.
        """

        while True:

            # watch for keyboard and mouse entry.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redrawing the screen in each iteration of while loop
            self.screen.fill(self.bg_color)

            # make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == "__main__":
    # make game instance
    ai = AlienInvasion()
    ai.run_game()