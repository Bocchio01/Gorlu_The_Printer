import json
import logging
from tkinter import font
from commons.lang import LangModel
from commons.config import ConfigModel
from commons.calibration import CalibrationModel
from commons.printimg import PrintImgModel
from commons.printhand import PrintHandModel
from commons.printtext import PrintTextModel


class Model(
    LangModel,
    ConfigModel,
    CalibrationModel,
    PrintImgModel,
    PrintHandModel,
    PrintTextModel
):

    def __init__(self):
        logging.debug(f"Model")
        self.settings = {}
        self.gui_opt = {}

        self.load_settings()
        self.load_gui_opt()

        for model in (LangModel, ConfigModel, CalibrationModel, PrintImgModel, PrintHandModel, PrintTextModel):
            model.__init__(self)

    def setup(self, controller):
        logging.debug(f"Model")
        self.controller = controller

    def get_settings(self):
        return self.settings

    def load_settings(self):
        self.settings = self.read_json(r"assets/settings.json")
        return self.settings

    def get_gui_opt(self):
        return self.gui_opt

    def load_gui_opt(self):
        logging.debug(f"Model")
        self.gui_opt = {**self.settings['GUI']}
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

    @staticmethod
    def save_json(path: str, data: dict | list, mode='w'):
        logging.debug(f"Model:path:{path}")
        with open(path, mode) as outfile:
            json.dump(
                data,
                outfile,
                sort_keys=False,
                indent=4
            )

    @staticmethod
    def read_json(path):
        logging.debug(f"Model:path:{path}")
        file = open(path)
        content = json.load(file)
        file.close()
        return content
