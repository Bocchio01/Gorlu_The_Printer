import logging
import tkinter as tk
from tkinter import ttk

from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfilename
import serial

import serial.tools.list_ports


class ConfigFrame(tk.Frame):
    def __init__(self, parent, controller, gui_opt):
        self.gui_opt = gui_opt
        self.controller = controller
        tk.Frame.__init__(self, parent, bg=gui_opt['bg_general'])

        self.text_0 = tk.Label(self, **gui_opt['text_config'])
        self.text_1 = tk.Label(self, **gui_opt['text_config'])
        self.text_2 = tk.Label(self, **gui_opt['text_config'])

        self.COM = ttk.Combobox(
            self,
            textvariable=tk.StringVar(),
            **gui_opt['combobox_config']
        )
        self.COM['font'] = ('calibri', 20)

        self.separator_0 = ttk.Separator(self, orient=tk.HORIZONTAL)
        self.separator_1 = ttk.Separator(self, orient=tk.HORIZONTAL)

        self.save_arduino_code = tk.Button(
            self, command=lambda: self.controller.save_arduino_code(),
            **gui_opt['button_config']
        )
        self.code_frame = tk.Frame(self)
        self.arduino_code = tk.Text(
            self.code_frame,
            height=12,
            width=70
        )
        self.arduino_scroll = ttk.Scrollbar(
            self.code_frame,
            orient=tk.VERTICAL,
            command=self.arduino_code.yview
        )
        self.arduino_code['yscrollcommand'] = self.arduino_scroll.set

        self.text_0.pack(pady=8)
        self.COM.pack(pady=5)
        self.separator_0.pack(fill=tk.X, padx=200, pady=15)
        self.text_1.pack()
        self.separator_1.pack(fill=tk.X, padx=200, pady=15)
        self.text_2.pack(pady=5)
        self.code_frame.pack(pady=10)
        self.arduino_code.grid(column=0, row=0, sticky='we')
        self.arduino_scroll.grid(column=1, row=0, sticky='ns')
        self.save_arduino_code.pack(pady=10)

        self.COM.bind(
            '<<ComboboxSelected>>',
            lambda e: self.controller.check_COM_port(self.COM.get())
        )

    def set_COM_ports_gui(self, ports):
        self.COM['values'] = ports

    def set_arduino_code_gui(self, arduino_code):
        self.arduino_code.insert('1.0', arduino_code)


class ConfigController:
    def __init__(self):
        logging.debug(f"ConfigController")
        COM_ports = self.model.get_COM_ports()
        self.set_COM_ports_gui(COM_ports)

        arduino_code = self.model.load_arduino_code()
        self.set_arduino_code_gui(arduino_code)

    def set_COM_ports_gui(self, ports):
        logging.debug(f"ConfigController")
        self.view.frames[ConfigFrame].set_COM_ports_gui(ports)

    def set_arduino_code_gui(self, arduino_code):
        logging.debug(f"ConfigController")
        self.view.frames[ConfigFrame].set_arduino_code_gui(arduino_code)

    def save_arduino_code(self):
        logging.debug(f"ConfigController")
        self.model.save_arduino_code()

    def check_COM_port(self, port):
        logging.debug(f"ConfigController")
        try:
            self.model.serial_port.close()
        except:
            pass
        try:
            self.model.serial_port = serial.Serial(port, 9600, timeout=1)
            self.view.prompt_message({
                'title': self.model.locale['set_COM_port'][0],
                'message': self.model.locale['set_COM_port'][1]
            })
        except:
            self.view.prompt_message({
                'title': self.model.locale['set_COM_port'][0],
                'message': self.model.locale['set_COM_port'][2]
            })


class ConfigModel:
    def __init__(self):
        logging.debug(f"ConfigModel")
        self.COM_ports = []
        self.arduino_code = ''
        self.serial_port = None

    def get_COM_ports(self):
        logging.debug(f"ConfigModel")
        for port in list(serial.tools.list_ports.comports()):
            self.COM_ports.append(port.device)

        if len(self.COM_ports) is 0:
            self.COM_ports = [f"COM{i}" for i in range(1, 11)]

        return self.COM_ports

    def get_arduino_code(self):
        logging.debug(f"ConfigModel")
        return self.arduino_code

    def load_arduino_code(self):
        logging.debug(f"ConfigModel")
        file = open(r'Arduino_code/Arduino_code.ino', 'r')
        self.arduino_code = file.read()
        file.close()

        return self.arduino_code

    def save_arduino_code(self):
        logging.debug(f"ConfigModel")
        filepath = asksaveasfilename(
            title=self.locale['save_arduino_code'][0],
            initialfile=self.locale['save_arduino_code'][1],
            defaultextension="ino",
            filetypes=[
                ("Arduino code", "*.ino"),
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )

        if not filepath:
            return
        with open(filepath, 'w') as output_file:
            output_file.write(self.get_arduino_code())


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
