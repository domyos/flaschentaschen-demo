import socket

class Flaschentaschen:
    def __init__(self, ip, port, canvas_width, canvas_height):
        self.ip = ip
        self.port = port
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

    def refresh_screen(self, canvas):
        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        result = bytearray()
        for y in range(self.canvas_height):
            for x in range(self.canvas_width): 
                for c in range(3):
                    result.append(canvas[y][x][c])
        header = b"P6 %d %d \n#FT:0 %d 0\n255\n" % (self.canvas_width, self.canvas_height, 0)
        connection.sendto(header + result, (self.ip, self.port))
