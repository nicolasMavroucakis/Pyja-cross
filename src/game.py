import pygame
from src.misc import *
import datetime
import src.connection as connection
import src.screens as screens
connection.connect()

def run(gameType, userInfo, gameTypeId):

    pygame.init() # iniciando a instancia do pygame

    # tabela com as cores que sao utilizadas
    colors = {
        "red": (255,0,0),
        "white": (200,200,200),
        "black": (0,0,0),
        "gray": (87,87,87,60),
        "win_bg": (8, 84, 84),
        "loose_bg": (239, 28, 28),
        "background": (6, 17, 17)
    }

    squaresAmount = 14 # quantidade de quadrados

    screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE) # criando a tela do pygame
    running = True # quando False o jogo fecha

    isEnd = False # quando True mostra a tela final
    isWin = False # ganhou ou perdeu o jogo

    pygame.display.set_caption("PyJa Cross") # Setando o nome da janela
    clock = pygame.time.Clock() # Delay entre os ticks do jogo

    icon = pygame.image.load("images/logo.png") # Selecionando o ícone da janela
    pygame.display.set_icon(icon) # Setando o ícone na janela do jogo

    selected = (0,0) # Ponto inicial 
    selectedDirection = "row" # Direção inicial

    type = gameType # Selecionando o tipo (python/java)
    # lista de palavras
    """
        Word(
            palavra,
            direcao,
            posicao da primeira letra,
            dica
        )
    """
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
    squares = [] # Quadrados para receber os clicks

    # Criar a tabela de jogo
    table = Table(screen, words, type) # Criando a tabela do jogo
    blocks = table.create() # Tabela do jogo

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

    # Atualiza a tabela
    def drawSheet(selected):

        gameArea = calcPercent(50, screen.get_width()) # Área do jogo
        squareSide = gameArea // squaresAmount # Tamanho do lado do quadrado

        marginLeft = calcVW(1,screen) # Margem à esquerda do quadrado
        marginTop = calcVH(2,screen) # Margem ao topo do quadrado

        font = pygame.font.SysFont(None, calcVW(4, screen)) # Setando a fonte das letras no jogo
        hintFont = pygame.font.SysFont(None, calcVH(3, screen)) # Setando a fonte das dicas

        # Desenha os quadrados
        for i in range(len(blocks)):
            for j in range(len(blocks[i])):
                if blocks[i][j]["enabled"]:

                    # Se estiver slecionado, desenha em vermelho, caso contrário, em branco
                    if (j,i) == selected:
                        blc = pygame.draw.rect(screen, colors["red"], (j * squareSide + marginLeft, i * squareSide + marginTop, squareSide, squareSide))
                    else:
                        blc = pygame.draw.rect(screen, colors["white"], (j * squareSide + marginLeft, i * squareSide + marginTop, squareSide, squareSide))

                    squares.append(blc) # Adiciona a lista de quadrados, para ser acessado ao clicar na tela

                    letter = font.render(blocks[i][j]["written"], True, colors["black"]) # Renderiza a letra
                    letterPos = letter.get_rect(center=calcCenter(j * squareSide + marginLeft, i * squareSide + marginTop, squareSide)) # Posiciona a letra
                    screen.blit(letter, letterPos) # Desenha a letra

                    number = hintFont.render(blocks[i][j]["number"], True, colors["black"]) # Número da palavra, para ser identificada com a dica
                    screen.blit(number, (j * squareSide + marginLeft + 3, i * squareSide + marginTop + 3)) # Desenha o número da letra
                    pygame.draw.rect(screen, colors["black"], (j * squareSide + marginLeft, i * squareSide + marginTop, squareSide, squareSide), 2) # Desenha o quadrado em volta

                else: # Desenha o quadrado com pouca opacidade quando não é utilizado no jogo
                    sfc = pygame.Surface(pygame.Rect(j * squareSide + marginLeft, i * squareSide + marginTop, squareSide, squareSide).size, pygame.SRCALPHA)
                    pygame.draw.rect(sfc, colors["gray"], sfc.get_rect())
                    screen.blit(sfc,(j * squareSide + marginLeft, i * squareSide + marginTop, squareSide, squareSide))

    def drawTimer(seconds): # Desenha o tempo na tela
        font = pygame.font.SysFont(None, calcVH(4, screen))
        text = font.render(convertTime(seconds), True, colors["white"])
        screen.blit(text, (calcVW(67, screen), calcVH(95, screen), calcVW(5, screen), calcVH(5, screen)))

    def updateGrid(selected, end = False, win = False, seconds = 0): # Atualiza a tela
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

    def updateSelected(selected, direction = None): # Altera o quadrado selecionado

        x,y = selected
        _selectedDirection = selectedDirection

        if direction == "down":

            i = y
            while True: # Desce um quadrado até encontrar o próximo que está ativado
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
            while True: # Sobe um quadrado até encontrar o próximo que está ativado
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
            while True: # Anda um quadrado para a direita até encontrar o próximo que está ativado
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
            while True: # Anda um quadrado para a direita até encontrar o próximo 
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

    def writeText(selected, text): # Indica qual letra deve ser escrita no quadrado selecionado e se move na direção da palavra
        direction = "right" if selectedDirection == "row" else "down" # Caso a palavra esteja na horizontal, se move para a direita, caso contrário, para baixo

        x,y = selected
        blocks[y][x]["written"] = text

        updateGrid(selected) # Atualiza a tela

        _selected,_ = updateSelected(selected, direction)

        return _selected

    def cleanField(selected): # Apaga a letra escrita no quadrado e se move na direção contrária da palavra
        direction = "left" if selectedDirection == "row" else "up" # Caso a palavra esteja na horizontal, se move para a esquerda, caso contrário, para cima

        position,_ = updateSelected(selected, direction)
        x,y = position
        blocks[y][x]["written"] = ""

        updateGrid(selected) # Atualiza a tela
        
        _selected, _ = updateSelected(selected, direction)

        return _selected

    def changeDirection(selected): # Muda a direção selecionada caso o usuário aperte ENTER em um quadrado que faz parte de 2 ou mais palavras
        x,y = selected
        newDirection = selectedDirection

        if len(blocks[y][x]["words"]) > 1:
            newDirection = "column" if selectedDirection == "row" else "row" # Caso a direção selecionada seja horizontal, alterará para vertical e vice-versa

        return newDirection

    def checkLetter(x, y): # Checa se a letra escrita está correta
        return blocks[y][x]["written"].upper() == blocks[y][x]["letter"].upper() or not blocks[y][x]["enabled"]

    def checkPoints(): # Chama a função checkLetter em todos os quadrados ativados
        win = True

        for y in range(len(blocks)):
            for x in range(len(blocks[y])):
                if not checkLetter(x, y): # Se alguma letra estiver errada, retornará False e o usuário perde o jogo
                    win = False

        return win


    def drawResult(win): # Desenha a tela final com base no seu resultado
        textBackground = pygame.Rect(100, 100, calcVW(50, screen), calcVH(30, screen)) # Desenha o fundo do texto
        textBackground.centerx = screen.get_width() // 2 # Calcula o X central da tela
        textBackground.centery = screen.get_height() // 2 # Calcula o Y central da tela

        font = pygame.font.SysFont(None, calcVW(8, screen)) # Cria a fonte do texto
        timeFont = pygame.font.SysFont(None, calcVW(5, screen)) # Cria a fonte do texto indicando o tempo

        screen.fill(colors["background"]) # Deixa o fundo completamente opaco

        if win: # Executa caso o usuário ganhe o jogo

            pygame.draw.rect(screen, colors["win_bg"], textBackground)

            text = font.render("VITÓRIA", True, colors["white"])
            textPos = text.get_rect(center = calcCenter2(textBackground.x, textBackground.y, calcVW(50, screen), calcVH(30, screen)))
            screen.blit(text, textPos)

            timeText = timeFont.render(convertTime(seconds), True, colors["white"])
            timeTextPos = timeText.get_rect(center = calcCenter2(textBackground.x, textBackground.y, calcVW(50, screen), calcVH(30, screen) + calcVH(23, screen)))
            screen.blit(timeText, timeTextPos)

        else: # Executa caso o usuário perca o jogo

            pygame.draw.rect(screen, colors["loose_bg"], textBackground)

            text = font.render("DERROTA", True, colors["white"])
            textPos = text.get_rect(center = calcCenter2(textBackground.x, textBackground.y, calcVW(50, screen), calcVH(30, screen)))
            screen.blit(text, textPos)

        buttonScale = 0.5 # Escala para o tamanho do botão

        closeButtonImg = pygame.image.load("images/close_button.png").convert_alpha() # Pega a imagem do botão de fechar
        #Posiciona o botão
        buttonPos = closeButtonImg.get_rect(center = calcCenter2(textBackground.x + calcVW(20, screen), textBackground.y + calcVH(36, screen), int(closeButtonImg.get_width() * buttonScale), int(closeButtonImg.get_height() * buttonScale)))
        closeButton = Button(screen, (buttonPos.left, buttonPos.top), closeButtonImg, 0.5) # Cria um botão com a classe Button do arquivo misc.py

        if closeButton.draw(): # Caso o botão seja apertado
            pygame.quit() # Fecha a janela do jogo 
            screens.open_main_screen(loginResult=userInfo) # Abre a tela inicial do programa

        pygame.display.update() # Atualiza a tela

    def createButtons(): # Cria o botão de enviar a resposta
        buttonImg = pygame.image.load("images/send_button.png").convert_alpha() # Pega a imagem do botão de enviar

        buttonLeft = calcVW(60, screen) # Calcula a margem à esquerda
        buttonTop = calcVH(80, screen) # Calcula a margem ao topo

        sendButton = Button(screen, (buttonLeft, buttonTop), buttonImg, 0.5) # Cria um botão com a classe Button do arquivo misc.py

        if sendButton.draw(): # Caso o botão seja apertado
            if checkPoints(): # Caso o usuário ganhe o jogo
                updateGrid(selected, True, True) # Atualiza a tela informando que o jogo acabou e que o usuário ganhou

                connection.updateUserTime(userInfo, seconds, gameTypeId) # Atualiza o tempo na database
                return True, True
            else:
                updateGrid(selected, True, False) # Atualiza a tela informando que o jogo acabou e que o usuário perdeu
                return True, False
            
        return False, False

    frameCount = 0 # Quantidade de frames executados, para calcular o tempo jogado

    while running:

        frameCount += 1 # Soma + 1 na quantidade de frames
        
        for event in pygame.event.get(): # Eventos pygame
            if event.type == pygame.QUIT: # Caso o usuário fecha o jogo
                running = False # Fecha a instância do pygame

            elif event.type == pygame.KEYDOWN: # Caso uma tecla seja pressionada
                char = event.unicode # Pega qual caractere foi inserido
                if char.isalpha(): # Checa se foi uma letra
                    selected = writeText(selected, char.upper()) # Escreve a letra

            elif event.type == pygame.MOUSEBUTTONDOWN: # Caso um botão do mouse seja pressionado
                pos = pygame.mouse.get_pos() # Pega a posição atual do mouse
                pressed = pygame.mouse.get_pressed()[0] == 1 # Checa se o botão apertado foi o botão 1 do mouse
                
                if pressed: # Se o botão apertado foi o botão 1
                    for i in squares:
                        if i.collidepoint(pos): # Checa se o mouse está colidinho com um quadrado

                            gameArea = calcPercent(50, screen.get_width()) # Calcula a área do jogo
                            squareSide = gameArea // squaresAmount # Calcula o tamanho do quadrado

                            _selected = (i.x // squareSide, i.y // squareSide -1 ) # Calcula qual quadrado foi selecionado
                            selected, selectedDirection = updateSelected(_selected, "down") # Atualiza o quadrado selecionado
                            break

        keys = pygame.key.get_pressed() # Tecla pressionada

        if keys[pygame.K_DOWN]: # Caso a telca seja a seta para baixo
            selected, selectedDirection = updateSelected(selected, "down") # Atualiza o quadrado selecionado com +1 no eixo Y
        if keys[pygame.K_UP]: # Caso a telca seja a seta para cima
            selected, selectedDirection = updateSelected(selected, "up") # Atualiza o quadrado selecionado com -1 no eixo Y
        if keys[pygame.K_RIGHT]: # Caso a telca seja a seta para direita
            selected, selectedDirection = updateSelected(selected, "right") # Atualiza o quadrado selecionado com +1 no eixo X
        if keys[pygame.K_LEFT]: # Caso a telca seja a seta para esquerda
            selected, selectedDirection = updateSelected(selected, "left") # Atualiza o quadrado selecionado com -1 no eixo X
        if keys[pygame.K_BACKSPACE]: # Caso a tecla seja BACKSPACE
            selected = cleanField(selected) # Apaga a letra do quadrado selecionado
        if keys[pygame.K_RETURN]: # Caso a tecla pressionada seja ENTER
            selectedDirection = changeDirection(selected) # Trica a direção selecionada

        isEnd, isWin = updateGrid(selected, isEnd, isWin, int(frameCount/1000 * 60)) # Chama a função de atualizar a tela

        if not isEnd:
            seconds = int(frameCount/1000 * 60) # Altera o tempo de jogo (60 FPS)

        clock.tick(15) # Função nativa do pygame de delay para rodar o loop principal

    pygame.quit() # Fecha a instância do pygame, caso a variável running tenha valor False

def stop(): # Fecha o jogo
    pygame.quit() # Fecha a instância do pygame