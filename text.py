from random import choice
import pygame
import pygame.freetype
from settings import Settings


class Text:
    """A class to manage the quote appearing on screen"""

    def __init__(self, t_game):
        """Initilize colour attributes and set text location"""

        # Assign screen to attribute of Text. 
        # Getting screen rectangle from Typist. 
        self.screen = t_game.screen
        self.screen_rect = t_game.screen.get_rect()
        self.settings = t_game.settings 
        
        # Assigning RGB values to colours.
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.grey = (128,128,128)


    
        # Creating a font instance. And setting text variables.
        self.font = pygame.freetype.Font('leorio.ttf', 32)
        self.font.origin = True
        self.reset_text()


    # 1. Getting a quote from a list.
    # 2. Setting curent index to zero to select 1st index.
    # 3. Calculate dimensions of the text. 
    # 4. Find baseline. font.origin is set to true, so the baseline will
    # be the y-coordinate of the text origin. This function accesses the 
    # 'y' attribute of the text rectangle.
    # 5. Create a surface to render the text on using the size of the 
    # created rect.
    # 6. Fill created surface with background colour.
    # 7. Allign center of text rect with center of screen rect.
    # 8. Calculate width and other metrics of each letter of the text. 
    # Glyph metrics are returned as a list of tuples , with each tuple 
    # giving metrics of single character. Horizontal advance is position 4.
    def reset_text(self): 
        self.text = self.get_random_quote()
        self.current_index = 0
        self.text_rect = self.font.get_rect(self.text) #1
        self.baseline = self.text_rect.y #2
        self.text_surf = pygame.Surface(self.text_rect.size) #3
        self.text_surf.fill(self.settings.bg_color) #4
        self.text_rect.center = self.screen_rect.center #5
        self.metrics = self.font.get_metrics(self.text) #6
    
    def get_random_quote(self):
        """Returns a random quote from a list of quotes."""
        filename = 'quotes.txt'
        with open(filename, 'r', encoding = 'UTF-8') as f:
            lines = f.readlines()
            quote = choice(lines).strip()

        return f'"{quote}"'

    def correct_key_press_colours(self):
        """Causes text on screen to be rendered a certain colour depending on 
        what the current index is"""
        x = 0 
        for (idx, (letter, metric)) in enumerate(zip(self.text, self.metrics)):
            if idx == self.current_index:
                color = self.white
            elif idx < self.current_index:
                color = self.green
            else:
                color = self.grey
            self.font.render_to(
                    self.text_surf, 
                    (x, self.baseline), 
                    letter, color, self.settings.bg_color)
            x += metric[4]

    def blitme(self):
        """Draws text to screen"""
        self.correct_key_press_colours()
        # Blitting text suface to text rectangle size
        self.screen.blit(self.text_surf, self.text_rect)





