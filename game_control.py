"""
Module that controls the two windows
"""

import welcome_gui
import puzzle_gui

if __name__ == "__main__":
    welcome = welcome_gui.Welcome()
    welcome.run()

    if welcome.start == True:
        pass
        
