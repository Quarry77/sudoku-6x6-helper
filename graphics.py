import tkinter as tk
from tkinter import ttk, font

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku 6x6 Helper - Main Menu")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=50)
        self.columnconfigure(0, weight=1)

        self.minsize(400, 300)
        # self.maxsize(800, 600)

        self.header = Header(self, "Main Menu", True)
        self.header.grid(row=0, column=0, sticky="nsew")

        self.menu = tk.Frame(self, bg="red")
        self.menu.grid(row=1, column=0, sticky="nsew")

class Header(ttk.Frame):
    def __init__(self, parent, header_text="Header", back_enabled=False):
        super().__init__(parent)
        self.parent = parent
        self.header_text = header_text
        self.back_enabled = back_enabled

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=9)

        if self.back_enabled:
            self.back_btn = ttk.Button(text="<-- Back")
            self.back_btn.grid(row=0, column=0, sticky="w")

        self.header_lbl = ttk.Label(self, text=self.header_text, font=("Helvetica", max(10, self.winfo_height() // 2)))
        self.header_lbl.grid(row=0, column=0, columnspan=2, sticky="ns")
        self.bind("<Configure>", self.resize_header)

    def back(self):
        pass

    def resize_header(self, event):
        self.header_lbl.config(font=("Helvetica", max(10, event.height // 2)))
        # self.parent.call('tk', 'scaling', event.height / 2)
        # print(event.height / 2)

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=9)

        if self.back_enabled:
            self.back_btn = ttk.Button(text="<-- Back")
            self.back_btn.grid(row=0, column=0)

        self.header_lbl = ttk.Label(self, text=self.header_text, font=("Helvetica", max(10, self.winfo_height() // 2)))
        self.header_lbl.grid(row=0, column=0, columnspan=2, sticky="ns")
        self.bind("<Configure>", self.resize_header)
