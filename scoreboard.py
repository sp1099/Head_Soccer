import pygame, os
from constants import *

class Scoreboard(pygame.sprite.Sprite):

    """
    Class Scoreboard:
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMAGES, SCOREBOARD_IMAGE))
        self.image = pygame.transform.scale(self.image, SCOREBOARD_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = SCOREBOARD_POSITION

        self.player1_score = 0
        self.player2_score = 0
        self.score1 = None
        self.score2 = None

    def update_scoreline(self, player1_score, player2_score):
        self.player1_score = player1_score
        self.player2_score = player2_score

    def update(self):
        self.score1 = FONT.render(str(self.player1_score), 1, WHITE)
        self.score2 = FONT.render(str(self.player2_score), 1, WHITE)


    def draw(self, field):
        field.blit(self.image, self.rect)
        field.blit(self.score1, (865, 250))
        field.blit(self.score2, (995, 250))
