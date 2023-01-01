import json
import logging
from tkinter import font
from PIL import ImageFont

from .sub.Mlang import LangModel
from .sub.Mconfig import ConfigModel
from .sub.Mcalibration import CalibrationModel
from .sub.Mprintimg import PrintImgModel
from .sub.Mprinthand import PrintHandModel
from .sub.Mprinttext import PrintTextModel

from .observable import Observable
from .Mabstraction import ModelABC


class Model(ModelABC):

    def __init__(self):
        logging.debug(f"Model")
        self.settings = Observable({})
        self.settings.addCallback(self.save_json)

        self.gui_opt = Observable({})
        self.locale = Observable({})

        self.LangModel = LangModel(self)
        self.ConfigModel = ConfigModel(self)
        self.CalibrationModel = CalibrationModel(self)
        self.PrintImgModel = PrintImgModel(self)
        self.PrintHandModel = PrintHandModel(self)
        self.PrintTextModel = PrintTextModel(self)

    def get_settings(self):

        if not self.settings.get():
            logging.debug(f"Model")
            file = self.read_json(r"assets/settings.json")
            self.settings.set(file)

        return self.settings.get()

    def get_locale(self):

        if not self.locale.get():
            logging.debug(f"Model")
            settings = self.get_settings()
            target = (
                settings['locale']
                if settings['locale'] in ['it', 'en', 'fr'] else
                'en'
            )

            locale = self.read_json(fr'assets/locale/{target}.json')
            self.locale.set(locale)

            settings['locale'] = target
            self.settings.set(settings)

        return self.locale.get()

    def get_gui_opt(self):

        if not self.gui_opt.get():
            logging.debug(f"Model")
            opt = {**self.get_settings()['GUI']}
            opt['text_font'] = font.Font(**opt['font'])
            opt['text_config'] = {
                'bg': opt['bg_general'],
                'font': opt['text_font']
            }
            opt['button_config'] = {
                'bg': opt['bg_button'],
                'font': opt['text_font']
            }
            opt['combobox_config'] = {
                'state': 'readonly',
                'font': opt['text_font']
            }
            opt['visualizer_config'] = {
                'bg': opt['bg_visualizer'],
                'bd': 1,
                'relief': 'solid',
                'height': opt['dim_visualizer'],
                'width': opt['dim_visualizer']
            }
            opt['main_frame'] = {
                'bg': opt['bg_general'],
                'borderwidth': 2,
                'relief': 'solid'
            }

            self.gui_opt.set(opt)

        return self.gui_opt.get()

    def get_font(self):
        logging.debug(f"Model: {self.get_settings()['fonts']}")

        if self.get_settings()['fonts'] == []:
            fonts = []
            for i in font.families():
                try:
                    ImageFont.truetype(i, size=12)
                    fonts.append(i)
                except:
                    pass
            self.settings.set({**self.get_settings(), 'fonts': fonts})

        return self.get_settings()['fonts']

    @staticmethod
    def save_json(data, path=r"assets/settings.json", mode='w'):
        logging.debug(f"Model:path:{path}")
        with open(path, mode) as outfile:
            json.dump(
                data,
                outfile,
                sort_keys=False,
                indent=4
            )

    @staticmethod
    def read_json(path=r"assets/settings.json"):
        logging.debug(f"Model:path:{path}")
        file = open(path)
        content = json.load(file)
        file.close()
        return content
