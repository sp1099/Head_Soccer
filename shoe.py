import pygame, os

from constants import *
from player import Player

class Shoe(Player):

    """
    Shoe Class
        Initializes Shoe Object
        Inherits from the pygame.sprite.Sprite class which must be initialized in the beginning
        Inherits from Player
        Handles shot physics and Shoe collision

    """

    def __init__(self, player_num, player):
        """
        :description:
            Initializes Shoe
            Uses a non-visible Surface for collision detection
            Sets Movement and Shot Flags for later Shot handling
        :parameter
            player_num (int): Determine which player the shoe is belonging to
            player (Player): Player which the shoe is belonging to
        :return
            None

        """
        # Initialize Sprite
        pygame.sprite.Sprite.__init__(self)
        self.player_num = player_num
        self.is_jumping = False
        self.move = False
        self.shot = False
        self.notLeft = False
        self.notRight = False
        self.image = pygame.Surface(SHOE_SIZE)
        # set_alpha(0) hides the sprite so that it is not displayed on the screen
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = SHOE_START_POSITION[self.player_num]

        self.player = player

        self.speedx = 0
        self.speedy = 0

    def shoe_collide(self, player):
        # on collision ball-shoe, Movement Flags get set according to the Player the shoe belongs to
        self.notLeft = player.notLeft
        self.notRight = player.notRight
        self.noJump = player.noJump
        self.speedy = player.speedy

    def event_handler(self):
        """
        :description:
            Event Handler for Shot interaction
            Checks for shot key of one player getting pressed
            then moves his shoe Surface accordingly and sets the shot flag
            also the players image gets replaced for the time th shot key is being pressed
        :parameter
            None
        :return
            None

        """
        self.shot = False
        Player.event_handler(self)
        # check for one of the shot keys being pressed
        keystate = pygame.key.get_pressed()
        if keystate[SHOT_KEY[self.player_num]] and not self.move:
            # adjustment of the Shoe Surface position
            if self.player_num == 0:
                self.rect.left -= 25
            else:
                self.rect.right += 25
            # setting Movement and shot flag
            self.move = True
            self.shot = True
            # replacing player image during shot for animation
            self.player.image = self.player.shot_image
        elif not keystate[SHOT_KEY[self.player_num]] and self.move:
            if self.player_num == 0:
                self.rect.left += 25
            else:
                self.rect.right -= 25
            self.move = False
            self.player.image = self.player.idle_image

    def draw(self, field):
        # draws the image onto the given field, which is the screen
        field.blit(self.image, self.rect)
