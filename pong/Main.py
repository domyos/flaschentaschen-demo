import Settings
import pygame

from Player import Player
from Ball import Ball

Settings.init()

pygame.init()
screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
clock = pygame.time.Clock()
running = True

Players = (Player(False), Player(True))
Ball = Ball()

currentPlayer = Players[0]

game_rect = pygame.Rect(0, 0, Settings.WIDTH, Settings.HEIGHT)


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
        pygame.draw.rect(screen, "red", rect)
        if not rect.colliderect(game_rect):
            collision = True
            wallCollides(index)

    if not collision:
        Ball.move()

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()