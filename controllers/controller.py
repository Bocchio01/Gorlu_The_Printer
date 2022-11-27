import logging

from views.Vabstraction import ViewABC
from models.Mabstraction import ModelABC

from controllers.Cabstraction import ControllerABC

from controllers.sub.Clang import LangController
from controllers.sub.Cinfo import InfoController
from controllers.sub.Cconfig import ConfigController
from controllers.sub.Ccalibration import CalibrationController
from controllers.sub.Cprintimg import PrintImgController
from controllers.sub.Cprinthand import PrintHandController


class Controller(ControllerABC):

    def __init__(self, root: ViewABC, model: ModelABC):
        logging.debug(f"Controller")
        self.root = root
        self.model = model

        self.Lang = LangController(self)
        self.Info = InfoController(self)
        self.Config = ConfigController(self)
        self.Calibration = CalibrationController(self)
        self.PrintImg = PrintImgController(self)
        self.PrintHand = PrintHandController(self)

    def start(self):
        logging.debug(f"Controller")
        self.root.add_menu(self, self.model.get_locale()['menu_'])
        self.root.show_view(self.Info.view)
        self.root.start_main_loop()
