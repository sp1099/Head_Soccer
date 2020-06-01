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
        Initializes the Head Soccer game
        Initializes all game assets (Player, Goals, Ball, etc.)
        Uses Sprite Groups for clarity of code and collision handling
        Handles the main game loop
    """

    def __init__(self, field):
        """
        :description:
            Initializes a Game_Manager Object
            Loads the images
            Creates Game Assets Objects
            Creates Sprite Groups
            Adds Game Assets to according Sprite Groups
            Starts the game loop
        :parameter
            field (pygame.display): screen on which the objects and the game are displayed
        :return
            None

        """
        # transfer field
        self.field = field
        # Initialize Clock object which keeps track of the in-game FPS
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load(os.path.join(IMAGES, BACKGROUND_IMAGE))
        self.background = pygame.transform.scale(self.background, FIELD_SIZE)
        # get start time of the game, used to determine the time fot the in-game Countdown Timer
        self.start_time = pygame.time.get_ticks()
        self.game_time = None
        # Initialize player scores
        self.player1_score = 0
        self.player2_score = 0

        # Initialize sprite groups and asset objects
        # All objects are stored in the all_sprites Group for updating and drawing
        self.all_sprites = pygame.sprite.Group()
        # Scoreboard
        self.scoreboard = Scoreboard()
        self.all_sprites.add(self.scoreboard)
        # Players
        self.player1 = Player(0)
        self.all_sprites.add(self.player1)
        self.player2 = Player(1)
        self.all_sprites.add(self.player2)
        # Shoes
        self.shoe1 = Shoe(0, self.player1)
        self.all_sprites.add(self.shoe1)
        self.shoe2 = Shoe(1, self.player2)
        self.all_sprites.add(self.shoe2)
        # Ball
        self.ball = Ball(self)
        self.all_sprites.add(self.ball)
        # Goals and Goal Crossbar assets
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
        # Field Level
        self.surface = Field_Level()
        self.all_sprites.add(self.surface)

        # additional sprite groups for collision detection
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

        # start game loop
        self.running = True
        self.game_loop()

    def game_loop(self):
        """
        :description:
            Handles the main game loop:
                Event Handling:
                    Checks for Quit
                    Checks for Timer run out
                    Checks for Collision
                    Some Assets have their own Event Handler which is called here
                Update:
                    update_sprites triggers several update function of the sprites that have one implemented
                Draw:
                    Normally all_sprites.draw would draw all the objects in the group as default
                    Due to some draw methods that have to do more than just display their image
                    own draw methods for all Sprites are implemented and called through iterating over all_sprites Group
        :parameter
            None
        :return
            None

        """
        while self.running:
            # GAME LOOP

            # takes care of stable FPS
            self.clock.tick(FPS)

            # Event Handling
            # Quit Detection
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Collision Detection
            # player-ball collision
            player_collision_list = pygame.sprite.spritecollide(self.ball, self.player_sprites, False)
            if player_collision_list:
                for player in player_collision_list:
                    self.ball.player_collision(player)
            # player-player collision
            player_collide = self.player1.rect.colliderect(self.player2.rect)
            if player_collide:
                self.player1.player_collide(self.player2)
                self.shoe1.shoe_collide(self.player1)
                self.shoe2.shoe_collide(self.player2)
            # own event handlers for players and shoes
            for sprite in self.player_sprites:
                sprite.event_handler()
            for sprite in self.shoe_sprites:
                sprite.event_handler()
            # ball-shoe collision (shot)
            shoe_collision_list = pygame.sprite.spritecollide(self.ball, self.shoe_sprites, False)
            if shoe_collision_list:
                for shoe in shoe_collision_list:
                    self.ball.shoe_collision(shoe)
            # ball-field collision
            surface_collision_list = pygame.sprite.spritecollide(self.ball, self.field_level_sprites, False)
            if surface_collision_list:
                self.ball.ground_collision()
            # ball-goal collision
            goal_collision_list = pygame.sprite.spritecollide(self.ball, self.goal_sprites, False)
            if goal_collision_list:
                for goal in goal_collision_list:
                    self.ball.goal_collision(goal, self.scoreboard)
            # ball-crossbar collision
            crossbar_collision_list = pygame.sprite.spritecollide(self.ball, self.crossbar_sprites, False)
            if crossbar_collision_list:
                for crossbar in crossbar_collision_list:
                    self.ball.crossbar_collision(crossbar)

            # Update
            # Updates Countdown Timer
            game_time = round((pygame.time.get_ticks() - self.start_time) / 1000)
            if game_time > GAME_LENGTH:
                self.display_result()
                self.running = False
            game_time_str = str((GAME_LENGTH - game_time) // 60) + " : " + str((GAME_LENGTH - game_time) % 60)
            self.game_time = FONT.render(game_time_str, 1, WHITE)
            game_time_rect = self.game_time.get_rect(center=SCOREBOARD_TIMER_POSITION)
            # Updates all sprites
            self.update_sprites()

            # Draw (background, all sprites and scoreline)
            self.field.blit(self.background, (0, 0))
            self.draw()
            self.field.blit(self.game_time, game_time_rect)

            pygame.display.flip()

    def update_sprites(self):
        """
        :description:
            Calls update function for all sprites and objects
        :parameter
            None
        :return
            None

        """
        self.all_sprites.update()

    def draw(self):
        """
        :description:
            Calls draw function for all sprites and objects
        :parameter
            None
        :return
            None

        """
        for sprite in self.all_sprites:
            sprite.draw(self.field)

    def display_result(self):
        """
        :description:
            Gets called when the Countdown Timer runs out
            Determines the result and displays it
            Freezes the screen for 3 seconds and the returns to the Start Menu
        :parameter
            None
        :return
            None

        """
        if self.player1_score > self.player2_score:
            result = FONT_CAPTION.render("PLAYER 1 WON", 1, BLACK)
        elif self.player1_score < self.player2_score:
            result = FONT_CAPTION.render("PLAYER 2 WON", 1, BLACK)
        else:
            result = FONT_CAPTION.render("TIE", 1, BLACK)
        result_rect = result.get_rect(center=RESULT_POSITION)
        self.field.blit(result, result_rect)
        pygame.display.update()
        pygame.time.wait(3000)
