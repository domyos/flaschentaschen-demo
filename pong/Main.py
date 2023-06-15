import Settings
import pygame
from Flaschentaschen import Flaschentaschen
from pong.Game import Game

# import o
# os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()
clock = pygame.time.Clock()
running = True

ip = 'localhost'
port = 1337
flaschentaschen = Flaschentaschen(ip, port, canvas_width=Settings.WIDTH, canvas_height=Settings.HEIGHT)

game = Game(flaschentaschen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                game.Players[0].paddle.isMoving = True
                game.Players[0].paddle.dir = 0
            if event.key == pygame.K_w:
                game.Players[0].paddle.isMoving = True
                game.Players[0].paddle.dir = 1
            if event.key == pygame.K_g:
                game.Players[1].paddle.isMoving = True
                game.Players[1].paddle.dir = 0
            if event.key == pygame.K_t:
                game.Players[1].paddle.isMoving = True
                game.Players[1].paddle.dir = 1
        if event.type == pygame.KEYUP:
            game.Players[0].paddle.isMoving = False
            game.Players[1].paddle.isMoving = False

    game.gameStep()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
