import tkinter
from slidingpuzzle import Puzzle

class Game:
    def __init__(self, size):
        self.size = size
        self.puzzle = Puzzle(self.size)
        self.default = self.puzzle.create_default().copy()
        self.complete = "Complete"

        self.root_window = tkinter.Tk()
        block = (self.root_window.winfo_screenheight())/19
        
        self.width = block * self.size
        self.height = block * self.size

        self.root_window.wm_title("Sliding Game")
        self.root_window.columnconfigure(0, weight = 0)
        self.root_window.columnconfigure(1, weight = 1)
        self.root_window.columnconfigure(2, weight = 0)
        self.root_window.rowconfigure(0, weight = 0)
        self.root_window.rowconfigure(1, weight = 1)
        self.root_window.rowconfigure(2, weight = 0)
        
        self._add_widgets()
        self.display_board()
        self._get_move()

    def display_board(self):
        self.board = tkinter.Canvas(master = self.root_window, width = self.width, height = self.height, background = "ivory3")
        self.board.grid(row = 1, column = 1, sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)
        self.board.bind("<Configure>", self._on_resize)
        self._draw_grid()
        self._label_board()

    def _label_board(self):
        self._get_coords()
        for x in range(self.size):
            for y in range(self.size):
                center = (self.list_coord[x][y][0] - self.width/self.size/2, self.list_coord[x][y][1] - self.height/self.size/2)
                if self.puzzle.board[x][y] != "B":
                    self.board.create_text(center[0], center[1], text = self.puzzle.board[x][y], font = ('Times', 13, 'bold'))

    def _get_coords(self):
        self.list_coord = [[] for i in range(self.size)]
        for x in range(1, self.size + 1):
            for y in range(1, self.size + 1):
                self.list_coord[x - 1].append(((y * self.width/self.size), x * self.height/self.size))
        
    def _draw_grid(self):
        for row in range(1, self.size):
            self.board.create_line(0.0, row * self.height/self.size, self.width, row * self.height/self.size, fill = "Black")
            self.board.create_line(row * self.width/self.size, 0.0, row * self.width/self.size, self.height, fill = "Black")

    def _get_move(self):
        self.root_window.bind("<Left>", self._left)
        self.root_window.bind("<Right>", self._right)
        self.root_window.bind("<Down>", self._down)
        self.root_window.bind("<Up>", self._up)
        self.root_window.focus()

    def _on_resize(self, event):
        self.board.delete(tkinter.ALL)
        self.width = self.board.winfo_width()
        self.height = self.board.winfo_height()
        self._draw_grid()
        self._label_board()
        
    def _left(self, event):
        self.puzzle.update_board("a")
        self.board.delete(tkinter.ALL)
        self._draw_grid()
        self._label_board()
        self.check_complete()

    def _right(self, event):
        self.puzzle.update_board("d")
        self.board.delete(tkinter.ALL)
        self._draw_grid()
        self._label_board()
        self.check_complete()

    def _down(self, event):
        self.puzzle.update_board("s")
        self.board.delete(tkinter.ALL)
        self._draw_grid()
        self._label_board()
        self.check_complete()

    def _up(self, event):
        self.puzzle.update_board("w")
        self.board.delete(tkinter.ALL)
        self._draw_grid()
        self._label_board()
        self.check_complete()

    def check_complete(self):
        if self.equal(self.puzzle.board, self.default):
            if self.complete != "Complete":
                self.complete = "Complete"
                self._update_status()
        else:
            if self.complete != "Incomplete":
                self.complete = "Incomplete"
                self._update_status()

    def equal(self, puz_one, puz_two):
        for i in range(self.size):
            for k in range(self.size):
                if puz_one[i][k] != puz_two[i][k]:
                    return False
        return True
    
    def scramble(self):
        self.puzzle.scramble()
        self.board.delete(tkinter.ALL)
        self._draw_grid()
        self._label_board()
        self.check_complete()

    def _add_scramble_button(self):
        self.scramble_button = tkinter.Button(self.root_window, text = "Scramble", command = self.scramble)
        self.scramble_button.grid(row = 0, column = 2, sticky = tkinter.E + tkinter.N)

    def reset(self):
        self.puzzle.reset()
        self.board.delete(tkinter.ALL)
        self._draw_grid()
        self._label_board()
        self.check_complete()

    def _add_reset_button(self):
        self.reset_button = tkinter.Button(self.root_window, text = "Reset", command = self.reset)
        self.reset_button.grid(row = 2, column = 2, sticky = tkinter.E + tkinter.S)

    def quit(self):
        self.root_window.destroy()

    def _add_quit_button(self):
        self.quit_button = tkinter.Button(self.root_window, text = "Quit", command = self.quit)
        self.quit_button.grid(row = 2, column = 0, sticky = tkinter.W + tkinter.S, padx = (0, 20))

    def _update_status(self):
        self.status['text'] = self.complete

    def _add_status(self):
        self.status = tkinter.Label(self.root_window, text = self.complete)
        self.status.place(anchor = tkinter.N + tkinter.W)

    def _add_widgets(self):
        self._add_scramble_button()
        self._add_reset_button()
        self._add_quit_button()
        self._add_status()
        
    def run(self):
        self.root_window.mainloop()
