import pygame

import Settings
from Ball import Ball
from Player import Player


class Game:
    def __init__(self, flaschentaschen):
        self.screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))

        self.Players = (Player(False), Player(True))
        self.Ball = Ball()

        self.currentPlayer = self.Players[1]

        self.game_rect = pygame.Rect(0, 0, Settings.WIDTH, Settings.HEIGHT)
        self.flaschentaschen = flaschentaschen

        self.font = pygame.font.Font("arial.ttf", 24)
        self.img1 = self.font.render(str(self.Players[0].score), True, (255, 255, 255))
        self.img2 = self.font.render(str(self.Players[1].score), True, (255, 255, 255))

        self.isColliding = False

    def makeCanvas(self):
        canvas = []
        for y in range(Settings.HEIGHT):
            canvas.append([])
            for x in range(Settings.WIDTH):
                canvas[y].append([])
                r, g, b, a = self.screen.get_at((x, y))
                color = [r, g, b]
                canvas[y][x] = color
        self.flaschentaschen.refresh_screen(canvas)

    def playerCollides(self, player):
        playerPosY = self.Players[1 if player else 0].paddle.get_posY()
        ballPosY = self.Ball.getY()
        relativeIntersectY = playerPosY - ballPosY
        normalizedRelativeIntersectionY = (relativeIntersectY / (Settings.PADDLE_HEIGHT / 2))
        bounceAngle = normalizedRelativeIntersectionY * Settings.MAXBOUNCE * -1
        self.Ball.speedX *= -1
        self.Ball.setAngle(bounceAngle)

    def wallCollides(self, ind):
        if ind <= 1:
            currAngle = self.Ball.getAngle()
            self.Ball.setAngle(360 - currAngle)
        else:
            curr = self.currentPlayer.player
            self.Players[1 if curr else 0].score += 1
            self.currentPlayer = self.Players[1]
            self.Ball = Ball()

    def gameStep(self):
        self.screen.fill("black")

        pygame.draw.circle(self.screen, Settings.ITEM_COLOR, self.Ball.get_center(), Settings.BALL_RADIUS)

        for player in self.Players:
            pygame.draw.rect(self.screen, Settings.ITEM_COLOR, player.paddle.get_rect())

        ballNearPlayer = self.Ball.getX() <= Settings.PADDLE_WIDTH or (
                    Settings.WIDTH - self.Ball.getX()) <= Settings.PADDLE_WIDTH

        if not self.isColliding and ballNearPlayer:
            if not self.currentPlayer.player and self.Players[0].paddle.get_rect().colliderect(
                    self.Ball.get_border_rects()[2]):
                self.isColliding = True
                self.playerCollides(self.currentPlayer.player)
            if self.currentPlayer.player and self.Players[1].paddle.get_rect().colliderect(
                    self.Ball.get_border_rects()[3]):
                self.isColliding = True
                self.playerCollides(self.currentPlayer.player)
        if self.isColliding and not self.Players[0].paddle.get_rect().colliderect(
                self.Ball.get_border_rects()[2]) and not self.Players[1].paddle.get_rect().colliderect(
            self.Ball.get_border_rects()[3]):
            self.isColliding = False
            self.currentPlayer = self.Players[0 if self.currentPlayer.player else 1]

        for index, rect in enumerate(self.Ball.get_border_rects()):
            if not rect.colliderect(self.game_rect):
                self.wallCollides(index)

        self.Ball.move()
        if self.Players[0].paddle.isMoving and self.Players[0].paddle.dir == 0:
            self.Players[0].paddle.move(False)
        if self.Players[0].paddle.isMoving and self.Players[0].paddle.dir == 1:
            self.Players[0].paddle.move(True)
        if self.Players[1].paddle.isMoving and self.Players[1].paddle.dir == 0:
            self.Players[1].paddle.move(False)
        if self.Players[1].paddle.isMoving and self.Players[1].paddle.dir == 1:
            self.Players[1].paddle.move(True)
        img1 = self.font.render(str(self.Players[0].score), False, (255, 255, 255))
        img2 = self.font.render(str(self.Players[1].score), False, (255, 255, 255))
        self.screen.blit(img1, (100, 1))
        self.screen.blit(img2, (1, 1))
        self.makeCanvas()
        pygame.display.flip()
