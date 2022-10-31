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


class View:
    def __init__(self):
        logging.debug(f"View")
        self.root = tk.Tk()
        self.root.geometry('1000x600')
        self.DICT = {
            'InfoFrame': InfoFrame,
            'ConfigFrame': ConfigFrame,
            'CalibrationFrame': CalibrationFrame,
            'PrintImgFrame': PrintImgFrame,
            'PrintHandFrame': PrintHandFrame,
            'PrintTextFrame': PrintTextFrame,
            'LangView': LangView,
        }

    def setup(self, controller):
        logging.debug(f"View")
        self.controller = controller
        self.gui_opt = self.controller.get_gui_opt()

        self.frames = {}

        for k, v in self.DICT.items():

            frame = v(self.root, self.controller, self.gui_opt)
            frame.config(borderwidth=2, relief='solid')

            self.frames[v] = frame

        self.menu = MenuView(self.root, self, self.controller)

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
        # self.frames[CalibrationFrame].set_calibration_to_gui(calibdata)
        self.root.config(menu=self.menu)

    def set_calibration_params_gui(self, params):
        logging.debug(f"View")
        self.frames[CalibrationFrame].set_calibration_params_gui(params)

    def set_COM_ports_gui(self, ports):
        logging.debug(f"View")
        self.frames[ConfigFrame].set_COM_ports_gui(ports)

    def set_arduino_code_gui(self, arduino_code):
        logging.debug(f"View")
        self.frames[ConfigFrame].set_arduino_code_gui(arduino_code)

    def open_img_gui(self, img_to_display, quality, filling):
        logging.debug(f"View")
        self.frames[PrintImgFrame].open_img_gui(
            img_to_display, quality, filling)

    def create_windows(self):
        logging.debug(f"View")
        self.subwindows = PrintImgSubWindows(self.controller, self.gui_opt)

    def update_progress_bar(self, data):
        logging.debug(f"View")
        self.subwindows.update_progress_bar(data)

    def destroy_windows(self):
        logging.debug(f"View")
        self.subwindows.destroy_windows()

    def create_line(self, lastx, lasty, x, y):
        logging.debug(f"View")
        self.frames[PrintHandFrame].create_line(lastx, lasty, x, y)

    def update_text(self, img):
        logging.debug(f"View")
        self.frames[PrintTextFrame].update_text(img)

    def set_fonts_gui(self, ports):
        logging.debug(f"View")
        self.frames[PrintTextFrame].set_fonts_gui(ports)

    def prompt_message(self, data: dict):
        logging.debug(f"View")
        showinfo(
            title=data['title'],
            message=data['message']
        )

    def start_main_loop(self):
        logging.debug(f"View")
        self.root.mainloop()
