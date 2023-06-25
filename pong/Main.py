import Settings
import pygame
from Flaschentaschen import Flaschentaschen
from Game import Game

# import os
# os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()
clock = pygame.time.Clock()

ip = 'localhost'
port = 1337
flaschentaschen = Flaschentaschen(ip, port, canvas_width=Settings.WIDTH, canvas_height=Settings.HEIGHT)

game = Game(flaschentaschen)


def gameOverStage():
    game.screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == Settings.ACCEPTSELECTION:
                game.currStage = "menuStage"
    font = pygame.font.Font('arial.ttf', Settings.FONTLG)
    font2 = pygame.font.Font('arial.ttf', Settings.FONTSM)
    img = font.render("Game Over", False, Settings.ITEM_COLOR)
    img2 = font2.render("Player 2 hat gewonnen!" if game.Players[0].score >= 10 else "Player 1 hat gewonnen!", False, Settings.ITEM_COLOR)
    game.screen.blit(img, (Settings.WIDTH // 2 - img.get_width() // 2, Settings.HEIGHT // 2 - img.get_height() // 2))
    game.screen.blit(img2, (Settings.WIDTH // 2 - img2.get_width() // 2, Settings.HEIGHT // 2 + img.get_height() // 2))


def gameStage():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == Settings.ACCEPTSELECTION:
                game.currStage = "menuStage"
    keys = pygame.key.get_pressed()
    if keys[Settings.PLAYER1_CONTROLS_DOWN]:
        game.Players[0].paddle.isMoving = True
        game.Players[0].paddle.dir = 0
    elif keys[Settings.PLAYER1_CONTROLS_UP]:
        game.Players[0].paddle.isMoving = True
        game.Players[0].paddle.dir = 1
    else:
        game.Players[0].paddle.isMoving = False
    if keys[Settings.PLAYER2_CONTROLS_DOWN]:
        game.Players[1].paddle.isMoving = True
        game.Players[1].paddle.dir = 0
    elif keys[Settings.PLAYER2_CONTROLS_UP]:
        game.Players[1].paddle.isMoving = True
        game.Players[1].paddle.dir = 1
    else:
        game.Players[1].paddle.isMoving = False

    game.gameStep()


def menuStage():
    game.screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == Settings.PLAYER1_CONTROLS_UP:
                game.selected = len(game.menuPoints.keys()) - 1 if game.selected == 0 else game.selected - 1
            if event.key == Settings.PLAYER1_CONTROLS_DOWN:
                game.selected = 0 if game.selected == len(game.menuPoints.keys()) - 1 else game.selected + 1
            if event.key == Settings.ACCEPTSELECTION and game.currStage == "menuStage":
                if game.selected == 2:
                    pygame.quit()
                elif game.selected == 1:
                    game.currStage = "helpStage"
                elif game.selected == 0:
                    game.Players[0].score = 0
                    game.Players[1].score = 0
                    game.currStage = "gameStage"
    fontLg = pygame.font.Font("arial.ttf", Settings.FONTLG)
    fontSm = pygame.font.Font("arial.ttf", Settings.FONTSM)
    img1 = fontLg.render("PyPong", False, Settings.ITEM_COLOR)
    game.screen.blit(img1, (Settings.WIDTH // 2 - img1.get_width() // 2,
                            Settings.HEIGHT // 10))
    for index, key in enumerate(game.menuPoints.keys()):
        img = fontSm.render(key, False, Settings.ITEM_COLOR)
        game.screen.blit(img,
                         (Settings.WIDTH // 2 - img.get_width() // 2, (index + 3) * (Settings.HEIGHT // 10)))
        if game.selected == game.menuPoints[key]:
            xPosDot = Settings.WIDTH // 5
            yPosDot = (index + 3) * (Settings.HEIGHT // 10) + Settings.BALL_RADIUS * 2
            pygame.draw.circle(game.screen, Settings.ITEM_COLOR, (xPosDot, yPosDot), Settings.BALL_RADIUS)
    game.makeCanvas()
    pygame.display.flip()


def helpStage():
    game.screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == Settings.ACCEPTSELECTION:
                game.selected = 0
                game.currStage = "menuStage"
    fontSm = pygame.font.Font("arial.ttf", Settings.FONTSM)
    imgs = [
        fontSm.render("Steuerung:", False, Settings.ITEM_COLOR),
        fontSm.render("Spieler 1", False, Settings.ITEM_COLOR),
        fontSm.render("Hoch: W", False, Settings.ITEM_COLOR),
        fontSm.render("Runter: S", False, Settings.ITEM_COLOR),
        fontSm.render("Spieler 2", False, Settings.ITEM_COLOR),
        fontSm.render("Hoch: T", False, Settings.ITEM_COLOR),
        fontSm.render("Runter: G", False, Settings.ITEM_COLOR),
        fontSm.render("Beide", False, Settings.ITEM_COLOR),
        fontSm.render("Bestätigen/Spiel beenden: Enter", False, Settings.ITEM_COLOR)
    ]
    for index, img in enumerate(imgs):
        game.screen.blit(img, (1, index * Settings.HEIGHT // 10))


while game.running:
    clock.tick(60)  # limits FPS to 60
    if game.currStage == "menuStage":
        menuStage()
    elif game.currStage == "gameStage":
        if game.Players[0].score >= 10 or game.Players[1].score >= 10:
            game.currStage = "gameOverStage"
        else:
            gameStage()
    elif game.currStage == "helpStage":
        helpStage()
    elif game.currStage == "gameOverStage":
        gameOverStage()
    game.makeCanvas()
    pygame.display.flip()
pygame.quit()
