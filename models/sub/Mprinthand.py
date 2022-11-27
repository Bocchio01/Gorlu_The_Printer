import logging

from models.observable import Observable
from models.Mabstraction import ModelABC
import math
from tkinter.filedialog import asksaveasfilename
from PIL import Image
import io


class PrintHandModel:
    def __init__(self, parent: ModelABC):
        self.parent = parent
        self.lastx = Observable(0)
        self.lasty = Observable(0)
        self.x = 0
        self.y = 0
        self.pen = 'U'

    def savePosn(self, event):
        logging.debug(f"PrintHandModel")

        self.x = self.lastx.get()
        self.y = self.lasty.get()

        self.pen = (
            'U'
            if math.sqrt((event.x - self.lastx.get()) ** 2 + (event.y - self.lasty.get()) ** 2) > 15 else
            'D'
        )

        dim_visualizer = self.parent.get_gui_opt()['dim_visualizer']

        if (
            (event.x > 0) and (event.x < dim_visualizer) and
            (event.x > 0) and (event.x < dim_visualizer)
        ):
            self.lastx.set(int(event.x))
            self.lasty.set(int(event.y))

    def save_canvas(self, board):
        logging.debug(f"PrintHandModel")

        ps = board.postscript()
        board_work = Image.open(io.BytesIO(ps.encode('utf-8')))
        filepath = asksaveasfilename(
            title=self.parent.get_locale()['saveCanvas_'][0],
            initialfile=self.parent.get_locale()['saveCanvas_'][1],
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
