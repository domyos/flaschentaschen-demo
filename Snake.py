import random
import keyboard

class Snake:
    def __init__(self, board_width, board_height, render_function):
        self.board_width = board_width
        self.board_height = board_height
        self.render_function = render_function

        self.dx = 1
        self.dy = 0
        self.length = 1
        self.body = [self.randomxy()]

        self.food = self.randomxy()
        self.count = 0

    def randomxy(self):
        return [random.randint(0, self.board_height - 1), random.randint(0, self.board_width - 1)]

    def tick(self):
        self.count += 1

        # Handle input
        pressed_key = keyboard.read_key()

        # left
        if pressed_key == 'a':
            self.body.insert(0, [self.body[0][0], (self.body[0][1] - 1) % self.board_width])
        # right
        elif pressed_key == 'd':
            self.body.insert(0, [self.body[0][0], (self.body[0][1] + 1) % self.board_width])
        # up
        elif pressed_key == 'w':
            self.body.insert(0, [(self.body[0][0] - 1) % self.board_height, self.body[0][1]])
        # down
        elif pressed_key == 's':
            self.body.insert(0, [(self.body[0][0] + 1) % self.board_height, self.body[0][1]])

        if(self.food == self.body[0] or self.count % 10 == 0):
            self.length += 1
            self.food = self.randomxy()

        self.body = self.body[:self.length]

        for i, pos in enumerate(self.body):
            if(self.body[i] == self.body[0] and i!=0):
                self.length = 1
                self.body = [self.randomxy()]

        self.render_function(self.board_width, self.board_height, self.body, self.food)
