import logging

from models.observable import Observable
from models.Mabstraction import ModelABC, PrintImgModelABC
from tkinter.filedialog import askopenfilename
import cv2


class PrintImgModel(PrintImgModelABC):
    def __init__(self, parent: ModelABC):
        self.parent = parent

        self.img_global = Observable(None)
        self.img_to_view = Observable(None)
        self.quality = Observable(100)
        self.filling = Observable(0)

    def open_img(self):
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
            self.quality.set(100)
            self.filling.set(0)
            return self.img_global.get()
