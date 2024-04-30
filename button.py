import pygame

class Button:

    def __init__(self, t_game, msg):
        """Initialize button attributes"""
        self.screen = t_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (21, 34, 48)
        self.text_color = (255, 255, 255)
        self.text_color_hover = (0, 255, 0)
        self.font = pygame.font.Font('Leorio.ttf', 50)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg in to a rendered image and center text on the button"""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def prep_hovered_msg(self, msg):
        """Turn msg in to a rendered image with different coloured text for 
        when mouse hovers over play button."""
        self.msg_image = self.font.render(
            msg, True, self.text_color_hover, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then the message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

   

        
