import tkinter
from slidingpuzzle import Puzzle

class Game:
    def __init__(self, size):
        self.size = size
        
        self.puzzle = Puzzle(self.size)
        self.puzzle.print_board()
