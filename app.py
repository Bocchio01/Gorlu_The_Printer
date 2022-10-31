import logging

from views.view import View
from controllers.controller import Controller
from models.model import Model

from PIL import EpsImagePlugin

EpsImagePlugin.gs_windows_binary = r'C:/Program Files/gs/gs9.53.3/bin/gswin64c'

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s:%(funcName)s():%(lineno)i: %(message)s"
)


if __name__ == "__main__":
    c = Controller(Model(), View())
    c.start()
