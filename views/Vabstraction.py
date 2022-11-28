from abc import ABC, abstractmethod
import tkinter as tk


class ViewABC(ABC, tk.Tk):

    @abstractmethod
    def __init__(self) -> None:
        tk.Tk.__init__(self)

    @abstractmethod
    def open_link(self, link: str) -> None:
        pass

    @abstractmethod
    def show_view(self, view) -> None:
        """
        Display the selected view and unpack all the others.

        :param view: View to be packed as current
        """
        pass

    @abstractmethod
    def prompt_message(self, data: dict) -> None:
        pass

    @abstractmethod
    def start_main_loop(self) -> None:
        """Start the tkinter GUI app"""
        pass
