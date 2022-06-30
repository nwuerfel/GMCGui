import sys, math
from PySide2.QtWidgets import (QApplication, QMainWindow, QAction, QLineEdit,
                                QWidget, QVBoxLayout, QComboBox, QLabel,
                                QPushButton)
from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtGui import QValidator, QDoubleValidator, QRegExpValidator

class RunButton(QWidget):

    def __init__(self,title):
        QWidget.__init__(self)
        self.title = title
        self.button = QPushButton(title)

        #self.icon // hell yeah draw my own

        self.setLayout(self.layout)

