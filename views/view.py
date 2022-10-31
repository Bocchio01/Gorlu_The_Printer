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
        self.root = tk.Tk()
        self.root.geometry('1000x600')

    def setup(self, controller):
        self.controller = controller
        self.gui_opt = self.controller.get_gui_opt()

        self.frames = {}

        for frame_name in (LangView, InfoFrame, ConfigFrame, CalibrationFrame, PrintImgFrame, PrintHandFrame, PrintTextFrame):

            frame = frame_name(self.root, self.controller, self.gui_opt)
            frame.config(borderwidth=2, relief='solid')

            self.frames[frame_name] = frame

        self.menu = MenuView(self.root, self, self.controller)

        if not self.gui_opt['lang']:
            self.show_frame(LangView)
        else:
            self.controller.set_locale(self.gui_opt['lang'])
            self.show_frame(InfoFrame)

    def show_frame(self, target_frame):
        for i in self.frames:
            self.frames[i].pack_forget()

        frame = self.frames[target_frame]
        frame.pack(fill=tk.BOTH, expand=True)

    def set_locale(self, locale):
        # self.frames[LangFrame].addLoadingBar(locale['loading_'])

        self.root.title(locale['windows_'])
        self.menu.entryconfigure(1, label=locale['menu_'][0][0])
        self.menu.entryconfigure(2, label=locale['menu_'][1][0])
        self.menu.entryconfigure(3, label=locale['menu_'][2])
        self.menu.entryconfigure(4, label=locale['menu_'][3])
        self.menu.entryconfigure(5, label=locale['menu_'][4])
        self.menu.entryconfigure(6, label=locale['menu_'][5])
        self.menu.entryconfigure(7, label=locale['menu_'][6][0])
        self.menu.info.entryconfigure(0, label=locale['menu_'][0][1])
        self.menu.info.entryconfigure(2, label=locale['menu_'][0][2])
        self.menu.info.entryconfigure(3, label=locale['menu_'][0][3])
        self.menu.config.entryconfigure(0, label=locale['menu_'][1][1])
        self.menu.config.entryconfigure(2, label=locale['menu_'][1][2])

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
        # self.frames[CalibrationFrame].set_calibration_to_gui(calibdata)
        self.root.config(menu=self.menu)

        self.show_frame(InfoFrame)

    def set_calibration_params_gui(self, params):
        self.frames[CalibrationFrame].set_calibration_params_gui(params)

    def set_COM_ports_gui(self, ports):
        self.frames[ConfigFrame].set_COM_ports_gui(ports)

    def set_arduino_code_gui(self, arduino_code):
        self.frames[ConfigFrame].set_arduino_code_gui(arduino_code)

    def open_img_gui(self, img_to_display, quality, filling):
        self.frames[PrintImgFrame].open_img_gui(
            img_to_display, quality, filling)

    def create_windows(self):
        self.subwindows = PrintImgSubWindows(self.controller, self.gui_opt)

    def update_progress_bar(self, data):
        self.subwindows.update_progress_bar(data)

    def destroy_windows(self):
        self.subwindows.destroy_windows()

    def prompt_message(self, data: dict):
        showinfo(
            title=data['title'],
            message=data['message']
        )

    def start_main_loop(self):
        # start the loop
        self.root.mainloop()
