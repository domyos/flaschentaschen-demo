#!/usr/bin/env python3

from Flaschentaschen import Flaschentaschen
from Snake import Snake
import time


def main():
    # Initialize Flaschentaschen screen
    ip = 'localhost'
    port = 1337
    canvas_width = 128
    canvas_height = 64
    flaschentaschen = Flaschentaschen(ip, port, canvas_width=canvas_width, canvas_height=canvas_height)

    # Initialize game
    def render_function(board_width, board_height, body, food):
        canvas = [[[0,0,0] for cell in range(board_width)] for row in range(board_height)]
        canvas[food[0]][food[1]] = [255, 0, 0]

        for part in body:
            canvas[part[0]][part[1]] = [255, 255, 255]

        flaschentaschen.refresh_screen(canvas)

    game = Snake(canvas_width, canvas_height, render_function)

    # Start game loop
    while True:
        game.tick()
        time.sleep(0.1)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
