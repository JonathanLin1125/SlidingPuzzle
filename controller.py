from slidingpuzzle import Puzzle

def get_board(size):
    board = []
    for i in range(size):
        row = input()
        board.append(row.split())
    return board

def get_size():
    size = int(input("Enter size of the board: "))
    return size

def get_move():
    move = input("Enter a move (wasd) or q to quit: ")
    return move

if __name__ == "__main__":
    size = get_size()
    board = get_board(size)
    
    puzzle = Puzzle(board, size)
    move = get_move()

    while move != "q":
        puzzle.update_board(move)
        puzzle.print_board()
        move = get_move()
