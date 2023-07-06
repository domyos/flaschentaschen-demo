import math

import pygame

WIDTH = 192
HEIGHT = 128
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 24
SPEED = 1.5

FONTLG = 15
FONTSM = 10

MAXBOUNCE = 80

BALL_RADIUS = 3

ITEM_COLOR = (255, 255, 255)

# Player 1 controls
PLAYER1_CONTROLS_UP = pygame.K_w
PLAYER1_CONTROLS_DOWN = pygame.K_s
ACCEPTSELECTION1 = pygame.K_v

# Player 2 controls
PLAYER2_CONTROLS_UP = pygame.K_UP
PLAYER2_CONTROLS_DOWN = pygame.K_DOWN
ACCEPTSELECTION2 = pygame.K_COMMA

def degToRad(angle):
    return angle * math.pi / 180


def radToDeg(angle):
    return angle * 180 / math.pi
