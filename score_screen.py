import pygame
from settings import Settings
from text import Text

class ScoreScreen:
    """Displays a score screen when quote is completed"""

    def __init__(self, t_game):
        """Initialize class attributes"""
        self.screen = t_game.screen
        self.screen_rect = t_game.screen.get_rect()
        self.settings = t_game.settings
        self.font = pygame.font.Font('Leorio.ttf', 50)
        self.color = self.settings.bg_color
        self.text_color = (255, 255, 255)

        # For calculating WPM
        self.start_time = None
        self.end_time = None
        self.word_count = None

        self.clock = pygame.time.Clock()

    def display_score(self):
        """Display WPM and give an option to play again"""
        self.total_time = self.end_time - self.start_time
        self.minute_time = self.total_time / 60_000
        self.wpm = int(self.word_count / self.minute_time)
        msg = "WPM: " + str(self.wpm)
        self.screen.fill(self.color)
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.midtop = self.screen_rect.midtop
        self.screen.blit(self.msg_image, self.msg_image_rect)





