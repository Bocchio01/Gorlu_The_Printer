import logging
from threading import Thread
import time
import tkinter as tk
from tkinter import ttk, font
from PIL import ImageTk, Image

import numpy as np
from tkinter.filedialog import askopenfilename, asksaveasfilename
import cv2


class PrintImgFrame(tk.Frame):
    def __init__(self, parent, controller, gui_opt):
        self.gui_opt = gui_opt
        self.controller = controller
        # ------------------------------
        # printimg_frame
        tk.Frame.__init__(self, parent, bg=gui_opt['bg_general'])

        self.filling = tk.IntVar(value=0)

        self.setting_frame = tk.Frame(self, bg=gui_opt['bg_general'])
        self.setting_text_0 = tk.Label(
            self.setting_frame,
            **gui_opt['text_config']
        )
        self.setting_text_1 = tk.Label(
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
        self.setting_selection = tk.Button(
            self.setting_frame,
            command=lambda: self.controller.open_img(),
            **gui_opt['button_config']
        )
        self.setting_quality = tk.Scale(
            self.setting_frame,
            orient=tk.HORIZONTAL,
            length=300,
            from_=1.0,
            to=500.0,
            command=lambda e: self.controller.change_quality(
                self.setting_quality.get()
            ),
            **gui_opt['button_config']
        )
        self.setting_filling = tk.Checkbutton(
            self.setting_frame,
            variable=self.filling,
            onvalue=1,
            offvalue=0,
            command=lambda: self.controller.change_filling(
                self.filling.get()
            ),
            **gui_opt['text_config']
        )
        self.setting_go = tk.Button(
            self.setting_frame,
            command=lambda: self.controller.start_thread(),
            state=tk.DISABLED,
            **gui_opt['button_config']
        )

        self.setting_go['font'] = ('calibri', 20, font.BOLD)

        self.visualizer_frame = tk.Frame(
            self,
            bg=gui_opt['bg_visualizer']
        )
        self.visualizer = tk.Label(
            self.visualizer_frame,
            **gui_opt['visualizer_config']
        )

        # printimg pack/grid
        self.setting_frame.rowconfigure([0, 3, 4, 7, 8], minsize=70)
        self.setting_frame.rowconfigure([2, 5, 6], minsize=40)
        self.setting_frame.rowconfigure(1, minsize=60)
        self.setting_frame.columnconfigure(0, minsize=400)

        self.setting_frame.pack(fill=tk.Y, side=tk.LEFT, pady=50)
        self.setting_text_0.grid(sticky='ns')
        self.setting_selection.grid(sticky='n')
        self.setting_separator_0.grid(padx=40, sticky='we')
        self.setting_text_1.grid(sticky='ns')
        self.setting_quality.grid(sticky='n')
        self.setting_filling.grid(sticky='wens')
        self.setting_separator_1.grid(padx=40, sticky='we')
        self.setting_go.grid(pady=30, sticky='s')
        self.visualizer_frame.pack(fill=tk.BOTH, expand=True)
        self.visualizer.pack(expand=True)

    def open_img_gui(self, img_to_display, quality, filling):
        logging.debug(f"{img_to_display} {quality} {filling}")
        self.setting_filling.config(state='normal')
        self.setting_quality.config(state='normal')
        self.setting_quality.set(quality)
        self.filling.set(filling)
        self.setting_go['state'] = tk.NORMAL

        self.visualizer.configure(image=img_to_display)
        self.visualizer.image = img_to_display


class PrintImgSubWindows(tk.Toplevel):
    def __init__(self, controller, gui_opt):
        self.gui_opt = gui_opt
        self.controller = controller
        # ------------------------------
        # SubWindows
        tk.Toplevel.__init__(
            self,
            bg=gui_opt['bg_general'],
            borderwidth=2,
            relief='solid'
        )

        self.geometry('300x200')
        self.sub_label = tk.Label(self, **gui_opt['text_config'])
        self.sub_progressbar = ttk.Progressbar(self, length=200, value=0)
        self.sub_button = tk.Button(
            self,
            text='STOP',
            command=lambda: self.controller.stop_print(),
            **gui_opt['button_config']
        )
        self.sub_label.pack(pady=20)
        self.sub_progressbar.pack()
        self.sub_button.pack(pady=20)
        self.protocol('WM_DELETE_WINDOW', lambda: self.controller.stop_print())

    def update_progress_bar(self, data):
        try:
            self.sub_progressbar['value'] = data['progress']
            self.sub_label['text'] = data['label']
            self.update()
        except:
            pass

    def destroy_windows(self):
        self.after(2000, self.destroy())


class PrintImgController:
    def __init__(self) -> None:
        self.user_stop = False
        pass

    def setup(self):
        pass

    def open_img(self):
        logging.debug("")
        if self.model.open_img() is not False:
            img_to_display = self.process_img()
            self.view.open_img_gui(
                img_to_display, self.model.quality, self.model.filling)

        else:
            logging.debug(f"Errore nell'apertuta dell'immagine")

    def change_quality(self, quality):
        logging.debug("")
        self.model.quality = quality
        img_to_display = self.process_img()
        self.view.open_img_gui(
            img_to_display, self.model.quality, self.model.filling)

    def change_filling(self, filling):
        logging.debug("")
        self.model.filling = filling
        img_to_display = self.process_img()
        self.view.open_img_gui(
            img_to_display, self.model.quality, self.model.filling)

    def process_img(self, print_go=0):
        logging.debug("")
        img_work = self.model.img_global
        quality = self.model.quality
        filling = self.model.filling
        height, width = img_work.shape[:2]
        dim_visualizer = self.model.gui_opt['dim_visualizer']

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

        if print_go:
            return(img_work, delta_X, delta_Y)
        else:
            return ImageTk.PhotoImage(
                image=Image.fromarray(img_work)
            )

    def start_thread(self):
        Thread(target=self.print_img()).start()

    def print_img(self):
        # ask 'process_img()' to get initial parameters
        # while all 'img_to_print' is not white, he continusly looks for next black pixel nearest from the previous one found
        # he uses slicing technique for 2D array to find black pixel position
        # by 'arduino_sender()' he send pen_position and coordinates to serial port
        self.user_stop = False
        self.view.create_windows()

        img_to_print, delta_X, delta_Y = self.process_img(1)
        calibration_params = self.model.get_calibration_params()
        logging.debug(self.model.calibration_params)
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
                'label': self.model.locale['sub_windows_'][1] % (cont, black_pixel, str(round(cont*100/black_pixel))+' %')
            })
        try:
            self.arduino_sender('U', 0, 0)
            self.view.destroy_windows()
        except:
            pass

    def stop_print(self):
        logging.debug(10*"Stop_print ")
        self.user_stop = True
        self.arduino_sender('U', 0, 0)
        self.view.destroy_windows()
        # self.user_stop = False

    def arduino_sender(self, pen, X, Y):
        logging.debug(f"{self.user_stop}")
        return True

    def arduino_sender1(self, pen, X, Y):
        logging.debug("")
        # he send data array = (pen_position, coordinate_point_X, coordinate_point_Y)
        # if pen_position is up, he wait for positive response ('A') from the board
        # if serial fails, return False
        calib_check = self.model.get_calibration_params()
        line = (f"{pen} {X} {Y}\n")
        if not calib_check:
            self.view.prompt_message(
                title=self.model.locale['error_msg'][0],
                message=self.model.locale['error_msg'][2]
            )

            return False
        try:
            self.serial_port.write(line.encode('utf-8'))
        except:
            self.view.prompt_message(
                title=self.model.locale['error_msg'][0],
                message=self.model.locale['error_msg'][1]
            )

            return False
        if (line[0] == 'U'):
            while self.serial_port.read() != str.encode('A'):
                continue


class PrintImgModel:
    def __init__(self):
        self.img_global = None
        self.quality = 100
        self.filling = 0

    def open_img(self):
        logging.debug("")
        filepath = askopenfilename(
            title=self.locale['openImg_'],
            filetypes=[
                ("File img", "*.jpg *.png *.jpeg"),
                ("JPG", "*.jpg"),
                ("PNG", "*.png"),
                ("JPEG", "*.jpeg"),
                ("All Files", "*.*")
            ]
        )

        if not filepath:
            return False
        else:
            self.img_global = cv2.imread(filepath)
            return self.img_global
