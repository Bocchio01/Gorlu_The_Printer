import logging

from views.sub.Vprinthand import PrintHandView
from controllers.Cabstraction import ControllerABC
from controllers.CoreProcess import CoreProcess
import math


class PrintHandController:
    def __init__(self, controller: ControllerABC):
        logging.debug(f"TemplateController")
        self.root = controller.root
        self.model = controller.model

        self.view = PrintHandView(
            self.root,
            self.model.get_locale()['PrintHandFrame'],
            self.model.get_gui_opt()
        )

        self.CoreProcess = CoreProcess(controller)

        self.view.setting_button_0.config(
            command=lambda: self.view.visualizer_board.delete('all')
        )

        self.view.setting_button_1.config(
            command=lambda: self.model.PrintHandModel.save_canvas(
                self.view.visualizer_board
            )
        )

        self.view.visualizer_board.bind(
            '<Button-1>',
            self.model.PrintHandModel.savePosn
        )
        self.view.visualizer_board.bind(
            '<B1-Motion>',
            self.model.PrintHandModel.savePosn
        )

        self.model.PrintHandModel.lasty.addMultipleCallback(
            [
                lambda e: self.CoreProcess.arduino_sender(
                    pen=self.model.PrintHandModel.pen,
                    X=self.model.PrintHandModel.lastx.get(),
                    Y=self.model.PrintHandModel.lasty.get()
                ),
                lambda e: self.view.addLine(
                    [
                        self.model.PrintHandModel.x,
                        self.model.PrintHandModel.y
                    ],
                    [
                        self.model.PrintHandModel.lastx.get(),
                        self.model.PrintHandModel.lasty.get()
                    ]
                ) if self.model.PrintHandModel.pen == 'D' else True
            ]
        )
