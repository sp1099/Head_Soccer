import pygame, os

from constants import *

class Player(pygame.sprite.Sprite):
    """
    Player Class:
    """

    def __init__(self, player_num):
        pygame.sprite.Sprite.__init__(self)

        self.player_num = player_num
        self.is_jumping = False

        #self.image = pygame.image.load(os.path.join(IMAGES, PLAYER_IMAGE[self.player_num])).convert()
        #self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = PLAYER_START_POSITION[self.player_num]

        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        if self.is_jumping:
            self.rect.y += self.speedy
            self.speedy += GRAVITY
            if self.rect.bottom >= FIELD_LEVEL:
                self.rect.bottom = FIELD_LEVEL
                self.is_jumping = False

    def draw(self, field):
        field.blit(self.image, self.rect)

    def event_handler(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[LEFT_KEY[self.player_num]]:
            self.speedx = -PLAYER_HOR_SPEED
        if keystate[RIGHT_KEY[self.player_num]]:
            self.speedx = PLAYER_HOR_SPEED
        if keystate[JUMP_KEY[self.player_num]]:
            self.jump()

    def jump(self):
         if self.rect.bottom == FIELD_LEVEL:
             self.is_jumping = True
             self.speedy = -PLAYER_JUMP_START_SPEED

