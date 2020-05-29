import pygame, os

from constants import *
from player import Player

class Shoe(Player):

    """
    Shoe Class
    """

    def __init__(self, player_num):
        pygame.sprite.Sprite.__init__(self)
        self.player_num = player_num
        self.is_jumping = False
        self.move = False
        self.shot = False

        self.image = pygame.image.load(os.path.join(IMAGES, SHOE_IMAGE))  # https://pixabay.com/de/photos/nike-fussballschuhe-fussball-sport-1271624/
        self.image = pygame.transform.scale(self.image, SHOE_SIZE)
        if self.player_num == 0:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = SHOE_START_POSITION[self.player_num]

        self.speedx = 0
        self.speedy = 0

    def event_handler(self):
        self.shot = False
        Player.event_handler(self)
        keystate = pygame.key.get_pressed()
        if keystate[SHOT_KEY[self.player_num]] and not self.move:
            if self.player_num == 0:
                self.rect.left -= 25
            else:
                self.rect.right += 25
            self.move = True
            self.shot = True
        elif not keystate[SHOT_KEY[self.player_num]] and self.move:
            if self.player_num == 0:
                self.rect.left += 25
            else:
                self.rect.right -= 25
            self.move = False

