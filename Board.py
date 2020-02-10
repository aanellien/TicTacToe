from enum import Enum
from typing import List, Iterable, Tuple

import numpy as np
from nptyping import Array

import Strings



class GameStatus(Enum):
    NOT_FINISHED = 1
    PLAYER1_WIN = 2
    PLAYER2_WIN = 3
    DRAW = 4


class Board:

    def __init__(self, board_size: int = 3, symbol1: str = Strings.DEFAULT_SYMBOL1,
                 symbol2: str = Strings.DEFAULT_SYMBOL2,
                 default_symbol: str = Strings.DEFAULT_SYMBOL_EMPTY,
                 name1: str = Strings.DEFAULT_NAME1, name2: str = Strings.DEFAULT_NAME2) -> None:

        if board_size < 3:
            raise ValueError(Strings.MSG_MIN_BD_SIZE)
        if len({symbol1, symbol2, default_symbol}) != 3:
            raise ValueError(Strings.MSG_UNIQ_SYB)

        name1,name2 = name1.strip(),name2.strip()
        if len({name1, name2}) < 2:
            raise ValueError(Strings.MSG_UNIQ_NAMES)
        for symbol in [symbol1, symbol2, default_symbol]:
            if len(symbol) != 1:
                raise ValueError(Strings.SYM_NOT_SIZE_1.format(symbol))
            if not (ord('!') <= ord(symbol) <= ord('~')):
                raise ValueError(Strings.SYB_NOT_ALLOW.format(symbol))

        self._board_size: int = board_size
        self._symbol1: str = symbol1
        self._symbol2: str = symbol2
        self._default_symbol: str = default_symbol
        self._name1: str = name1
        self._name2: str = name2
        self._createBoard()
        self._status: GameStatus = GameStatus.NOT_FINISHED

    def printBoard(self) -> None:
        for i in range(self._board_size):
            for j in range(self._board_size):
                print(self._board[i, j], end=Strings.SEPERATION_SYM)
            print()

    def _createBoard(self) -> None:
        self._board: Array[np.str, ..., ...] = np.full((self._board_size, self._board_size), self._default_symbol)
        self._turn = 1
        self._status: GameStatus = GameStatus.NOT_FINISHED

    def getCurrentSymbol(self) -> str:
        if self._turn % 2 == 1:
            return self._symbol1
        return self._symbol2

    def getCurrentPlayer(self) -> str:
        if self._turn % 2 == 1:
            return self._name1
        return self._name2

    def _checkValidInput(self, coordinates: str) -> Tuple[int, int]:
        try:
            array_values: List[int] = [int(x) - 1 for x in coordinates.split(",")]
        except:
            raise ValueError(Strings.CORD_NOT_INT)
        if len(array_values) != 2:
            raise ValueError(Strings.MOVE_NOT_2_CORD)


        return array_values[0],array_values[1]

    def _checkValidCoordinates(self, row: int, col: int) -> None:
        if not (0 <= row < self._board_size and 0 <= col < self._board_size):
            raise ValueError(Strings.CORD_OUT_BOUND)
        if self._board[row, col] != self._default_symbol:
            raise ValueError(Strings.MSG_OCCUPIED_SQUARE)

    def makeMove(self, row: int, col: int) -> None:
        if self._status != GameStatus.NOT_FINISHED:
            raise ValueError(Strings.GAME_FINISHED.format(self._status.name))
        self._checkValidCoordinates(row, col)
        self._board[row, col] = self.getCurrentSymbol()

        if self.isWin():
            if self._turn % 2 == 1:
                self._status = GameStatus.PLAYER1_WIN
            else:
                self._status = GameStatus.PLAYER2_WIN
        elif self._turn == self._board_size ** 2:
            self._status = GameStatus.DRAW

        else:
            self._turn += 1

    def play(self) -> None:
        self._createBoard()

        while (self._status == GameStatus.NOT_FINISHED):
            current_name: str = self.getCurrentPlayer()
            current_symbol: str = self.getCurrentSymbol()
            self.printBoard()

            while (True):
                try:
                    coordinates: str = input(Strings.MSG_MAKE_MOVE.format(current_name))
                    row, col = self._checkValidInput(coordinates)
                    self.makeMove(row, col)
                    break
                except Exception as e:
                    print(str(e))
                    continue

        self.printBoard()
        print(Strings.RESULT.format(self._status.name))

    def isWin(self) -> bool:
        return self._checkRows() or self._checkCols() or self._checkIncDia() or self._checkDecDia()

    def _checkRows(self) -> bool:
        for row in self._board:
            if self._generalCheck(row):
                return True
        return False

    def _checkCols(self) -> bool:
        for i in range(self._board_size):
            col = self._board[:, i]
            if self._generalCheck(col):
                return True
        return False

    def _checkIncDia(self) -> bool:
        values: List[str] = []
        for i in range(self._board_size):
            values.append(self._board[i, i])
        return self._generalCheck(values)

    def _checkDecDia(self) -> bool:
        values: List[str] = []
        for i in range(self._board_size):
            values.append(self._board[i, -i - 1])
        return self._generalCheck(values)

    def _generalCheck(self, arr: Iterable[str]) -> bool:
        return self._default_symbol not in arr and len(set(arr)) == 1

    def setBoard(self, board: Array[str, str]) -> None:
        if len(board.shape) != 2:
            raise ValueError(Strings.BOARD_INVALID_DIM)
        if board.shape[0] != board.shape[1]:
            raise ValueError(Strings.BOARD_NOT_SQUARE)
        if board.shape[0] < 3:
            raise ValueError(Strings.BOARD_ATLEAST_3)
        flat_board: Array[np.str, ...] = board.flatten()
        if set(flat_board) - set({self._symbol1, self._symbol2,
                                  self._default_symbol}) != {}:
            raise ValueError(Strings.INVALID_BRD_SYM)
        player1_count = np.count_nonzero(flat_board == self._symbol1)
        player2_count = np.count_nonzero(flat_board == self._symbol2)
        if player1_count - player2_count not in (0, 1):
            raise ValueError(Strings.INVAL_POSITION)
        turn = player1_count + player2_count

        self._board = board
        self._board_size = self._board.shape[0]

    def getBoard(self):
        return self._board

    def getStatus(self):
        return self._status
