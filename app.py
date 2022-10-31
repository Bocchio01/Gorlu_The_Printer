import logging

from views.view import View
from controllers.controller import Controller
from models.model import Model


logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s:%(funcName)s():%(lineno)i: %(message)s"
)


if __name__ == "__main__":
    c = Controller(Model(), View())
    c.start()
