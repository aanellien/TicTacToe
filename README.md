# TicTacToe
#### TicTacToe Open Source Project Template Instructions


## Installation

Uses Python3.7

1) To setup environment  read at https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
    requirement.txt is at TicTacToe/requirement.txt

2) Run a default 3*3 tictactoe console game by Running  python TicTacToe.py 
3) Run a n*n tictactoe console game  by running  python TicTacToeNSize.py
4) run the written tests by running python Tests.py


# TicTacToe

**Description**:   This project can help you play a tic-tac-toe game of N*N board over 
variety of UI. The project has implemented the game in console. The logic of the game
is exposed through functions, which user can extend to play on any UI, without needing
to focus on the game logic.

  - **Technology stack**: It is coded in Python 3.7 . The library functions gives you access to the complete game logic,
  helping you reuse with other interfaces.  An implementation of the game with console interface,
  comes along with this project.
  
  - **Status**:  Beta - Next phase will cover unit tests for all functions as well 
  as integration test of some example games played. The unit tests will also verify  the message in value error 
  - This project can support any N*N tictactoe game. 
  - It has been fully
  implement using type hints for greater safety
  - It allows you to load a in-between game rather than start from beginning everytime.
  - It exposes core logic of the game which can be used in your own project.
  - It has a lot of error checking logic to overcome most edge cases.
  - Has multiple randomized tests




## Dependencies


requirement.txt having the python libraries required is present in the project folder.
It uses numpy for the array utility to store the game state. 
Other libraries mainly support type hinting



## Usage

2) Run a default 3*3 tictactoe by Running  python TicTacToe.py 
3) Run a n*n tictactoe by running  python TicTacToeNSize.py
4) run the written tests by running python Tests.py


Walkthrough for developers who want to use the current functionality to 
provide a non-console UI for this game.

Board.py has the main logic

1) Construct  Board class object by using the following constructor
       a) Board size should be an integer > 2
       
       b) symbol1,name1 belong to player 1
       
       c) symbol2,name2 belong to player2
       
       d) Default Symbol is the default cell symbol before any move is done
       
       e) all symbols should be unique of each other
       
       f) symbols are not allowed to have \n,\t,' ' and any other character
       which interferes in console printing of game board
       
       g) Both players should have different names      
       
       
       

board = Board( board_size: int = 3, symbol1: str = Strings.DEFAULT_SYMBOL1,
                 symbol2: str = Strings.DEFAULT_SYMBOL2,
                 default_symbol: str = Strings.DEFAULT_SYMBOL_EMPTY,
                 name1: str = Strings.DEFAULT_NAME1, name2: str = Strings.DEFAULT_NAME2) -> None:
                 raise Value Error if invalid arguments
           
                 
2)  Play using console output by 
board.play() and following instructions. If you are not using console UI, this functionality
is not required.

3)You can save, load a game state.
     a)save  -> board.getBoard() -> will give you 2d numpy array 
                                    of current board state
     b)load -> board.setBoard(board) where board is the stored 2d numpy
     array. It will also update the game state. This raises value error when invalid value.     
     c)be sure to initiate all symbols to same values between games sessions
4) Get game status by calling getStatus()
    statuses are enum with name,values being
        NOT_FINISHED = 1
        PLAYER1_WIN = 2
        PLAYER2_WIN = 3
        DRAW = 4
  
5)  board.makeMove(row: int,col: int)     
       Will try to make a move. The program autodetects whose turn it is and accordingly
       places symbol in that row,col. Invalid values will throw a value error with message explaining the error````


## How to test the software

python Tests.py

## Known issues

1) Unit Tests are not complete
2) No Integration tests written as of now. 
3) No Doc strings for the functions
4) Unit tests do not check between various types of Value Errors. The message of the error can be used by using 
5) Some of the unit tests need to be broken into smaller parts 
6) current console implementation of gracefully exiting from a running game without finishing it. Need to add a seperate character like 'q' to allow uses to exit game midway.


## Getting help




If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.


## Getting involved
    1)We are currently trying to write an AI which can play N*N tictactoe very well. 
    Basic Min_Max+Alpha_beta pruning will be too slow for large problem solving(n=50).
    2)Limited depth min-max+pruning+heuristic for the depth is what we are focusing on.
    3)Reusing the previous calulations will be a big bonus.
----

## Open source licensing info
It has a fair use usage policy. If you are going to reuse this code elsewhere, please
do not forget to credit the author. 

----

## Credits 
1) The team which has sent me the project.
  (a)I originally didnt plan on spending more than 1 hour as tic-tac-toe is too basic
  (b) Which is true
  (c) But making it robust handling 
        (i) Edge cases
        (ii) Allowing other developers to reuse functionality in different project
        (iii) Having Robust testing 
        (iv) Code simple to read,understand
        (v) Following good software engineering practises
  (d) Testing took me more time. I know basic architecture of testing 
  from unit tests,integration test,workflow testing, white,black boxes etc.
  Knew the basic logic , but have never implemented it on a project.
  
  (e) After writing tests, felt the need to break 
  original code into much smaller modules breaking tight coupling between 
  data inputting and core logic,
2) Team for being patient with me , family for supporting me when I am down last few days with chicken pox and fever due to that. Very unfortunate timing.
  
   
   

