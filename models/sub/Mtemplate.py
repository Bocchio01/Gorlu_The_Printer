import logging

from models.observable import Observable
from models.Mabstraction import ModelABC


class TemplateModel:
    def __init__(self, parent: ModelABC):
        self.parent = parent
