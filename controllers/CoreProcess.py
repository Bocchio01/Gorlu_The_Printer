import logging

from models.observable import Observable
from controllers.Cabstraction import ControllerABC
import cv2
import time
import numpy as np


class CoreProcess:
    def __init__(self, controller: ControllerABC):
        logging.debug(f"CoreProcess")
        self.root = controller.root
        self.model = controller.model

        self.delta_Y: int = 0
        self.delta_X: int = 0
        self.user_stop = Observable(False)

        self.progress = Observable(0)
        self.black_pixel = 0
        self.cont = 0

    def process_img(self):
        img_work = self.model.PrintImgModel.img_global.get()
        quality: int = self.model.PrintImgModel.quality.get()
        filling: int = self.model.PrintImgModel.filling.get()
        height, width = img_work.shape[:2]
        dim_visualizer = self.model.get_gui_opt()['dim_visualizer']

        self.delta_Y, self.delta_X = (
            ((dim_visualizer - round(height*dim_visualizer/width)), 0)
            if (width > height) else
            (0, (dim_visualizer - round(width*dim_visualizer/height)))
        )

        img_work = cv2.resize(
            img_work,
            (
                dim_visualizer-self.delta_X,
                dim_visualizer-self.delta_Y
            )
        )

        img_work = (
            cv2.bitwise_not(cv2.Canny(img_work, quality, quality))
            if not filling else
            cv2.threshold(
                cv2.cvtColor(img_work, cv2.COLOR_BGR2GRAY),
                quality / 2,
                255,
                cv2.THRESH_BINARY
            )[1]
        )

        self.model.PrintImgModel.img_to_view.set(img_work)

    def print_img(self):
        logging.debug(f"PrintImgController")

        img_to_print = self.model.PrintImgModel.img_to_view.get()

        dim_visualizer = self.model.get_gui_opt()['dim_visualizer']

        self.black_pixel = np.sum(img_to_print == 0)
        X, Y, self.cont = 0, 0, 0
        while not img_to_print.all() and not self.user_stop.get():
            i, self.cont = 0, self.cont + 1
            while True:
                i += 1
                try:
                    y = np.where(
                        img_to_print[
                            max(0, Y-i): Y+i+1,
                            max(0, X-i): X+i+1
                        ] == 0)[0][0]

                    x = np.where(
                        img_to_print[
                            max(0, Y-i): Y+i+1,
                            max(0, X-i): X+i+1
                        ] == 0)[1][0]

                    X, Y = x + max(0, X-i), y + max(0, Y-i)
                    img_to_print[Y][X] = 255
                    break
                except:
                    pass
            if self.arduino_sender(
                ('U' if (i > 2) else 'D'),
                (X + self.delta_X/2)*250/dim_visualizer,
                (Y + self.delta_Y/2)*250/dim_visualizer
            ) == False:
                self.user_stop.set(True)
                break
            time.sleep(0.01)

            self.progress.set(round(self.cont*100/self.black_pixel)),

    def arduino_sender(self, pen: str, X: int | float, Y: int | float):
        # logging.debug(f"PrintImgController:{pen}:{X}:{Y}")
        return True

    def arduino_sender(self, pen: str, X: int | float, Y: int | float):
        logging.debug(f"PrintImgController:{pen}:{X}:{Y}")
        calibration_params = self.model.CalibrationModel.get_calibration_params()

        line = (
            f"{pen} {round(int(calibration_params['X']) * X)} {round(int(calibration_params['Y']) * Y)}\n")
        if not calibration_params:
            self.root.prompt_message({
                'title': self.model.get_locale()['error_msg'][0],
                'message': self.model.get_locale()['error_msg'][2]
            })

            return False
        try:
            self.model.ConfigModel.serial_port.write(line.encode('utf-8'))
        except:
            self.root.prompt_message({
                'title': self.model.get_locale()['error_msg'][0],
                'message': self.model.get_locale()['error_msg'][1]
            })

            return False
        if (line[0] == 'U'):
            while self.model.ConfigModel.serial_port.read() != str.encode('A'):
                continue
