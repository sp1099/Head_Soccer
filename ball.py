import pygame, os
import time
from constants import *
from helper_sprites import Crossbar_Collision_Front, Crossbar_Collision_Top


class Ball(pygame.sprite.Sprite):
    """
    Ball Class:
    """

    def __init__(self, game_handler):
        pygame.sprite.Sprite.__init__(self)
        self.lastGroundCollision = time.time()
        self.game = game_handler
        self.image = pygame.image.load(os.path.join(IMAGES, BALL_IMAGE))
        self.image = pygame.transform.scale(self.image, BALL_SIZE)
        self.image.set_colorkey((0, 0, 255))
        self.rect = self.image.get_rect()
        self.reset_ball()
        self.oldMaxHeight = self.rect.midtop

    def update(self):
        if abs(self.speedx) > BALL_MAX_SPEED:
            self.speedx = self.sign(self.speedx) * BALL_MAX_SPEED
        self.rect.x += self.speedx
        self.speedx = self.speedx * 0.99999
        self.rect.y += self.speedy
        self.speedy += GRAVITY
        if self.rect.bottom > FIELD_LEVEL + 2:
            self.rect.bottom = FIELD_LEVEL + 2
        if self.rect.right < 0 or self.rect.left > 1920:
            self.reset_ball()


    def player_collision(self, player):
        if player.rect.collidepoint(self.rect.midbottom) is not player.rect.collidepoint(self.rect.midtop):
            if player.rect.collidepoint(self.rect.midbottom):
                self.rect.bottom = player.rect.top - 5
                if self.rect.center > player.rect.center and self.speedx == 0:
                    self.speedx = -5
                elif self.rect.center < player.rect.center and self.speedx == 0:
                    self.speedx = 5
                if player.speedy < 0:
                    self.speedy = abs(self.speedy) * - 0.75 - 10
                else:
                    self.speedy = abs(self.speedy) * - 0.75
            elif player.rect.collidepoint(self.rect.midtop) and self.rect.midbottom > player.rect.midbottom:
                self.rect.left = player.rect.right + 5
                self.speedx += 5
                self.speedy = 20
            else:
                self.rect.right = player.rect.left - 5
                self.speedx -= 5
                self.speedy = 20
        else:
            if player.rect.right - 20 < self.rect.right and not player.rect.collidepoint(self.rect.midtop):
                self.rect.left = player.rect.right + 5
            elif player.rect.left + 20 > self.rect.left and not player.rect.collidepoint(self.rect.midtop):
                self.rect.right = player.rect.left - 5
        self.manipulate_speedx(player)
        if abs(self.speedx) > 25 and self.rect.bottom > FIELD_LEVEL - 20:
            self.speedy = abs(self.speedx)/2

    def draw(self, field):
        field.blit(self.image, self.rect)

    def shoe_collision(self, shoe):
        if shoe.shot:
            if shoe.player_num == 0:
                self.speedy = 50
                self.speedx -= 30
            else:
                self.speedy = 50
                self.speedx += 30
        elif shoe.move:
            self.manipulate_speedx(shoe)

    def ground_collision(self):
        self.newGroundCollision = time.time()
        self.speedx *= 0.99
        self.time = self.newGroundCollision - self.lastGroundCollision
        if 0.08 < self.time < 0.4 + self.speedx * 0.005 or (abs(self.speedy) < 7):
            self.speedy = 0
        else:
            self.speedy = -int(self.speedy * 0.75)
        self.lastGroundCollision = time.time()

    def goal_collision(self, goal, scoreboard):
        if goal.goal_num == 0:
            self.game.player2_score += 1
        else:
            self.game.player1_score += 1
        scoreboard.update_scoreline(self.game.player1_score, self.game.player2_score)
        self.rect.bottomleft = BALL_START_POSITION

        self.game.player1.rect.bottomleft = PLAYER_START_POSITION[self.game.player1.player_num]
        self.game.player2.rect.bottomleft = PLAYER_START_POSITION[self.game.player2.player_num]
        self.game.shoe1.rect.bottomleft = SHOE_START_POSITION[self.game.shoe1.player_num]
        self.game.shoe2.rect.bottomleft = SHOE_START_POSITION[self.game.shoe2.player_num]

        self.speedx = 0
        self.speedy = 0

    def crossbar_collision(self, crossbar):
        if isinstance(crossbar, Crossbar_Collision_Front):
            self.speedx = -self.speedx * 0.9
        elif isinstance(crossbar, Crossbar_Collision_Top):
            self.speedy = -self.speedy * 0.75


    def manipulate_speedx(self, player):
        if player.speedx == 0:
            self.speedx = -self.speedx * 0.9
        elif self.speedx == 0:
            self.speedx = player.speedx + self.sign(player.speedx) * 10
        elif (self.speedx * player.speedx) > 0:
            if abs(player.speedx) > abs(self.speedx):
                self.speedx = self.speedx + player.speedx
            else:
                self.speedx = -self.speedx + player.speedx
        else:
            self.speedx = -(self.speedx) + player.speedx + self.sign(player.speedx) * 20
        if self.speedx > BALL_MAX_SPEED:
            self.speedx = BALL_MAX_SPEED

    def manipulate_speedy(self, player):
        self.speedy = -int(self.speedy * 0.75) + abs(player.speedy)

    def sign(self, num):
        return (num//abs(num))

    def reset_ball(self):
        self.rect.bottomleft = BALL_START_POSITION
        self.speedx = 0
        self.speedy = 0


