from optparse import OptionError
import tkinter as tk
from tkinter import ttk, font
from PIL import ImageTk, Image


class PrintHandFrame(tk.Frame):
    def __init__(self, parent, controller, gui_opt):
        self.gui_opt = gui_opt
        self.controller = controller
        # ------------------------------
        # printhand_frame
        tk.Frame.__init__(self, parent, bg=gui_opt['bg_general'])

        self.setting_frame = tk.Frame(self, bg=gui_opt['bg_general'])
        self.setting_text_0 = tk.Label(
            self.setting_frame, **gui_opt['text_config'])
        self.setting_text_1 = tk.Label(
            self.setting_frame, **gui_opt['text_config'])
        self.setting_text_2 = tk.Label(
            self.setting_frame, **gui_opt['text_config'])
        self.setting_text_3 = tk.Label(
            self.setting_frame, **gui_opt['text_config'])
        self.setting_separator_0 = ttk.Separator(
            self.setting_frame, orient=tk.HORIZONTAL)
        self.setting_separator_1 = ttk.Separator(
            self.setting_frame, orient=tk.HORIZONTAL)
        self.setting_button_0 = tk.Button(
            self.setting_frame, command=lambda: self.visualizer_board.delete('all'), **gui_opt['button_config'])
        self.setting_button_1 = tk.Button(
            self.setting_frame, command=lambda: self.controller.saveCanvas(), **gui_opt['button_config'])

        self.visualizer_frame = tk.Frame(
            self, bg=gui_opt['bg_visualizer'])
        self.visualizer_board = tk.Canvas(
            self.visualizer_frame, **gui_opt['visualizer_config'])

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
            '<Button-1>', self.controller.savePosn)
        self.visualizer_board.bind(
            '<B1-Motion>', self.controller.addLine)


class PrintHandController:
    def __init__(self) -> None:
        pass

    # printhand references
    def savePosn(self, event):
        # he gets coordinates from the current mouse position
        # if new position is far from the previous one, set pen_position up
        # by 'arduino_sender' sends pen_position and current coordinates to the board
        global lastx, lasty
        try:
            if ((abs(event.x - lastx) > 15) or (abs(event.y - lasty) > 15)):
                s = 'U'
            else:
                s = 'D'
        except:
            s = 'U'
        lastx, lasty = event.x, event.y
        if ((lastx > 0) and (lastx < dim_visualizer) and (lasty > 0) and (lasty < dim_visualizer)):
            arduino_sender(s, round(setting_data[2]*event.x/2),
                           round(setting_data[3]*event.y/2))

    def addLine(self, event):
        # draw a line on the whiteboard and call 'savePosn()' to get next mouse position
        printhand_visualizer_board.create_line(lastx, lasty, event.x, event.y)
        savePosn(event)

    def saveCanvas(self):
        # create a postscript file and ask filepath to save the canvas witheboard
        # then he eliminate postscript file
        printhand_visualizer_board.postscript(
            file="sources\\data\\Lavagna__work.eps")
        board_work = Image.open("sources\\data\\Lavagna__work.eps")
        filepath = asksaveasfilename(title=saveCanvas_[lang][0], initialfile=saveCanvas_[lang][1], defaultextension="png", filetypes=[
                                     ("PNG", "*.png"), ("JPG", "*.jpg"), ("JPEG", "*.jpeg"), ("All Files", "*.*")])
        if filepath:
            board_work.save(filepath)
        else:
            pass
        board_work.close()
        os.remove("sources\\data\\Lavagna__work.eps")
