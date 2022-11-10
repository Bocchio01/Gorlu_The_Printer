import logging

from views.abstraction import ViewABC
from models.abstraction import ModelABC

from controllers.abstraction import ControllerABC

from controllers.sub.config import ConfigController
from controllers.sub.calibration import CalibrationController


class Controller(ControllerABC):

    def __init__(self, root: ViewABC, model: ModelABC):
        logging.debug(f"Controller")
        self.root = root
        self.model = model

        # self.model.setup(self)
        # self.root.setup(self)

        self.Config: ConfigController = ConfigController(self)
        self.Calibration: CalibrationController = CalibrationController(self)

    def start(self):
        logging.debug(f"Controller")
        self.Calibration.view.pack()
        self.root.start_main_loop()

    def get_gui_opt(self):
        logging.debug(f"Controller")
        return self.model.get_gui_opt()
