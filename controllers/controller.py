import logging
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
    PrintImgController,
    PrintHandController,
    PrintTextController
):

    def __init__(self, model, view):
        logging.debug(f"Controller")
        self.model = model
        self.view = view
        self.serial_port = None

        self.model.setup(self)
        self.view.setup(self)

        for controller in (MenuController, CalibrationController, ConfigController, PrintImgController, PrintHandController, PrintTextController):
            controller.__init__(self)
            try:
                controller.setup(self)
            except:
                pass

    def start(self):
        logging.debug(f"Controller")
        if self.model.locale:
            self.view.set_locale(self.model.locale)
            self.view.show_frame('InfoFrame')
        else:
            self.view.show_frame('LangView')
        self.view.start_main_loop()

    def get_gui_opt(self):
        logging.debug(f"Controller")
        return self.model.get_gui_opt()

    def get_locale(self):
        logging.debug(f"Controller")
        return self.model.get_locale()

    def change_locale(self, lang):
        logging.debug(f"Controller:{lang}")
        locale = self.model.get_locale(lang)
        self.set_calibration_params_gui(self.get_calibration_params())
        self.view.set_locale(locale)
        self.view.show_frame('InfoFrame')
