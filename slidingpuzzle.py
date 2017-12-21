import random
from functools import reduce

class Puzzle:

    def __init__(self, size, start_board = []):
        self.size = size
        self.board = start_board
        if self.board == []:
            self.board = self.create_default()
        self.blank_cord = self.find_blank()

    def create_default(self):
        board = []
        for mult in range(1, self.size + 1):
            board.append([num for num in range((mult - 1) * self.size + 1, mult * self.size + 1)])
        del board[self.size - 1][self.size - 1]
        board[self.size - 1].append("B")
        return board

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

    def reset(self):
        self.board = self.create_default()
        self.blank_cord = self.find_blank()

    def scramble(self):
        random.shuffle(self.board)
        for i in range(len(self.board)):
            random.shuffle(self.board[i])
        self.blank_cord = self.find_blank()
        self._get_inversion_count()
        if self._check_solvable() == False:
            self.scramble()

    def _get_inversion_count(self):
        inv_count = 0
        single_list = reduce((lambda x,y: x + y), self.board)
        for i in range(self.size * self.size - 1):
            for j in range(i + 1, self.size * self.size):
                if single_list[i] != "B" and single_list[j] != "B" and int(single_list[i]) > int(single_list[j]):
                    inv_count += 1
        return inv_count
            

    def _check_solvable(self):
        inv_count = self._get_inversion_count()
        if self.size % 2 != 0 and inv_count % 2 == 0:
            return True
        elif self.size % 2 == 0 and (self.size - self.blank_cord[0] + 1) % 2 != 0 and inv_count % 2 != 0:
            return True
        elif self.size % 2 == 0 and (self.size - self.blank_cord[0] + 1) % 2 == 0 and inv_count % 2 == 0:
            return True
        else:
            return False

    def print_board(self):
        for row in self.board:
            for col in row:
                print(str(col) + " ", end="")
            print()

                
        
