import keyboard

class Snake:
    def __init__(self, board_width, board_height, render_function):
        self.board_width = board_width
        self.board_height = board_height
        self.render_function = render_function

        self.dx = 1
        self.dy = 0
        self.x = board_width // 2
        self.y = board_height // 2
        print("init")

    def tick(self):
        
        # Clear board
        board = [[0 for i in range(self.board_width)] for j in range(self.board_height)]

        # Render snake
        board[self.y][self.x] = 1

        # Handle input
        if keyboard.is_pressed('p'):
            print("You pressed p")


        self.x += self.dx
        self.y += self.dy

        self.render_function(board)
        print('tick %d %d'%(self.x, self.y))
