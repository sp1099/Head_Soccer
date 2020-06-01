import pygame, os, sys
from constants import *
from game_handler import Game_Manager


class Start_Menu:

    """
    Class Start_Menu
        Initializes pygame and the Start Screen
        Starts the start_menu_loop which shows the Start Screen
        When the user presses the Start Button an Game Manager object is inizialized which starts the real game

    """

    def __init__(self):
        """
        :description:
            Initializes a Start_Menu Object
            Loads the images
            Renders the font
        :parameter
            None
        :return
            None

        """
        pygame.init()
        self.field = pygame.display.set_mode(FIELD_SIZE)
        pygame.display.set_caption("Head Soccer")

        self.background = pygame.image.load(os.path.join(IMAGES, BACKGROUND_IMAGE))
        self.background = pygame.transform.scale(self.background, FIELD_SIZE)

        # button creation and rendering
        self.start_button = pygame.Rect((0, 0), BUTTON_SIZE)
        self.start_button.center = BUTTON_POSITION
        self.start_button_text = FONT.render("Start the Game!", 1, BLACK)
        self.start_button_text_rect = self.start_button_text.get_rect(center=BUTTON_POSITION)
        # Caption Rendering
        self.caption = FONT_CAPTION.render("Head Soccer", 1, BLACK)
        self.caption_rect = self.caption.get_rect(center=CAPTION_POSITION)

        # lists for player keys fonts and their drawing rects
        self.player1_keys = []
        self.player1_keys_rect = []
        self.player2_keys = []
        self.player2_keys_rect = []
        self.render_player_keys()

        self.start_menu_loop()


    def start_menu_loop(self):
        """
        :description:
            function that runs the start menu loop
            checks for start button click and quit click
                also checks for mouse over button hover
            shows the rendered images and fonts
        :parameter
            None
        :return
            None

        """
        while 1:
            # get mouse pos and check if button rect is hovered
            # changes button color accordingly
            mouse_pos = pygame.mouse.get_pos()
            if self.start_button.collidepoint(mouse_pos):
                button_color = GREY
            else:
                button_color = WHITE

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # check for mouse click
                # starts game if mouse also hovered over button
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.start_button.collidepoint(event.pos):
                            # head soccer game start
                            head_soccer = Game_Manager(self.field)

            # displaying the rendered images and fonts
            self.field.blit(self.background, (0, 0))
            self.field.blit(self.caption, self.caption_rect)
            pygame.draw.rect(self.field, button_color, self.start_button)
            self.field.blit(self.start_button_text, self.start_button_text_rect)
            for i in range(len(self.player1_keys)):
                self.field.blit(self.player1_keys[i], self.player1_keys_rect[i])
                self.field.blit(self.player2_keys[i], self.player2_keys_rect[i])

            pygame.display.flip()

    def render_player_keys(self):
        """
        :description
            outsourced function for clarity of code that renders the player keys
            reason for that: render func does not support newline character
                             Each line therefore is separately rendered and added to a list
        :parameter
            None
        :return:
            None

        """
        self.player1_keys.append(FONT_SCORE.render("PLAYER 1 KEYS:", 1, BLACK))
        self.player1_keys_rect.append(self.player1_keys[0].get_rect(center=PLAYER1_KEYS_POSITION[0]))
        self.player1_keys.append(FONT.render("'A' -> Move Left", 1, BLACK))
        self.player1_keys_rect.append(self.player1_keys[1].get_rect(center=PLAYER1_KEYS_POSITION[1]))
        self.player1_keys.append(FONT.render("'D' -> Move Right", 1, BLACK))
        self.player1_keys_rect.append(self.player1_keys[2].get_rect(center=PLAYER1_KEYS_POSITION[2]))
        self.player1_keys.append(FONT.render("'W' -> JUMP", 1, BLACK))
        self.player1_keys_rect.append(self.player1_keys[3].get_rect(center=PLAYER1_KEYS_POSITION[3]))
        self.player1_keys.append(FONT.render("'SPACEBAR' -> Shoot", 1, BLACK))
        self.player1_keys_rect.append(self.player1_keys[4].get_rect(center=PLAYER1_KEYS_POSITION[4]))

        self.player2_keys.append(FONT_SCORE.render("PLAYER 2 KEYS:", 1, BLACK))
        self.player2_keys_rect.append(self.player2_keys[0].get_rect(center=PLAYER2_KEYS_POSITION[0]))
        self.player2_keys.append(FONT.render("'LEFT' -> Move Left", 1, BLACK))
        self.player2_keys_rect.append(self.player2_keys[1].get_rect(center=PLAYER2_KEYS_POSITION[1]))
        self.player2_keys.append(FONT.render("'RIGHT' -> Move Right", 1, BLACK))
        self.player2_keys_rect.append(self.player2_keys[2].get_rect(center=PLAYER2_KEYS_POSITION[2]))
        self.player2_keys.append(FONT.render("'UP' -> JUMP", 1, BLACK))
        self.player2_keys_rect.append(self.player2_keys[3].get_rect(center=PLAYER2_KEYS_POSITION[3]))
        self.player2_keys.append(FONT.render("'P' -> Shoot", 1, BLACK))
        self.player2_keys_rect.append(self.player2_keys[4].get_rect(center=PLAYER2_KEYS_POSITION[4]))
