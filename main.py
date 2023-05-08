import pygame
from misc import *
import time

pygame.init()

colors = {
    "red": (255,0,0),
    "white": (200,200,200),
    "black": (0,0,0),
    "gray": (100,100,100),
    "win_bg": (8, 84, 84)
}

screen = pygame.display.set_mode((550,700))
running = True
inGame = False

pygame.display.set_caption("PyJa Cross", "https://cdn-icons-png.flaticon.com/512/124/124034.png?w=360")
clock = pygame.time.Clock()
# icon = pygame.image.load("logo.png")
# pygame.display.set_icon(icon)

font = pygame.font.SysFont(None, 50)
titleFont = pygame.font.SysFont(None, 100)

squareSide = 60
selected = (0,0)
selectedDirection = "row"

words = [
    { "word": "pygame", "direction": "row" },
    { "word": "joptionpane", "direction": "column"}
]

hints = [
    "Biblioteca para criar jogos em python.",
    "Pacote para interfaces gráficas em java."
]

blocks = [
    [{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": True, "letter": "j", "written": "", "words": [1] },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },],
    [{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": True, "letter": "o", "written": "", "words": [1] },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },],
    [{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": True, "letter": "p", "written": "", "words": [1] },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },],
    [{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": True, "letter": "t", "written": "", "words": [1] },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },],
    [{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": True, "letter": "i", "written": "", "words": [1] },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },],
    [{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": True, "letter": "o", "written": "", "words": [1] },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },],
    [{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": True, "letter": "n", "written": "", "words": [1] },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },],
    [{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": True, "letter": "p", "written": "", "words": [1] },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },],
    [{ "enabled": True, "letter": "p", "written": "P", "words": [0] },{ "enabled": True, "letter": "y", "written": "Y" , "words": [0]},{ "enabled": True, "letter": "g", "written": "", "words": [0] },{ "enabled": True, "letter": "a", "written": "", "words": [0, 1] },{ "enabled": True, "letter": "m", "written": "", "words": [0] },{ "enabled": True, "letter": "e", "written": "", "words": [0] },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },],
    [{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": True, "letter": "n", "written": "", "words": [1] },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },],
    [{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": True, "letter": "e", "written": "", "words": [1] },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },{ "enabled": False, "letter": "" , "written": "", "words": None },]
]

def drawSheet(selected):
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            if blocks[i][j]["enabled"]:
                if (j,i) == selected:
                    pygame.draw.rect(screen, colors["red"], (j * 50, i * 50, squareSide, squareSide))
                else:
                    pygame.draw.rect(screen, colors["white"], (j * 50, i * 50, squareSide, squareSide))

                letter = font.render(blocks[i][j]["written"], True, colors["black"])
                screen.blit(letter, (j * 50 + 15, i * 50 + 10))
            else:
                pygame.draw.rect(screen, colors["gray"], (j * 50, i * 50, squareSide, squareSide))

            pygame.draw.rect(screen, colors["black"], (j * 50, i * 50, squareSide, squareSide), 2)


def updateGrid(selected):
    drawSheet(selected)
    createButtons()
    pygame.display.update()

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

def getWordDirection(selected):
    x,y = selected
    

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
        text = titleFont.render("VITÓRIA", True, colors["white"])
        screen.blit(text, (130, 235))
        pygame.display.update()

def createButtons():
    buttonImg = pygame.image.load("images/send_button.png").convert_alpha()

    sendButton = Button((200, 600), buttonImg, 0.5)
    if sendButton.draw(screen):
        if checkPoints():
            while True:
                pygame.time.delay(100)
                drawResult(True)
                time.sleep(5)
                pygame.quit()

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

    updateGrid(selected)

    clock.tick(15)

pygame.quit()