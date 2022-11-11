import logging

from tkinter.messagebox import showinfo
from controllers.Cabstraction import ControllerABC, CalibrationControllerABC
from views.sub.Vcalibration import CalibrationFrame


class CalibrationController(CalibrationControllerABC):
    def __init__(self, controller: ControllerABC):
        logging.debug(f"CalibrationController")
        self.root = controller.root
        self.model = controller.model

        self.view = CalibrationFrame(
            self.root,
            self.model.get_locale()['CalibrationFrame'],
            self.model.get_gui_opt()
        )

        self.model.CalibrationModel.calibration_params.addCallback(
            self.set_calibration_params_gui
        )

        self.view.setting_load.config(
            command=self.set_calibration_params
        )

        self.model.CalibrationModel.get_calibration_params()

    def set_calibration_params_gui(self, params):
        logging.debug(f"CalibrationController")
        logging.debug(f"{params}")
        locale = self.model.get_locale()
        if locale:
            params = {**params}
            params['X'] = (
                locale['direction_'][0]
                if params['X'] == 1 else
                locale['direction_'][1]
            )
            params['Y'] = (
                locale['direction_'][0]
                if params['Y'] == 1 else
                locale['direction_'][1]
            )
            self.view.set_calibration_params(params)

    def set_calibration_params(self):
        logging.debug(f"CalibrationController")
        data = {
            'UP': self.view.servo_max.get(),
            'DOWN': self.view.servo_min.get(),
            'X': self.view.setting_direction_X.get(),
            'Y': self.view.setting_direction_Y.get()
        }

        try:
            params = self.model.CalibrationModel.set_calibration_params(data)
            self.set_calibration_params_gui(params)
            self.test_plotter()
        except:
            showinfo(
                title=self.model.locale['error_msg'][0],
                message=self.model.locale['set_calibration_params_'][1]
            )

    def test_plotter(self):
        logging.debug(f"CalibrationController")
        # try:
        #     self.serial_port.open()
        # except:
        #     try:
        #         self.serial_port.close()
        #         self.serial_port.open()
        #     except:
        #         self.view.prompt_message({
        #             'title': self.model.locale['error_msg'][0],
        #             'message': self.model.locale['set_calibration_params_'][1]
        #         })
        #         return False

        # time.sleep(2)
        # self.serial_port.write(
        #     f'{self.model.calibration_params["UP"]} {self.model.calibration_params["DOWN"]}'.encode('utf-8'))

        # for j in range(1, 5):
        #     for i in range(1, -1, -1):
        #         s = ('D' if ((i+j) % 2) == 0 else 'U')
        #         self.arduino_sender(
        #             s, self.model.calibration_params["X"] * j * 30 * i, self.model.calibration_params["Y"] * j * 30 * i)
        #         time.sleep(0.5)
