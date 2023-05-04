import pygame

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
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            if blocks[i][j]["enabled"]:
                # print(i,j)
                pygame.draw.rect(screen, colors["white"], (j * 50, i * 50, squareSide, squareSide))

            else:
                pygame.draw.rect(screen, colors["gray"], (j * 50, i * 50, squareSide, squareSide))

            pygame.draw.rect(screen, colors["black"], (j * 50, i * 50, squareSide, squareSide), 2)

            letter = font.render(blocks[i][j]["written"], True, colors["red"])
            screen.blit(letter, (j * 50 + 167, i * 50 + 117))

def updateGrid():
    drawSheet()
    pygame.display.update()

while running:

    pygame.time.delay(100)

    screen.fill(colors["red"])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    updateGrid()

pygame.quit()
