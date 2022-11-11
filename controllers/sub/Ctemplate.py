import logging

from views.sub.Vtemplate import TemplateView
from controllers.Cabstraction import ControllerABC


class TemplateController:
    def __init__(self, controller: ControllerABC):
        logging.debug(f"TemplateController")
        self.root = controller.root
        self.model = controller.model

        self.view = TemplateView(
            self.root,
            self.model.get_locale()['TemplateFrame'],
            self.model.get_gui_opt()
        )
