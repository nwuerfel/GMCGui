from PySide2.QtWidgets import (QApplication, QMainWindow, QAction, QLineEdit,
                                QWidget, QGridLayout)
from PySide2.QtCore import QObject, Signal, Slot
from . import DataAndOptionsTab
from . import BasicOptions

class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        self.DataAndOptionsTab = DataAndOptionsTab.DataAndOptionsTab()
        self.optionsGroup = BasicOptions.BasicOptions()

        self.layout = QGridLayout()

        self.layout.setColumnMinimumWidth(0,444)
        self.layout.setColumnMinimumWidth(1,40)
        self.layout.setRowMinimumHeight(0,10)
        self.layout.setRowMinimumHeight(4,10)

        self.layout.addWidget(self.DataAndOptionsTab,1,0)
        self.layout.addWidget(self.optionsGroup,1,2)
        self.setLayout(self.layout)
        
