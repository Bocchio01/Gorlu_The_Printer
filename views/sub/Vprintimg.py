import logging

import tkinter as tk
from tkinter import ttk, font
from PIL import ImageTk, Image


class PrintImgView(tk.Frame):
    def __init__(self, master: tk.Tk, locale: dict, gui_opt: dict) -> None:

        tk.Frame.__init__(self, master, **gui_opt['main_frame'])

        self.filling = tk.IntVar(value=0)

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
        self.setting_separator_0 = ttk.Separator(
            self.setting_frame,
            orient=tk.HORIZONTAL
        )
        self.setting_separator_1 = ttk.Separator(
            self.setting_frame,
            orient=tk.HORIZONTAL
        )
        self.setting_selection = tk.Button(
            self.setting_frame,
            text=locale['setting_selection'],
            **gui_opt['button_config']
        )
        self.setting_quality = tk.Scale(
            self.setting_frame,
            orient=tk.HORIZONTAL,
            length=300,
            from_=1.0,
            to=500.0,
            **gui_opt['button_config']
        )
        self.setting_filling = tk.Checkbutton(
            self.setting_frame,
            text=locale['setting_filling'],
            variable=self.filling,
            onvalue=1,
            offvalue=0,
            **gui_opt['text_config']
        )
        self.setting_go = tk.Button(
            self.setting_frame,
            text=locale['setting_go'],
            state=tk.DISABLED,
            **gui_opt['button_config']
        )

        self.setting_go['font'] = ('calibri', 20, font.BOLD)

        self.visualizer_frame = tk.Frame(
            self,
            bg=gui_opt['bg_visualizer']
        )
        self.visualizer = tk.Label(
            self.visualizer_frame,
            **gui_opt['visualizer_config']
        )

        self.setting_frame.rowconfigure([0, 3, 4, 7, 8], minsize=70)
        self.setting_frame.rowconfigure([2, 5, 6], minsize=40)
        self.setting_frame.rowconfigure(1, minsize=60)
        self.setting_frame.columnconfigure(0, minsize=400)

        self.setting_frame.pack(fill=tk.Y, side=tk.LEFT, pady=50)
        self.setting_text_0.grid(sticky='ns')
        self.setting_selection.grid(sticky='n')
        self.setting_separator_0.grid(padx=40, sticky='we')
        self.setting_text_1.grid(sticky='ns')
        self.setting_quality.grid(sticky='n')
        self.setting_filling.grid(sticky='wens')
        self.setting_separator_1.grid(padx=40, sticky='we')
        self.setting_go.grid(pady=30, sticky='s')
        self.visualizer_frame.pack(fill=tk.BOTH, expand=True)
        self.visualizer.pack(expand=True)

    def set_img(self, img_to_display):
        logging.debug(f"PrintImgFrame:{img_to_display}")
        self.setting_filling.config(state='normal')
        self.setting_quality.config(state='normal')
        self.setting_go['state'] = tk.NORMAL

        image = ImageTk.PhotoImage(
            image=Image.fromarray(img_to_display)
        )

        self.visualizer.configure(image=image)
        self.visualizer.image = image
