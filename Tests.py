import io
import random
import unittest
from typing import List
from unittest.mock import patch
import numpy as np
from nptyping import Array
import Strings
from Board import Board


class UnitTestsBoard(unittest.TestCase):

    def setUp(self):
        random.seed(0)

    def test_initialize_positive(self):
        for i in range(3, 21):
            board: Board = Board(board_size=i)
            self.assertEqual(board._board.shape, (i, i))
            self.assertEqual(set(board._board.flatten()), {Strings.DEFAULT_SYMBOL_EMPTY})

    def test_initialize_error(self):
        for i in range(-10,3):
            self.assertRaises(ValueError,Board,i)

        i: int =3
        self.assertRaises(ValueError,Board,i,'A','B','A')
        self.assertRaises(ValueError,Board,i,'A','A','A')

        Board(i,'A','B','C')


        self.assertRaises(ValueError,Board,i,name1='AB',name2='AB')
        self.assertRaises(ValueError,Board,i,name1='AB',name2='AB ')
        self.assertRaises(ValueError,Board,i,name1='AB ',name2='AB ')
        self.assertRaises(ValueError,Board,i,name1='AB   ',name2='  AB ')


        Board(i,'A','B')

        self.assertRaises(ValueError,Board,i,'A','B','CA')
        self.assertRaises(ValueError, Board,i, 'AA', 'B', 'C')
        self.assertRaises(ValueError, Board,i, 'A', 'BA', 'C')
        self.assertRaises(ValueError, Board,i, 'AA', 'BA', 'CA')

        Board(i,'A','B','C')
        for symbol in ['\n','\t',' ']:
            self.assertRaises(ValueError,Board,i,symbol)

    def test_get_current_symbol(self):
        board: Board= Board()
        self.assertEqual(board.getCurrentSymbol(),board._symbol1)
        board.makeMove(1,1)
        self.assertEqual(board.getCurrentSymbol(),board._symbol2)
        board.makeMove(2,1)
        self.assertEqual(board.getCurrentSymbol(), board._symbol1)
        board.makeMove(2, 2)
        self.assertEqual(board.getCurrentSymbol(), board._symbol2)

    def test_get_current_player(self):
        board: Board = Board()
        self.assertEqual(board.getCurrentPlayer(), board._name1)
        board.makeMove(1, 1)
        self.assertEqual(board.getCurrentPlayer(), board._name2)
        board.makeMove(2, 1)
        self.assertEqual(board.getCurrentPlayer(), board._name1)
        board.makeMove(2, 2)
        self.assertEqual(board.getCurrentPlayer(), board._name2)

    def test_check_valid_row_col(self):
            board: Board= Board()

            self.assertRaises(ValueError, board._checkValidInput,'0.,0')
            self.assertRaises(ValueError, board._checkValidInput,'a,b')

            self.assertRaises(ValueError,board._checkValidInput,'0 0')
            self.assertRaises(ValueError,board._checkValidInput,'0  0')
            self.assertRaises(ValueError,board._checkValidInput,'0,0,0')
            self.assertRaises(ValueError,board._checkValidInput,'1 1,')

            self.assertEqual((0,0),board._checkValidInput('1,1'))
            self.assertEqual((2,1),board._checkValidInput('3,2'))
            self.assertEqual((4,3),board._checkValidInput('5,4'))

    def test_check_valid_coords(self):
        for i in range(3,51):
            board: Board= Board(i)
            self.assertRaises(ValueError,board._checkValidCoordinates,-1,-1)
            self.assertRaises(ValueError,board._checkValidCoordinates,i,i)

            for j in range(10):
                row = random.randint(1,i-1)
                col = random.randint(1,i-1)
                board._board[row,col]= board._symbol1
                self.assertRaises(ValueError,board._checkValidCoordinates,row,col)
                board._checkValidCoordinates(0,0)
                board._board[row, col] = board._default_symbol



    def test_print_board(self):
        end_pos = 0
        for i in range(3, 21):
            for j in range(21):
                board: Board = Board(board_size=i)
                rows: List[List[str]] = []

                for row in range(i):
                    row = []
                    for col in range(i):
                        row.append(random.choice([Strings.DEFAULT_SYMBOL_EMPTY,
                                                  Strings.DEFAULT_SYMBOL1,
                                                  Strings.DEFAULT_SYMBOL2]))
                    rows.append(row)
                board_values: Array[np.str, ..., ...] = np.array(rows)
                board._board=board_values
                with patch('sys.stdout', new_callable=io.StringIO) as mock_out:
                    board.printBoard()
                    new_string = str(mock_out.getvalue())
                    b = np.array(new_string.replace('\n', '').split(' ')[:-1])
                    b = b.reshape(i, i)
                    np.testing.assert_array_equal(b, board_values)

    def test_checkRows(self):
        for i in range(50):
            size = random.randint(3, 50)
            array = np.full((size, size), fill_value=Strings.DEFAULT_SYMBOL_EMPTY)
            row = random.randint(0, size - 1)
            array[row] = np.full(size, fill_value=Strings.DEFAULT_SYMBOL1)
            board = Board(size)
            board._board = array
            self.assertTrue(board._checkRows())

    def test_checkCols(self):
        for i in range(50):
            size = random.randint(3, 50)
            array = np.full((size, size), fill_value=Strings.DEFAULT_SYMBOL_EMPTY)
            col = random.randint(0, size - 1)
            array[:, col] = np.full(size, fill_value=Strings.DEFAULT_SYMBOL1)
            board = Board(size)
            board._board=array
            value=board._checkCols()
            self.assertTrue(board._checkCols(), msg=f"{array} is returning False")

    def test_increasingDiagonal(self):
        for i in range(50):
            size = random.randint(3, 50)
            array = np.full((size, size), fill_value=Strings.DEFAULT_SYMBOL_EMPTY)
            for i in range(size):
                array[i, i] = Strings.DEFAULT_SYMBOL1
            board = Board(size)
            board._board=array
            self.assertTrue(board._checkIncDia(), msg=f"{array} is returning False")

    def test_decreasingDiagonal(self):
        for i in range(50):
            size = random.randint(3, 50)
            array = np.full((size, size), fill_value=Strings.DEFAULT_SYMBOL_EMPTY)
            for i in range(size):
                array[i, -i - 1] = Strings.DEFAULT_SYMBOL1
            board = Board(size)
            board._board=array
            self.assertTrue(board._checkDecDia(), msg=f"{array} is returning False")

if __name__=='__main__':
    unittest.main()