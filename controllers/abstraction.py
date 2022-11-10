from abc import ABC, abstractmethod
import tkinter as tk

from models.abstraction import ModelABC


class ControllerABC(ABC):

    @abstractmethod
    def __init__(self, root: tk.Tk, model: ModelABC):
        self.root = root
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def get_gui_opt(self):
        pass
