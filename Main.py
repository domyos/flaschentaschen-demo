#!/usr/bin/env python3

from Flaschentaschen import Flaschentaschen
from GameOfLife import GameOfLife
import time


def main():
    # Initialize Flaschentaschen screen
    ip = '192.168.1.23'
    port = 1337
    canvas_width = 192
    canvas_height = 128
    flaschentaschen = Flaschentaschen(ip, port, canvas_width=canvas_width, canvas_height=canvas_height)

    # Initialize game
    def render_function(board):
        color_black = [0,0,0]
        color_white = [255,255,255]
        canvas = [[color_black if cell == 0 else color_white for cell in row] for row in board]
        flaschentaschen.refresh_screen(canvas)

    game = GameOfLife(canvas_width, canvas_height, render_function)

    # Start game loop
    while True:
        game.tick()
        time.sleep(0.1)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
