import logging
import tkinter as tk
import webbrowser


class MenuView(tk.Menu):
    def __init__(self, parent, view, controller):
        self.view = view
        self.controller = controller
        self.list_frames = list(view.frames.keys())

        tk.Menu.__init__(self, parent)

        self.info = tk.Menu(self, tearoff=0)
        self.config = tk.Menu(self, tearoff=0)
        self.help = tk.Menu(self, tearoff=0)

        self.add_cascade(menu=self.info)
        self.add_cascade(menu=self.config)
        self.add_command(
            command=lambda: self.view.show_frame(self.list_frames[3])
        )
        self.add_command(
            command=lambda: self.view.show_frame(self.list_frames[4])
        )
        self.add_command(
            command=lambda: self.view.show_frame(self.list_frames[5])
        )
        self.add_command(
            command=lambda: self.view.show_frame(self.list_frames[6])
        )
        self.add_cascade(menu=self.help)

        self.info.add_command(
            command=lambda: self.view.show_frame(self.list_frames[1])
        )
        self.info.add_separator()
        self.info.add_command(command=lambda: self.controller.open_link(
            'https://github.com/Bocchio01/Arduino_CNC_plotter')
        )
        self.info.add_command(command=lambda: self.controller.open_link(
            'https://bocchio.dev/article/gorlu-the-printer')
        )

        self.config.add_command(
            command=lambda: self.view.show_frame(self.list_frames[2])
        )
        self.config.add_separator()
        self.config.add_command(command=lambda: self.controller.open_link(
            'https://learn.adafruit.com/adafruit-motor-shield/library-install')
        )

        self.help.add_command(
            command=lambda: self.view.show_frame(self.list_frames[0]),
            label='Preferences'
        )
        self.help.add_command(
            command=lambda: self.controller.set_locale('it'),
            label='IT'
        )
        self.help.add_command(
            command=lambda: self.controller.set_locale('en'),
            label='EN'
        )
        self.help.add_command(
            command=lambda: self.controller.set_locale('fr'),
            label='FR'
        )

        # self.help.add_command(label='IT',
        #                       image=PhotoImage(
        #                           file='assets/img/it.png'),
        #                       compound='left',
        #                       command=lambda: self.controller.set_locale('it'),
        #                       )


class MenuController:
    def __init__(self) -> None:
        pass

    def open_link(self, link):
        logging.debug(f"")
        webbrowser.open_new(link)
