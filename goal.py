import pygame, os

from constants import *


class Goal(pygame.sprite.Sprite):
    """
    Goal Class:
    """

    def __init__(self, goal_num):
        pygame.sprite.Sprite.__init__(self)

        self.goal_num = goal_num

        self.image = pygame.image.load(os.path.join(IMAGES, GOAL_IMAGE))
        self.image = pygame.transform.scale(self.image, GOAL_SIZE)
        if self.goal_num == 0:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = GOAL_POSITION[self.goal_num]

    def update(self):
        pass

    def event_handler(self):
        pass
