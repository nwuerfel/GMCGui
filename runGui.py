import sys
import GuiElements.MainWindow as mw
from PySide2.QtWidgets import QApplication
from PySide2 import QtCore, QtGui

if __name__ == "__main__":

    # Qt Application
    app = QApplication(sys.argv)
    window = mw.MainWindow()
    window.resize(888, 480)
    window.show()

    # Execute application
    sys.exit(app.exec_())

