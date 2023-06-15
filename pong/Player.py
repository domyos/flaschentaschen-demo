from Paddle import Paddle


class Player:
    score = 0

    def __init__(self, player):
        self.paddle = Paddle(player)
        self.player = player

