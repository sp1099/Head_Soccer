import pygame
import os
import sys

from constants import *
from player import Player
from ball import Ball
from goal import Goal
from scoreboard import Scoreboard
from shoe import Shoe
from helper_sprites import Field_Level, Goal_Collision


class Game_Manager:
    """
    Game Manager Class:
    """

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.field = pygame.display.set_mode(FIELD_SIZE)
        self.background = pygame.image.load(os.path.join(IMAGES, BACKGROUND_IMAGE))
        self.background = pygame.transform.scale(self.background, FIELD_SIZE)

        self.player1_score = 0
        self.player2_score = 0

        self.all_sprites = pygame.sprite.Group()
        self.scoreboard = Scoreboard()
        self.all_sprites.add(self.scoreboard)
        self.player1 = Player(0)
        self.all_sprites.add(self.player1)
        self.player2 = Player(1)
        self.all_sprites.add(self.player2)
        self.shoe1 = Shoe(0)
        self.all_sprites.add(self.shoe1)
        self.shoe2 = Shoe(1)
        self.all_sprites.add(self.shoe2)
        self.ball = Ball(self)
        self.all_sprites.add(self.ball)
        self.goal1 = Goal(0)
        self.all_sprites.add(self.goal1)
        self.goal1_col = Goal_Collision(0)
        self.all_sprites.add(self.goal1_col)
        self.goal2 = Goal(1)
        self.all_sprites.add(self.goal2)
        self.goal2_col = Goal_Collision(1)
        self.all_sprites.add(self.goal2_col)
        self.surface = Field_Level()
        self.all_sprites.add(self.surface)

        self.player_sprites = pygame.sprite.Group()
        self.player_sprites.add(self.player1)
        self.player_sprites.add(self.player2)

        self.goal_sprites = pygame.sprite.Group()
        self.goal_sprites.add(self.goal1_col)
        self.goal_sprites.add(self.goal2_col)

        self.shoe_sprites = pygame.sprite.Group()
        self.shoe_sprites.add(self.shoe1)
        self.shoe_sprites.add(self.shoe2)

        self.field_level_sprites = pygame.sprite.Group()
        self.field_level_sprites.add(self.surface)

        self.game_loop()

    def game_loop(self):
        while 1:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            for sprite in self.player_sprites:
                sprite.event_handler()

            for sprite in self.shoe_sprites:
                sprite.event_handler()

            player_collision_list = pygame.sprite.spritecollide(self.ball, self.player_sprites, False)
            if player_collision_list:
                for player in player_collision_list:
                    self.ball.player_collision(player)

            shoe_collision_list = pygame.sprite.spritecollide(self.ball, self.shoe_sprites, False)
            if shoe_collision_list:
                for shoe in shoe_collision_list:
                    self.ball.shoe_collision(shoe)

            surface_collision_list = pygame.sprite.spritecollide(self.ball, self.field_level_sprites, False)
            if surface_collision_list:
                self.ball.ground_collision()

            goal_collision_list = pygame.sprite.spritecollide(self.ball, self.goal_sprites, False)
            if goal_collision_list:
                for goal in goal_collision_list:
                    self.ball.goal_collision(goal, self.scoreboard)

            self.update_sprites()

            self.field.blit(self.background, (0, 0))
            self.all_sprites.draw(self.field)

            pygame.display.flip()

    def update_sprites(self):
        self.player_sprites.update()
        self.shoe_sprites.update()
        self.ball.update()
        self.scoreboard.update(self.field)
