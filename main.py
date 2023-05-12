import pygame
from misc import *

pygame.init()

colors = {
    "red": (255,0,0),
    "white": (200,200,200),
    "black": (0,0,0),
    "gray": (100,100,100),
    "win_bg": (8, 84, 84),
    "loose_bg": (239, 28, 28)
}

screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
running = True
inGame = False
isEnd = False
isWin = False

screenWidth = screen.get_width()
screenHeight = screen.get_height()

pygame.display.set_caption("PyJa Cross", "https://cdn-icons-png.flaticon.com/512/124/124034.png?w=360")
clock = pygame.time.Clock()
# icon = pygame.image.load("images/logo.png")
# pygame.display.set_icon(icon)

fonts = {
    "default": pygame.font.SysFont(None, 50),
    "title": pygame.font.SysFont(None, 100),
    "hints": pygame.font.SysFont(None, 25)
}

selected = (0,0)
selectedDirection = "row"

words = [
    { "word": "pygame", "direction": "row", "position": (9, 1), "hint": "Biblioteca para criar jogos em python." },
    { "word": "joptionpane", "direction": "column", "position": (1, 4), "hint": "Pacote para interfaces gráficas em java." },
    { "word": "print", "direction": "column", "position": (1, 9), "hint": "Comando para escrever algo na tela em python." }
]

table = Table(screen, words)
blocks = table.create()

def calcCenter(x, y):
    xCenter = (x + (x + 50)) / 2 + 2
    yCenter = (y + (y + 50)) / 2 + 2

    return (xCenter, yCenter)

def drawSheet(selected):

    gameArea = calcPercent(50, screen.get_width())
    squareSide = int(gameArea / 11)
    print(squareSide)

    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            if blocks[i][j]["enabled"]:
                if (j,i) == selected:
                    pygame.draw.rect(screen, colors["red"], (j * 50, i * 50, squareSide, squareSide))
                else:
                    pygame.draw.rect(screen, colors["white"], (j * 50, i * 50, squareSide, squareSide))

                letter = fonts["default"].render(blocks[i][j]["written"], True, colors["black"])
                letterPos = letter.get_rect(center=calcCenter(j * 50, i * 50))
                screen.blit(letter, letterPos)

                number = fonts["hints"].render(blocks[i][j]["number"], True, colors["black"])
                screen.blit(number, (j * 50 + 3, i * 50 + 3))
                pygame.draw.rect(screen, colors["black"], (j * 50, i * 50, squareSide, squareSide), 2)
            else:
                pygame.draw.rect(screen, colors["gray"], (j * 50, i * 50, squareSide, squareSide))


def updateGrid(selected, end = False, win = False):
    Hints(screen, words)
    if not end:
        drawSheet(selected)
        isEnd = createButtons()
        isWin = False
    else:
        isWin = True
        isEnd = True
        drawResult(win)
    pygame.display.update()

    return isEnd, isWin

def updateSelected(selected, direction):

    x,y = selected
    
    _selectedDirection = selectedDirection

    if direction == "down":

        i = y
        while True:
            if i == len(blocks) - 1:
                i = 0
            else:
                i += 1

            if blocks[i][x]["enabled"]:
                y = i

                _selectedDirection = words[blocks[i][x]["words"][0]]["direction"]

                break

    elif direction == "up":
        i = y
        while True:
            if i == 0:
                i = len(blocks) - 1
            else:
                i -= 1

            if blocks[i][x]["enabled"]:
                y = i

                _selectedDirection = words[blocks[i][x]["words"][0]]["direction"]

                break

    elif direction == "right":
        i = x
        while True:
            if i == len(blocks[y]) - 1:
                i = 0
            else:
                i += 1

            if blocks[y][i]["enabled"]:
                x = i

                _selectedDirection = words[blocks[y][i]["words"][0]]["direction"]

                break

    elif direction == "left":
        i = x
        while True:
            if i == 0 :
                i = len(blocks[y]) - 1
            else:
                i -= 1

            if blocks[y][i]["enabled"]:
                x = i

                _selectedDirection = words[blocks[y][i]["words"][0]]["direction"]

                break

    return (x,y), _selectedDirection   

def writeText(selected, text):
    direction = "right" if selectedDirection == "row" else "down"

    x,y = selected
    blocks[y][x]["written"] = text
    updateGrid(selected)

    _selected,_ = updateSelected(selected, direction)

    return _selected

def cleanField(selected):

    direction = "left" if selectedDirection == "row" else "up"

    position,_ = updateSelected(selected, direction)
    x,y = position
    blocks[y][x]["written"] = ""

    updateGrid(selected)
    
    _selected, _ = updateSelected(selected, direction)

    return _selected

def changeDirection(selected):
    x,y = selected
    newDirection = selectedDirection

    if len(blocks[y][x]["words"]) > 1:
        newDirection = "column" if selectedDirection == "row" else "row"

    return newDirection

def checkLetter(x, y):
    if blocks[y][x]["written"].upper() == blocks[y][x]["letter"].upper() or not blocks[y][x]["enabled"]:
        return True
    else:
        return False

def checkPoints():
    win = True

    for y in range(len(blocks)):
        for x in range(len(blocks[y])):
            if not checkLetter(x, y):
                win = False

    return win

def drawResult(win):
    if win:
        pygame.draw.rect(screen, colors["win_bg"], pygame.Rect(100, 200, 350, 150))
        text = fonts["title"].render("VITÓRIA", True, colors["white"])
        screen.blit(text, (130, 235))
        pygame.display.update()
    else:
        pygame.draw.rect(screen, colors["loose_bg"], pygame.Rect(50, 200, 450, 150))
        text = fonts["title"].render("DERROTA", True, colors["white"])
        screen.blit(text, (110,240))
        pygame.display.update()

def createButtons():
    buttonImg = pygame.image.load("images/send_button.png").convert_alpha()

    sendButton = Button(screen, (200, 600), buttonImg, 0.5)
    if sendButton.draw():
        if checkPoints():
            updateGrid(selected, True, True)
            return True
        else:
            updateGrid(selected, True, False)
            return True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            char = event.unicode
            if char.isalpha():
                selected = writeText(selected, char.upper())
            

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        selected, selectedDirection = updateSelected(selected, "down")
    if keys[pygame.K_UP]:
        selected, selectedDirection = updateSelected(selected, "up")
    if keys[pygame.K_RIGHT]:
        selected, selectedDirection = updateSelected(selected, "right")
    if keys[pygame.K_LEFT]:
        selected, selectedDirection = updateSelected(selected, "left")
    if keys[pygame.K_BACKSPACE]:
        selected = cleanField(selected)
    if keys[pygame.K_RETURN]:
        selectedDirection = changeDirection(selected)

    isEnd, isWin = updateGrid(selected, isEnd, isWin)

    clock.tick(15)

pygame.quit()