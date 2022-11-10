from abc import ABC, abstractmethod
from models.observable import Observable

from models.sub.config import ConfigModel
from models.sub.calibration import CalibrationModel


class ModelABC(ABC):

    def __init__(self):
        self.settings = Observable({})
        self.gui_opt = Observable({})
        self.locale = Observable({})

        # Adding as instances all models for the app
        # for cl in submodel:
        #     logging.debug(f"Registering submodel: {cl.__name__}")
        #     self.__dict__[cl.__name__] = cl(self)
        self.ConfigModel: ConfigModel
        self.CalibrationModel: CalibrationModel

    @abstractmethod
    def get_settings(self):
        pass

    @abstractmethod
    def get_gui_opt(self):
        pass

    @staticmethod
    @abstractmethod
    def save_json(data: dict | list, path: str = r"assets/settings.json", mode='w'):
        pass

    @staticmethod
    @abstractmethod
    def read_json(path):
        pass
