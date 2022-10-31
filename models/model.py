import json
import logging
from tkinter import font
from commons.config import ConfigModel
from commons.calibration import CalibrationModel
from commons.printimg import PrintImgModel
from commons.printhand import PrintHandModel
from commons.printtext import PrintTextModel


class Model(
    ConfigModel,
    CalibrationModel,
    PrintImgModel,
    PrintHandModel,
    PrintTextModel
):

    def __init__(self):
        logging.debug(f"Model")
        self.locale = {}
        self.gui_opt = {}

        for model in (ConfigModel, CalibrationModel, PrintImgModel, PrintHandModel, PrintTextModel):
            model.__init__(self)

    def setup(self, controller):
        logging.debug(f"Model")
        self.controller = controller
        self.get_calibration_params()
        self.get_gui_opt()
        if self.gui_opt['lang'] in ['it', 'en', 'fr']:
            self.get_locale(self.gui_opt['lang'])
        self.get_fonts()

    def get_locale(self, target: str = None):
        logging.debug(f"Model:target:{target}")
        if (
            target and
            (
                not self.locale or
                self.gui_opt['lang'] is not target
            )
        ):
            self.locale = self.read_json(fr'assets/locale/{target}.json')

            self.gui_opt['lang'] = target
            json = self.read_json(fr'assets/config/GUI.json')
            json['lang'] = self.gui_opt['lang']
            self.save_json(fr'assets/config/GUI.json', json)

        return self.locale

    def get_gui_opt(self):
        logging.debug(f"Model")
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
