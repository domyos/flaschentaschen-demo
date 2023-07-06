import pygame

import Settings


class Paddle:

    _width = Settings.PADDLE_WIDTH
    _height = Settings.PADDLE_HEIGHT

    def __init__(self, side):
        self._posY = (Settings.HEIGHT // 2)
        self._posX = 0 if not side else Settings.WIDTH - self._width
        self._leftOrRight = side
        self.isMoving = False
        self.dir = 0

    def get_posX(self):
        return self._posX

    def get_posY(self):
        return self._posY

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def get_rect(self):
        y1 = self._posY - self._height // 2
        rect = (self._posX, y1, self._width, self._height)
        return pygame.Rect(rect)

    def move(self, isUpOrDown):
        if isUpOrDown:
            if self._posY - 1 - (self._height // 2) < 0:
                self._posY = self._height // 2
            else:
                self._posY -= 1 * Settings.SPEED
        else:
            if self._posY + 1 + (self._height // 2) > Settings.HEIGHT:
                self._posY = Settings.HEIGHT - (self._height // 2)
            else:
                self._posY += 1 * Settings.SPEED
