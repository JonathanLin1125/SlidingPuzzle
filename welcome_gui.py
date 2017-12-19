"""
Welcome menu to select board size and start
"""

import tkinter

DEFAULT = 4

class Welcome:
    def __init__(self):
        self.root_window = tkinter.Tk()
        self.root_window.resizable(width = False, height = False)
        self.root_window.wm_title("Sliding Puzzle Menu")
        self._add_widgets()

    def _add_title(self):
        title = tkinter.Label(self.root_window, text = "Sliding Puzzle Menu", font = ("Helvetica", 14))
        title.grid(row = 0, column = 0, columnspan = 3)

    def _add_size_label(self):
        size_label = tkinter.Label(self.root_window, text = "Board Size", font = ("Helvetica", 10))
        size_label.grid(row = 1, column = 1)

    def _size_selected():
        pass

    def _add_size_menu(self):
        self.var = tkinter.IntVar()
        self.var.set(DEFAULT)
        size_menu = tkinter.OptionMenu(self.root_window, self.var, 3,4,5,6,7,8,9,10,11,12, command = self._size_selected)
        size_menu.grid(row = 2, column = 1)

    def _start():
        pass

    def _add_start(self):
        start_button = tkinter.Button(self.root_window, text = "Start", command = self._start)
        start_button.grid(row = 3, column = 0)

    def _quit():
        pass

    def _add_quit(self):
        quit_button = tkinter.Button(self.root_window, text = "Quit", command = self._quit)
        quit_button.grid(row = 3, column = 2)
    
    def _add_widgets(self):
        self._add_title()
        self._add_size_label()
        self._add_size_menu()
        self._add_start()
        self._add_quit()

    def run(self):
        self.root_window.mainloop()
