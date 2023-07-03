import socket

class Flaschentaschen:
    def __init__(self, ip, port, canvas_width, canvas_height):
        self.ip = ip
        self.port = port
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def refresh_screen(self, canvas):
        half_width = self.canvas_width // 2
        half_height = self.canvas_height // 2

        # Split canvas into four equal quadrants
        top_left = [canvas[i][:half_width] for i in range(half_height)]
        bottom_left = [canvas[i][:half_width] for i in range(half_height, self.canvas_height)]
        top_right = [canvas[i][half_width:] for i in range(half_height)]
        bottom_right = [canvas[i][half_width:] for i in range(half_height, self.canvas_height)]

        # Send each quadrant individually to Flaschentaschen server to avoid packets that are greater than MTU
        self.send(canvas = top_left,        x_offset = 0,           y_offset = 0)
        self.send(canvas = top_right,       x_offset = half_width,  y_offset = 0)
        self.send(canvas = bottom_left,     x_offset = 0,           y_offset = half_height)
        self.send(canvas = bottom_right,    x_offset = half_width,  y_offset = half_height)


    def send(self, canvas, x_offset, y_offset):
        result = bytearray()
        for y in range(len(canvas)):
            for x in range(len(canvas[0])): 
                for c in range(3):
                    result.append(canvas[y][x][c])
        header = b"P6 %d %d \n#FT:%d %d 0\n255\n" % (len(canvas[0]), len(canvas), x_offset, y_offset)
        self.connection.sendto(header + result, (self.ip, self.port))
