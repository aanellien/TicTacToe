from TicTacToe import playCustomTicTacToe
if __name__ == '__main__':
    while(True):
        size_str: str = input("Enter side length of board you want to play-(3-50)")
        try:
            size: int = int(size_str)
            if size<3 or size > 50:
                print("Size values only between 3 to 50 or allowed")
                continue
            playCustomTicTacToe(size)
            break

        except:
            continue



