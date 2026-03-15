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

        self.cells = GameGrid(self, width=300, height=200)
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

class GameGrid(ttk.Frame):
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
                self.cells[r][c] = Cell(self, c, r, bg=f"#ffffff", highlightthickness=0)
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
                self.cells[r][c].width = desired_size
                self.cells[r][c].height = desired_size
                self.cells[r][c].update_lines()


class Cell(tk.Canvas):
    def __init__(self, parent, x=0, y=0, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.x = x
        self.y = y
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.wall_inner_top = self.create_line(0, 0, 0, 0)
        self.wall_inner_bottom = self.create_line(0, 0, 0, 0)
        self.wall_inner_left = self.create_line(0, 0, 0, 0)
        self.wall_inner_right = self.create_line(0, 0, 0, 0)
        self.wall_outer_top = self.create_line(0, 0, 0, 0)
        self.wall_outer_bottom = self.create_line(0, 0, 0, 0)
        self.wall_outer_left = self.create_line(0, 0, 0, 0)
        self.wall_outer_right = self.create_line(0, 0, 0, 0)
        self.corner_top_left = self.create_line(0, 0, 0, 0)
        self.corner_top_right = self.create_line(0, 0, 0, 0)
        self.corner_bottom_left = self.create_line(0, 0, 0, 0)
        self.corner_bottom_right = self.create_line(0, 0, 0, 0)
        self.reset_state()
        self.update_lines()

    def reset_state(self):
        # Cell Walls
        self.itemconfig(self.wall_inner_top, state="hidden")
        self.itemconfig(self.wall_inner_bottom, state="hidden")
        self.itemconfig(self.wall_inner_left, state="hidden")
        self.itemconfig(self.wall_inner_right, state="hidden")
        if self.x > 0 and self.x < 7 and self.y > 0 and self.y < 6:
            self.itemconfig(self.wall_inner_bottom, state="normal")
        if self.x > 0 and self.x < 6 and self.y > 0 and self.y < 7:
            self.itemconfig(self.wall_inner_right, state="normal")

        # Outer Walls
        self.itemconfig(self.wall_outer_top, state="hidden")
        self.itemconfig(self.wall_outer_bottom, state="hidden")
        self.itemconfig(self.wall_outer_left, state="hidden")
        self.itemconfig(self.wall_outer_right, state="hidden")
        if self.x == 0 and self.y > 0 and self.y < 7:
            self.itemconfig(self.wall_outer_right, state="normal")
        if self.x == 7 and self.y > 0 and self.y < 7:
            self.itemconfig(self.wall_outer_left, state="normal")
        if self.y == 0 and self.x > 0 and self.x < 7:
            self.itemconfig(self.wall_outer_bottom, state="normal")
        if self.y == 7 and self.x > 0 and self.x < 7:
            self.itemconfig(self.wall_outer_top, state="normal")

    def update_lines(self):
        # Inner Walls
        wall_inner_top_state = self.itemcget(self.wall_inner_top, "state")
        wall_inner_bottom_state = self.itemcget(self.wall_inner_bottom, "state")
        wall_inner_left_state = self.itemcget(self.wall_inner_left, "state")
        wall_inner_right_state = self.itemcget(self.wall_inner_right, "state")
        self.delete(self.wall_inner_top)
        self.delete(self.wall_inner_bottom)
        self.delete(self.wall_inner_left)
        self.delete(self.wall_inner_right)
        self.wall_inner_top = self.create_line(0, 0, self.width, 0, fill="black", width=1, state=wall_inner_top_state)
        self.wall_inner_bottom = self.create_line(0, self.height-1, self.width, self.height-1, fill="black", width=1, state=wall_inner_bottom_state)
        self.wall_inner_left = self.create_line(0, 0, 0, self.height, fill="black", width=1, state=wall_inner_left_state)
        self.wall_inner_right = self.create_line(self.width-1, 0, self.width-1, self.height, fill="black", width=1, state=wall_inner_right_state)

        # Outer Walls
        wall_outer_top_state = self.itemcget(self.wall_outer_top, "state")
        wall_outer_bottom_state = self.itemcget(self.wall_outer_bottom, "state")
        wall_outer_left_state = self.itemcget(self.wall_outer_left, "state")
        wall_outer_right_state = self.itemcget(self.wall_outer_right, "state")
        self.delete(self.wall_outer_top)
        self.delete(self.wall_outer_bottom)
        self.delete(self.wall_outer_left)
        self.delete(self.wall_outer_right)
        self.wall_outer_top = self.create_line(0, 1, self.width, 1, fill="black", width=3, state=wall_outer_top_state)
        self.wall_outer_bottom = self.create_line(0, self.height-2, self.width, self.height-2, fill="black", width=3, state=wall_outer_bottom_state)
        self.wall_outer_left = self.create_line(1, 0, 1, self.height, fill="black", width=3, state=wall_outer_left_state)
        self.wall_outer_right = self.create_line(self.width-2, 0, self.width-2, self.height, fill="black", width=3, state=wall_outer_right_state)

        # Corners
        self.delete(self.corner_top_left)
        self.delete(self.corner_top_right)
        self.delete(self.corner_bottom_left)
        self.delete(self.corner_bottom_right)
        if self.x == 0 and self.y ==0:
            self.corner_top_left = self.create_rectangle(self.width-3, self.height-3, self.width, self.height, fill="black")
        if self.x == 7 and self.y ==0:
            self.corner_top_right = self.create_rectangle(0, self.height, 2, self.height-3, fill="black")
        if self.x == 0 and self.y == 7:
            self.corner_bottom_left = self.create_rectangle(self.width-3, 0, self.width, 2, fill="black")
        if self.x == 7 and self.y == 7:
            self.corner_bottom_right = self.create_rectangle(0, 0, 2, 2, fill="black")
