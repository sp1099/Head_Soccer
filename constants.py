import pygame

"""
    CONSTANTS FILE:
        File for constants used for positioning, sizes, Fonts, etc.
        most of the numbers are representing pixels for pygame to work with
        Note: Most Constants have are tuples because most of the assets of the game exist two times and must be mirrored
              of their position
    
"""
# Fonts and Colors
pygame.font.init()
FONT = pygame.font.SysFont("gillsansfett", 60)
FONT_SCORE = pygame.font.SysFont("gillsansfett", 90)
FONT_CAPTION = pygame.font.SysFont("gillsansfett", 120)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (175, 175, 175)

# Folder for images
IMAGES = "images"
# Game Settings
FPS = 60
GAME_LENGTH = 180
GRAVITY = 2

# Field Settings
FIELD_SIZE = (1920, 1080)
FIELD_LEVEL = 900
FIELD_LEVEL_SIZE = (FIELD_SIZE[0], 50)
FIELD_LEVEL_POSITION = (0, 900)
BACKGROUND_IMAGE = "head_soccer_stadium.jpg"    # link: https://www.pinterest.de/pin/717550153115081077/

# Button Settings
BUTTON_SIZE = (600, 100)
BUTTON_POSITION = (FIELD_SIZE[0] / 2, FIELD_SIZE[1] / 2)
BUTTON_TEXT_POSITION = (760, 515)

# Start Menu Settings
CAPTION_POSITION = (FIELD_SIZE[0] / 2, 250)
PLAYER1_KEYS_POSITION = ((FIELD_SIZE[0] / 4, 700),
                         (FIELD_SIZE[0] / 4, 820),
                         (FIELD_SIZE[0] / 4, 890),
                         (FIELD_SIZE[0] / 4, 960),
                         (FIELD_SIZE[0] / 4, 1030))
PLAYER2_KEYS_POSITION = (((FIELD_SIZE[0] / 4) * 3, 700),
                         ((FIELD_SIZE[0] / 4) * 3, 820),
                         ((FIELD_SIZE[0] / 4) * 3, 890),
                         ((FIELD_SIZE[0] / 4) * 3, 960),
                         ((FIELD_SIZE[0] / 4) * 3, 1030))
RESULT_POSITION = (FIELD_SIZE[0] / 2, FIELD_SIZE[1] / 2)

# Player Settings
PLAYER_IMAGE = ("head_soccer_player.png", "head_soccer_player.png")     # link: https://opengameart.org/content/football-sprite-based-on-lpc-set
PLAYER_SHOT_IMAGE = ("head_soccer_player_shot.png", "head_soccer_player_shot.png")
PLAYER_SIZE = (80, 150)
PLAYER_START_POSITION = ((1600, FIELD_LEVEL), (300, FIELD_LEVEL))
PLAYER_HOR_SPEED = 10
PLAYER_JUMP_START_SPEED = 25
# Player Movement Keys
JUMP_KEY = (pygame.K_UP, pygame.K_w)
LEFT_KEY = (pygame.K_LEFT, pygame.K_a)
RIGHT_KEY = (pygame.K_RIGHT, pygame.K_d)

# Shoe Settings
SHOE_SIZE = (80, 30)
SHOE_START_POSITION = ((1600, FIELD_LEVEL), (300, FIELD_LEVEL))
# Shot Keys
SHOT_KEY = (pygame.K_p, pygame.K_SPACE)

# Ball Settings
BALL_IMAGE = "head_soccer_ball.png"     # link: https://opengameart.org/content/soccer-ball
BALL_SIZE = (50, 50)
BALL_START_POSITION = (FIELD_SIZE[0]/2, FIELD_SIZE[1]/3)
BALL_MAX_SPEED = 30

# Goal Settings
GOAL_IMAGE = "head_soccer_goal.png"     # self made: Credits to Liam O'Meara
GOAL_SIZE = (125, 370)
GOAL_POSITION = ((25, FIELD_LEVEL+7), (FIELD_SIZE[0]-25-GOAL_SIZE[0], FIELD_LEVEL+7))   # offset to set goal to field_level, not the image
# Goal Collision Settings
GOAL_COLLISION_SIZE = (25, 310)
GOAL_COLLISION_POSITION = ((40, FIELD_LEVEL), (FIELD_SIZE[0]-40-25, FIELD_LEVEL))

# Scoreboard Settings
SCOREBOARD_IMAGE = "head_soccer_scoreboard.png"     # link: https://pixabay.com/de/illustrations/fu%C3%9Fball-stadion-spielfeld-anzeige-1428860/
SCOREBOARD_SIZE = (300, 250)
SCOREBOARD_POSITION = (FIELD_SIZE[0] / 2, 275)
SCOREBOARD_TIMER_POSITION = (FIELD_SIZE[0] / 2, 180)
SCORE_POSITION = ((FIELD_SIZE[0] / 2 - SCOREBOARD_SIZE[0] / 4, 290),
                  (FIELD_SIZE[0] / 2 + SCOREBOARD_SIZE[0] / 4, 290))

# Crossbar Settings
CROSSBAR_FRONT_SIZE = (60, 10)
CROSSBAR_FRONT_POSITION = ((130, 565), (1790, 565))
CROSSBAR_FRONT_ROTATION = (53, -53)
CROSSBAR_TOP_SIZE = (130, 10)
CROSSBAR_TOP_POSITION = ((0, 540), (1920 - CROSSBAR_TOP_SIZE[0], 540))
