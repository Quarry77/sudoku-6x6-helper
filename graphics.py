from tkinter import *

class MainMenuWindow:
    def __init__(self, font_size=32):
        self.root = Tk()
        self.root.title("Sudoku 6x6 Helper - Main Menu")
        self.board = Frame(self.root, bg="white")
        self.board.grid(row=0, rowspan=8)

        self.bottom_frame = Frame(self.root)

class GameWindow:
    def __init__(self, font_size=32):
        self.root = Tk()
        self.root.title("Sudoku 6x6  - Game")
        self.board = Frame(self.root, bg="white")
        self.board.grid(row=0, rowspan=8)

        self.bottom_frame = Frame(self.root)