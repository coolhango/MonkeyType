
import sys 
import pygame
from settings import Settings
from game_stats import GameStats
from score_screen import ScoreScreen
from text import Text
from button import Button

class Typist:
    """Class to manage assets and behaviour of the game"""

    def __init__(self):
        """Initialize the game and resources"""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Typist")

        # Initializing instances of Text, GameStats, and ScoreScreen for use.
        self.stats = GameStats(self)
        self.text = Text(self)
        self.score_screen = ScoreScreen(self)

        # Creating a play button for the beginning of the game and for 
        # playing again. 
        self.play_button = Button(self, 'Play')
        self.again_button = Button(self, 'Play again')
        
    def run_game(self):
        """Start the loop for the game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Repond to keypresses and mouse events."""
        # Listening for keyboard and mouse events. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if self.text.current_index < len(self.text.text):
                    if event.unicode == (
                        self.text.text[self.text.current_index]):
                        self.text.current_index += 1
                        # Start timer once first letter has been typed.
                        if self.text.current_index == 1:
                            self.score_screen.start_time = (
                            pygame.time.get_ticks())
                        # End the timer once the last letter has been typed.
                        if self.text.current_index == len(self.text.text):
                            self.score_screen.end_time = (
                            pygame.time.get_ticks())
            # Move to score screen if last character is typed.
            if self.text.current_index == len(self.text.text):
                self.stats.round_over = True
            # Check if play button is clicked.
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_again_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True
                
    def check_mouse_hover_play(self):
        """Displays green text if mouse if hovered over play button"""
        mouse_pos = pygame.mouse.get_pos()
        # Call for green message to be displayed if mouse hovered.
        if self.play_button.rect.collidepoint(mouse_pos):
            self.play_button.prep_hovered_msg('Play')
        else:
            self.play_button.prep_msg('Play')

    def _check_again_button(self, mouse_pos):
        """Start the game again if the player clicks 'play again'"""
        if self.stats.round_over:
            if self.again_button.rect.collidepoint(mouse_pos):
                self.stats.round_over = False
                self.text.reset_text()
                self.stats.game_active = True

    def check_mouse_hover_again(self):
        mouse_pos = pygame.mouse.get_pos()
        # Call for green message to be displayed if mouse hovered.
        if self.again_button.rect.collidepoint(mouse_pos):
            self.again_button.prep_hovered_msg('Play again')
        else:
            self.again_button.prep_msg('Play again')

    def _get_word_count(self):
        """Gets the word count of the string currently displayed on screen"""
        # A word counts as 5 characters.
        self.score_screen.word_count = int((len(self.text.text)) / 5)
        
    def _update_screen(self):
        """Update images on screen, and flip to the new screen"""
        # If game active, draw background colour, blit current text to screen, 
        # calculate word count. 
        if self.stats.game_active:
            self.screen.fill(self.settings.bg_color)
            self.text.blitme()
            self._get_word_count()
    
        # If typing is finished, move to score screen.
        if self.stats.round_over == True:
            self.score_screen.display_score()
            self.again_button.draw_button()
            self.check_mouse_hover_again()

        # If game inactive, display play button.
        if not self.stats.game_active:
            self.screen.fill(self.settings.bg_color)
            self.check_mouse_hover_play()
            self.play_button.draw_button()
        
        # Makes drawn screen visible.
        pygame.display.flip()
        self.score_screen.clock.tick(60)

if __name__ == '__main__':
    # Make game instance and run the game.
    ai = Typist()
    ai.run_game()
