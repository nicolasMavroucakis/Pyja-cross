import pygame
import math

pygame.init()

colors = {
    "red": (255,0,0),
    "white": (200,200,200),
    "black": (0,0,0),
    "gray": (100,100,100)
}

screen = pygame.display.set_mode((550,545))
running = True

pygame.display.set_caption("PyJa Cross", "https://cdn-icons-png.flaticon.com/512/124/124034.png?w=360")

font = pygame.font.SysFont(None, 50)

squareSide = 60

drawed = False

words = [
    "pygame",
    "joptionpane"
]

hints = [
    "Biblioteca para criar jogos em python.",
    "Pacote para interfaces gráficas em java."
]

blocks = [
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "j", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "o", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "p", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "t", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "i", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "o", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "n", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "p", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": True, "letter": "p", "written": "P" },{ "enabled": True, "letter": "y", "written": "Y" },{ "enabled": True, "letter": "g", "written": "" },{ "enabled": True, "letter": "a", "written": "" },{ "enabled": True, "letter": "m", "written": "" },{ "enabled": True, "letter": "e", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "n", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "e", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },]
]

def drawSheet():
    for y in range(len(blocks)):
        for x in range(len(blocks[y])):
            if blocks[y][x]["enabled"]:
                pygame.draw.rect(screen, colors["white"], (x * 50, y * 50, squareSide, squareSide))

            else:
                pygame.draw.rect(screen, colors["gray"], (x * 50, y * 50, squareSide, squareSide))

            pygame.draw.rect(screen, colors["black"], (x * 50, y * 50, squareSide, squareSide), 2)

            letter = font.render(blocks[y][x]["written"], True, colors["red"])
            screen.blit(letter, (x * 50 + 167, y * 50 + 117))

def updateGrid():
    drawSheet()
    pygame.display.update()

# def updateSelected(selected, direction):

    # x,y = selected

    # if direction == "right":

    #     newPos = getNextEnabled(selected, direction)

    #     selected = newPos

    # elif direction == "left":
    #     if x-1 < 0:

    #         if y-1 < 0:
    #             y = len(blocks) - 1
    #             x = len(blocks[y]) - 1
            
    #         else:
    #             y -= 1
    #             x = len(blocks[y])

    #     else:

    #         x -= 1

    # updateGrid();

while running:

    pygame.time.delay(100)
    updateGrid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            x,y = pos

            squareY = math.floor(y / len(blocks))

            squareX = math.floor(x / len(blocks[squareY]))

            print(squareX, squareY)

pygame.quit()
