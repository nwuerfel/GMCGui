from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QLineEdit
from PySide2.QtCore import QObject, Signal, Slot
from . import MainWidget

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("GMC GUI")

        self.menu = self.menuBar()
        self.shortcutMenu = self.menu.addMenu("Shortcuts")

        exitAction = QAction("Exit",self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(self.exit_app)

        self.shortcutMenu.addAction(exitAction)
        mainWidget = MainWidget.MainWidget()
        self.setCentralWidget(mainWidget)

    @Slot()
    def exit_app(self):
        QApplication.quit()

