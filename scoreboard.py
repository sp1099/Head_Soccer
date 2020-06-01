import pygame, os
from constants import *

class Scoreboard(pygame.sprite.Sprite):

    """
    Class Scoreboard:
        Initializes Scoreboard Object
        Inherits from the pygame.sprite.Sprite class which must be initialized in the beginning
        Keeps track of the scorline of the match
        Displays the scoreline

    """

    def __init__(self):
        """
        :description:
            Initializes Scoreboard
            Scoreline initialized wit 0:0 in the beginning
            Loads the image
        :parameter
            None
        :return
            None

        """
        # Initialize Sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMAGES, SCOREBOARD_IMAGE))
        self.image = pygame.transform.scale(self.image, SCOREBOARD_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = SCOREBOARD_POSITION

        # Scoreline Initialization
        self.player1_score = 0
        self.player2_score = 0
        self.score1 = None
        self.score1_rect = None
        self.score2 = None
        self.score2_rect = None

    def update_scoreline(self, player1_score, player2_score):
        # updates the scores of both players
        self.player1_score = player1_score
        self.player2_score = player2_score

    def update(self):
        # renders the Score-Font of the new Scoreline
        self.score1 = FONT_SCORE.render(str(self.player1_score), 1, WHITE)
        self.score1_rect = self.score1.get_rect(center=SCORE_POSITION[0])
        self.score2 = FONT_SCORE.render(str(self.player2_score), 1, WHITE)
        self.score2_rect = self.score2.get_rect(center=SCORE_POSITION[1])

    def draw(self, field):
        # draws the image onto the given field, which is the screen
        # also draws the Score-Fonts to the field
        field.blit(self.image, self.rect)
        field.blit(self.score1, self.score1_rect)
        field.blit(self.score2, self.score2_rect)
