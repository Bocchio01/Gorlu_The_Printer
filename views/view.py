import logging
import webbrowser

import tkinter as tk
from views.Vabstraction import ViewABC
from controllers.Cabstraction import ControllerABC
from tkinter.messagebox import showinfo


class View(ViewABC, tk.Tk):
    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.geometry('1000x600')

    def add_menu(self, controller: ControllerABC, locale: dict):
        menu = MenuView(self, controller, locale)
        self.config(menu=menu)

    def open_link(self, link: str) -> None:
        logging.debug(f"MenuController:{link}")
        webbrowser.open_new(link)

    def show_view(self, view: tk.Frame = None) -> None:
        """
        Display the selected view and unpack all the others.

        :param view: View to be packed as current
        """
        logging.debug(f"View:view:{view}")

        for v in self.winfo_children():
            v.pack_forget()

        view.pack(fill=tk.BOTH, expand=True)

    def prompt_message(self, data: dict):
        showinfo(
            title=data['title'],
            message=data['message']
        )

    def start_main_loop(self) -> None:
        """Start the tkinter GUI app"""
        self.mainloop()


class MenuView(tk.Menu):
    def __init__(self, master: tk.Tk, controller: ControllerABC, locale: dict):
        logging.debug(f"MenuView")

        tk.Menu.__init__(self, master)

        self.info = tk.Menu(self, tearoff=0)

        self.add_cascade(menu=self.info, label=locale[0][0])
        self.info.add_command(
            label=locale[0][1],
            command=lambda: controller.root.show_view(controller.Info.view)
        )
        self.info.add_command(
            label=locale[0][2],
            command=lambda: controller.root.show_view(controller.Lang.view)
        )
        self.info.add_separator()
        self.info.add_command(
            label=locale[0][3],
            command=lambda: controller.root.open_link(
                'https://github.com/Bocchio01/Arduino_CNC_plotter'
            )
        )
        self.info.add_command(
            label=locale[0][4],
            command=lambda: controller.root.open_link(
                'https://bocchio.dev/article/gorlu-the-printer'
            )
        )

        self.info.add_command(
            label=locale[0][5],
            command=lambda: controller.root.open_link(
                'https://learn.adafruit.com/adafruit-motor-shield/library-install'
            )
        )

        self.add_command(
            label=locale[1],
            command=lambda: controller.root.show_view(
                controller.Config.view
            )
        )
        self.add_command(
            label=locale[2],
            command=lambda: controller.root.show_view(
                controller.Calibration.view
            )
        )
        self.add_command(
            label=locale[3],
            command=lambda: controller.root.show_view(
                controller.PrintImg.view
            )
        )
        self.add_command(
            label=locale[4],
            command=lambda: controller.root.show_view(
                controller.PrintHand.view
            )
        )
        self.add_command(
            label=locale[5],
            command=lambda: controller.root.show_view(
                None
                # controller.  # .view
            )
        )
