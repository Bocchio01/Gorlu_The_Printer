import logging
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

from tkinter.messagebox import showinfo
import time


class CalibrationFrame(tk.Frame):
    def __init__(self, parent, controller, gui_opt):
        self.gui_opt = gui_opt
        self.controller = controller
        # -------------------------------
        # calibration_frame
        self.servo_max = tk.IntVar()
        self.servo_min = tk.IntVar()
        tk.Frame.__init__(self, parent, bg=gui_opt['bg_general'])

        self.setting_frame = tk.Frame(self, bg=gui_opt['bg_general'])
        self.setting_text_0 = tk.Label(
            self.setting_frame,
            **gui_opt['text_config']
        )
        self.setting_text_1 = tk.Label(
            self.setting_frame,
            **gui_opt['text_config']
        )
        self.setting_text_2 = tk.Label(
            self.setting_frame,
            **gui_opt['text_config']
        )
        self.setting_text_3 = tk.Label(
            self.setting_frame,
            **gui_opt['text_config']
        )
        self.setting_text_4 = tk.Label(
            self.setting_frame,
            **gui_opt['text_config']
        )
        self.setting_text_5 = tk.Label(
            self.setting_frame,
            **gui_opt['text_config']
        )
        self.setting_text_6 = tk.Label(
            self.setting_frame,
            **gui_opt['text_config']
        )
        self.setting_separator_0 = ttk.Separator(
            self.setting_frame,
            orient=tk.HORIZONTAL
        )
        self.setting_separator_1 = ttk.Separator(
            self.setting_frame,
            orient=tk.HORIZONTAL
        )
        self.setting_servo_max = tk.Entry(
            self.setting_frame,
            textvariable=self.servo_max,
            width=10,
            font=gui_opt['text_font']
        )
        self.setting_servo_min = tk.Entry(
            self.setting_frame,
            textvariable=self.servo_min,
            width=10,
            font=gui_opt['text_font']
        )
        self.setting_direction_X = ttk.Combobox(
            self.setting_frame,
            width=15,
            textvariable=tk.StringVar(),
            **gui_opt['combobox_config']
        )
        self.setting_direction_Y = ttk.Combobox(
            self.setting_frame,
            width=15,
            textvariable=tk.StringVar(),
            **gui_opt['combobox_config']
        )
        self.setting_load = tk.Button(
            self.setting_frame,
            command=lambda: self.controller.set_calibration_params({
                'UP': self.servo_max.get(),
                'DOWN': self.servo_min.get(),
                'X': self.setting_direction_X.get(),
                'Y': self.setting_direction_Y.get()
            }),
            **gui_opt['button_config']
        )

        self.visualizer_frame = tk.Frame(self, bg=gui_opt['bg_visualizer'])
        self.visualizer = tk.Label(
            self.visualizer_frame, **gui_opt['visualizer_config']
        )

        img_calibration = ImageTk.PhotoImage(
            Image.open(r'assets/img/calibration.png')
        )
        self.visualizer.configure(image=img_calibration)
        self.visualizer.image = img_calibration

        # calibration pack/grid
        self.setting_frame.rowconfigure([0, 4, 8, 9], minsize=70)
        self.setting_frame.rowconfigure([1, 2, 5, 6], minsize=20)
        self.setting_frame.rowconfigure([3, 7], minsize=30)
        self.setting_frame.columnconfigure(0, minsize=400)

        self.setting_frame.pack(fill=tk.Y, side=tk.LEFT, pady=50)
        self.setting_text_0.grid(sticky='ns')
        self.setting_text_1.grid(row=1, padx=80, sticky='nsw')
        self.setting_text_2.grid(row=2, padx=80, sticky='nsw')
        self.setting_servo_max.grid(row=1, padx=80, sticky='e')
        self.setting_servo_min.grid(row=2, padx=80, sticky='e')
        self.setting_separator_0.grid(padx=40, sticky='wes')
        self.setting_text_3.grid(sticky='ns')
        self.setting_text_4.grid(row=5, padx=30, sticky='nsw')
        self.setting_text_5.grid(row=6, padx=30, sticky='nsw')
        self.setting_direction_X.grid(row=5, padx=30, sticky='e')
        self.setting_direction_Y.grid(row=6, padx=30, sticky='e')
        self.setting_separator_1.grid(padx=40, sticky='wes')
        self.setting_text_6.grid(sticky='s')
        self.setting_load.grid(sticky='s')
        self.visualizer_frame.pack(fill=tk.BOTH, expand=True)
        self.visualizer.pack(expand=True)

    def set_calibration_params_gui(self, params):
        logging.debug(f"CalibrationView:{params}")
        self.servo_max.set(params['UP'])
        self.servo_min.set(params['DOWN'])
        self.setting_direction_X.set(params['X'])
        self.setting_direction_Y.set(params['Y'])


class CalibrationController():
    def __init__(self) -> None:
        logging.debug(f"CalibrationController")
        pass

    def setup(self):
        logging.debug(f"CalibrationController")
        self.set_calibration_params_gui(self.get_calibration_params())

    def get_calibration_params(self):
        logging.debug(f"CalibrationController")
        return self.model.get_calibration_params()

    def set_calibration_params_gui(self, params):
        logging.debug(f"CalibrationController")
        locale = self.model.get_locale()
        params = {**params}
        params['X'] = (locale['direction_'][0] if params['X']
                       == 1 else locale['direction_'][1])
        params['Y'] = (locale['direction_'][0] if params['Y']
                       == 1 else locale['direction_'][1])
        self.view.set_calibration_params_gui(params)

    def set_calibration_params(self, data: dict):
        logging.debug(f"CalibrationController")
        try:
            params = self.model.set_calibration_params(data)
            self.set_calibration_params_gui(params)
            # self.test_plotter()
        except:
            showinfo(
                title=self.model.locale['error_msg'][0],
                message=self.model.locale['set_calibration_params_'][1]
            )

    def test_plotter(self):
        logging.debug(f"CalibrationController")
        try:
            self.serial_port.open()
        except:
            try:
                self.serial_port.close()
                self.serial_port.open()
            except:
                self.view.prompt_message({
                    'title': self.model.locale['error_msg'][0],
                    'message': self.model.locale['set_calibration_params_'][1]
                })
                return False

        time.sleep(2)
        self.serial_port.write(
            f'{self.model.calibration_params["UP"]} {self.model.calibration_params["DOWN"]}'.encode('utf-8'))

        for j in range(1, 5):
            for i in range(1, -1, -1):
                s = ('D' if ((i+j) % 2) == 0 else 'U')
                self.arduino_sender(
                    s, self.model.calibration_params["X"] * j * 30 * i, self.model.calibration_params["Y"] * j * 30 * i)
                time.sleep(0.5)


class CalibrationModel:
    def __init__(self) -> None:
        logging.debug(f"CalibrationModel")
        self.calibration_params = {}

        self.DEFAULT_CALIBRATION_PARAMS = {
            'UP': 155,
            'DOWN': 129,
            'X': 1,
            'Y': 1
        }

    def get_calibration_params(self):
        logging.debug(f"CalibrationModel")
        if not self.calibration_params:
            try:
                self.calibration_params = self.read_json(
                    r'assets/config/plotter.json'
                )
            except:
                self.calibration_params = self.DEFAULT_CALIBRATION_PARAMS

        return self.calibration_params

    def set_calibration_params(self, data):
        logging.debug(f"CalibrationModel:{data}")
        if (
            (data['UP'] < 180) and (data['DOWN'] < 180) and
            (data['UP'] > 0) and (data['DOWN'] > 0)
        ):
            data['X'] = (1 if data['X'] ==
                         self.locale['direction_'][0] else -1)
            data['Y'] = (1 if data['Y'] ==
                         self.locale['direction_'][0] else -1)
            self.calibration_params = data
            self.save_json(
                r'assets/config/plotter.json',
                self.calibration_params
            )
        else:
            raise ValueError("Errore nei dati inseriti")
        return self.calibration_params
