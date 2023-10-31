import pygame, os

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#Functions
def caminhoPrograma():
    diretorio_programa = str(__file__)
    caminho = ""
    for i in range (len(diretorio_programa) -1, -1, -1):                #Se estiver a correr no VSC ou no Linux
        if diretorio_programa[i] == "/":
            caminho = diretorio_programa[0:i]
            break
    if len(caminho) == 0:                                               #Se estiver a correr no Windows
        for i in range (len(diretorio_programa) -1, -1, -1):
            if diretorio_programa[i] == "\\":
                caminho = diretorio_programa[0:i]
                break
    return caminho

#RGB
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load(caminhoPrograma() + chr(92) + "assets\crown.png"), (44, 25))
