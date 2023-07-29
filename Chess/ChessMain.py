"""
Основной файл драйвера.
Обработка пользовательского ввода.
Отображение текущего объекта статуса игры.
"""

import pygame as p
import ChessEngine, ChessAI
import sys
from multiprocessing import Process, Queue

BOARD_WIDTH = BOARD_HEIGHT = 512
MOVE_LOG_PANEL_WIDTH = 250
MOVE_LOG_PANEL_HEIGHT = BOARD_HEIGHT
DIMENSION = 8
SQUARE_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def loadImages():
    """
    Инициализирует глобальный каталог изображений.

    """
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))


def main():
    """
    Основной механизм для нашего кода.
    Это позволит обрабатывать пользовательский ввод и обновлять графику.
    """
    p.init()
    screen = p.display.set_mode((BOARD_WIDTH + MOVE_LOG_PANEL_WIDTH, BOARD_HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    #valid_moves = gs.getValidMoves()
    move_made = False  # переменная флага, указывающая, когда выполняется перемещение
    animate = False  # переменная флага, указывающая, когда мы должны анимировать перемещение
    loadImages()  # сделайте это только один раз перед циклом while
    running = True
    square_selected = ()  # изначально квадрат не выбран, это позволит отслеживать последний щелчок пользователя (кортеж (строка, столбец))
    player_clicks = []  # это позволит отслеживать клики игрока (два кортежа)
    game_over = False
    ai_thinking = False
    move_undone = False
    move_finder_process = None
    move_log_font = p.font.SysFont("Arial", 14, False, False)
    player_one = True  # если человек играет белыми, то это будет правдой, в противном случае ложью
    player_two = False  # если компьютер играет белыми, то это будет True, в противном случае False

    while running:
        human_turn = (gs.white_to_move and player_one) or (not gs.white_to_move and player_two)
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # mouse handler
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen) # рисует квадраты на доске
    drawPieces(screen, gs.board) # рисует фигуры на этих квадратах


def drawBoard(screen):
    """
    Прорисовка квадтратов на доске.
    Верхний левый квадрат всегда светлый.
    """
    global colors
    colors = [p.Color("#b7b3b4"), p.Color("#3f372e")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def drawPieces(screen, board):
    """
    Draw the pieces on the board using the current game_state.board
    """
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

if __name__ == "__main__":
    main()
