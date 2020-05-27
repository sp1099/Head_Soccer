import pygame, os

from constants import *


class Ball(pygame.sprite.Sprite):
    """
    Ball Class:
    """

    def __init__(self, game_handler):
        pygame.sprite.Sprite.__init__(self)

        self.game = game_handler
        self.image = pygame.image.load(os.path.join(IMAGES, BALL_IMAGE))
        self.image = pygame.transform.scale(self.image, BALL_SIZE)
        self.image.set_colorkey((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = BALL_START_POSITION
        #self.rect.bottomleft = (1000, FIELD_LEVEL)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        if abs(self.speedx) > BALL_MAX_SPEED:
            self.speedx = self.sign(self.speedx) * BALL_MAX_SPEED
        self.rect.x += self.speedx
        self.speedx = self.speedx * 0.99999
        self.rect.y += self.speedy
        self.speedy += GRAVITY

    def player_collision(self, player):
        self.manipulate_speedx(player)

    def ground_collision(self):
        if abs(self.speedy) < 7:
            self.speedy = 0
        else:
            self.speedy = -int(self.speedy * 0.75)

    def goal_collision(self, goal, scoreboard):
        if goal.goal_num == 0:
            self.game.player1_score += 1
        else:
            self.game.player2_score += 1
        scoreboard.update_scoreline(self.game.player1_score, self.game.player2_score)
        self.rect.bottomleft = BALL_START_POSITION

        self.game.player1.rect.bottomleft = PLAYER_START_POSITION[self.game.player1.player_num]
        self.game.player2.rect.bottomleft = PLAYER_START_POSITION[self.game.player2.player_num]
        self.speedx = 0
        self.speedy = 0

    def manipulate_speedx(self, player):
        if player.speedx == 0:
            self.speedx = -self.speedx
        elif self.speedx == 0:
            self.speedx = player.speedx + self.sign(player.speedx) * 10
        elif (self.speedx * player.speedx) > 0:
            if player.speedx > self.speedx:
                self.speedx = self.speedx + player.speedx
            else:
                self.speedx = -self.speedx
        else:
            self.speedx = -self.speedx + player.speedx + self.sign(player.speedx) * 20

    def manipulate_speedy(self, player):
        self.speedy = -int(self.speedy * 0.75) + abs(player.speedy)

    def sign(self, num):
        return (num//abs(num))


