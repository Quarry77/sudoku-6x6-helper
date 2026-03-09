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
        self.style.theme_use('clam')
        self.style.configure('Red.TFrame',background="#FFB19B")
        self.style.configure('Blue.TFrame',background="#C6C6FF")
        self.style.configure('Green.TFrame',background="#E5F7E5")

        self.header = Header(self, "Main Menu", height=30)
        self.header.grid(row=0, column=0, sticky="nsew")

        self.maker_screen = Maker(self, style="Blue.TFrame")
        self.maker_screen.grid(row=1, column=0, sticky="nsew")

        self.player_screen = Player(self, style="Green.TFrame")
        self.player_screen.grid(row=1, column=0, sticky="nsew")

        self.menu = Menu(self, style="Red.TFrame")
        self.menu.grid(row=1, column=0, sticky="nsew")

class Header(ttk.Frame):
    def __init__(self, parent, header_text="Header", back_enabled=False, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.header_text = header_text
        self.back_enabled = back_enabled

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=9)
        self.grid_propagate(False)

        
        self.back_btn = ttk.Button(text="<-- Back", command=self.back)
        self.back_btn.grid(row=0, column=0, sticky="w")

        if not self.back_enabled:
            self.back_btn.grid_remove()

        self.header_lbl = ttk.Label(self, text=self.header_text, font=("Helvetica", max(10, self.winfo_height() // 2), "bold"))
        self.header_lbl.grid(row=0, column=0, columnspan=2, sticky="ns")

    def back(self):
        self.parent.menu.tkraise()
        self.back_enabled = False
        self.back_btn.grid_remove()
        self.header_lbl.config(text="Main Menu")


class Menu(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        self.columnconfigure(4, weight=1)

        self.new_game_btn = ttk.Button(self, text="Load Game", command=self.load_maker)
        self.new_game_btn.grid(row=1, column=1)

        self.new_game_btn = ttk.Button(self, text="Load Game", command=self.load_player)
        self.new_game_btn.grid(row=2, column=1)

        self.new_game_btn = ttk.Button(self, text="Maker", command=self.go_to_maker)
        self.new_game_btn.grid(row=1, column=2)

        self.new_game_btn = ttk.Button(self, text="Player", command=self.go_to_player)
        self.new_game_btn.grid(row=2, column=2)

        self.new_game_btn = ttk.Button(self, text="Clear Game", command=self.clear_maker)
        self.new_game_btn.grid(row=1, column=3)

        self.new_game_btn = ttk.Button(self, text="Clear Game", command=self.clear_player)
        self.new_game_btn.grid(row=2, column=3)

    def load_maker(self):
        print("TODO: Load Maker")

    def load_player(self):
        print("TODO: Load Player")

    def go_to_maker(self):
        self.parent.maker_screen.tkraise()
        self.parent.header.header_lbl.config(text="Sudoku Maker")
        self.parent.header.back_enabled = True
        self.parent.header.back_btn.grid()

    def go_to_player(self):
        self.parent.player_screen.tkraise()
        self.parent.header.header_lbl.config(text="Sudoku Player")
        self.parent.header.back_enabled = True
        self.parent.header.back_btn.grid()

    def clear_maker(self):
        print("TODO: Clear Maker")

    def clear_player(self):
        print("TODO: Clear Player")

class Maker(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        self.columnconfigure(4, weight=1)

class Player(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        self.columnconfigure(4, weight=1)