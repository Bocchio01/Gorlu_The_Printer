import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

from UI.ui_main import Ui_MainWindow
from UI.uifunctions import UiFunctions


class GUI(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		UiFunctions.set_ui_definitions(self)

class CMD():
	def __init__(self):
		print("CMD")


if __name__ == "__main__":
	if (len(sys.argv) > 1):
		cmd = CMD(sys.argv[1:])
	else:
		app = QApplication(sys.argv)
		gui = GUI()
		gui.show()
		sys.exit(app.exec())