from abc import ABC, abstractmethod
import tkinter as tk


class ViewABC(ABC, tk.Tk):

    @abstractmethod
    def __init__(self) -> None:
        tk.Tk.__init__(self)

    @abstractmethod
    def show_view(self, view) -> None:
        pass

    @abstractmethod
    def start_main_loop(self) -> None:
        pass
