import random
from copy import deepcopy

class GameOfLife:
    def initialize_board(self, board_width, board_height):
        return [[random.randint(0, 1) for i in range(board_width)] for j in range(board_height)]
    
    def __init__(self, board_width, board_height, render_function):
        self.board_width = board_width
        self.board_height = board_height
        self.board = self.initialize_board(board_width, board_height)
        self.render_function = render_function
    
    def check_neighbors(self, x, y):
        neighbours = 0
        if(self.board[(x-1) % self.board_height][y] == 1):
            neighbours += 1
        if(self.board[(x-1) % self.board_height][(y-1) % self.board_width] == 1):
            neighbours += 1
        if(self.board[x][(y-1) % self.board_width] == 1):
            neighbours += 1
        if(self.board[(x+1) % self.board_height][(y-1) % self.board_width] == 1):
            neighbours += 1
        if(self.board[(x+1) % self.board_height][y] == 1):
            neighbours += 1
        if(self.board[(x+1) % self.board_height][(y+1) % self.board_width] == 1):
            neighbours += 1
        if(self.board[x][(y+1) % self.board_width] == 1):
            neighbours += 1
        if(self.board[(x-1) % self.board_height][(y+1) % self.board_width] == 1):
            neighbours += 1
        return neighbours

    def tick(self):
        next_frame = deepcopy(self.board)
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                neighbours = self.check_neighbors(x, y)
                if self.board[x][y] == 1:
                    if neighbours > 3:
                        next_frame[x][y] = 0
                    if(neighbours == 2):
                        next_frame[x][y] = 1
                    if(neighbours == 3):
                        next_frame[x][y] = 1
                    if neighbours < 2:
                        next_frame[x][y] = 0	
                if self.board[x][y] == 0:
                    if(neighbours == 3):
                        next_frame[x][y] = 1

        self.board = next_frame
        self.render_function(self.board)