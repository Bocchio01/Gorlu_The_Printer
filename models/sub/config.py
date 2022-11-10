import logging

from models.observable import Observable
import serial.tools.list_ports
from tkinter.filedialog import asksaveasfilename


class ConfigModel:
    def __init__(self, parent):
        self.parent = parent

        self.COM_ports = Observable([])
        self.arduino_code = Observable('')
        self.serial_port = Observable(None)

    def get_COM_ports(self) -> list:
        """Get all avaible COM ports to connect the arduino board."""

        COM_ports = []
        for port in list(serial.tools.list_ports.comports()):
            COM_ports.append(port.device)

        if len(COM_ports) == 0:
            COM_ports = [f"COM{i}" for i in range(1, 11)]

        return self.COM_ports.set(COM_ports)

    def get_arduino_code(self) -> str:
        """Get the arduino code from external file or from the Observer if already loaded."""

        if not self.arduino_code.get():
            file = open(r'Arduino_code/Arduino_code.ino', 'r')
            self.arduino_code.set(file.read())
            file.close()

        return self.arduino_code.get()

    def save_arduino_code(self) -> None:
        """Save the arduino code to a file choosen via default system windows."""

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
