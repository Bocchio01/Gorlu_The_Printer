import tkinter as tk
from PIL import ImageTk, Image


class LangView(tk.Frame):
    def __init__(self, parent, controller, gui_opt):
        self.gui_opt = gui_opt
        self.controller = controller
        # ------------------------------
        # lang_frame
        tk.Frame.__init__(self, parent, bg=gui_opt['bg_general'])

        self.it = self.createButtonWidget(
            data={
                'src': 'it',
                'text': 'Iniziamo!'
            }
        )
        self.en = self.createButtonWidget(
            data={
                'src': 'en',
                'text': 'Lets start!'
            }
        )

        self.fr = self.createButtonWidget(
            data={
                'src': 'fr',
                'text': 'Alle!'
            }
        )

        self.it.pack(side=tk.LEFT, expand=True)
        self.en.pack(side=tk.LEFT, expand=True)
        self.fr.pack(side=tk.LEFT, expand=True)

    def createButtonWidget(self, data: dict[str, str]):
        flag_image = ImageTk.PhotoImage(
            Image.open(fr'assets/img/{data["src"]}.png')
        )

        frame = tk.Frame(
            self, bg=self.gui_opt['bg_general'], **self.gui_opt['border'])

        label = tk.Label(
            frame,
            image=flag_image,
            bg=self.gui_opt['bg_general']
        )
        label.image = flag_image

        button = tk.Button(
            frame,
            text=data['text'],
            command=lambda: self.controller.set_locale(data['src']),
            **self.gui_opt['button_config']
        )

        label.pack()
        button.pack(fill=tk.X, pady=(30, 0))
        return frame
