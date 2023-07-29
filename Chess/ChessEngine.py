"""
Хранение всей информации о текущем состоянии шахматной партии.
Определение допустимых ходов в текущем состоянии.
Он будет вести журнал перемещений.
"""


class GameState:
    def __init__(self):
        """
        Доска представляет собой 2d-список размером 8х8, каждый элемент в списке состоит из 2 символов.
        Первый символ обозначает цвет фигуры: "b" или "w".
        Второй символ обозначает тип фрагмента: 'R', 'N', 'B', 'Q', 'K' или 'p'.
        "--" представляет собой пустое пространство без фрагмента.
        """
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        # self.moveFunctions = {"p": self.getPawnMoves, "R": self.getRookMoves, "N": self.getKnightMoves,
        #                       "B": self.getBishopMoves, "Q": self.getQueenMoves, "K": self.getKingMoves}
        self.white_to_move = True
        self.move_log = []
        self.white_king_location = (7, 4)
        self.black_king_location = (0, 4)
        self.checkmate = False
        self.stalemate = False
        self.in_check = False
        self.pins = []
        self.checks = []
        self.enpassant_possible = ()  # coordinates for the square where en-passant capture is possible
        self.enpassant_possible_log = [self.enpassant_possible]
        # self.current_castling_rights = CastleRights(True, True, True, True)
        # self.castle_rights_log = [CastleRights(self.current_castling_rights.wks, self.current_castling_rights.bks,
        #                                        self.current_castling_rights.wqs, self.current_castling_rights.bqs)]