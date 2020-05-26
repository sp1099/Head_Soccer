import pygame, os

from constants import *

class Field_Level(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(FIELD_LEVEL_SIZE)
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.topleft = FIELD_LEVEL_POSITION


class Goal_Collision(pygame.sprite.Sprite):

    def __init__(self, goal_num):
        pygame.sprite.Sprite.__init__(self)

        self.goal_num = goal_num

        self.image = pygame.Surface(GOAL_COLLISION_SIZE)
        #self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (GOAL_COLLISION_POSITION[self.goal_num])