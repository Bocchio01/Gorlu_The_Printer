import tkinter as tk


class TemplateView(tk.Frame):
    def __init__(self, master: tk.Tk, locale: dict, gui_opt: dict) -> None:

        tk.Frame.__init__(self, master, **gui_opt['main_frame'])
