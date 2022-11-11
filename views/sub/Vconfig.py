import logging

import tkinter as tk
from tkinter import ttk


class ConfigView(tk.Frame):
    def __init__(self, master: tk.Tk, locale: dict, gui_opt: dict) -> None:

        tk.Frame.__init__(self, master, **gui_opt['main_frame'])

        self.text_0 = tk.Label(
            self,
            text=locale['text_0'],
            **gui_opt['text_config']
        )
        self.text_1 = tk.Label(
            self,
            text=locale['text_1'],
            **gui_opt['text_config']
        )
        self.text_2 = tk.Label(
            self,
            text=locale['text_2'],
            **gui_opt['text_config']
        )

        self.COM = ttk.Combobox(
            self,
            textvariable=tk.StringVar(),
            **gui_opt['combobox_config']
        )
        self.COM['font'] = ('calibri', 20)

        self.separator_0 = ttk.Separator(self, orient=tk.HORIZONTAL)
        self.separator_1 = ttk.Separator(self, orient=tk.HORIZONTAL)

        self.save_arduino_code = tk.Button(
            self,
            text=locale['save_arduino_code'],
            ** gui_opt['button_config']
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

    def set_COM_ports(self, ports):
        logging.debug(f"ConfigView")
        self.COM['values'] = ports

    def set_arduino_code(self, arduino_code):
        logging.debug(f"ConfigView")
        self.arduino_code.insert('1.0', arduino_code)
