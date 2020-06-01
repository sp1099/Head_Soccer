import pygame, os
import time
from constants import *
from helper_sprites import Crossbar_Collision_Front, Crossbar_Collision_Top


class Ball(pygame.sprite.Sprite):
    """
    Ball Class:
        Initializes a Ball Object
        Inherits from the pygame.sprite.Sprite class which must be initialized in the beginning
        Most important Class in the game
        Handles the whole ball physics
            Ball Movement
            Change of Movement (Due to Collision)
            Goal Detection
    """

    def __init__(self, game_handler):
        """
        :description:
            Initializes a Ball Object
            Inherits from the pygame.sprite.Sprite class which must be initialized in the beginning
            Loads the image
            Resets the ball to its starting position
        :parameter
            game_handler (Game_Manager): Class that holds the game (because Ball class needs access to all classes)
        :return
            None

        """
        # Initialize Sprite
        pygame.sprite.Sprite.__init__(self)
        self.lastGroundCollision = time.time()
        self.game = game_handler
        self.image = pygame.image.load(os.path.join(IMAGES, BALL_IMAGE))
        self.image = pygame.transform.scale(self.image, BALL_SIZE)
        self.rect = self.image.get_rect()
        self.reset_ball()
        self.oldMaxHeight = self.rect.midtop

    def update(self):
        """
        :description:
            Updates the current position of the ball based on the old position and the calculated speed of the ball
            Integrates a max Ball speed so that the Ball will never get to fast to play fluently
            Also integrates friction in x direction and gravity in y direction
            If the Ball is flies outside the screen it gets reset to the start position
        :parameter
            None
        :return
            None

        """
        # Check for speed higher than BALL_MAX_SPEED
        if abs(self.speedx) > BALL_MAX_SPEED:
            self.speedx = self.sign(self.speedx) * BALL_MAX_SPEED
        # adjustment of the x position
        self.rect.x += self.speedx
        self.speedx = self.speedx * 0.99999
        # adjustment of the y position
        self.rect.y += self.speedy
        self.speedy += GRAVITY
        if self.rect.bottom > FIELD_LEVEL + 2:
            self.rect.bottom = FIELD_LEVEL + 2
        # check for Ball outside screen
        if self.rect.right < 0 or self.rect.left > 1920:
            self.reset_ball()

    def player_collision(self, player):
        """
        :description:
            Handles collision between Ball and a Player
            changes the speed of the Ball according to where it hit the player
                necessary so the ball will perform understandable movements after colliding with a Player
        :parameter
            player (Player): Player which the Ball collided with
        :return
            None

        """
        # check where the collision took place
        # move the ball a bit so that there are no "multiple" collisions inside the player
        # also for a better experience, even while on the floor on collision th ball is getting a slight y speedup
        if player.rect.collidepoint(self.rect.midbottom) is not player.rect.collidepoint(self.rect.midtop):
            # collision at bottom of the player
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
            # collision at top of the player
            elif player.rect.collidepoint(self.rect.midtop) and self.rect.midbottom > player.rect.midbottom:
                self.rect.left = player.rect.right + 5
                self.speedx += 5
                self.speedy = 20
            else:
                self.rect.right = player.rect.left - 5
                self.speedx -= 5
                self.speedy = 20
        else:
            # collision on one of the player sides
            if player.rect.right - 20 < self.rect.right and not player.rect.collidepoint(self.rect.midtop):
                self.rect.left = player.rect.right + 5
            elif player.rect.left + 20 > self.rect.left and not player.rect.collidepoint(self.rect.midtop):
                self.rect.right = player.rect.left - 5
        # function to manipulate the ball speed based on the player movement
        self.manipulate_speedx(player)
        # y direction speed increment
        if abs(self.speedx) > 25 and self.rect.bottom > FIELD_LEVEL - 20:
            self.speedy = abs(self.speedx)/2

    def draw(self, field):
        # draws the image onto the given field, which is the screen
        field.blit(self.image, self.rect)

    def shoe_collision(self, shoe):
        """
        :description:
            Handles collision between Ball and a Shoe
            changes the speed of the Ball when shot with a shoe
                ball will perform a parabolic curve
        :parameter
            shoe (Shoe): Shoe which the Ball collided with
        :return
            None

        """
        if shoe.shot:
            # set ball speed to shot speed, direction depending on which Player/Shoe hit the Ball
            if shoe.player_num == 0:
                self.speedy = 50
                self.speedx -= 30
            else:
                self.speedy = 50
                self.speedx += 30
        elif shoe.move:
            # function to manipulate the ball speed based on the player movement
            self.manipulate_speedx(shoe)

    def ground_collision(self):
        """
        :description:
            Handles collision between Ball and a Ground_Surface
            inverts the y speed of the Ball when colliding with the Ground
                beneath a certain value the y speed must be set to 0, otherwise the Ball bounces forever
        :parameter
            None
        :return
            None

        """
        # keep track of the time between to ground collisions
        self.newGroundCollision = time.time()
        self.speedx *= 0.99
        self.time = self.newGroundCollision - self.lastGroundCollision
        # check if the Ball is so slow that its y speed must be set to 0
        if 0.08 < self.time < 0.4 + self.speedx * 0.005 or (abs(self.speedy) < 7):
            self.speedy = 0
        else:
            # otherwise y speed gets inverted and decreased by a factor
            self.speedy = -int(self.speedy * 0.75)
        self.lastGroundCollision = time.time()

    def goal_collision(self, goal, scoreboard):
        """
        :description:
            Handles collision between Ball and a Goal
            Resets the Ball and Players to to start position
            updates the scoreline of the Scoreboard
        :parameter
            goal (Goal): Goal which the Ball collided with
            scoreboard (Scoreboard): Scoreboard to update its scoreline
        :return
            None

        """
        # Score updates
        if goal.goal_num == 0:
            self.game.player2_score += 1
        else:
            self.game.player1_score += 1
        # Scoreline update of the scoreboard
        scoreboard.update_scoreline(self.game.player1_score, self.game.player2_score)
        # Reset ball and Players
        self.rect.bottomleft = BALL_START_POSITION
        self.game.player1.rect.bottomleft = PLAYER_START_POSITION[self.game.player1.player_num]
        self.game.player2.rect.bottomleft = PLAYER_START_POSITION[self.game.player2.player_num]
        self.game.shoe1.rect.bottomleft = SHOE_START_POSITION[self.game.shoe1.player_num]
        self.game.shoe2.rect.bottomleft = SHOE_START_POSITION[self.game.shoe2.player_num]

        self.speedx = 0
        self.speedy = 0

    def crossbar_collision(self, crossbar):
        """
        :description:
            Handles collision between Ball and a Crossbar
            Differs between crossbar front and crossbar top
                when hit the crossbar front the x speed gets inverted
                when hit the crossbar top the y speed gets inverted
                both times with integrated friction factor
        :parameter
            crossbar (Crossbar_Top or Crossbar_Front): Crossbar which the Ball collided with
        :return
            None

        """
        # Collision with Crossbar Front
        if isinstance(crossbar, Crossbar_Collision_Front):
            self.speedx = -self.speedx * 0.9
        # Collision with Crossbar Top
        elif isinstance(crossbar, Crossbar_Collision_Top):
            self.speedy = -self.speedy * 0.75

    def manipulate_speedx(self, player):
        """
        :description:
            Adjusts the speed of the Ball depending on the speed of the player
                player standing:
                    ball reflecting with integrated friction
                player towards the ball:
                    ball reflecting with speed increase
                player away from ball:
                    ball reflecting with speed decrease
        :parameter
            player (Player): Player which the Ball collided with
        :return
            None
        """

        #difficulty:
        #   -player object has no member variable speedx
        #   -wrong data types
        #   -overflow
        """
        import sys

        player.temp = ["speedx", sys.float_info.max]
        ball.temp = [None, sys.float_info.max]
        message = "New speedx value is {speedx}"

        for i in range(0,1):
            player.speedx = player.temp[i]
            ball.speedx = self.temp[i]
            ball.manipulate_speedx(player)
            print(message.format(speedx = ball.speedx))

        del player.speedx
        ball.manipulate_speedx(player)
        print(message.format(speedx = ball.speedx))
        """
        # player standing still
        if player.speedx == 0:
            self.speedx = -self.speedx * 0.9
        elif self.speedx == 0:
            self.speedx = player.speedx + self.sign(player.speedx) * 10
        # player towards ball
        elif (self.speedx * player.speedx) > 0:
            if abs(player.speedx) > abs(self.speedx):
                self.speedx = self.speedx + player.speedx
            else:
                self.speedx = -self.speedx + player.speedx
        # player away from ball
        else:
            self.speedx = -(self.speedx) + player.speedx + self.sign(player.speedx) * 20
        # check for max ball speed
        if abs(self.speedx) > BALL_MAX_SPEED:
            self.speedx = self.sign(self.speedx) * BALL_MAX_SPEED

    def manipulate_speedy(self, player):
        # inverts the y speed of the ball
        # integrates friction factor
        self.speedy = -int(self.speedy * 0.75) + abs(player.speedy)

    def sign(self, num):
        """
        :description:
            returns the sign / direction of the ball speed
        :parameter
            num (int): number to determine the sign of
        :return
            sign (int): either +1 or -1

        """

        #difficulty:
        #   wrong data type
        #   num is zero
        #   num is complex
        """
        num = ["num", 0, 2 + 3j]
        message = "Return value of sign({num}) is {value}"

        for i in num:
            result = ball.sign(i)
            print(message.format(num = i, value = result))
        """
        return (num//abs(num))

    def reset_ball(self):
        # resets Ball to Starting Position with no speed
        self.rect.bottomleft = BALL_START_POSITION
        self.speedx = 0
        self.speedy = 0


