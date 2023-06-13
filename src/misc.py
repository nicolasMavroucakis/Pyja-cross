import pygame

class Button(): # Botão do pygame
    def __init__(self, screen, pos, image, scale): # Construtor da classe

        width = calcPercent(40, screen.get_width()) # Calcula a largura do botão
        height = calcPercent(30, screen.get_height()) # Calcula a altura do botão

        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) # Seta a imagem do botão
        self.rect = self.image.get_rect() # Pega as informações da imagem do botão
        self.rect.topleft = pos # Posição do botão

        self.screen = screen # Tela do jogo para desenhar o botão

    def draw(self): # Desenha o botão e retorna True caso seja pressionado

        action = False # Indica se o botão foi pressionado
        pos = pygame.mouse.get_pos() # Pega a posição do mouse

        if self.rect.collidepoint(pos): # Se a o mouse colide com o botão
            if pygame.mouse.get_pressed()[0] == 1: # Se o botão pressionado foi o botão 1 do mouse
                action = True

        self.screen.blit(self.image, (self.rect.x, self.rect.y)) # Desenha o botão na tela

        return action

class Table(): # Tabela de jogo
    def __init__(self, screen, words, type): # Construtor da classe

        # Tabela vazia que será alterada de acordo com as palavras
        table = [
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" }],
        ]

        for i in range(len(words[type])): # Para cada palavra
            word = words[type][i] # Indica qual palavra vai ser utilizada

            splittedWord = splitWord(word.word) # Separa as letras da palavra
            y,x = word.position # posição da primeira letra da palavra
            direction = word.direction # Direção da palavra


            table[y - 1][x - 1]["number"] = f"{i + 1}" # Indica o número da palavra

            for letter in splittedWord: # Para cada letra
                block = table[y - 1][x - 1] # Indica qual quadrado ta tabela vai ser utilizado

                block["letter"] = letter # Seta a letra correta
                block["enabled"] = True # Ativa o quadrado
                block["words"].append(i) # Adiciona a palavra a este quadrado

                if direction == "row": # Se for na horizontal, vai adicionar 1 no eixo X, caso contrário, adiciona 1 no eixo Y
                    x += 1
                else:
                    y += 1

        self.screen = screen # Tela do jogo para desenhar a tabela
        self.table = table # Tabela

    def create(self): # Cria a tabela
        return self.table
    
class Hints(): # Lista de dicas
    def __init__(self, screen, words, type): # Construtor da classe
        textHeight = calcVH(4, screen) # Altura do texto
        textLeft = calcVW(55, screen) # Calcula a margem à esquerda
        textTop = calcVH(4, screen) # Calcula a margem ao topo

        font = pygame.font.SysFont(None, calcVH(4, screen)) # Cria a fonte do texto

        for i in range(len(words[type])): # Para cada palavra
            word = words[type][i] # Indica a palavra que vai ser utilizada

            text = font.render(f"{i + 1}. {word.hint}", False, (200,200,200)) # Renderiza o texto da dica
            screen.blit(text, (textLeft, textTop)) # Insere o texto na tela
            textTop += textHeight # Soma à margem ao topo para não ocorrer sobreposição no texto

class Word(): # Palavra do jogo
    def __init__(self, word, direction, position, hint): # Construtor da classe
        self.word = word # Palavra
        self.direction = direction # Direção
        self.position = position # Posição inicial
        self.hint = hint # Dica

class RankPosition(): # Posição no ranking
    def __init__(self, position, name, time, color): # Construtor da classe
        self.position = position # Posição
        self.name = name # Nome do usuário
        self.time = time # Tempo do usuário
        self.color = color # Cor do fundo

def splitWord(word): # Separa as letras das palavras
    chars = []
    for i in word:
        chars.append(i)

    return chars

def calcPercent(percent, val): # Calcula uma porcentagem
    p1 = int(val / 100)
    return percent * p1

def calcVH(val, screen): # Calcula a ViewHeight (inspirado no CSS)
    height = screen.get_height()
    vh = int(height / 100)
    return val * vh

def calcVW(val, screen): # Calcula a ViewWidth (inspirado no CSS)
    width = screen.get_width()
    vw = int(width / 100)
    return val * vw

"""
    words = [ word() ]

    word = {
        "word": "palavra",
        "direction": "row/column",
        "position": (y,x)
    }

"""