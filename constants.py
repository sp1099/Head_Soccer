import pygame

pygame.font.init()
IMAGES = "images"
FPS = 60

FIELD_SIZE = (1920, 1080)
FIELD_LEVEL = 900
FIELD_LEVEL_SIZE = (FIELD_SIZE[0], 50)
FIELD_LEVEL_POSITION = (0, 900)
GRAVITY = 2
BACKGROUND_IMAGE = "head_soccer_stadium.jpg"    #link: https://www.pinterest.de/pin/717550153115081077/

PLAYER_IMAGE = ("", "")
PLAYER_SIZE = (80, 180)
PLAYER_START_POSITION = ((1600, FIELD_LEVEL), (300, FIELD_LEVEL))
PLAYER_HOR_SPEED = 10
PLAYER_JUMP_START_SPEED = 25
JUMP_KEY = (pygame.K_UP, pygame.K_w)
LEFT_KEY = (pygame.K_LEFT, pygame.K_a)
RIGHT_KEY = (pygame.K_RIGHT, pygame.K_d)

SHOE_IMAGE = "head_soccer_shoe.jpeg"
SHOE_SIZE = (60, 30)
SHOE_START_POSITION = ((1600, FIELD_LEVEL), (320, FIELD_LEVEL))
SHOT_KEY = (pygame.K_p, pygame.K_SPACE)

BALL_IMAGE = "head_soccer_ball.png"     #link: https://opengameart.org/content/soccer-ball
BALL_SIZE = (50, 50)
BALL_START_POSITION = (FIELD_SIZE[0]/2, FIELD_SIZE[1]/3)
BALL_MAX_SPEED = 50

GOAL_IMAGE = "head_soccer_goal.png"
GOAL_SIZE = (125, 370)
GOAL_POSITION = ((25, FIELD_LEVEL+7), (FIELD_SIZE[0]-25-GOAL_SIZE[0], FIELD_LEVEL+7))   # offset to set goal to field_level, not the image
GOAL_COLLISION_SIZE = (25, 290)
GOAL_COLLISION_POSITION = ((40, FIELD_LEVEL), (FIELD_SIZE[0]-40-25, FIELD_LEVEL))

SCOREBOARD_IMAGE = "head_soccer_scoreboard.png"
SCOREBOARD_SIZE = (300, 250)
SCOREBOARD_POSITION = (810, 400)

FONT = pygame.font.SysFont("ROGFonts", 75)
WHITE = (255, 255, 255)

