import logging

from views.sub.Vlang import LangView
from controllers.Cabstraction import ControllerABC, LangControllerABC


class LangController(LangControllerABC):
    def __init__(self, controller: ControllerABC):
        logging.debug(f"LangController")
        self.root = controller.root
        self.model = controller.model

        self.view = LangView(
            self.root,
            {},
            self.model.get_gui_opt()
        )

        # for lang in ['it', 'en', 'fr']:
        self.view.it.button.config(
            command=lambda: self.model.LangModel.change_locale('it')
        )
        self.view.en.button.config(
            command=lambda: self.model.LangModel.change_locale('en')
        )
        self.view.fr.button.config(
            command=lambda: self.model.LangModel.change_locale('fr')
        )
