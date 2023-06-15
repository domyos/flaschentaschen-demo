import math
import random

# 96*128
import pygame

import Settings


class Ball:
    _posX = 0
    _posY = 0
    _direction = True
    _angle = 0

    def __init__(self):
        self._posX = Settings.WIDTH // 2
        self._posY = Settings.HEIGHT // 2
        self._direction = True
        self._angle = random.randint(-80, 80)

    def get_center(self):
        return list([self._posX, self._posY])

    def get_rect(self):
        return pygame.Rect(self._posX - Settings.BALL_RADIUS, self._posY - Settings.BALL_RADIUS, 2 * Settings.BALL_RADIUS, 2 * Settings.BALL_RADIUS)

    def get_border_rects(self):
        rect1 = pygame.Rect(self._posX - 2, self._posY - Settings.BALL_RADIUS - 2, 4, 4)
        rect2 = pygame.Rect(self._posX - 2, self._posY + Settings.BALL_RADIUS - 2, 4, 4)
        rect3 = pygame.Rect(self._posX - Settings.BALL_RADIUS - 2, self._posY - 2, 4, 4)
        rect4 = pygame.Rect(self._posX + Settings.BALL_RADIUS - 2, self._posY - 2, 4, 4)
        return [rect1, rect2, rect3, rect4]

    def move(self):
        newX = math.cos(Settings.degToRad(self._angle))
        newY = math.sin(Settings.degToRad(self._angle))
        posX = self._posX + newX
        posY = self._posY + newY
        self._posX = posX
        self._posY = posY
