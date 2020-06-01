import pygame, os

from constants import *

class Field_Level(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(FIELD_LEVEL_SIZE)
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.topleft = FIELD_LEVEL_POSITION

    def draw(self, field):
        field.blit(self.image, self.rect)


class Goal_Collision(pygame.sprite.Sprite):

    def __init__(self, goal_num):
        pygame.sprite.Sprite.__init__(self)

        self.goal_num = goal_num

        self.image = pygame.Surface(GOAL_COLLISION_SIZE)
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (GOAL_COLLISION_POSITION[self.goal_num])

    def draw(self, field):
        field.blit(self.image, self.rect)


class Crossbar_Collision_Front(pygame.sprite.Sprite):

    def __init__(self, goal_num):
        pygame.sprite.Sprite.__init__(self)

        self.goal_num = goal_num

        self.image = pygame.Surface(CROSSBAR_FRONT_SIZE)
        self.image.set_alpha(0)
        self.image.convert_alpha()
        self.image = pygame.transform.rotate(self.image, CROSSBAR_FRONT_ROTATION[self.goal_num])
        self.rect = self.image.get_rect()
        self.rect.center = CROSSBAR_FRONT_POSITION[goal_num]

    def draw(self, field):
        field.blit(self.image, self.rect)


class Crossbar_Collision_Top(pygame.sprite.Sprite):

    def __init__(self, goal_num):
        pygame.sprite.Sprite.__init__(self)

        self.goal_num = goal_num

        self.image = pygame.Surface(CROSSBAR_TOP_SIZE)
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.topleft = CROSSBAR_TOP_POSITION[goal_num]

    def draw(self, field):
        field.blit(self.image, self.rect)