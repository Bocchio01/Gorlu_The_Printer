import logging
import tkinter as tk
from PIL import ImageTk, Image

from commons.info import InfoFrame


class LangView(tk.Frame):
    def __init__(self, parent, controller, gui_opt):
        logging.debug(f"LangView")
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
        logging.debug(f"LangView")
        flag_image = ImageTk.PhotoImage(
            Image.open(fr'assets/img/{data["src"]}.png')
        )

        frame = tk.Frame(
            self,
            bg=self.gui_opt['bg_general'],
            **self.gui_opt['border']
        )

        label = tk.Label(
            frame,
            image=flag_image,
            bg=self.gui_opt['bg_general']
        )
        label.image = flag_image

        button = tk.Button(
            frame,
            text=data['text'],
            command=lambda: self.controller.change_locale(data['src']),
            **self.gui_opt['button_config']
        )

        label.pack()
        button.pack(fill=tk.X, pady=(30, 0))
        return frame


class LangController:
    def __init__(self):
        logging.debug(f"LangController")
        chosen_lang = self.model.get_settings()['locale']
        if chosen_lang in ['it', 'en', 'fr']:
            locale = self.model.load_locale(target=chosen_lang)
            self.view.set_locale(locale)
            self.view.show_frame(InfoFrame)
        else:
            self.view.show_frame(LangView)

    def get_locale(self):
        logging.debug(f"LangController")
        return self.model.get_locale()

    def change_locale(self, lang):
        logging.debug(f"LangController:{lang}")
        locale = self.model.load_locale(target=lang)
        self.set_calibration_params_gui(self.get_calibration_params())
        self.view.set_locale(locale)
        self.view.show_frame(InfoFrame)


class LangModel:
    def __init__(self):
        logging.debug(f"LangModel")
        self.locale = {}

    def get_locale(self):
        logging.debug(f"LangModel")
        return self.locale

    def load_locale(self, target: str):
        logging.debug(f"LangModel:target:{target}")

        self.locale = self.read_json(fr'assets/locale/{target}.json')

        self.settings['locale'] = target
        self.save_json(r"assets/settings.json", self.settings)

        return self.locale


# if __name__ == "__main__":
#     from tests.test import Test
#     c = Test(LangModel(), LangView(), LangController())
#     c.start()
