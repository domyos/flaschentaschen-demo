from Paddle import Paddle


class Player:

    def __init__(self, player):
        self.paddle = Paddle(player)
        self.player = player
        self.score = 0

