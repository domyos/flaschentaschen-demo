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

    def __init__(self, player):
        self._posX = Settings.WIDTH // 2
        self._posY = Settings.HEIGHT // 2
        self._direction = player
        self._angle = random.randint(-80, 80)
        self.speedX = 1 if self._direction else -1

    def get_center(self):
        return list([self._posX, self._posY])

    def get_rect(self):
        return pygame.Rect(self._posX - Settings.BALL_RADIUS, self._posY - Settings.BALL_RADIUS, 2 * Settings.BALL_RADIUS, 2 * Settings.BALL_RADIUS)

    def get_border_rects(self):
        rect1 = pygame.Rect(self._posX - 1, self._posY - Settings.BALL_RADIUS - 1, 1, 1)
        rect2 = pygame.Rect(self._posX - 1, self._posY + Settings.BALL_RADIUS - 1, 1, 1)
        rect3 = pygame.Rect(self._posX - Settings.BALL_RADIUS - 1, self._posY - 1, 1, 1)
        rect4 = pygame.Rect(self._posX + Settings.BALL_RADIUS - 1, self._posY - 1, 1, 1)
        return [rect1, rect2, rect3, rect4]

    def move(self):
        newX = math.cos(Settings.degToRad(self._angle)) * self.speedX * Settings.SPEED
        newY = math.sin(Settings.degToRad(self._angle)) * Settings.SPEED
        posX = self._posX + newX
        posY = self._posY + newY
        self._posX = posX
        self._posY = posY

    def getAngle(self):
        return self._angle

    def setAngle(self, angle):
        self._angle = angle

    def getY(self):
        return self._posY

    def getX(self):
        return self._posX
