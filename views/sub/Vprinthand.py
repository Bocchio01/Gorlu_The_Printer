import logging
import tkinter as tk
from tkinter import ttk


class PrintHandView(tk.Frame):
    def __init__(self, master: tk.Tk, locale: dict, gui_opt: dict) -> None:

        tk.Frame.__init__(self, master, **gui_opt['main_frame'])

        self.setting_frame = tk.Frame(self, bg=gui_opt['bg_general'])
        self.setting_text_0 = tk.Label(
            self.setting_frame,
            text=locale['setting_text_0'],
            **gui_opt['text_config']
        )
        self.setting_text_1 = tk.Label(
            self.setting_frame,
            text=locale['setting_text_1'],
            **gui_opt['text_config']
        )
        self.setting_text_2 = tk.Label(
            self.setting_frame,
            text=locale['setting_text_2'],
            **gui_opt['text_config']
        )
        self.setting_text_3 = tk.Label(
            self.setting_frame,
            text=locale['setting_text_3'],
            **gui_opt['text_config']
        )
        self.setting_separator_0 = ttk.Separator(
            self.setting_frame,
            orient=tk.HORIZONTAL
        )
        self.setting_separator_1 = ttk.Separator(
            self.setting_frame,
            orient=tk.HORIZONTAL
        )
        self.setting_button_0 = tk.Button(
            self.setting_frame,
            text=locale['setting_button_0'],
            **gui_opt['button_config']
        )
        self.setting_button_1 = tk.Button(
            self.setting_frame,
            text=locale['setting_button_1'],
            **gui_opt['button_config']
        )

        self.visualizer_frame = tk.Frame(
            self,
            bg=gui_opt['bg_visualizer']
        )
        self.visualizer_board = tk.Canvas(
            self.visualizer_frame,
            **gui_opt['visualizer_config']
        )

        # printhand pack/grid
        self.setting_frame.rowconfigure([0, 3, 4, 6, 7], minsize=70)
        self.setting_frame.rowconfigure([2, 5], minsize=30)
        self.setting_frame.rowconfigure(1, minsize=30)
        self.setting_frame.columnconfigure(0, minsize=400)

        self.setting_frame.pack(fill=tk.Y, side=tk.LEFT, pady=50)
        self.setting_text_0.grid(sticky='ns')
        self.setting_separator_0.grid(padx=40, sticky='we')
        self.setting_text_1.grid(pady=10, sticky='ns')
        self.setting_text_2.grid(sticky='ns')
        self.setting_text_3.grid(sticky='ns')
        self.setting_separator_1.grid(padx=40, sticky='we')
        self.setting_button_0.grid(pady=20, sticky='s')
        self.setting_button_1.grid(pady=0, sticky='n')
        self.visualizer_frame.pack(fill=tk.BOTH, expand=True)
        self.visualizer_board.pack(expand=True)

    def addLine(self, pre, next):
        logging.debug(f"PrintHandView {pre} : {next}")
        self.visualizer_board.create_line(pre, next)
        self.update()
