import logging
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class CalibrationFrame(tk.Frame):
    def __init__(self, master: tk.Tk, gui_opt: dict) -> None:

        tk.Frame.__init__(self, master, bg=gui_opt['bg_general'])

        self.servo_max = tk.IntVar()
        self.servo_min = tk.IntVar()

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

    def set_calibration_params(self, params):
        logging.debug(f"CalibrationView:{params}")
        self.servo_max.set(params['UP'])
        self.servo_min.set(params['DOWN'])
        self.setting_direction_X.set(params['X'])
        self.setting_direction_Y.set(params['Y'])
