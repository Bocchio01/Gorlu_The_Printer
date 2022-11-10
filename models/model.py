import json
import logging
from tkinter import font


from .sub.config import ConfigModel
from .sub.calibration import CalibrationModel

from .observable import Observable
from .abstraction import ModelABC


class Model(ModelABC):

    def __init__(self):
        logging.debug(f"Model")
        self.settings = Observable({})
        self.settings.addCallback(self.save_json)

        self.gui_opt = Observable({})
        self.locale = Observable({})

        # self.get_settings()
        # self.load_gui_opt()

        # Adding as instances all models for the app
        # for cl in submodel:
        #     logging.debug(f"Registering submodel: {cl.__name__}")
        #     self.__dict__[cl.__name__] = cl(self)
        self.ConfigModel = ConfigModel(self)
        self.CalibrationModel = CalibrationModel(self)

    def get_settings(self) -> dict:
        """
        Get the overall app settings from external file or from the Observer if already loaded.
        The external file is a json containing:
            - calibration
            - locale
            - GUI
            - fonts
        """
        logging.debug(f"Model")
        if not self.settings.get():
            file = self.read_json(r"assets/settings.json")
            self.settings.set(file)

        return self.settings.get()

    def get_locale(self) -> dict:
        """
        Read from settings the value for the locale and set te variable reading from the correct json locale file.

        If the 'locale' isn't set yet, open by default the 'en-locale'
        """
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

    def get_gui_opt(self) -> dict:
        """
        Compute the options necessary for the GUI, retriving necessary infos from the settings variable.
        """
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

        self.gui_opt.set(opt)

        return self.gui_opt.get()

    @staticmethod
    def save_json(data: dict | list, path: str = r"assets/settings.json", mode='w'):
        """
        Save the input data into a json format file.

        :param data: The dictionary to be saved into the file
        :param path: String containing filepath
        :param mode: possible value 'w' | 'a'
        """
        logging.debug(f"Model:path:{path}")
        with open(path, mode) as outfile:
            json.dump(
                data,
                outfile,
                sort_keys=False,
                indent=4
            )

    @staticmethod
    def read_json(path: str = r"assets/settings.json"):
        """
        Read the content from a json format file.

        :param path: String containing filepath
        """
        logging.debug(f"Model:path:{path}")
        file = open(path)
        content = json.load(file)
        file.close()
        return content
