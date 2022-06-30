from PySide2.QtWidgets import (QApplication, QMainWindow, QAction, 
                                QLineEdit, QWidget, QLabel,
                                QGridLayout, QTabWidget)
from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtGui import QPixmap
from . import GeomVisualizer as gv      
class DataAndOptionsTab(QTabWidget):
    
    def __init__(self):
        QTabWidget.__init__(self)
        self.GeomPage = gv.GeomVisualizer()
        self.addTab(self.GeomPage,"Geometry Visualizer")
        self.setTabPosition(QTabWidget.North)

        

