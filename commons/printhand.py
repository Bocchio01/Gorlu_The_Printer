import io
import logging
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
from PIL import Image


class PrintHandFrame(tk.Frame):
    def __init__(self, parent, controller, gui_opt):
        logging.debug(f"PrintHandFrame")
        self.gui_opt = gui_opt
        self.controller = controller
        # ------------------------------
        # printhand_frame
        tk.Frame.__init__(self, parent, bg=gui_opt['bg_general'])

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
        self.setting_separator_0 = ttk.Separator(
            self.setting_frame,
            orient=tk.HORIZONTAL
        )
        self.setting_separator_1 = ttk.Separator(
            self.setting_frame,
            orient=tk.HORIZONTAL
        )
        self.setting_button_0 = tk.Button(
            self.setting_frame,
            command=lambda: self.visualizer_board.delete('all'),
            **gui_opt['button_config']
        )
        self.setting_button_1 = tk.Button(
            self.setting_frame,
            command=lambda: self.controller.save_canvas(self.visualizer_board),
            **gui_opt['button_config']
        )

        self.visualizer_frame = tk.Frame(
            self,
            bg=gui_opt['bg_visualizer']
        )
        self.visualizer_board = tk.Canvas(
            self.visualizer_frame,
            **gui_opt['visualizer_config']
        )

        # printhand pack/grid
        self.setting_frame.rowconfigure([0, 3, 4, 6, 7], minsize=70)
        self.setting_frame.rowconfigure([2, 5], minsize=30)
        self.setting_frame.rowconfigure(1, minsize=30)
        self.setting_frame.columnconfigure(0, minsize=400)

        self.setting_frame.pack(fill=tk.Y, side=tk.LEFT, pady=50)
        self.setting_text_0.grid(sticky='ns')
        self.setting_separator_0.grid(padx=40, sticky='we')
        self.setting_text_1.grid(pady=10, sticky='ns')
        self.setting_text_2.grid(sticky='ns')
        self.setting_text_3.grid(sticky='ns')
        self.setting_separator_1.grid(padx=40, sticky='we')
        self.setting_button_0.grid(pady=20, sticky='s')
        self.setting_button_1.grid(pady=0, sticky='n')
        self.visualizer_frame.pack(fill=tk.BOTH, expand=True)
        self.visualizer_board.pack(expand=True)

        self.visualizer_board.bind(
            '<Button-1>',
            lambda e: self.controller.save_position(e)
        )
        self.visualizer_board.bind(
            '<B1-Motion>',
            lambda e: self.controller.add_line(e)
        )

        # self.visualizer_board.postscript()

    def create_line(self, lastx, lasty, x, y):
        self.visualizer_board.create_line(lastx, lasty, x, y)


class PrintHandController:
    def __init__(self) -> None:
        logging.debug(f"PrintHandController")
        self.last = {
            'x': None,
            'y': None
        }
        pass

    # printhand references
    def save_position(self, event):
        logging.debug(f"PrintHandController")
        # he gets coordinates from the current mouse position
        # if new position is far from the previous one, set pen_position up
        # by 'arduino_sender' sends pen_position and current coordinates to the board

        dim_visualizer = self.model.get_gui_opt()['dim_visualizer']
        calibration_params = self.model.get_calibration_params()

        try:
            if (
                abs(event.x - self.last['x']) > 15 or
                abs(event.y - self.last['y']) > 15
            ):
                s = 'U'
            else:
                s = 'D'
        except:
            s = 'U'
        self.last['x'], self.last['y'] = event.x, event.y

        if (
            self.last['x'] > 0 and
            self.last['x'] < dim_visualizer and
            self.last['y'] > 0 and
            self.last['y'] < dim_visualizer
        ):
            self.arduino_sender(
                s,
                round(calibration_params['X']*event.x/2),
                round(calibration_params['Y']*event.y/2)
            )

    def add_line(self, event):
        logging.debug(f"PrintHandController")
        # draw a line on the whiteboard and call 'save_position()' to get next mouse position
        self.view.frames[PrintHandFrame].create_line(
            self.last['x'], self.last['y'], event.x, event.y)
        self.save_position(event)

    def save_canvas(self, board):
        logging.debug(f"PrintHandController")
        self.model.save_canvas(board)


class PrintHandModel:
    def __init__(self) -> None:
        logging.debug(f"PrintHandModel")
        pass

    def save_canvas(self, board):
        logging.debug(f"PrintHandModel")

        ps = board.postscript()
        board_work = Image.open(io.BytesIO(ps.encode('utf-8')))
        filepath = asksaveasfilename(
            title=self.locale['saveCanvas_'][0],
            initialfile=self.locale['saveCanvas_'][1],
            defaultextension="png",
            filetypes=[
                ("PNG", "*.png"),
                ("JPG", "*.jpg"),
                ("JPEG", "*.jpeg"),
                ("All Files", "*.*")
            ]
        )
        if filepath:
            board_work.save(filepath)
        else:
            pass
        board_work.close()
