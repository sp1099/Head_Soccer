import pygame, os
from constants import *

class Scoreboard(pygame.sprite.Sprite):

    """
    Class Scoreboard:
    """
    player1_score = 0
    player2_score = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMAGES, SCOREBOARD_IMAGE))
        self.image = pygame.transform.scale(self.image, SCOREBOARD_SIZE)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = SCOREBOARD_POSITION

    def update_scoreline(self, player1_score, player2_score):
        Scoreboard.player1_score = player1_score
        Scoreboard.player2_score = player2_score

    def update(self, field):
        score1 = FONT.render(str(Scoreboard.player1_score), 1, WHITE)
        score2 = FONT.render(str(Scoreboard.player2_score), 1, WHITE)
        field.blit(score1, (865, 250))
        field.blit(score2, (995, 250))
        pygame.display.update()

