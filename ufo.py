import pygame


class Ufo:
    """A class to manage ufos."""

    def __init__(self, ai_game):
        """Initialize the UFO and set its position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ufo and get its rect.
        self.image = pygame.image.load("./images/ufo-4778062_1920.bmp")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # start the ufo at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ufo at the center of the screen."""
        self.screen.blit(self.image, self.rect)
