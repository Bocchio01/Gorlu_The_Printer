import logging

import tkinter as tk
from tkinter import ttk


class PrintTextView(tk.Frame):
    def __init__(self, master: tk.Tk, locale: dict, gui_opt: dict) -> None:

        tk.Frame.__init__(self, master, **gui_opt['main_frame'])

        self.text_dimension = tk.IntVar(value=30)

        self.setting_frame = tk.Frame(
            self,
            bg=gui_opt['bg_general']
        )
        self.setting_text_0 = tk.Label(
            self.setting_frame,
            text=locale['setting_text_0'],
            **gui_opt['text_config']
        )
        self.setting_text_5 = tk.Label(
            self.setting_frame,
            text=locale['setting_text_5'],
            **gui_opt['text_config']
        )
        self.setting_entry = tk.Text(
            self.setting_frame,
            font=('calibri', 13),
            width=35,
            height=4
        )
        self.setting_separator_0 = ttk.Separator(
            self.setting_frame,
            orient=tk.HORIZONTAL
        )
        self.setting_separator_2 = ttk.Separator(
            self.setting_frame,
            orient=tk.HORIZONTAL
        )
        self.setting_rotation = tk.Scale(
            self.setting_frame,
            orient=tk.HORIZONTAL,
            length=300,
            from_=-180.0,
            to=180.0,
            # command=fontChanged,
            **gui_opt['button_config']
        )

        self.setting_button = tk.Button(
            self.setting_frame,
            text=locale['setting_button'],
            # command=lambda: printText(),
            **gui_opt['button_config']
        )

        self.setting_subframe = tk.Frame(
            self.setting_frame,
            bg=gui_opt['bg_general']
        )
        self.setting_text_1 = tk.Label(
            self.setting_subframe,
            text=locale['setting_text_1'],
            **gui_opt['text_config']
        )
        self.setting_text_4 = tk.Label(
            self.setting_subframe,
            text=locale['setting_text_4'],
            **gui_opt['text_config']
        )
        self.setting_text_2 = tk.Label(
            self.setting_subframe,
            text=locale['setting_text_2'],
            **gui_opt['text_config']
        )
        self.setting_text_3 = tk.Label(
            self.setting_subframe,
            text=locale['setting_text_3'],
            **gui_opt['text_config']
        )
        self.setting_separator_1 = ttk.Separator(
            self.setting_subframe,
            orient=tk.VERTICAL
        )
        self.setting_dimension = tk.Entry(
            self.setting_subframe,
            textvariable=self.text_dimension,
            font=gui_opt['text_font'],
            width=3
        )
        self.setting_character = ttk.Combobox(
            self.setting_subframe,
            width=10,
            textvariable=tk.StringVar(),
            **gui_opt['combobox_config']
        )
        self.setting_align_o = ttk.Combobox(
            self.setting_subframe,
            width=9,
            textvariable=tk.StringVar(),
            **gui_opt['combobox_config']
        )
        self.setting_align_v = ttk.Combobox(
            self.setting_subframe,
            width=9,
            textvariable=tk.StringVar(),
            **gui_opt['combobox_config']
        )

        self.visualizer_frame = tk.Frame(
            self,
            bg=gui_opt['bg_visualizer']
        )
        self.visualizer = tk.Label(
            self.visualizer_frame,
            **gui_opt['visualizer_config']
        )

        # printtext pack/grid
        self.setting_frame.rowconfigure(0, minsize=50)
        self.setting_frame.rowconfigure([1, 2, 3, 5, 6, 7], minsize=30)
        self.setting_frame.rowconfigure(4, minsize=40)
        self.setting_frame.columnconfigure(0, minsize=400)

        self.setting_subframe.columnconfigure(0, minsize=180)
        self.setting_subframe.columnconfigure(1, minsize=50)
        self.setting_subframe.columnconfigure(2, minsize=60)
        self.setting_subframe.rowconfigure([0, 1, 2], minsize=40)

        self.setting_frame.pack(fill=tk.Y, side=tk.LEFT, pady=50)
        self.setting_text_0.grid(sticky='s')
        self.setting_entry.grid(padx=30, pady=10, sticky='n')
        self.setting_separator_0.grid(padx=40, sticky='we')

        self.setting_subframe.grid()
        self.setting_text_1.grid(row=0, column=0, sticky='ns')
        self.setting_text_4.grid(row=0, column=2, sticky='ns')
        self.setting_text_2.grid(row=1, column=0, sticky='w')
        self.setting_text_3.grid(row=2, column=0, sticky='w')
        self.setting_dimension.grid(row=1, column=0, sticky='e')
        self.setting_character.grid(row=2, column=0, sticky='e')
        self.setting_align_o.grid(row=1, column=2)
        self.setting_align_v.grid(row=2, column=2)
        self.setting_separator_1.grid(column=1, row=1, rowspan=3, sticky='ns')

        self.setting_text_5.grid(sticky='ns')
        self.setting_rotation.grid(row=5)
        self.setting_separator_2.grid(padx=40, sticky='wes')
        self.setting_button.grid(pady=20, sticky='n')
        self.visualizer_frame.pack(fill=tk.BOTH, expand=True)
        self.visualizer.pack(expand=True)

        # self.setting_entry.bind('<Key>', fontChanged)
        # self.setting_dimension.bind('<Return>', fontChanged)
        # self.setting_dimension.bind("<FocusOut>", fontChanged)
        # self.setting_character.bind('<<ComboboxSelected>>', fontChanged)
        # self.setting_align_o.bind('<<ComboboxSelected>>', fontChanged)
        # self.setting_align_v.bind('<<ComboboxSelected>>', fontChanged)
