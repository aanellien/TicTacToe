from typing import List

import Strings
from Board import Board
from Strings import SEPERATION_SYM

DEFAULT_NAMES: List[str] = [Strings.DEFAULT_NAME1, Strings.DEFAULT_NAME2]
INVALID_SYMBOLS: List[str] = [Strings.DEFAULT_SYMBOL_EMPTY, SEPERATION_SYM]


class TicTacToe:
    def __init__(self, board_size: int = 3) -> None:
        self.board_size: int = board_size
        self.board: Board = Board(board_size)
        self.board.printBoard()
        self._populateNames()

    def _isValidName(self, name):
        return name not in DEFAULT_NAMES and len(name) > 0 and '\\' not in name

    def _isValidSymbol(self, symbol):
        return len(symbol) > 0 and symbol[0] not in INVALID_SYMBOLS and '\\' not in symbol

    def _populateNames(self) -> None:
        name1: str = input(Strings.MSG_NAME.format(Strings.DEFAULT_NAME1)).strip()
        if not self._isValidName(name1):
            print(Strings.MSG_NAME_FORB.format(name1))
            name1 = Strings.DEFAULT_NAME1

        print(Strings.MSG_NAME_CONF.format(name1))

        symbol1: str = input(Strings.MSG_SYMBOL.format(name1)).strip()
        if not self._isValidSymbol(symbol1):
            print(Strings.MG_SYMBOL_FORB.format(symbol1))
            symbol1 = Strings.DEFAULT_SYMBOL1

        symbol1 = symbol1[0]
        print(Strings.MG_SYMBOL_CONf.format(name1, symbol1))

        name2: str = input(Strings.MSG_NAME.format(Strings.DEFAULT_NAME2)).strip()
        if not self._isValidName(name2) or name2 == name1:
            print(Strings.MG_SYMBOL_FORB.format(name2))
            name2 = Strings.DEFAULT_NAME2
        print(Strings.MSG_NAME_CONF.format(name2))

        symbol2: str = input(Strings.MSG_SYMBOL.format(name2)).strip()
        if not self._isValidSymbol(symbol2) or symbol2[0] == symbol1[0]:
            print(Strings.MG_SYMBOL_FORB.format(symbol2))
            symbol2 = Strings.DEFAULT_SYMBOL2 if symbol1 != Strings.DEFAULT_SYMBOL2 else Strings.DEFAULT_SYMBOL1

        symbol2 = symbol2[0]
        print(Strings.MG_SYMBOL_CONf.format(name2, symbol2))

    def play(self) -> None:
        self.board.play()


def playBasicTicTacToe() -> None:
    playCustomTicTacToe(3)


def playCustomTicTacToe(size: int) -> None:
    tictactoe: TicTacToe = TicTacToe(size)
    tictactoe.play()


if __name__ == "__main__":
    playBasicTicTacToe()
