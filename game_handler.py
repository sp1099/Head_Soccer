import pygame
import os
import sys

from constants import *
from player import Player
from ball import Ball
from goal import Goal
from scoreboard import Scoreboard
from shoe import Shoe
from helper_sprites import Field_Level, Goal_Collision, Crossbar_Collision_Front, Crossbar_Collision_Top


class Game_Manager:
    """
    Game Manager Class:
    """

    def __init__(self, field):
        self.field = field
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(os.path.join(IMAGES, BACKGROUND_IMAGE))
        self.background = pygame.transform.scale(self.background, FIELD_SIZE)

        self.start_time = pygame.time.get_ticks()
        self.game_time = None

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
        self.goal1_crossbar_front = Crossbar_Collision_Front(0)
        self.all_sprites.add(self.goal1_crossbar_front)
        self.goal1_crossbar_top = Crossbar_Collision_Top(0)
        self.all_sprites.add(self.goal1_crossbar_top)

        self.goal2 = Goal(1)
        self.all_sprites.add(self.goal2)
        self.goal2_col = Goal_Collision(1)
        self.all_sprites.add(self.goal2_col)
        self.goal2_crossbar_front = Crossbar_Collision_Front(1)
        self.all_sprites.add(self.goal2_crossbar_front)
        self.goal2_crossbar_top = Crossbar_Collision_Top(1)
        self.all_sprites.add(self.goal2_crossbar_top)

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

        self.crossbar_sprites = pygame.sprite.Group()
        self.crossbar_sprites.add(self.goal1_crossbar_front)
        self.crossbar_sprites.add(self.goal2_crossbar_front)
        self.crossbar_sprites.add(self.goal1_crossbar_top)
        self.crossbar_sprites.add(self.goal2_crossbar_top)

        self.game_loop()

    def game_loop(self):
        while 1:
            # Countdown Timer
            game_time = round((pygame.time.get_ticks() - self.start_time) / 1000)
            if game_time > GAME_LENGTH:
                self.display_result()
                break
            game_time_str = str((GAME_LENGTH - game_time) // 60) + " : " + str((GAME_LENGTH - game_time) % 60)
            self.game_time = FONT.render(game_time_str, 1, WHITE)

            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            player_collision_list = pygame.sprite.spritecollide(self.ball, self.player_sprites, False)
            if player_collision_list:
                for player in player_collision_list:
                    self.ball.player_collision(player)

            player_collide = self.player1.rect.colliderect(self.player2.rect)
            if player_collide:
                self.player1.player_collide(self.player2)
                self.shoe1.shoe_collide(self.player1)
                self.shoe2.shoe_collide(self.player2)

            for sprite in self.player_sprites:
                sprite.event_handler()

            for sprite in self.shoe_sprites:
                sprite.event_handler()

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

            crossbar_collision_list = pygame.sprite.spritecollide(self.ball, self.crossbar_sprites, False)
            if crossbar_collision_list:
                for crossbar in crossbar_collision_list:
                    self.ball.crossbar_collision(crossbar)

            self.update_sprites()

            self.field.blit(self.background, (0, 0))
            self.draw()
            self.field.blit(self.game_time, (900, 158))

            pygame.display.flip()

    def update_sprites(self):
        self.player_sprites.update()
        self.shoe_sprites.update()
        self.ball.update()
        self.scoreboard.update()

    def draw(self):
        for sprite in self.all_sprites:
            sprite.draw(self.field)

    def display_result(self):
        if self.player1_score > self.player2_score:
            result = FONT_CAPTION.render("PLAYER 1 WON", 1, (0, 0, 0))
        elif self.player1_score < self.player2_score:
            result = FONT_CAPTION.render("PLAYER 2 WON", 1, (0, 0, 0))
        else:
            result = FONT_CAPTION.render("TIE", 1, (0, 0, 0))
        result_rect = result.get_rect(center=RESULT_POSITION)
        self.field.blit(result, result_rect)
        pygame.display.update()
        pygame.time.wait(3000)
