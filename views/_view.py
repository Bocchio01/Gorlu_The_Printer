import logging
import tkinter as tk
from tkinter.messagebox import showinfo

from commons.lang import LangView
from commons.info import InfoFrame
from commons.config import ConfigFrame
from commons.calibration import CalibrationFrame
from commons.printimg import PrintImgFrame
from commons.printhand import PrintHandFrame
from commons.printtext import PrintTextFrame

from commons.printimg import PrintImgSubWindows
from commons.menu import MenuView


subviews = {
    # InfoFrame,
    ConfigFrame,
    CalibrationFrame,
    # PrintImgFrame,
    # PrintHandFrame,
    # PrintTextFrame,
    # LangView,
}


class View:
    def __init__(self):
        logging.debug(f"View")
        self.root = tk.Tk()
        self.root.geometry('1000x600')

    def setup(self, controller):
        logging.debug(f"View")
        self.controller = controller
        self.gui_opt = self.controller.get_gui_opt()

        self.registersubviews(subviews)

        self.menu = MenuView(self.root, self, self.controller)

    def registersubviews(self, views: list) -> None:
        """Adding as instances all views for the app"""

        for cl in views:
            logging.debug(f"Registering subviews: {cl.__name__}")
            self.__dict__[cl.__name__] = cl(
                self.root,
                self.controller,
                self.gui_opt
            )

    def show_frame(self, target_frame):
        logging.debug(f"Target:{target_frame}")

        if type(target_frame) is str:
            target_frame = self.DICT[target_frame]

        for i in self.frames:
            self.frames[i].pack_forget()

        frame = self.frames[target_frame]
        frame.pack(fill=tk.BOTH, expand=True)

    def set_locale(self, locale):
        logging.debug(f"View")

        self.root.title(locale['windows_'])
        self.menu.set_locale(locale)

        for frame in self.frames:
            cl = self.frames[frame]
            members = [
                attr
                for attr in dir(cl)
                if not callable(getattr(cl, attr))
                and not attr.startswith("_")
            ]
            for member in members:
                try:
                    cl.__dict__[member].config(
                        text=locale[cl.__class__.__name__][member]
                    )
                except:
                    pass

        self.frames[CalibrationFrame].setting_direction_X.config(
            value=(locale['direction_']))
        self.frames[CalibrationFrame].setting_direction_Y.config(
            value=(locale['direction_']))
        self.frames[PrintTextFrame].setting_align_o.config(
            value=locale['align_o'])
        self.frames[PrintTextFrame].setting_align_v.config(
            value=locale['align_v'])

        self.frames[PrintTextFrame].setting_align_o.set(locale['align_o'][1])
        self.frames[PrintTextFrame].setting_align_v.set(locale['align_v'][1])

        self.root.config(menu=self.menu)

    def create_windows(self):
        logging.debug(f"View")
        self.subwindows = PrintImgSubWindows(self.controller, self.gui_opt)

    def update_progress_bar(self, data):
        logging.debug(f"View")
        self.subwindows.update_progress_bar(data)

    def destroy_windows(self):
        logging.debug(f"View")
        self.subwindows.destroy_windows()

    def prompt_message(self, data: dict):
        logging.debug(f"View")
        showinfo(
            title=data['title'],
            message=data['message']
        )

    def start_main_loop(self):
        logging.debug(f"View")
        self.root.mainloop()
