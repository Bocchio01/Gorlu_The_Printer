from abc import ABC, abstractmethod
from models.observable import Observable


class ModelABC(ABC):

    @abstractmethod
    def __init__(self):
        self.settings: Observable
        self.gui_opt: Observable
        self.locale: Observable

        self.LangModel: LangModelABC
        self.ConfigModel: ConfigModelABC
        self.CalibrationModel: CalibrationModelABC
        self.PrintImgModel: PrintImgModelABC
        self.PrintHandModel: PrintHandModelABC
        self.PrintTextModel: PrintTextModelABC

    @abstractmethod
    def get_settings(self) -> dict:
        """
        Get the overall app settings from external file or from the Observer if already loaded.
        The external file is a json containing:
            - calibration
            - locale
            - GUI
            - fonts

        :return dict: complete settings dict
        """
        pass

    @abstractmethod
    def get_locale(self) -> dict:
        """
        Read from settings the value of language tag and set locale with the correct content from external file.

        :return dict: complete current locale dict
        """
        pass

    @abstractmethod
    def get_gui_opt(self) -> dict:
        """
        Read from settings the base and compute the complete dict of options necessary for the GUI.

        :return dict: complete GUI options
        """

        pass

    @staticmethod
    @abstractmethod
    def save_json(data: dict | list, path: str, mode: str) -> None:
        """
        Save data into a json format file.

        :param dict | list data: content to be saved
        :param str path: path of the external file
        :param str mode: opening file mode ('w' | 'a')
        """
        pass

    @staticmethod
    @abstractmethod
    def read_json(path: str) -> dict | list:
        """
        Read and parse the content from a json external file.

        :param str path: path of the external file
        :return dict | list: content of the file
        """
        pass


class LangModelABC(ABC):
    @abstractmethod
    def __init__(self, parent: ModelABC) -> None:
        pass

    @abstractmethod
    def change_locale(self, target: str) -> None:
        """
        Update the settings observer with the new value for locale chosen.

        :param str target: one of the possible language tag
        """
        pass


class ConfigModelABC(ABC):
    @abstractmethod
    def __init__(self, parent: ModelABC) -> None:
        self.com_ports = Observable([])
        self.arduino_code = Observable('')
        self.serial_port = Observable(None)
        pass

    @abstractmethod
    def get_COM_ports(self) -> list[str]:
        """
        Get all avaible COM ports to connect the arduino board.

        :return list[str]: list of possible COM ports available
        """
        pass

    @abstractmethod
    def get_arduino_code(self) -> str:
        """
        Get the arduino code from external file.

        :return str: arduino code
        """
        pass

    @abstractmethod
    def save_arduino_code(self) -> None:
        """
        Save the arduino code to a file choosen via default system windows.
        """
        pass


class CalibrationModelABC(ABC):
    @abstractmethod
    def __init__(self, parent: ModelABC) -> None:
        self.calibration_params = Observable({})
        pass

    @abstractmethod
    def get_calibration_params(self) -> dict:
        """
        Get calibration paramathers from the settings variable.
        If settings are not avaiable, he set a default dict.
        """
        pass

    @abstractmethod
    def set_calibration_params(self, data: dict) -> dict:
        """
        Set calibration paramethers after being modified by user from View.

        Perform a data validation.
        Raise 'ValueError' if data are out of permitted ranges.
        """
        pass


class PrintImgModelABC(ABC):
    @abstractmethod
    def __init__(self, parent: ModelABC):
        self.img_global = Observable(None)
        self.img_to_view = Observable(None)
        self.quality = Observable(100)
        self.filling = Observable(0)
        pass

    @abstractmethod
    def open_img(self):
        """
        Open and set as a cv2.imread() the varible img_global.
        Set to 100 the quality.
        Set to 0 the filling.

        :return np.array: data into the img_global variable
        """


class PrintHandModelABC(ABC):
    @abstractmethod
    def __init__(self, parent: ModelABC):
        self.pen: str = 'U'
        self.lastx = Observable(0)
        self.lasty = Observable(0)
        pass

    @abstractmethod
    def savePosn(self):
        """
        Update the last coordinates taken from the board
        """


class PrintTextModelABC(ABC):
    @abstractmethod
    def __init__(self, parent: ModelABC):
        self.parent = parent
        self.img_text = Observable()
        self.setting_entry = Observable("")
        self.setting_dimension = Observable(30)
        self.setting_character = Observable()
        self.setting_align_o = Observable()
        self.setting_align_v = Observable()
        self.setting_rotation = Observable()

    @abstractmethod
    def update_img(self):
        pass
