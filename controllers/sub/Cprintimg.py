import logging

from views.sub.Vprintimg import PrintImgView
from views.sub.Vsubwindows import SubWindows
from controllers.Cabstraction import ControllerABC
from controllers.CoreProcess import CoreProcess


from threading import Thread


class PrintImgController:
    def __init__(self, controller: ControllerABC):
        logging.debug(f"PrintImgController")
        self.root = controller.root
        self.model = controller.model

        self.subwindows: SubWindows
        self.CoreProcess = CoreProcess(controller)

        self.view = PrintImgView(
            self.root,
            self.model.get_locale()['PrintImgFrame'],
            self.model.get_gui_opt()
        )

        self.model.PrintImgModel.img_global.addCallback(
            lambda e: self.CoreProcess.process_img()
        )

        self.model.PrintImgModel.img_to_view.addCallback(
            self.view.set_img
        )

        self.model.PrintImgModel.filling.addMultipleCallback(
            [
                self.view.filling.set,
                lambda e: self.CoreProcess.process_img()
            ]
        )

        self.model.PrintImgModel.quality.addMultipleCallback(
            [
                self.view.setting_quality.set,
                lambda e: self.CoreProcess.process_img()
            ]
        )

        self.view.setting_selection.config(
            command=self.model.PrintImgModel.open_img
        )

        self.view.setting_quality.config(
            command=lambda e: self.model.PrintImgModel.quality.set(
                self.view.setting_quality.get()
            )
        )

        self.view.setting_filling.config(
            command=lambda: self.model.PrintImgModel.filling.set(
                self.view.filling.get()
            )
        )

        self.view.setting_go.config(
            command=lambda: self.start_thread()
        )

    def start_thread(self):
        logging.debug(f"PrintImgController")

        self.CoreProcess.user_stop.set(False)
        self.subwindows = SubWindows({}, self.model.get_gui_opt())

        self.subwindows.button.config(
            command=lambda: self.stop_print()
        )
        self.subwindows.protocol('WM_DELETE_WINDOW', lambda: self.stop_print())

        self.CoreProcess.progress.addCallback(
            lambda e: self.subwindows.update_progress_bar({
                "progress": self.CoreProcess.progress.get(),
                "label": self.model.get_locale()['sub_windows_'][1] % (self.CoreProcess.cont, self.CoreProcess.black_pixel, str(round(self.CoreProcess.cont*100/self.CoreProcess.black_pixel))+' %')
            })
        )

        self.CoreProcess.progress.addCallback(
            lambda e: self.stop_print() if self.CoreProcess.progress.get() == 100 else True
        )

        self.CoreProcess.user_stop.addCallback(
            lambda e: self.stop_print() if self.CoreProcess.user_stop.get() else True
        )

        Thread(target=self.CoreProcess.print_img).start()

    def stop_print(self):
        # self.CoreProcess.user_stop.set(True)
        self.CoreProcess.arduino_sender('U', 0, 0)
        self.subwindows.destroy_windows()
