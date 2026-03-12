import tkinter as tk
from tkinter import ttk, font

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Sudoku 6x6 Helper - Main Menu")
        self.geometry(f"{self.winfo_screenwidth()//2}x{self.winfo_screenheight()//2}+{self.winfo_screenwidth()//4}+{self.winfo_screenheight()//4}")

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.minsize(400, 300)

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Red.TFrame',background="#FFB19B")
        self.style.configure('Blue.TFrame',background="#C6C6FF")
        self.style.configure('Green.TFrame',background="#E5F7E5")

        self.header = Header(self, "Main Menu", height=35)
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
        self.new_game_btn.grid(row=1, column=1, padx=5, pady=5)

        self.new_game_btn = ttk.Button(self, text="Load Game", command=self.load_player)
        self.new_game_btn.grid(row=2, column=1, padx=5, pady=5)

        self.new_game_btn = ttk.Button(self, text="Maker", command=self.go_to_maker, padding=10)
        self.new_game_btn.grid(row=1, column=2, pady=5)

        self.new_game_btn = ttk.Button(self, text="Player", command=self.go_to_player, padding=10)
        self.new_game_btn.grid(row=2, column=2, pady=5)

        self.new_game_btn = ttk.Button(self, text="Clear Game", command=self.clear_maker)
        self.new_game_btn.grid(row=1, column=3, padx=5, pady=5)

        # self.new_game_btn = ttk.Button(self, text="Clear Game", command=self.clear_player)
        # self.new_game_btn.grid(row=2, column=3, padx=5, pady=5)

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
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)

        self.cells = GameCells(self, width=300, height=200)
        self.cells.grid(row=1, column=1, sticky="nsew")

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

class GameCells(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.after_id = None

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=1)
        self.columnconfigure(7, weight=1)

        self.bind("<Configure>", self.enforce_aspect_ratio)

        self.cells = [[None for _ in range(8)] for _ in range(8)]
        for r in range(8):
            for c in range(8):
                # self.cells[r][c] = tk.Frame(self, bg=f"#{9-c}{9-c}{r+2}{r+2}{(c+r)%10}{(c+r)%10}", height=20, width=20)
                # self.cells[r][c] = tk.Frame(self, bg=f"#ffffff", height=20, width=20)
                # self.cells[r][c] = tk.Canvas(self, bg=f"#ffffff", highlightthickness=(c>0 and r>0 and c<7 and r<7)/2, highlightbackground="black")
                self.cells[r][c] = tk.Canvas(self, bg=f"#ffffff", highlightthickness=0)
                self.cells[r][c].create_line(0, 0, 100, 100, fill="black")
                self.cells[r][c].create_line(100, 0, 0, 100, fill="black")
                self.cells[r][c].grid(row=r, column=c, sticky="nsew")
                # self.cells[r][c].grid(row=r, column=c, sticky="nsew")

    def on_configure_bind(self, event):
        # Cancel any pending 'after_idle' calls
        if self.after_id:
            self.after_cancel(self.after_id)
        
        # Schedule the actual update function to run when idle
        self.after_id = self.after_idle(self.enforce_aspect_ratio)

    def enforce_aspect_ratio(self, event=None):
        desired_size = min(self.master.winfo_width(), self.master.winfo_height())/10
        for r in range(8):
            for c in range(8):
                self.cells[r][c].config(width=desired_size, height=desired_size)
                # self.cells[r][c].update_idletasks()