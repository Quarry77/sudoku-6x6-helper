from tkinter import *
from tkinter import ttk
import tkinter as tk
from graphics import MainMenuWindow, GameWindow

def main():
    main_menu = MainMenuWindow()

    # root = Tk()
    # root.title("Sudoku 6x6 Helper")
    # root.geometry("648x1100+960-150")

    # frm = ttk.Frame(root, padding=10)
    # frm.grid()
    # ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=10, row=0)
    main_menu.root.mainloop()

if __name__ == '__main__':
    main()