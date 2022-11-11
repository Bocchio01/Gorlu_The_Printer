import logging

import tkinter as tk
from PIL import ImageTk, Image


class LangView(tk.Frame):
    def __init__(self, master: tk.Tk, locale: dict, gui_opt: dict) -> None:

        tk.Frame.__init__(self, master, **gui_opt['main_frame'])

        self.it: tk.Frame = self.createButtonWidget(
            data={
                'src': 'it',
                'text': 'Iniziamo!'
            },
            gui_opt=gui_opt
        )
        self.en: tk.Frame = self.createButtonWidget(
            data={
                'src': 'en',
                'text': 'Lets start!'
            },
            gui_opt=gui_opt
        )

        self.fr: tk.Frame = self.createButtonWidget(
            data={
                'src': 'fr',
                'text': 'Alle!'
            },
            gui_opt=gui_opt
        )

        self.it.pack(side=tk.LEFT, expand=True)
        self.en.pack(side=tk.LEFT, expand=True)
        self.fr.pack(side=tk.LEFT, expand=True)

    def createButtonWidget(self, data: dict[str, str], gui_opt: dict):
        logging.debug(f"LangView")
        flag_image = ImageTk.PhotoImage(
            Image.open(fr'assets/img/{data["src"]}.png')
        )

        frame = tk.Frame(
            self,
            bg=gui_opt['bg_general'],
            **gui_opt['border']
        )

        frame.label = tk.Label(
            frame,
            image=flag_image,
            bg=gui_opt['bg_general']
        )
        frame.label.image = flag_image

        frame.button = tk.Button(
            frame,
            text=data['text'],
            # command=lambda: self.controller.change_locale(data['src']),
            **gui_opt['button_config']
        )

        frame.label.pack()
        frame.button.pack(fill=tk.X, pady=(30, 0))
        return frame
