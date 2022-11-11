import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class InfoView(tk.Frame):
    def __init__(self, master: tk.Tk, locale: dict, gui_opt: dict) -> None:

        tk.Frame.__init__(self, master, **gui_opt['main_frame'])

        self.name = tk.Label(
            self,
            text=locale['name'],
            **gui_opt['text_config']
        )
        self.text_1 = tk.Label(
            self,
            text=locale['text_1'],
            **gui_opt['text_config']
        )
        self.text_2 = tk.Label(
            self,
            text=locale['text_2'],
            **gui_opt['text_config']
        )
        self.img = tk.Label(self, bg=gui_opt['bg_general'])
        self.separator_0 = ttk.Separator(self, orient=tk.HORIZONTAL)

        img_gorlu = ImageTk.PhotoImage(
            Image.open(fr'assets/img/info.png')
        )
        self.img.configure(image=img_gorlu)
        self.img.image = img_gorlu

        self.name.pack(fill=tk.X, pady=30)
        self.separator_0.pack(fill=tk.X, padx=200)
        self.text_1.pack(fill=tk.X, pady=30)
        self.img.pack(pady=5)
        self.text_2.pack(fill=tk.X, pady=30)
