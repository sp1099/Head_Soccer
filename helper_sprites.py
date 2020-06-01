import pygame, os

from constants import *

class Field_Level(pygame.sprite.Sprite):
    """
    Field_Level Class:
        Helper Sprite for determining when the ball hits the ground
        Inherits from the pygame.sprite.Sprite class which must be initialized in the beginning

    """

    def __init__(self):
        """
        :description:
            Initializes a Field Level Helper Object
            A surface used only for collision detection of ball and field
            position under the players so they can stand on it and the ball will be reflected of it
        :parameter
            None
        :return
            None

        """
        # Initialize Sprite
        pygame.sprite.Sprite.__init__(self)

        # image loading, transforming and positioning
        self.image = pygame.Surface(FIELD_LEVEL_SIZE)
        # set_alpha(0) hides the sprite so that it is not displayed on the screen
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.topleft = FIELD_LEVEL_POSITION

    def draw(self, field):
        # draws the non-visible image onto the given field, which is the screen
        field.blit(self.image, self.rect)


class Goal_Collision(pygame.sprite.Sprite):
    """
    Field_Level Class:
        Helper Sprite for determining a Goal
        Inherits from the pygame.sprite.Sprite class which must be initialized in the beginning

    """

    def __init__(self, goal_num):
        """
        :description:
            Initializes a  Field Level Helper Object
            A surface used only for collision detection of ball and "real Goal"
            positioned inside the goal so that at collision the whole ball is inside the goal
        :parameter
            goal_num (int): 0 (left) or 1 (right) to determine which Goal is meant to be used
        :return
            None

        """
        # Initialize Sprite
        pygame.sprite.Sprite.__init__(self)

        self.goal_num = goal_num
        # image loading, transforming and positioning
        self.image = pygame.Surface(GOAL_COLLISION_SIZE)
        # set_alpha(0) hides the sprite so that it is not displayed on the screen
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (GOAL_COLLISION_POSITION[self.goal_num])

    def draw(self, field):
        # draws the non-visible image onto the given field, which is the screen
        field.blit(self.image, self.rect)


class Crossbar_Collision_Front(pygame.sprite.Sprite):
    """
    Field_Level Class:
        Helper Sprite for determining a Goal
        Inherits from the pygame.sprite.Sprite class which must be initialized in the beginning

    """

    def __init__(self, goal_num):
        """
        :description:
            Initializes a  Crossbar_Front Helper Object
            A surface used only for collision detection of ball and front side of the crossbar
            when the ball hits the front side of the crossbar its x speed is getting reflected
        :parameter
            goal_num (int): 0 (left) or 1 (right) to determine which Goal is meant to be used
        :return
            None

        """
        # Initialize Sprite
        pygame.sprite.Sprite.__init__(self)

        self.goal_num = goal_num
        # image loading, transforming and positioning
        self.image = pygame.Surface(CROSSBAR_FRONT_SIZE)
        # set_alpha(0) hides the sprite so that it is not displayed on the screen
        self.image.set_alpha(0)
        self.image.convert_alpha()
        self.image = pygame.transform.rotate(self.image, CROSSBAR_FRONT_ROTATION[self.goal_num])
        self.rect = self.image.get_rect()
        self.rect.center = CROSSBAR_FRONT_POSITION[goal_num]

    def draw(self, field):
        # draws the non-visible image onto the given field, which is the screen
        field.blit(self.image, self.rect)


class Crossbar_Collision_Top(pygame.sprite.Sprite):
    """
    Field_Level Class:
        Helper Sprite for determining a Goal
        Inherits from the pygame.sprite.Sprite class which must be initialized in the beginning

    """

    def __init__(self, goal_num):
        """
        :description:
            Initializes a  Crossbar_Top Helper Object
            A surface used only for collision detection of ball and top side of the crossbar
            when the ball hits the top side of the crossbar its y speed is getting reflected
        :parameter
            goal_num (int): 0 (left) or 1 (right) to determine which Goal is meant to be used
        :return
            None

        """
        # Initialize Sprite
        pygame.sprite.Sprite.__init__(self)

        self.goal_num = goal_num
        # image loading, transforming and positioning
        self.image = pygame.Surface(CROSSBAR_TOP_SIZE)
        # set_alpha(0) hides the sprite so that it is not displayed on the screen
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.topleft = CROSSBAR_TOP_POSITION[goal_num]

    def draw(self, field):
        # draws the non-visible image onto the given field, which is the screen
        field.blit(self.image, self.rect)