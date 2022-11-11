import logging

from models.observable import Observable
from models.Mabstraction import ModelABC
from tkinter.filedialog import askopenfilename
import cv2


class PrintImgModel:
    def __init__(self, parent: ModelABC):
        self.parent = parent

        self.img_global = Observable(None)
        self.quality = Observable(100)
        self.filling = Observable(0)

    def open_img(self):
        """Open and set as a cv2.imread the varible img_global"""
        logging.debug(f"PrintImgModel")
        filepath = askopenfilename(
            title=self.parent.get_locale()['openImg_'],
            filetypes=[
                ("File img", "*.jpg *.png *.jpeg"),
                ("JPG", "*.jpg"),
                ("PNG", "*.png"),
                ("JPEG", "*.jpeg"),
                ("All Files", "*.*")
            ]
        )

        if not filepath:
            return
        else:
            self.img_global.set(cv2.imread(filepath))
            return self.img_global.get()
