import logging

import serial

import serial.tools.list_ports

from views.sub.Vconfig import ConfigView
from controllers.Cabstraction import ControllerABC, ConfigControllerABC


class ConfigController(ConfigControllerABC):
    def __init__(self, controller: ControllerABC):
        logging.debug(f"ConfigController")
        self.root = controller.root
        self.model = controller.model

        self.view = ConfigView(
            self.root,
            self.model.get_locale()['ConfigFrame'],
            self.model.get_gui_opt()
        )

        self.model.ConfigModel.com_ports.addCallback(
            self.view.set_COM_ports
        )
        self.model.ConfigModel.arduino_code.addCallback(
            self.view.set_arduino_code
        )

        self.view.save_arduino_code.config(
            command=self.model.ConfigModel.save_arduino_code
        )

        self.view.COM.bind(
            '<<ComboboxSelected>>',
            lambda e: self.check_COM_port(self.view.COM.get())
        )

        self.model.ConfigModel.get_COM_ports()
        self.model.ConfigModel.get_arduino_code()

    def check_COM_port(self, port):
        logging.debug(f"ConfigController")
        # try:
        #     self.model.serial_port.close()
        # except:
        #     pass
        # try:
        #     self.model.serial_port = serial.Serial(
        #         port, 9600, timeout=1)
        #     self.view.prompt_message({
        #         'title': self.model.locale['set_COM_port'][0],
        #         'message': self.model.locale['set_COM_port'][1]
        #     })
        # except:
        #     self.view.prompt_message({
        #         'title': self.model.locale['set_COM_port'][0],
        #         'message': self.model.locale['set_COM_port'][2]
        #     })
