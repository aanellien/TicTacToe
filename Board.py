from typing import List, Iterable
import numpy as np
from nptyping import Array
import Strings

class Board:
    def __init__(self, board_size: int = 3, symbol1: str = Strings.DEFAULT_SYMBOL1,
                 symbol2: str = Strings.DEFAULT_SYMBOL2,
                 default_symbol: str = Strings.DEFAULT_SYMBOL_EMPTY,
                 name1: str = Strings.DEFAULT_NAME1, name2: str = Strings.DEFAULT_NAME2):
        self.board_size: int = board_size
        self.symbol1: str = symbol1
        self.symbol2: str = symbol2
        self.default_symbol: str = default_symbol
        self.name1: str = name1
        self.name2: str = name2
        self.createBoard()

    def printBoard(self) -> None:
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(self.board[i, j], end=' ')
            print()

    def createBoard(self) -> None:
        self.board: Array[np.str, np.str] = np.full((self.board_size, self.board_size), self.default_symbol)

    def play(self) -> None:
        self.createBoard()

        turn: int = 1
        while (turn <= self.board_size ** 2):
            current_name: str = self.name1
            current_symbol: str = self.symbol1
            if turn % 2 == 0:
                current_name = self.name2
                current_symbol = self.symbol2
            try:
                self.printBoard()
                coordinates: str = input(Strings.MSG_MAKE_MOVE.format(current_name))
                array_values: List[int] = [int(x) - 1 for x in coordinates.split(",")]
                if len(array_values) != 2:
                    raise ValueError()
                row: int = array_values[0]
                col: int = array_values[1]
                if not (0 <= row < self.board_size and 0 <= col < self.board_size):
                    raise ValueError()
                if self.board[row, col] != self.default_symbol:
                    print(Strings.MSG_OCCUPIED_SQUARE)
                    raise ValueError()

            except:
                print(Strings.MSG_INVALID_MOVE)
                continue

            self.board[row, col] = current_symbol
            turn += 1
            if self.isWin():
                print("Congratulations, {} has won the game".format(current_name))
                break
        self.printBoard()
        if not self.isWin():
            print("It has been a draw between {} and {}".format(self.name1, self.name2))

    def isWin(self) -> bool:
        return self.checkRows() or self.checkCols() or self.checkIncDia() or self.checkIncDia()

    def checkRows(self) -> bool:
        for row in self.board:
            if self.generalCheck(row):
                return True
        return False

    def checkCols(self) -> bool:
        for i in range(self.board_size):
            col = self.board[:, i]
            if self.generalCheck(col):
                return True
        return False

    def checkIncDia(self) -> bool:
        values: List[str] = []
        for i in range(self.board_size):
            values.append(self.board[i, i])
        return self.generalCheck(values)

    def checkDecDia(self) -> bool:
        values: List[str] = []
        for i in range(self.board_size):
            values.append(self.board[i, -i - 1])
        return self.generalCheck(values)

    def generalCheck(self, arr: Iterable[str]) -> bool:
        return self.default_symbol not in arr and len(set(arr)) == 1