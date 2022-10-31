import logging
from threading import Thread

from commons.menu import MenuController

from commons.config import ConfigController
from commons.calibration import CalibrationController
from commons.printimg import PrintImgController
from commons.printhand import PrintHandController
from commons.printtext import PrintTextController


class Controller(
    MenuController,
    CalibrationController,
    ConfigController,
    PrintImgController
):

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.serial_port = None

        self.model.setup(self)
        self.view.setup(self)

        for controller in (MenuController, CalibrationController, ConfigController, PrintImgController):
            controller.__init__(self)
            try:
                controller.setup(self)
            except:
                pass

    def start(self):
        self.view.start_main_loop()

    def get_gui_opt(self):
        return self.model.get_gui_opt()

    def get_locale(self):
        return self.model.locale

    def set_locale(self, lang):
        logging.debug(f"")
        logging.debug(lang)
        self.view.set_locale(self.model.get_locale(lang))

    def savePosn(self):
        pass

    def addLine(self):
        pass

    def fontChanged(self):
        pass
