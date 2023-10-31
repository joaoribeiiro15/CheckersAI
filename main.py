import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, caminhoPrograma
#from checkers.constants import WIDTH, HEIGHT
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60
dificulty = 1

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers - Dificuldade: FÁCIL')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen2 = pygame.display.set_mode((WIDTH, HEIGHT))

def mensagem(msg,cor, pos = [225, 300], tamanho = 50):
    mesg = pygame.font.SysFont(None, tamanho).render(msg, True, cor)
    screen.blit(mesg, pos)

def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y)) # this is a rect pygame.Rect


def button(screen2, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen2, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen2, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen2, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen2, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen2, (100, 100, 100), (x, y, w , h))
    return screen2.blit(text_render, (x, y)) # this is a rect pygame.Rect


def start():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        #CHAMAR A I.A.
        if game.turn == WHITE:
            #QUANTO MAIOR O VALOR DA DIFICULTY MAIS A I.A. IRÁ PROCESSAR MAIS INFORMAÇÃO PARA JOGAR MELHOR
            value, new_board = minimax(game.get_board(), dificulty, WHITE, game)
            if dificulty in [1,3]:
                pygame.time.delay(1000)
            game.ai_move(new_board)
        
        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

def dif(valor): 
    global dificulty
    if valor == 1:
        pygame.display.set_caption('Checkers - Dificuldade: FÁCIL')
    elif valor == 3:
        pygame.display.set_caption('Checkers - Dificuldade: MÉDIO')
    elif valor == 4:
        pygame.display.set_caption('Checkers - Dificuldade: DIFÍCIL')
    dificulty = valor
    menu()

def difMenu():
    screen.fill([0,0,0])
    mensagem("Dificuldade:", [255,255,255], [225, 300], 80)
    posicoes = [180, 310, 458]
    b4 = button(screen2, (posicoes[0], 400), "FÁCIL") 
    b5 = button(screen2, (posicoes[1], 400), "MÉDIO")
    b6 = button(screen2, (posicoes[2], 400), "DÍFICIL")
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b4.collidepoint(pygame.mouse.get_pos()):
                    dif(1)
                if b5.collidepoint(pygame.mouse.get_pos()):
                    dif(3)
                if b6.collidepoint(pygame.mouse.get_pos()):
                    dif(4)
        pygame.display.update()

def menu():
    global dificulty, caminho

    image = pygame.image.load(caminhoPrograma() + chr(92) + "assets\checkers.png")
    screen.blit(image, (0, 0))


    b1 = button(screen, (330, 700), "SAIR")
    b2 = button(screen, (500, 700), "JOGAR")
    b3 = button(screen, (100, 700), "OPÇÕES")
    
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    start()
                elif b3.collidepoint(pygame.mouse.get_pos()):
                    difMenu()

        pygame.display.update()
menu()
pygame.quit()