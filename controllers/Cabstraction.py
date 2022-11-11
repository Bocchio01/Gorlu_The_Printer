from abc import ABC, abstractmethod

from models.Mabstraction import ModelABC
from views.Vabstraction import ViewABC


class ControllerABC(ABC):
    @abstractmethod
    def __init__(self, root: ViewABC, model: ModelABC):
        self.root = root
        self.model = model

    @abstractmethod
    def start(self):
        pass


class InfoControllerABC(ABC):
    @abstractmethod
    def __init__(self, controller: ControllerABC) -> None:
        pass


class LangControllerABC(ABC):
    @abstractmethod
    def __init__(self, controller: ControllerABC) -> None:
        pass


class ConfigControllerABC(ABC):
    @abstractmethod
    def __init__(self, controller: ControllerABC) -> None:
        pass

    @abstractmethod
    def check_COM_port(self, port: str = None) -> None:
        """Check for selected port"""
        pass


class CalibrationControllerABC(ABC):
    @abstractmethod
    def __init__(self, controller: ControllerABC) -> None:
        pass

    @abstractmethod
    def set_calibration_params_gui(self, params: dict) -> None:
        pass

    @abstractmethod
    def set_calibration_params(self) -> None:
        pass

    @abstractmethod
    def test_plotter(self) -> None:
        pass
