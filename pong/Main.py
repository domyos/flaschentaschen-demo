import Settings
import pygame
from Flaschentaschen import Flaschentaschen
from Player import Player
from Ball import Ball
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

Settings.init()

pygame.init()
screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
clock = pygame.time.Clock()
running = True

Players = (Player(False), Player(True))
Ball = Ball()

currentPlayer = Players[0]

ip = 'localhost'
port = 1337
flaschentaschen = Flaschentaschen(ip, port, canvas_width=Settings.WIDTH, canvas_height=Settings.HEIGHT)

game_rect = pygame.Rect(0, 0, Settings.WIDTH, Settings.HEIGHT)


def makeCanvas():
    canvas = []
    for y in range(Settings.HEIGHT):
        canvas.append([])
        for x in range(Settings.WIDTH):
            canvas[y].append([])
            r, g, b, a = screen.get_at((x, y))
            color = [r, g, b]
            canvas[y][x] = color
    flaschentaschen.refresh_screen(canvas)


def playerCollides(player):
    print(f"colliding player {1 if player else 2}")


def wallCollides(ind):
    print(f"colling {'top' if ind == 0 else 'bottom' if ind == 1 else 'left' if ind == 2 else 'right'} Wall")


while running:

    collision = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    player_rects = []

    for Player in Players:
        currPlayerRect = pygame.Rect(Player.paddle.get_rect())
        player_rects.append(currPlayerRect)
        pygame.draw.rect(screen, Settings.ITEM_COLOR, currPlayerRect)

    pygame.draw.circle(screen, Settings.ITEM_COLOR, Ball.get_center(), Settings.BALL_RADIUS)

    for rect in player_rects:
        if rect.colliderect(Ball.get_border_rects()[2]) or rect.colliderect(Ball.get_border_rects()[3]):
            collision = True
            playerCollides(currentPlayer.player)

    for index, rect in enumerate(Ball.get_border_rects()):
        if not rect.colliderect(game_rect):
            collision = True
            wallCollides(index)

    if not collision:
        Ball.move()

    pygame.display.flip()

    makeCanvas()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
