import pygame

class Button():
    def __init__(self, screen, pos, image, scale):

        width = calcPercent(40, screen.get_width())
        height = calcPercent(30, screen.get_height())

        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.clicked = False
        self.screen = screen

    def draw(self):

        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

class Table():
    def __init__(self, screen, words, type):

        table = [
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },],
            [{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },{ "enabled": False, "letter": "", "written": "", "words": [], "number": "" },]
        ]

        for i in range(len(words[type])):
            word = words[type][i]

            splittedWord = splitWord(word.word)
            y,x = word.position
            direction = word.direction

            table[y - 1][x - 1]["number"] = f"{i + 1}"

            for letter in splittedWord:
                block = table[y - 1][x - 1]

                block["letter"] = letter
                block["enabled"] = True
                block["words"].append(i)

                if direction == "row":
                    x += 1
                else:
                    y += 1

        self.screen = screen
        self.table = table

    def create(self):
        return self.table
    
class Hints():
    def __init__(self, screen, words, type):
        textHeight = calcVH(4, screen)
        textLeft = calcVW(55, screen)
        textTop = calcVH(4, screen)

        font = pygame.font.SysFont(None, calcVH(4, screen))

        for i in range(len(words[type])):
            word = words[type][i]

            text = font.render(f"{i + 1}. {word.hint}", False, (200,200,200))
            screen.blit(text, (textLeft, textTop))
            textTop += textHeight

class Word():
    def __init__(self, word, direction, position, hint):
        self.word = word
        self.direction = direction
        self.position = position
        self.hint = hint

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class RankPosition():
    def __init__(self, position, name, time, color):
        self.position = position
        self.name = name
        self.time = time
        self.color = color

def splitWord(word):
    chars = []
    for i in word:
        chars.append(i)

    return chars

def calcPercent(percent, val):
    p1 = int(val / 100)
    return percent * p1

def calcVH(val, screen):
    height = screen.get_height()
    vh = int(height / 100)
    return val * vh

def calcVW(val, screen):
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