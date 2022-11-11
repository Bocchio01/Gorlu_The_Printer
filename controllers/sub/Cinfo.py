import logging

from views.sub.Vinfo import InfoView
from controllers.Cabstraction import ControllerABC, InfoControllerABC


class InfoController(InfoControllerABC):
    def __init__(self, controller: ControllerABC):
        logging.debug(f"InfoController")
        self.root = controller.root
        self.model = controller.model

        self.view = InfoView(
            self.root,
            self.model.get_locale()['InfoFrame'],
            self.model.get_gui_opt()
        )
