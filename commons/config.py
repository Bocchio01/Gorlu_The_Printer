import logging
import tkinter as tk
from tkinter import ttk

from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfilename
import serial

import serial.tools.list_ports


class ConfigController:
    def __init__(self, parent):
        logging.debug(f"ConfigController")
        self.parent = parent

        COM_ports = self.parent.model.ConfigModel.get_COM_ports()
        self.set_COM_ports_gui(COM_ports)

        arduino_code = self.parent.model.ConfigModel.load_arduino_code()
        self.set_arduino_code_gui(arduino_code)

    def set_COM_ports_gui(self, ports):
        logging.debug(f"ConfigController")
        self.parent.view.ConfigFrame.set_COM_ports_gui(ports)

    def set_arduino_code_gui(self, arduino_code):
        logging.debug(f"ConfigController")
        self.parent.view.ConfigFrame.set_arduino_code_gui(arduino_code)

    def save_arduino_code(self):
        logging.debug(f"ConfigController")
        self.parent.model.ConfigModel.save_arduino_code()

    def check_COM_port(self, port):
        logging.debug(f"ConfigController")
        try:
            self.parent.model.serial_port.close()
        except:
            pass
        try:
            self.parent.model.serial_port = serial.Serial(
                port, 9600, timeout=1)
            self.parent.view.prompt_message({
                'title': self.parent.model.locale['set_COM_port'][0],
                'message': self.parent.model.locale['set_COM_port'][1]
            })
        except:
            self.parent.view.prompt_message({
                'title': self.parent.model.locale['set_COM_port'][0],
                'message': self.parent.model.locale['set_COM_port'][2]
            })


# if __name__ == "__main__":
#     from ..models.model import Model
#     root = tk.Tk()
#     c = ConfigController
#     c.__main__(
#         ConfigModel,
#         ConfigFrame(root, c,
#                     Model.get_gui_opt
#                     )
#     )
#     root.mainloop()
