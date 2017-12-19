import tkinter
from slidingpuzzle import Puzzle

class Game:
    def __init__(self, size):
        self.time = 0.0
        self.size = size
        self.puzzle = Puzzle(self.size)

        self.root_window = tkinter.Tk()
        block = (self.root_window.winfo_screenheight())/19
        self.side = block * self.size

        self.root_window.wm_title("Sliding Game")
        self.root_window.columnconfigure(0, weight = 0)
        self._add_widgets()
        self.display_board()

        

    def display_board(self):
        self.board = tkinter.Canvas(master = self.root_window, width = self.side, height = self.side, background = "White")
        self.board.grid(row = 1, column = 0, columnspan = 3, sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)
        """Finish building the board
        """


    def _add_timer_label(self):
        self.timer_label = tkinter.Label(self.root_window, text = "Timer: " + str(self.time))
        self.timer_label.grid(row = 0, column = 0, sticky = tkinter.W + tkinter.N)

    def scramble(self):
        self.puzzle.scramble()

    def _add_scramble_button(self):
        self.scramble_button = tkinter.Button(self.root_window, text = "Scramble", command = self.scramble)
        self.scramble_button.grid(row = 0, column = 2, sticky = tkinter.E + tkinter.N)

    def start(self):
        pass
    
    def _add_start_button(self):
        self.start_button = tkinter.Button(self.root_window, text = "Start", command = self.start)
        self.start_button.grid(row = 2, column = 0, sticky = tkinter.W + tkinter.S)

    def reset(self):
        pass

    def _add_reset_button(self):
        self.reset_button = tkinter.Button(self.root_window, text = "Reset", command = self.reset)
        self.reset_button.grid(row = 2, column = 0, sticky = tkinter.E + tkinter.S)

    def quit(self):
        pass

    def _add_quit_button(self):
        self.quit_button = tkinter.Button(self.root_window, text = "Quit", command = self.quit)
        self.quit_button.grid(row = 2, column = 2, sticky = tkinter.E + tkinter.S)

    def _add_widgets(self):
        self._add_timer_label()
        self._add_scramble_button()
        self._add_start_button()
        self._add_reset_button()
        self._add_quit_button()
        

    def run(self):
        self.root_window.mainloop()
