import tkinter as tk
from tkinter import ttk
import logging


class SubWindows(tk.Toplevel):
    def __init__(self, locale: dict, gui_opt: dict) -> None:

        tk.Toplevel.__init__(self, **gui_opt['main_frame'])

        self.geometry('300x200')
        self.label = tk.Label(self, **gui_opt['text_config'])
        self.progressbar = ttk.Progressbar(self, length=200, value=0)
        self.button = tk.Button(
            self,
            text='STOP',
            **gui_opt['button_config']
        )
        self.label.pack(pady=20)
        self.progressbar.pack()
        self.button.pack(pady=20)
        self.update()

    def update_progress_bar(self, data: dict) -> None:
        logging.debug(f"PrintImgSubWindows {data}")
        self.progressbar['value'] = data['progress']
        try:
            self.progressbar['value'] = data['progress']
            self.label['text'] = data['label']
            self.update()
        except:
            pass

    def destroy_windows(self):
        logging.debug(f"PrintImgSubWindows")
        self.after(1500, lambda: self.destroy())
