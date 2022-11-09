import logging
from commons.menu import MenuController

from commons.lang import LangController
from commons.config import ConfigController
from commons.calibration import CalibrationController
from commons.printimg import PrintImgController
from commons.printhand import PrintHandController
from commons.printtext import PrintTextController


class Controller(
    MenuController,
    LangController,
    CalibrationController,
    ConfigController,
    PrintImgController,
    PrintHandController,
    PrintTextController
):

    def __init__(self, view, model):
        logging.debug(f"Controller")
        self.view = view
        self.model = model

        self.model.setup(self)
        self.view.setup(self)

        for controller in (MenuController, LangController, CalibrationController, ConfigController, PrintImgController, PrintHandController, PrintTextController):
            controller.__init__(self)

    def start(self):
        logging.debug(f"Controller")
        self.view.start_main_loop()

    def get_gui_opt(self):
        logging.debug(f"Controller")
        return self.model.get_gui_opt()
