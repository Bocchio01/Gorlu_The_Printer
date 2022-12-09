import logging

from views.sub.Vprinttext import PrintTextView
from controllers.Cabstraction import ControllerABC
import numpy as np
import cv2
import tk


class PrintTextController:
    def __init__(self, controller: ControllerABC):
        logging.debug(f"PrintTextController")
        self.root = controller.root
        self.model = controller.model

        self.controller = controller

        self.view = PrintTextView(
            self.root,
            self.model.get_locale()['PrintTextFrame'],
            self.model.get_gui_opt()
        )

        self.view.setting_button.config(
            command=self.print_text
        )

        self.view.setting_align_o.config(
            value=self.model.get_locale()['align_o']
        )
        self.view.setting_align_v.config(
            value=self.model.get_locale()['align_v']
        )
        self.view.setting_character.config(
            values=self.model.get_settings()['fonts']
        )

        self.view.setting_entry.insert(
            '1.0', self.model.PrintTextModel.setting_entry.get()
        )

        self.view.text_dimension.set(
            self.model.PrintTextModel.setting_dimension.get()
        )

        self.view.setting_character.set(
            self.model.PrintTextModel.setting_character.get()
        )
        self.view.setting_align_o.set(
            self.model.PrintTextModel.setting_align_o.get()
        )
        self.view.setting_align_v.set(
            self.model.PrintTextModel.setting_align_v.get()
        )

        self.view.setting_rotation.config(
            command=lambda e: self.model.PrintTextModel.setting_rotation.set(
                self.view.setting_rotation.get()
            )
        )

        self.model.PrintTextModel.setting_rotation.addCallback(
            lambda e: self.model.PrintTextModel.update_img()
        )
        self.model.PrintTextModel.setting_entry.addCallback(
            lambda e: self.model.PrintTextModel.update_img()
        )
        self.model.PrintTextModel.setting_dimension.addCallback(
            lambda e: self.model.PrintTextModel.update_img()
        )
        self.model.PrintTextModel.setting_character.addCallback(
            lambda e: self.model.PrintTextModel.update_img()
        )
        self.model.PrintTextModel.setting_align_o.addCallback(
            lambda e: self.model.PrintTextModel.update_img()
        )
        self.model.PrintTextModel.setting_align_v.addCallback(
            lambda e: self.model.PrintTextModel.update_img()
        )

        self.view.setting_entry.bind(
            '<KeyRelease>',
            lambda e: self.model.PrintTextModel.setting_entry.set(
                self.view.setting_entry.get('1.0', 'end-1c')
            )
        )
        self.view.setting_dimension.bind(
            '<Return>',
            lambda e: self.model.PrintTextModel.setting_dimension.set(
                self.view.setting_dimension.get()
            )
        )
        self.view.setting_dimension.bind(
            "<FocusOut>",
            lambda e: self.model.PrintTextModel.setting_dimension.set(
                self.view.setting_dimension.get()
            )
        )
        self.view.setting_character.bind(
            '<<ComboboxSelected>>',
            lambda e: self.model.PrintTextModel.setting_character.set(
                self.view.setting_character.get()
            )
        )
        self.view.setting_align_o.bind(
            '<<ComboboxSelected>>',
            lambda e: self.model.PrintTextModel.setting_align_o.set(
                self.view.setting_align_o.get()
            )
        )
        self.view.setting_align_v.bind(
            '<<ComboboxSelected>>',
            lambda e: self.model.PrintTextModel.setting_align_v.set(
                self.view.setting_align_v.get()
            )
        )

        self.model.PrintTextModel.img_text.addCallback(
            lambda e: self.view.visualizer.config(
                image=self.model.PrintTextModel.img_text.get()
            )
        )

        self.model.PrintTextModel.update_img()

    def print_text(self):
        self.model.PrintImgModel.img_global.set(
            np.array(self.model.PrintTextModel.text_image.get())
        )

        self.root.show_view(self.controller.PrintImg.view)
