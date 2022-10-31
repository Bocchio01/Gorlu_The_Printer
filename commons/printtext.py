import tkinter as tk
from tkinter import ttk, font
from PIL import ImageTk, Image


class PrintTextFrame(tk.Frame):
    def __init__(self, parent, controller, gui_opt):
        self.gui_opt = gui_opt
        self.controller = controller
        # ------------------------------
        # frame
        text_dimension = tk.IntVar(value=30)
        tk.Frame.__init__(self, parent, bg=gui_opt['bg_general'])

        self.setting_frame = tk.Frame(self, bg=gui_opt['bg_general'])
        self.setting_text_0 = tk.Label(
            self.setting_frame, **gui_opt['text_config'])
        self.setting_text_5 = tk.Label(
            self.setting_frame, **gui_opt['text_config'])
        self.setting_entry = tk.Text(
            self.setting_frame, font=('calibri', 13), width=35, height=4)
        self.setting_separator_0 = ttk.Separator(
            self.setting_frame, orient=tk.HORIZONTAL)
        self.setting_separator_2 = ttk.Separator(
            self.setting_frame, orient=tk.HORIZONTAL)
        self.setting_rotation = tk.Scale(self.setting_frame, orient=tk.HORIZONTAL, length=300,
                                         from_=-180.0, to=180.0, command=self.controller.fontChanged(), **gui_opt['button_config'])
        self.setting_button = tk.Button(
            self.setting_frame, command=lambda: self.controller.printText(), **gui_opt['button_config'])

        self.setting_subframe = tk.Frame(
            self.setting_frame, bg=gui_opt['bg_general'])
        self.setting_text_1 = tk.Label(
            self.setting_subframe, **gui_opt['text_config'])
        self.setting_text_4 = tk.Label(
            self.setting_subframe, **gui_opt['text_config'])
        self.setting_text_2 = tk.Label(
            self.setting_subframe, **gui_opt['text_config'])
        self.setting_text_3 = tk.Label(
            self.setting_subframe, **gui_opt['text_config'])
        self.setting_separator_1 = ttk.Separator(
            self.setting_subframe, orient=tk.VERTICAL)
        self.setting_dimension = tk.Entry(
            self.setting_subframe, textvariable=text_dimension, font=gui_opt['text_font'], width=3)
        self.setting_character = ttk.Combobox(
            self.setting_subframe, width=10, textvariable=tk.StringVar(), **gui_opt['combobox_config'])
        self.setting_align_o = ttk.Combobox(
            self.setting_subframe, width=9, textvariable=tk.StringVar(), **gui_opt['combobox_config'])
        self.setting_align_v = ttk.Combobox(
            self.setting_subframe, width=9, textvariable=tk.StringVar(), **gui_opt['combobox_config'])

        visualizer_frame = tk.Frame(self, bg=gui_opt['bg_visualizer'])
        visualizer = tk.Label(visualizer_frame, **gui_opt['visualizer_config'])

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
        visualizer_frame.pack(fill=tk.BOTH, expand=True)
        visualizer.pack(expand=True)

        self.setting_entry.bind('<Key>', self.controller.fontChanged())
        self.setting_dimension.bind('<Return>', self.controller.fontChanged())
        self.setting_dimension.bind(
            "<FocusOut>", self.controller.fontChanged())
        self.setting_character.bind(
            '<<ComboboxSelected>>', self.controller.fontChanged())
        self.setting_align_o.bind(
            '<<ComboboxSelected>>', self.controller.fontChanged())
        self.setting_align_v.bind(
            '<<ComboboxSelected>>', self.controller.fontChanged())


class PrintTextController:
    def __init__(self) -> None:
        pass

    # printtext referencs
    def fontChanged(self, event):
        # when a text parameters is changhed, he reload the entire text and save il into an image file (using PIL library funtions)
        # then he set the 'text image' into the 'text page'
        # text_image is declared as a global variable
        global text_image
        text_to_print = printtext_setting_entry.get('1.0', 'end-1c')
        text_image = Image.new('RGB', (500, 500), (255, 255, 255))
        draw = ImageDraw.Draw(text_image)
        font_ = ImageFont.truetype(printtext_setting_character.get(
        ), size=int(printtext_setting_dimension.get()))
        w, h = draw.textsize(text_to_print, font=font_)

        horizontal = {align_o[lang][0]: (1, 'left'), align_o[lang][1]: (
            (500-w)/2, 'center'), align_o[lang][2]: ((500-w-1), 'right')}
        vertical = {align_v[lang][0]: 1, align_v[lang]
                    [1]: (500-h)/2, align_v[lang][2]: (500-h-1)}

        X, align = horizontal[printtext_setting_align_o.get()]
        Y = vertical[printtext_setting_align_v.get()]

        draw.text((X, Y), font=font_, text=text_to_print,
                  fill='black', align=align)
        text_image = text_image.rotate(printtext_setting_rotation.get())
        img_to_show = ImageTk.PhotoImage(text_image)

        printtext_visualizer.config(image=img_to_show)
        printtext_visualizer.image = img_to_show

    def printText(self):
        # he set img_global as text_image (taken from 'fontChanghed()')
        # open 'printimg page'
        global img_global, text_image
        img_global = np.array(text_image)
        printimg_setting_filling.config(state='normal')
        printimg_setting_quality.config(state='normal')
        process_img(0)
        openPage(3)
