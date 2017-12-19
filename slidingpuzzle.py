class Puzzle:
    BOARD_SIZE = 4

    def __init__(self, start_board, size = BOARD_SIZE):
        self.board = start_board
        self.size = size
        self.blank_cord = self.find_blank()

    def update_board(self, key):
        if key == "w":
            if self.blank_cord[0] != self.size - 1:
                self.board[self.blank_cord[0]][self.blank_cord[1]] = self.board[self.blank_cord[0] + 1][self.blank_cord[1]]
                self.board[self.blank_cord[0] + 1][self.blank_cord[1]] = "B"
                self.blank_cord = (self.blank_cord[0] + 1, self.blank_cord[1])
        elif key == "s":
            if self.blank_cord[0] != 0:
                self.board[self.blank_cord[0]][self.blank_cord[1]] = self.board[self.blank_cord[0] - 1][self.blank_cord[1]]
                self.board[self.blank_cord[0] - 1][self.blank_cord[1]] = "B"
                self.blank_cord = (self.blank_cord[0] - 1, self.blank_cord[1])
        elif key == "a":
            if self.blank_cord[1] != self.size - 1:
                self.board[self.blank_cord[0]][self.blank_cord[1]] = self.board[self.blank_cord[0] ][self.blank_cord[1] + 1]
                self.board[self.blank_cord[0]][self.blank_cord[1] + 1] = "B"
                self.blank_cord = (self.blank_cord[0], self.blank_cord[1] + 1)
        elif key == "d":
            if self.blank_cord[1] != 0:
                self.board[self.blank_cord[0]][self.blank_cord[1]] = self.board[self.blank_cord[0]][self.blank_cord[1] - 1]
                self.board[self.blank_cord[0]][self.blank_cord[1] - 1] = "B"
                self.blank_cord = (self.blank_cord[0], self.blank_cord[1] - 1)

    def find_blank(self):
        for row in self.board:
            for col in row:
                if col == "B":
                    return (self.board.index(row), row.index(col))

    def print_board(self):
        for row in self.board:
            for col in row:
                print(col + " ", end="")
            print()

                
        
