import logging

from threading import Thread

from views.sub.Vprintimg import PrintImgView
from controllers.Cabstraction import ControllerABC

import time
from PIL import ImageTk, Image

import numpy as np
import cv2


class PrintImgController:
    def __init__(self, controller: ControllerABC):
        logging.debug(f"PrintImgController")
        self.root = controller.root
        self.model = controller.model

        self.view = PrintImgView(
            self.root,
            self.model.get_locale()['PrintImgFrame'],
            self.model.get_gui_opt()
        )

        self.model.PrintImgModel.filling.addCallback(
            self.view.filling.set
        )
        self.model.PrintImgModel.filling.addCallback(
            lambda e: self.process_img()
        )

        self.model.PrintImgModel.quality.addCallback(
            self.view.setting_quality.set
        )
        self.model.PrintImgModel.quality.addCallback(
            lambda e: self.process_img()
        )

        self.view.setting_selection.config(
            command=self.model.PrintImgModel.open_img
        )

        self.view.setting_quality.config(
            command=lambda e: self.model.PrintImgModel.quality.set(
                self.view.setting_quality.get()
            )
        )

        self.view.setting_filling.config(
            command=lambda: self.model.PrintImgModel.filling.set(
                self.view.filling.get()
            )
        )

        self.view.setting_go.config(
            command=lambda: self.start_thread
        )

    def process_img(self, print_go=0):
        logging.debug(f"PrintImgController:{print_go}")
        img_work = self.model.PrintImgModel.img_global.get()
        quality = self.model.PrintImgModel.quality.get()
        filling = self.model.PrintImgModel.filling.get()
        height, width = img_work.shape[:2]
        dim_visualizer = self.model.get_gui_opt()['dim_visualizer']

        delta_Y, delta_X = (
            ((dim_visualizer - round(height*dim_visualizer/width)), 0)
            if (width > height) else
            (0, (dim_visualizer - round(width*dim_visualizer/height)))
        )

        img_work = cv2.resize(
            img_work,
            (
                dim_visualizer-delta_X,
                dim_visualizer-delta_Y
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

        self.model.PrintImgModel.img_global.set(img_work)
        self.view.set_img(img_work)

    def start_thread(self):
        logging.debug(f"PrintImgController")
        Thread(target=self.print_img()).start()

    def print_img(self):
        logging.debug(f"PrintImgController")
        # ask 'process_img()' to get initial parameters
        # while all 'img_to_print' is not white, he continusly looks for next black pixel nearest from the previous one found
        # he uses slicing technique for 2D array to find black pixel position
        # by 'arduino_sender()' he send pen_position and coordinates to serial port
        self.user_stop = False
        self.view.create_windows()

        img_to_print, delta_X, delta_Y = self.process_img(1)
        calibration_params = self.model.CalibrationModel.get_calibration_params()
        dim_visualizer = self.model.get_gui_opt()['dim_visualizer']

        black_pixel = np.sum(img_to_print == 0)
        X, Y, cont = 0, 0, 0
        while not img_to_print.all() and not self.user_stop:
            i, cont = 0, cont + 1
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
                round(int(calibration_params['X']) *
                      (X + delta_X/2)*250/dim_visualizer),
                round(int(calibration_params['Y']) *
                      (Y + delta_Y/2)*250/dim_visualizer)
            ) == False:
                self.user_stop = True
                break
            time.sleep(0.01)

            self.view.update_progress_bar({
                'progress': round(cont*100/black_pixel),
                'label': self.model.get_locale()['sub_windows_'][1] % (cont, black_pixel, str(round(cont*100/black_pixel))+' %')
            })
        try:
            self.arduino_sender('U', 0, 0)
            self.view.destroy_windows()
        except:
            pass

    def stop_print(self):
        logging.debug(f"PrintImgController")
        self.user_stop = True
        self.arduino_sender('U', 0, 0)
        self.view.destroy_windows()
        # self.user_stop = False

    def arduino_sender(self, pen, X, Y):
        logging.debug(f"PrintImgController:{pen}:{X}:{Y}")
        return True

    def arduino_sender1(self, pen, X, Y):
        logging.debug(f"PrintImgController:{pen}:{X}:{Y}")
        # he send data array = (pen_position, coordinate_point_X, coordinate_point_Y)
        # if pen_position is up, he wait for positive response ('A') from the board
        # if serial fails, return False
        calib_check = self.model.CalibrationModel.get_calibration_params()
        line = (f"{pen} {X} {Y}\n")
        if not calib_check:
            self.view.prompt_message({
                'title': self.model.get_locale()['error_msg'][0],
                'message': self.model.get_locale()['error_msg'][2]
            })

            return False
        try:
            self.serial_port.write(line.encode('utf-8'))
        except:
            self.view.prompt_message({
                'title': self.model.get_locale()['error_msg'][0],
                'message': self.model.get_locale()['error_msg'][1]
            })

            return False
        if (line[0] == 'U'):
            while self.serial_port.read() != str.encode('A'):
                continue
