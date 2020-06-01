import pygame, os

from constants import *
from player import Player

class Shoe(Player):

    """
    Shoe Class
    """

    def __init__(self, player_num, player):
        pygame.sprite.Sprite.__init__(self)
        self.player_num = player_num
        self.is_jumping = False
        self.move = False
        self.shot = False
        self.notLeft = False
        self.notRight = False
        self.image = pygame.Surface(SHOE_SIZE)
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = SHOE_START_POSITION[self.player_num]

        self.player = player

        self.speedx = 0
        self.speedy = 0

    def shoe_collide(self, player):
        self.notLeft = player.notLeft
        self.notRight = player.notRight
        self.noJump = player.noJump
        self.speedy = player.speedy

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
            self.player.image = self.player.shot_image
        elif not keystate[SHOT_KEY[self.player_num]] and self.move:
            if self.player_num == 0:
                self.rect.left += 25
            else:
                self.rect.right -= 25
            self.move = False
            self.player.image = self.player.idle_image

    def draw(self, field):
        field.blit(self.image, self.rect)
