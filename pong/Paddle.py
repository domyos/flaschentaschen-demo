import Settings


class Paddle:
    _posY = 0
    _width = Settings.PADDLE_WIDTH
    _height = Settings.HEIGHT // 5
    _posX = 0
    _leftOrRight = True

    def __init__(self, side):
        self._posY = (Settings.HEIGHT // 2)
        self._posX = 0 if side else Settings.WIDTH - self._width
        self._leftOrRight = side

    def get_posX(self):
        return self._posX

    def get_posY(self):
        return self._posY

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def get_rect(self):
        x1 = 0 if self._leftOrRight else Settings.WIDTH - self._width
        y1 = self._posY - self._height // 2
        rect = (x1, y1, self._width, self._height)
        return rect

    def move(self, isUpOrDown):
        if isUpOrDown:
            if self._posY - 1 - (self._height // 2) < 0:
                self._posY = self._height // 2
            else:
                self._posY -= 1
        else:
            if self._posY + 1 + (self._height // 2) > Settings.HEIGHT:
                self._posY = Settings.HEIGHT
            else:
                self._posY += 1
