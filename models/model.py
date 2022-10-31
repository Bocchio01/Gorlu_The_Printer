import json
import logging
from tkinter import font
from PIL import ImageFont

from commons.config import ConfigModel
from commons.calibration import CalibrationModel
from commons.printimg import PrintImgModel


class Model(
    ConfigModel,
    CalibrationModel,
    PrintImgModel
):

    def __init__(self):
        self.locale = {}
        self.gui_opt = {}
        self.fonts = []

        for model in (ConfigModel, CalibrationModel, PrintImgModel):
            model.__init__(self)

    def setup(self, controller):
        self.controller = controller
        # self.model.get_fonts()

    def get_locale(self, target: str):
        logging.debug(f"Target:{target}")
        if not self.locale or self.gui_opt['lang'] is not target:
            logging.debug(f"Loading lang")
            self.locale = self.read_json(fr'assets/locale/{target}.json')

            self.gui_opt['lang'] = target
            json = self.read_json(fr'assets/config/GUI.json')
            json['lang'] = self.gui_opt['lang']
            self.save_json(fr'assets/config/GUI.json', json)

        return self.locale

    def get_gui_opt(self):
        if not self.gui_opt:
            self.gui_opt = self.read_json(fr'assets/config/GUI.json')

            self.gui_opt['text_font'] = font.Font(**self.gui_opt['font'])
            self.gui_opt['text_config'] = {
                'bg': self.gui_opt['bg_general'],
                'font': self.gui_opt['text_font']
            }
            self.gui_opt['button_config'] = {
                'bg': self.gui_opt['bg_button'],
                'font': self.gui_opt['text_font']
            }
            self.gui_opt['combobox_config'] = {
                'state': 'readonly',
                'font': self.gui_opt['text_font']
            }
            self.gui_opt['visualizer_config'] = {
                'bg': self.gui_opt['bg_visualizer'],
                'bd': 1,
                'relief': 'solid',
                'height': self.gui_opt['dim_visualizer'],
                'width': self.gui_opt['dim_visualizer']
            }

        return self.gui_opt

    def get_fonts(self):
        if not self.fonts:
            for i in font.families():
                try:
                    ImageFont.truetype(i, size=12)
                    self.fonts.append(i)
                except:
                    pass

        return self.fonts

    @staticmethod
    def save_json(path: str, data: dict | list, mode='w'):
        with open(path, mode) as outfile:
            json.dump(
                data,
                outfile,
                sort_keys=False,
                indent=4
            )

    @staticmethod
    def read_json(path):
        file = open(path)
        content = json.load(file)
        file.close()
        return content
