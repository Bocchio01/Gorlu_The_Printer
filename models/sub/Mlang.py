import logging

from models.Mabstraction import ModelABC, LangModelABC


class LangModel(LangModelABC):
    def __init__(self, parent: ModelABC):
        self.parent = parent

    def change_locale(self, target):
        logging.debug(f"LangModel:targt:{target}")

        settings = self.parent.settings.get()
        settings['locale'] = target

        self.parent.settings.set(settings)

        logging.info(f"Reload app to effectively change the languages")
