import logging

from models.observable import Observable
from models.Mabstraction import ModelABC
from PIL import Image, ImageTk, ImageFont, ImageDraw


class PrintTextModel:
    def __init__(self, parent: ModelABC):
        self.parent = parent
        self.text_image = Observable()
        self.img_text = Observable()
        self.setting_entry = Observable("")
        self.setting_dimension = Observable(30)
        self.setting_character = Observable()
        self.setting_align_o = Observable(
            self.parent.get_locale()['align_o'][1])
        self.setting_align_v = Observable(
            self.parent.get_locale()['align_v'][1])
        self.setting_rotation = Observable(0)

    def update_img(self):
        logging.debug(f"PrintTextModel")

        text_to_print = self.setting_entry.get()
        self.text_image.set(Image.new('RGB', (500, 500), (255, 255, 255)))
        draw = ImageDraw.Draw(self.text_image.get())
        font_ = ImageFont.truetype(
            self.setting_character.get(),
            size=int(self.setting_dimension.get())
        )
        w, h = draw.textsize(text_to_print, font=font_)

        horizontal = {
            self.parent.get_locale()['align_o'][0]: (1, 'left'),
            self.parent.get_locale()['align_o'][1]: ((500-w)/2, 'center'),
            self.parent.get_locale()['align_o'][2]: ((500-w-1), 'right')
        }
        vertical = {
            self.parent.get_locale()['align_v'][0]: 1,
            self.parent.get_locale()['align_v'][1]: (500-h)/2,
            self.parent.get_locale()['align_v'][2]: (500-h-1)
        }

        X, align = horizontal[self.setting_align_o.get()]
        Y = vertical[self.setting_align_v.get()]

        draw.text(
            (X, Y),
            font=font_,
            text=text_to_print,
            fill='black',
            align=align
        )
        self.text_image.set(self.text_image.get().rotate(
            self.setting_rotation.get())
        )
        self.img_text.set(ImageTk.PhotoImage(self.text_image.get()))

        # self.parent.PrintImgModel.img_global.set(self.text_image)
        # self.view.update_text(img_to_show)
