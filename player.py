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
        self.notRight = False
        self.notLeft = False
        self.noJump = False
        self.speedx = 0
        self.speedy = 0

    def update(self):
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
        field.blit(self.image, self.rect)

    def player_collide(self, player):
        if (self.rect.right > player.rect.right) and (self.rect.left - player.rect.right < 0) and self.rect.bottom > player.rect.top + 15 and player.rect.bottom > self.rect.top + 15 and self.speedx <= 0:
            self.notLeft = True
            player.notRight = True
        elif self.rect.left < player.rect.left and (self.rect.right - player.rect.left > 0) and player.rect.bottom > self.rect.top + 15 and self.rect.bottom > player.rect.top + 15 and self.speedx >= 0:
            self.notRight = True
            player.notLeft = True
        if self.rect.bottom <= player.rect.top + 15:
            self.speedy = 0
            player.noJump = True
        elif player.rect.bottom <= self.rect.top + 15:
            player.speedy = 0
            self.noJump = True

    def event_handler(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[LEFT_KEY[self.player_num]] and not self.notLeft:
            self.speedx = -PLAYER_HOR_SPEED
        if keystate[RIGHT_KEY[self.player_num]] and not self.notRight:
            self.speedx = PLAYER_HOR_SPEED
        if keystate[JUMP_KEY[self.player_num]] and not self.noJump:
            self.jump()

    def jump(self):
         if self.rect.bottom == FIELD_LEVEL:
             self.is_jumping = True
             self.speedy = -PLAYER_JUMP_START_SPEED

