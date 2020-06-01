import pygame, os

from constants import *

class Player(pygame.sprite.Sprite):
    """
    Player Class:
        Initializes Player Object
        Inherits from the pygame.sprite.Sprite class which must be initialized in the beginning
        Handles Player Movement and Player-Player Collision
    """

    def __init__(self, player_num):
        """
        :description:
            Initializes Player
            Loads image
            Sets Movement and Shot Flags for later movement handling
        :parameter
            player_num (int): Determine which player should be used
        :return
            None

        """
        # Initialize Sprite
        pygame.sprite.Sprite.__init__(self)

        self.player_num = player_num
        self.is_jumping = False
        # Loading two images (idle and shot)
        self.idle_image = pygame.image.load(os.path.join(IMAGES, PLAYER_IMAGE[self.player_num]))
        self.shot_image = pygame.image.load(os.path.join(IMAGES, PLAYER_SHOT_IMAGE[self.player_num]))
        # images of right side player must be flipped so they face each other
        if self.player_num == 0:
            self.idle_image = pygame.transform.flip(self.idle_image, True, False)
            self.shot_image = pygame.transform.flip(self.shot_image, True, False)
        self.idle_image = pygame.transform.scale(self.idle_image, PLAYER_SIZE)
        self.shot_image = pygame.transform.scale(self.shot_image, PLAYER_SIZE)
        self.image = self.idle_image
        self.rect = self.image.get_rect()
        self.rect.bottomleft = PLAYER_START_POSITION[self.player_num]
        # initialize movement flags
        self.notRight = False
        self.notLeft = False
        self.noJump = False
        self.speedx = 0
        self.speedy = 0

    def update(self):
        """
        :description:
            Updates the player position
            For the y physics gravity is integrated when the player is jumping
            Also when hitting the floor  the player gets et on field level height
        :parameter
            None
        :return
            None

        """
        self.rect.x += self.speedx
        self.notRight = False
        self.notLeft = False
        self.noJump = False
        if self.is_jumping:
            self.rect.y += self.speedy
            self.speedy += GRAVITY
            if self.rect.bottom >= FIELD_LEVEL:
                self.rect.bottom = FIELD_LEVEL
                self.is_jumping = False

    def draw(self, field):
        # draws the image onto the given field, which is the screen
        field.blit(self.image, self.rect)

    def player_collide(self, player):
        """
        :description:
            Handles Player-Player Collision
            The players cannot move through each other
            but they can stand on each other (then jumping is not possible)
        :parameter
            player (Player): Determine which player should be used
        :return
            None

        """
        # Check for player collision on the sides
        if (self.rect.right > player.rect.right) and (self.rect.left - player.rect.right < 0) and self.rect.bottom > player.rect.top + 15 and player.rect.bottom > self.rect.top + 15 and self.speedx <= 0:
            self.notLeft = True
            player.notRight = True
        elif self.rect.left < player.rect.left and (self.rect.right - player.rect.left > 0) and player.rect.bottom > self.rect.top + 15 and self.rect.bottom > player.rect.top + 15 and self.speedx >= 0:
            self.notRight = True
            player.notLeft = True
        # check for player collision on the top
        if self.rect.bottom <= player.rect.top + 15:
            self.speedy = 0
            player.noJump = True
        elif player.rect.bottom <= self.rect.top + 15:
            player.speedy = 0
            self.noJump = True

    def event_handler(self):
        """
        :description:
            Handles the user input events regarding the player movement
            move left, move right, jump
        :parameter
            None
        :return
            None

        """
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        # check for move left
        if keystate[LEFT_KEY[self.player_num]] and not self.notLeft:
            self.speedx = -PLAYER_HOR_SPEED
        # check for move right
        if keystate[RIGHT_KEY[self.player_num]] and not self.notRight:
            self.speedx = PLAYER_HOR_SPEED
        # check for jump
        if keystate[JUMP_KEY[self.player_num]] and not self.noJump:
            self.jump()

    def jump(self):
        # enables the player to jump (sets the y speed to jump speed)
        # only possible if the player is standing on the ground
        if self.rect.bottom == FIELD_LEVEL:
            self.is_jumping = True
            self.speedy = -PLAYER_JUMP_START_SPEED

