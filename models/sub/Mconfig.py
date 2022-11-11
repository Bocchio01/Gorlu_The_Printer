import logging

from models.observable import Observable
from models.Mabstraction import ModelABC, ConfigModelABC
import serial.tools.list_ports
from tkinter.filedialog import asksaveasfilename


class ConfigModel(ConfigModelABC):
    def __init__(self, parent: ModelABC):
        self.parent = parent

        self.com_ports = Observable([])
        self.arduino_code = Observable('')
        self.serial_port = Observable(None)

    def get_COM_ports(self):
        com_ports = []
        for port in list(serial.tools.list_ports.comports()):
            com_ports.append(port.device)

        if len(com_ports) == 0:
            com_ports = [f"COM{i}" for i in range(1, 11)]

        self.com_ports.set(com_ports)
        return self.com_ports.get()

    def get_arduino_code(self):

        if not self.arduino_code.get():
            file = open(r'Arduino_code/Arduino_code.ino', 'r')
            self.arduino_code.set(file.read())
            file.close()

        return self.arduino_code.get()

    def save_arduino_code(self):

        filepath = asksaveasfilename(
            title=self.parent.locale.get()['save_arduino_code'][0],
            initialfile=self.parent.locale.get()['save_arduino_code'][1],
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
            output_file.write(self.arduino_code.get())
