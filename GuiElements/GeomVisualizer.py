from PySide2.QtWidgets import (QApplication, QMainWindow, QAction, 
                                QLineEdit, QWidget, QLabel,
                                QGridLayout, QTabWidget)
from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtGui import QPixmap

class GeomVisualizer(QWidget):

    def __init__(self):
        QWidget.__init__(self) 

        self.canvas = QPixmap('./GuiElements/images/placeholder_datavisualizer.jpg')

        self.label = QLabel()
        self.label.setPixmap(self.canvas)


        self.grid = QGridLayout()
        self.grid.addWidget(self.label,0,0)

        self.label.show()

        self.setLayout(self.grid)
