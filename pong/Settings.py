import math

WIDTH = 128
HEIGHT = 96
PADDLE_WIDTH = 5

BALL_RADIUS = 5

ITEM_COLOR = (255, 255, 255)

PLAYER1_CONTROLS_UP = "W"
PLAYER1_CONTROLS_DOWN = "S"
PLAYER2_CONTROLS_UP = "O"
PLAYER2_CONTROLS_DOWN = "L"


def init():
    global WIDTH
    global HEIGHT
    global PADDLE_WIDTH


def degToRad(angle):
    return angle * math.pi / 180


def radToDeg(angle):
    return angle * 180 / math.pi
