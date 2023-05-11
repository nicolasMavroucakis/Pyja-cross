import pygame

class Button():
    def __init__(self, pos, image, scale):

        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.clicked = False

    def draw(self, screen):

        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        self.screen = screen
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

class Table():
    def __init__(self, screen, words):

        textHeight = 30
        textStart = 50

        font = pygame.font.SysFont(None, 25)

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

        for i in range(len(words)):
            word = words[i]

            splittedWord = splitWord(word["word"])
            y,x = word["position"]
            direction = word["direction"]
            hint = word["hint"]

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

            text = font.render(f"{i + 1}. {hint}", False, (200,200,200))
            screen.blit(text, (600, textStart))
            textStart += textHeight

        self.table = table


    def create(self):
        return self.table
    

def splitWord(word):
    chars = []
    for i in word:
        chars.append(i)

    return chars

"""
    words = [ word() ]

    word = {
        "word": "palavra",
        "direction": "row/column",
        "position": (y,x)
    }

"""