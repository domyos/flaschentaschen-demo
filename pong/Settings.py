import math

import pygame

WIDTH = 128
HEIGHT = 96
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 24
SPEED = 1

FONTLG = 15
FONTSM = 10

MAXBOUNCE = 80

BALL_RADIUS = 3

ITEM_COLOR = (255, 255, 255)

PLAYER1_CONTROLS_UP = pygame.K_w
PLAYER1_CONTROLS_DOWN = pygame.K_s
PLAYER2_CONTROLS_UP = pygame.K_t
PLAYER2_CONTROLS_DOWN = pygame.K_g
ACCEPTSELECTION = pygame.K_RETURN

def degToRad(angle):
    return angle * math.pi / 180


def radToDeg(angle):
    return angle * 180 / math.pi
