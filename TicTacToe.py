import Strings
from .Board import Board

class TicTacToe:
    def __init__(self, board_size: int = 3):
        self.board_size: int = board_size
        self.board: Board = Board(board_size)
        self.board.printBoard()
        self.populateNames()

    def populateNames(self) -> None:
        name1: str = input(Strings.MSG_NAME.format(Strings.DEFAULT_NAME1)).strip()
        if len(name1) == 0:
            name1 = Strings.DEFAULT_NAME1
        if name1 == Strings.DEFAULT_NAME2:
            print(Strings.MSG_NAME_FORB.format(name1))
            name1 = Strings.DEFAULT_NAME1
        print(Strings.MSG_NAME_CONF.format(name1))

        symbol1: str = input(Strings.MSG_SYMBOL.format(name1)).strip()
        if len(symbol1) == 0 or symbol1[0] == Strings.DEFAULT_SYMBOL_EMPTY:
            print(Strings.MG_SYMBOL_FORB.format(symbol1))
            symbol1 = Strings.DEFAULT_SYMBOL1
        else:
            symbol1 = symbol1[0]
        print(Strings.MG_SYMBOL_CONf.format(name1, symbol1))

        name2: str = input(Strings.MSG_NAME.format(Strings.DEFAULT_NAME2)).strip()
        if name2 == Strings.DEFAULT_NAME1 or name2 == name1 or len(name2) == 0:
            print(Strings.MG_SYMBOL_FORB.format(name2))
            name2 = Strings.DEFAULT_NAME2
        print(Strings.MSG_NAME_CONF.format(name2))

        symbol2: str = input(Strings.MSG_SYMBOL.format(name2)).strip()
        if len(symbol2) == 0 or symbol2[0] == symbol1 or symbol2[0] == Strings.DEFAULT_SYMBOL_EMPTY:
            print(Strings.MG_SYMBOL_FORB.format(symbol2))
            symbol2 = Strings.DEFAULT_SYMBOL2 if symbol1 != Strings.DEFAULT_SYMBOL2 else Strings.DEFAULT_SYMBOL1
        else:
            symbol2 = symbol2[0]
        print(Strings.MG_SYMBOL_CONf.format(name2, symbol2))

    def play(self) -> None:
        self.board.play()


def playBasicTicTacToe() -> None:
    playCustomTicTacToe(3)


def playCustomTicTacToe(size: int) -> None:
    playCustomTicTacToe(size)


if __name__ == "__main__":
    playBasicTicTacToe()
