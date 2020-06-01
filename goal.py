import pygame, os

from constants import *


class Goal(pygame.sprite.Sprite):
    """
    Goal Class:
        Initializes a Goal Object
        Inherits from the pygame.sprite.Sprite class which must be initialized in the beginning
        Actually a quite static class with no interaction (only image displaying)
        Goal interaction are handled via the helper sprites

    """

    def __init__(self, goal_num):
        """
        :description:
            Initializes a Goal Object
            Loads image and flips it if it is the second goal
        :parameter
            goal_num (int): 0 (left) or 1 (right) to determine which Goal is meant to be used
        :return
            None

        """
        # Initialize Sprite
        pygame.sprite.Sprite.__init__(self)

        self.goal_num = goal_num

        # image loading, transforming and positioning
        self.image = pygame.image.load(os.path.join(IMAGES, GOAL_IMAGE))
        self.image = pygame.transform.scale(self.image, GOAL_SIZE)
        if self.goal_num == 0:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = GOAL_POSITION[self.goal_num]

    def update(self):
        pass

    def draw(self, field):
        # draws the image onto the given field, which is the screen
        field.blit(self.image, self.rect)
