import pygame, os, sys
from constants import *
from game_handler import Game_Manager


class Start_Menu:

    """
    Class Start_Menu
    """

    def __init__(self):
        pygame.init()
        self.field = pygame.display.set_mode(FIELD_SIZE)
        pygame.display.set_caption("Head Soccer")

        self.background = pygame.image.load(os.path.join(IMAGES, BACKGROUND_IMAGE))
        self.background = pygame.transform.scale(self.background, FIELD_SIZE)

        self.start_button = pygame.Rect((0, 0), BUTTON_SIZE)
        self.start_button.center = BUTTON_POSITION
        self.start_button_text = FONT.render("Start the Game!", 1, (0, 0, 0))
        self.caption = FONT_CAPTION.render("Head Soccer", 1, (0, 0, 0))
        self.caption_rect = self.caption.get_rect(center=CAPTION_POSITION)

        self.start_menu_loop()


    def start_menu_loop(self):
        while 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.start_button.collidepoint(mouse_pos):
                button_color = (175, 175, 175)
            else:
                button_color = WHITE

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.start_button.collidepoint(event.pos):
                            game = Game_Manager(self.field)

            self.field.blit(self.background, (0, 0))
            self.field.blit(self.caption, self.caption_rect)
            pygame.draw.rect(self.field, button_color, self.start_button)
            self.field.blit(self.start_button_text, BUTTON_TEXT_POSITION)

            pygame.display.flip()
