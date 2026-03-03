from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("Sudoku 6x6 Helper")
root.geometry("648x1100+960-150")

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=10, row=0)
root.mainloop()