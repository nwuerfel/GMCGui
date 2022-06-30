import sys, math
from PySide2.QtWidgets import (QApplication, QMainWindow, QAction, QLineEdit,
                                QWidget, QVBoxLayout, QComboBox, QLabel)
from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtGui import QValidator, QDoubleValidator, QRegExpValidator
from. import Selectors as slx

RunChoices = ["Run 1", "Run 2", "Run 3", "Run 5", "Run 6"]
OutputChoices = ["SQL", "SQL and ROOT"]
TargetChoices = ["LH2", "Empty", "LD2", "None", "C", "Fe", "W"]
EventPositionChoices = ["Target", "Dump"]
GeneratorChoices = ["DY", "JPsi", "Psip"]


class BasicOptions(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.group = QVBoxLayout()

        self.runComboBox = slx.ComboBox("Run Preset", RunChoices)
        self.outputComboBox = slx.ComboBox("Output Format", OutputChoices)
        self.targetComboBox = slx.ComboBox("Target Choice", TargetChoices)
        self.eventposComboBox = slx.ComboBox("Event Position", EventPositionChoices)
        self.generatorComboBox = slx.ComboBox("Event Generator", GeneratorChoices )
        self.NEvents = slx.IntTextEntryBox("Events to Generate","Number of Events",1)
        self.NGridJobs = slx.IntTextEntryBox("Grid Jobs to Run", "Number of Jobs",1)
        self.OutputFilePrompt = slx.TextEntryBox("Output Path","/path/to/output/file")

        self.group.addWidget(self.runComboBox)
        self.group.addWidget(self.outputComboBox)
        self.group.addWidget(self.targetComboBox)
        self.group.addWidget(self.eventposComboBox)
        self.group.addWidget(self.generatorComboBox)
        self.group.addWidget(self.NEvents)
        self.group.addWidget(self.NGridJobs)
        self.group.addWidget(self.OutputFilePrompt)
        
        self.setLayout(self.group) 
        
        
        
