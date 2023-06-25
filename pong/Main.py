import Settings
import pygame
from Flaschentaschen import Flaschentaschen
from pong.Game import Game

# import o
# os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()
clock = pygame.time.Clock()
global running
running = True

ip = 'localhost'
port = 1337
flaschentaschen = Flaschentaschen(ip, port, canvas_width=Settings.WIDTH, canvas_height=Settings.HEIGHT)

game = Game(flaschentaschen)

currStage = "menuStage"

selected = 0

menuPoints = {
    "Spiel starten": 0,
    "Steuerung": 1,
    "Spiel beenden": 2,
}

def gameStage():
    global running
    global currStage
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == Settings.PLAYER1_CONTROLS_DOWN:
                game.Players[0].paddle.isMoving = True
                game.Players[0].paddle.dir = 0
            if event.key == Settings.PLAYER1_CONTROLS_UP:
                game.Players[0].paddle.isMoving = True
                game.Players[0].paddle.dir = 1
            if event.key == Settings.PLAYER2_CONTROLS_DOWN:
                game.Players[1].paddle.isMoving = True
                game.Players[1].paddle.dir = 0
            if event.key == Settings.PLAYER2_CONTROLS_UP:
                game.Players[1].paddle.isMoving = True
                game.Players[1].paddle.dir = 1
            if event.key == Settings.ACCEPTSELECTION:
                currStage = "menuStage"
        if event.type == pygame.KEYUP:
            game.Players[0].paddle.isMoving = False
            game.Players[1].paddle.isMoving = False

    game.gameStep()


def menuStage():
    game.screen.fill("black")
    global running
    global selected
    global currStage
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == Settings.PLAYER1_CONTROLS_UP:
                selected = len(menuPoints.keys()) - 1 if selected == 0 else selected - 1
            if event.key == Settings.PLAYER1_CONTROLS_DOWN:
                selected = 0 if selected == len(menuPoints.keys()) - 1 else selected + 1
            if event.key == Settings.ACCEPTSELECTION:
                if selected == 2:
                    pygame.quit()
                elif selected == 1:
                    currStage = "helpStage"
                elif selected == 0:
                    currStage = "gameStage"
    fontLg = pygame.font.SysFont("Arial", Settings.FONTLG)
    fontSm = pygame.font.SysFont("Arial", Settings.FONTSM)
    img1 = fontLg.render("PyPong", True, Settings.ITEM_COLOR)
    game.screen.blit(img1, (Settings.WIDTH // 2 - img1.get_width() // 2,
                            Settings.HEIGHT // 10))
    for index, key in enumerate(menuPoints.keys()):
        img = fontSm.render(key, True, Settings.ITEM_COLOR)
        game.screen.blit(img,
                         (Settings.WIDTH // 2 - img.get_width() // 2, (index + 3) * (Settings.HEIGHT // 10)))
        if selected == menuPoints[key]:
            xPosDot = Settings.WIDTH // 5
            yPosDot = (index + 3) * (Settings.HEIGHT // 10) + Settings.BALL_RADIUS * 2
            pygame.draw.circle(game.screen, Settings.ITEM_COLOR, (xPosDot, yPosDot), Settings.BALL_RADIUS)

    pygame.display.flip()


def helpStage():
    game.screen.fill("black")
    global running
    global currStage
    global selected
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == Settings.ACCEPTSELECTION:
                selected = 0
                currStage = "menuStage"
    fontSm = pygame.font.SysFont("Arial", Settings.FONTSM)
    imgs = [
        fontSm.render("Steuerung:", True, Settings.ITEM_COLOR),
        fontSm.render("Spieler 1", True, Settings.ITEM_COLOR),
        fontSm.render("Hoch: W", True, Settings.ITEM_COLOR),
        fontSm.render("Runter: S", True, Settings.ITEM_COLOR),
        fontSm.render("Spieler 2", True, Settings.ITEM_COLOR),
        fontSm.render("Hoch: T", True, Settings.ITEM_COLOR),
        fontSm.render("Runter: G", True, Settings.ITEM_COLOR),
        fontSm.render("Beide", True, Settings.ITEM_COLOR),
        fontSm.render("Bestätigen/Spiel beenden: Enter", True, Settings.ITEM_COLOR)
    ]
    for index, img in enumerate(imgs):
        game.screen.blit(img, (1, index * Settings.HEIGHT // 10))
    pygame.display.flip()


while running:
    clock.tick(60)  # limits FPS to 60
    if currStage == "menuStage":
        menuStage()
    elif currStage == "gameStage":
        gameStage()
    elif currStage == "helpStage":
        helpStage()
pygame.quit()
