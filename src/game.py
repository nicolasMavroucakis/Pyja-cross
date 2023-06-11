import pygame
from src.misc import *
import datetime
import src.connection as connection
import src.screens as screens
connection.connect()

def run(gameType, userInfo, gameTypeId):

    pygame.init()

    transparentEmptyBackground = False

    colors = {
        "red": (255,0,0),
        "white": (200,200,200),
        "black": (0,0,0),
        "gray": (87,87,87,60),
        "win_bg": (8, 84, 84),
        "loose_bg": (239, 28, 28),
        "background": (6, 17, 17)
    }

    squaresAmount = 14

    screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
    running = True
    global inGame
    inGame = False

    isEnd = False
    isWin = False

    global screenWidth
    screenWidth = screen.get_width()
    global screenHeight
    screenHeight = screen.get_height()

    pygame.display.set_caption("PyJa Cross")
    clock = pygame.time.Clock()

    icon = pygame.image.load("images/logo.png")
    pygame.display.set_icon(icon)

    selected = (0,0)
    selectedDirection = "row"

    type = gameType
    words = {
        "python": [ 
            Word("variavel", "row", (1,1), "Espaço de memória para armazenar valores no programa."), 
            Word("recursao", "column", (1,3), "Técnica em que uma função chama a si mesma.") ,
            Word("lista", "column", (1,8), "Coleção mutável ordenada de elementos."), 
            Word("input", "row", (2,8), "Dados fornecidos pelo usuário."), 
            Word("atributo", "row", (5,8), "Característica de uma classe."), 
            Word("break", "column", (5,12), "Interrompe a execução de um loop ou switch-case."), 
            Word("algoritmo", "row", (7,3), "Conjunto de passos sequenciais."), 
            Word("return", "column", (7,7), "Comando utilizado para retornar um valor de uma função."), 
            Word("null", "row", (12,7), "Representa a ausência de um objeto ou referência."), 
        ],
        "java": [ 
            Word("encapsulamento", "row", (1,1), "Protege os dados e comportamentos internos de uma classe."), 
            Word("classes", "column", (1,3), "Estruturas que definem objetos e suas características."),
            Word("sobrecarga", "row", (4,3), "Vários métodos com o mesmo nome e diferentes parâmetros."),
            Word("alinhamento", "column", (4,12), "Organização visualmente ordenada de elementos de código."),
            Word("biblioteca", "row", (9,3), "Conjunto de código pré-escrito que realiza tarefas específicas."),
            Word("compilacao", "row", (14,3), "Tradução de código-fonte Java em código executável."),
            Word("interface", "row", (11,4), "Define os métodos que uma classe deve implementar."),
            Word("heranca", "column", (4,14), "Herdar características de outra classe."),
            Word("try", "row", (15,13), "Tentar a execução de um código."),
        ]
    }
    squares = []

    # Criar a tabela de jogo
    table = Table(screen, words, type)
    blocks = table.create()

    seconds = 0

    # Calcula o centro do quadrado
    def calcCenter(x, y, squareSide):
        xCenter = (x + (x + squareSide)) / 2 + 2
        yCenter = (y + (y + squareSide)) / 2 + 2

        return (xCenter, yCenter)

    # Calcula o centro geral
    def calcCenter2(x, y, width, height):
        xCenter = (x + (x + width)) / 2
        yCenter = (y + (y + height)) / 2

        return (xCenter, yCenter)

    # Transforma os segundos em horas, minutos e segundos
    def convertTime(seconds):
        time = str(datetime.timedelta(seconds=seconds))
        return time

    def drawSheet(selected):

        # Área do jogo
        gameArea = calcPercent(50, screen.get_width())
        squareSide = gameArea // squaresAmount

        marginLeft = calcVW(1,screen)
        marginTop = calcVH(2,screen)

        font = pygame.font.SysFont(None, calcVW(4, screen))
        hintFont = pygame.font.SysFont(None, calcVH(3, screen))

        for i in range(len(blocks)):
            for j in range(len(blocks[i])):
                if blocks[i][j]["enabled"]:

                    if (j,i) == selected:
                        blc = pygame.draw.rect(screen, colors["red"], (j * squareSide + marginLeft, i * squareSide + marginTop, squareSide, squareSide))
                    else:
                        blc = pygame.draw.rect(screen, colors["white"], (j * squareSide + marginLeft, i * squareSide + marginTop, squareSide, squareSide))

                    squares.append(blc)

                    letter = font.render(blocks[i][j]["written"], True, colors["black"])
                    letterPos = letter.get_rect(center=calcCenter(j * squareSide + marginLeft, i * squareSide + marginTop, squareSide))
                    screen.blit(letter, letterPos)

                    # ignore = font.render(blocks[i][j]["letter"], True, colors["gray"])
                    # _letterPos = letter.get_rect(center=calcCenter(j * squareSide + marginLeft, i * squareSide + marginTop, squareSide))
                    # screen.blit(ignore, _letterPos)

                    number = hintFont.render(blocks[i][j]["number"], True, colors["black"])
                    screen.blit(number, (j * squareSide + marginLeft + 3, i * squareSide + marginTop + 3))
                    pygame.draw.rect(screen, colors["black"], (j * squareSide + marginLeft, i * squareSide + marginTop, squareSide, squareSide), 2)
                else:
                    if not transparentEmptyBackground:
                        sfc = pygame.Surface(pygame.Rect(j * squareSide + marginLeft, i * squareSide + marginTop, squareSide, squareSide).size, pygame.SRCALPHA)
                        pygame.draw.rect(sfc, colors["gray"], sfc.get_rect())
                        screen.blit(sfc,(j * squareSide + marginLeft, i * squareSide + marginTop, squareSide, squareSide))

    def drawTimer(seconds):
        font = pygame.font.SysFont(None, calcVH(4, screen))
        text = font.render(convertTime(seconds), True, colors["white"])
        screen.blit(text, (calcVW(67, screen), calcVH(95, screen), calcVW(5, screen), calcVH(5, screen)))

    def updateGrid(selected, end = False, win = False, seconds = 0):
        screen.fill(colors["background"])
        if not end:
            
            Hints(screen, words, type)
            drawSheet(selected)
            drawTimer(seconds)
            isEnd, isWin = createButtons()

        else:
            isWin = win
            isEnd = True
            
            screen.fill([255,255,255])
            drawResult(win)
        pygame.display.update()

        return isEnd, isWin

    def updateSelected(selected, direction = None):

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

                    _selectedDirection = words[type][blocks[i][x]["words"][0]].direction

                    break

                if i == y:
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

                    _selectedDirection = words[type][blocks[i][x]["words"][0]].direction

                    break

                if i == y:
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

                    _selectedDirection = words[type][blocks[y][i]["words"][0]].direction

                    break

                if i == x:
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

                    _selectedDirection = words[type][blocks[y][i]["words"][0]].direction

                    break

                if i == x:
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
        textBackground = pygame.Rect(100, 100, calcVW(50, screen), calcVH(30, screen))
        textBackground.centerx = screen.get_width() // 2
        textBackground.centery = screen.get_height() // 2

        font = pygame.font.SysFont(None, calcVW(8, screen))
        timeFont = pygame.font.SysFont(None, calcVW(5, screen))

        screen.fill(colors["background"])

        if win:

            pygame.draw.rect(screen, colors["win_bg"], textBackground)

            text = font.render("VITÓRIA", True, colors["white"])
            textPos = text.get_rect(center = calcCenter2(textBackground.x, textBackground.y, calcVW(50, screen), calcVH(30, screen)))
            screen.blit(text, textPos)

            timeText = timeFont.render(convertTime(seconds), True, colors["white"])
            timeTextPos = timeText.get_rect(center = calcCenter2(textBackground.x, textBackground.y, calcVW(50, screen), calcVH(30, screen) + calcVH(23, screen)))
            screen.blit(timeText, timeTextPos)

        else:

            pygame.draw.rect(screen, colors["loose_bg"], textBackground)

            text = font.render("DERROTA", True, colors["white"])
            textPos = text.get_rect(center = calcCenter2(textBackground.x, textBackground.y, calcVW(50, screen), calcVH(30, screen)))
            screen.blit(text, textPos)

        buttonScale = 0.5

        closeButtonImg = pygame.image.load("images/close_button.png").convert_alpha()
        buttonPos = closeButtonImg.get_rect(center = calcCenter2(textBackground.x + calcVW(20, screen), textBackground.y + calcVH(36, screen), int(closeButtonImg.get_width() * buttonScale), int(closeButtonImg.get_height() * buttonScale)))
        closeButton = Button(screen, (buttonPos.left, buttonPos.top), closeButtonImg, 0.5)

        if closeButton.draw():
            pygame.quit()
            screens.open_main_screen(loginResult=userInfo)

        pygame.display.update()

    def createButtons():
        buttonImg = pygame.image.load("images/send_button.png").convert_alpha()

        buttonLeft = calcVW(60, screen)
        buttonTop = calcVH(80, screen)

        sendButton = Button(screen, (buttonLeft, buttonTop), buttonImg, 0.5)

        if sendButton.draw():
            if checkPoints():
                updateGrid(selected, True, True)

                print(userInfo)
                print(seconds)
                print(gameTypeId)

                connection.updateUserTime(userInfo, seconds, gameTypeId)
                return True, True
            else:
                updateGrid(selected, True, False)
                return True, False
            
        return False, False

    frameCount = 0

    while running:

        frameCount += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                char = event.unicode
                if char.isalpha():
                    selected = writeText(selected, char.upper())

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pressed = pygame.mouse.get_pressed()[0] == 1
                
                if pressed:
                    for i in squares:
                        if i.collidepoint(pos):
                            _selected = (i.x // 50, i.y // 50 -1 )
                            selected, selectedDirection = updateSelected(_selected, "down")
                            break

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

        isEnd, isWin = updateGrid(selected, isEnd, isWin, int(frameCount/1000 * 60))

        if not isEnd:
            seconds = int(frameCount/1000 * 60)

        clock.tick(15)

    pygame.quit()

def stop():
    pygame.quit()