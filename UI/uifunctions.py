from UI.ui_main import Ui_MainWindow
from model.appsettings import AppSettings

class UiFunctions:
	def __init__(self):
		super(UiFunctions, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

	
	def set_ui_definitions(self):

		settings = AppSettings()
		self.settings = settings.items

		self.ui.stackedWidgetMain.setCurrentWidget(self.ui.pageHome)
		self.ui.actionHome.triggered.connect(lambda e:self.ui.stackedWidgetMain.setCurrentIndex(0))
		self.ui.actionArduino_Config.triggered.connect(lambda e:self.ui.stackedWidgetMain.setCurrentIndex(1))
		
		#screen = QDesktopWidget().screenGeometry()     
		#self.setGeometry(0, 0, 0.5*screen.width(), 0.5*screen.height())
		#self.setAttribute(Qt.WA_TranslucentBackground)
		#self.setWindowFlags(Qt.FramelessWindowHint| Qt.WindowSystemMenuHint| Qt.WindowMinimizeButtonHint)
		#self.setWindowState(Qt.WindowFullScreen)


		self.setWindowTitle("Gorlu the printer")
		# self.resize(self.settings["startup_size"][0], self.settings["startup_size"][1])
		# self.setMinimumSize(self.settings["minimum_size"][0], self.settings["minimum_size"][1])
		