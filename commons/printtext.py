import logging
import tkinter as tk
from tkinter import ttk
import numpy as np
from tkinter import font
from PIL import Image, ImageTk, ImageFont, ImageDraw


class PrintTextFrame(tk.Frame):
    def __init__(self, parent, controller, gui_opt):
        logging.debug(f"PrintTextFrame")
        self.gui_opt = gui_opt
        self.controller = controller
        # ------------------------------
        # frame
        text_dimension = tk.IntVar(value=30)
        tk.Frame.__init__(self, parent, bg=gui_opt['bg_general'])

        self.setting_frame = tk.Frame(self, bg=gui_opt['bg_general'])
        self.setting_text_0 = tk.Label(
            self.setting_frame,
            **gui_opt['text_config']
        )
        self.setting_text_5 = tk.Label(
            self.setting_frame,
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
            command=lambda e: self.update_paramether(),
            **gui_opt['button_config']
        )
        self.setting_button = tk.Button(
            self.setting_frame,
            command=lambda: self.controller.print_text(),
            **gui_opt['button_config']
        )

        self.setting_subframe = tk.Frame(
            self.setting_frame,
            bg=gui_opt['bg_general']
        )
        self.setting_text_1 = tk.Label(
            self.setting_subframe,
            **gui_opt['text_config']
        )
        self.setting_text_4 = tk.Label(
            self.setting_subframe,
            **gui_opt['text_config']
        )
        self.setting_text_2 = tk.Label(
            self.setting_subframe,
            **gui_opt['text_config']
        )
        self.setting_text_3 = tk.Label(
            self.setting_subframe,
            **gui_opt['text_config']
        )
        self.setting_separator_1 = ttk.Separator(
            self.setting_subframe,
            orient=tk.VERTICAL
        )
        self.setting_dimension = tk.Entry(
            self.setting_subframe,
            textvariable=text_dimension,
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

        self.visualizer_frame = tk.Frame(self, bg=gui_opt['bg_visualizer'])
        self.visualizer = tk.Label(
            self.visualizer_frame, **gui_opt['visualizer_config'])

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

        self.setting_entry.bind(
            '<Key>',
            lambda e: self.update_paramether()
        )
        self.setting_dimension.bind(
            '<Return>',
            lambda e: self.update_paramether()
        )
        self.setting_dimension.bind(
            "<FocusOut>",
            lambda e: self.update_paramether()
        )
        self.setting_character.bind(
            '<<ComboboxSelected>>',
            lambda e: self.update_paramether()
        )
        self.setting_align_o.bind(
            '<<ComboboxSelected>>',
            lambda e: self.update_paramether()
        )
        self.setting_align_v.bind(
            '<<ComboboxSelected>>',
            lambda e: self.update_paramether()
        )

    def update_paramether(self):
        self.controller.font_changed({
            'setting_entry': self.setting_entry.get('1.0', 'end-1c'),
            'setting_character': self.setting_character.get(),
            'setting_dimension': self.setting_dimension.get(),
            'setting_align_o': self.setting_align_o.get(),
            'setting_align_v': self.setting_align_v.get(),
            'setting_rotation': self.setting_rotation.get()
        })

    def update_text(self, img):
        self.visualizer.config(image=img)
        self.visualizer.image = img

    def set_fonts_gui(self, fonts):
        self.setting_character.config(value=fonts)
        self.setting_character.set(fonts[0])
        pass


class PrintTextController:
    def __init__(self) -> None:
        logging.debug(f"PrintTextController")
        pass

    def setup(self):
        logging.debug(f"PrintTextController")
        self.view.set_fonts_gui(self.get_fonts())

        pass

    def get_fonts(self):
        logging.debug(f"PrintTextController")
        return self.model.get_fonts()

    def font_changed(self, data):
        logging.debug(f"PrintTextController")
        text_to_print = data['setting_entry']
        text_image = Image.new('RGB', (500, 500), (255, 255, 255))
        draw = ImageDraw.Draw(text_image)
        font_ = ImageFont.truetype(
            data['setting_character'],
            size=int(data['setting_dimension'])
        )
        w, h = draw.textsize(text_to_print, font=font_)

        horizontal = {
            self.model.locale['align_o'][0]: (1, 'left'),
            self.model.locale['align_o'][1]: ((500-w)/2, 'center'),
            self.model.locale['align_o'][2]: ((500-w-1), 'right')
        }
        vertical = {
            self.model.locale['align_v'][0]: 1,
            self.model.locale['align_v'][1]: (500-h)/2,
            self.model.locale['align_v'][2]: (500-h-1)
        }

        X, align = horizontal[data['setting_align_o']]
        Y = vertical[data['setting_align_v']]

        draw.text(
            (X, Y),
            font=font_,
            text=text_to_print,
            fill='black',
            align=align
        )
        text_image = text_image.rotate(data['setting_rotation'])
        img_to_show = ImageTk.PhotoImage(text_image)

        self.model.text_image = text_image
        self.view.update_text(img_to_show)

    def print_text(self):
        self.model.img_global = np.array(self.model.text_image)
        img_to_display = self.process_img()
        self.view.open_img_gui(
            img_to_display,
            self.model.quality,
            self.model.filling
        )
        self.view.show_frame('PrintImgFrame')


class PrintTextModel:
    def __init__(self) -> None:
        logging.debug(f"PrintTextModel")
        self.text_image = None
        self.fonts = []

        pass

    def get_fonts(self):
        logging.debug(f"Model")
        if not self.fonts:
            for i in font.families():
                try:
                    ImageFont.truetype(i, size=12)
                    self.fonts.append(i)
                except:
                    pass

        return self.fonts
