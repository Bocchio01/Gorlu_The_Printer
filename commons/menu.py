import logging
import tkinter as tk
import webbrowser


class MenuView(tk.Menu):
    def __init__(self, parent, view, controller):
        logging.debug(f"MenuView")
        self.view = view
        self.controller = controller

        tk.Menu.__init__(self, parent)

        self.info = tk.Menu(self, tearoff=0)
        self.config = tk.Menu(self, tearoff=0)
        self.help = tk.Menu(self, tearoff=0)

        self.add_cascade(menu=self.info)
        self.add_command(
            command=lambda: self.view.show_frame('ConfigFrame')
        )
        self.add_command(
            command=lambda: self.view.show_frame('CalibrationFrame')
        )
        self.add_command(
            command=lambda: self.view.show_frame('PrintImgFrame')
        )
        self.add_command(
            command=lambda: self.view.show_frame('PrintHandFrame')
        )
        self.add_command(
            command=lambda: self.view.show_frame('PrintTextFrame')
        )

        self.info.add_command(
            command=lambda: self.view.show_frame('InfoFrame')
        )
        self.info.add_command(
            command=lambda: self.view.show_frame('LangView')
        )
        self.info.add_separator()
        self.info.add_command(
            command=lambda: self.controller.open_link(
                'https://github.com/Bocchio01/Arduino_CNC_plotter'
            )
        )
        self.info.add_command(
            command=lambda: self.controller.open_link(
                'https://bocchio.dev/article/gorlu-the-printer'
            )
        )

        self.info.add_command(
            command=lambda: self.controller.open_link(
                'https://learn.adafruit.com/adafruit-motor-shield/library-install'
            )
        )

    def set_locale(self, locale):
        logging.debug(f"MenuView")
        self.entryconfigure(1, label=locale['menu_'][0][0])
        self.entryconfigure(2, label=locale['menu_'][1])
        self.entryconfigure(3, label=locale['menu_'][2])
        self.entryconfigure(4, label=locale['menu_'][3])
        self.entryconfigure(5, label=locale['menu_'][4])
        self.entryconfigure(6, label=locale['menu_'][5])
        self.info.entryconfigure(0, label=locale['menu_'][0][1])
        self.info.entryconfigure(1, label=locale['menu_'][0][2])
        self.info.entryconfigure(3, label=locale['menu_'][0][3])
        self.info.entryconfigure(4, label=locale['menu_'][0][4])
        self.info.entryconfigure(5, label=locale['menu_'][0][5])


class MenuController:
    def __init__(self):
        logging.debug(f"MenuController")

    def open_link(self, link):
        logging.debug(f"MenuController:{link}")
        webbrowser.open_new(link)
