import tkinter as tk
from views.abstraction import ViewABC


class View(ViewABC, tk.Tk):
    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.geometry('1000x600')

    def start_main_loop(self):
        self.mainloop()
