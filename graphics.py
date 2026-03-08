import tkinter as tk
from tkinter import ttk, font

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku 6x6 Helper - Main Menu")

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.minsize(400, 300)
        # self.maxsize(800, 600)

        # self.header = Header(self, "Main Menu", True, height=300)
        # self.header.pack(side="top", fill="x", expand=True)

        # self.menu = tk.Frame(self, bg="red")
        # self.menu.pack(side="bottom", fill="both", expand=True)

        self.style = ttk.Style()
        self.style.configure('Red.TFrame',background="red")

        self.header = Header(self, "Main Menu", True)
        self.header.grid(row=0, column=0, sticky="nsew")

        self.game_screen = tk.Frame(self, bg="blue")
        self.game_screen.grid(row=1, column=0, sticky="nsew")

        self.menu = Menu(self, style="Red.TFrame")
        self.menu.grid(row=1, column=0, sticky="nsew")

class Header(ttk.Frame):
    def __init__(self, parent, header_text="Header", back_enabled=False, *args, **kwargs):
        super().__init__(parent, **kwargs)
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

    def back(self):
        pass


class Menu(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)

        self.new_game_btn = ttk.Button(self, text="New Game")
        self.new_game_btn.grid(row=1, column=1)
