import sys, math
from PySide2.QtWidgets import (QApplication, QMainWindow, QAction, QLineEdit,
                                QWidget, QVBoxLayout, QComboBox, QLabel)
from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtGui import QValidator, QDoubleValidator, QRegExpValidator



class ComboBox(QWidget):

    def __init__(self,title,items):
        QWidget.__init__(self)
        self.title = title
        self.comboBox = QComboBox()
        self.comboBox.addItems(items)

        #self.icon // hell yeah draw my own

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel(self.title))
        self.layout.addWidget(self.comboBox)
        self.setLayout(self.layout)

class UserEntryBox(QWidget):
    def __init__(self,title,label):
        QWidget.__init__(self)
        self.title = title
        self.textInput = QLineEdit()
        self.textInput.setPlaceholderText(label)

        #self.icon // hell yeah draw my own
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel(self.title))
        self.layout.addWidget(self.textInput)
        self.textInput.setStyleSheet("background-color : rgba(255,0,0,75);")
        self.setLayout(self.layout)
        self.textInput.editingFinished.connect(self.saveInput)
        self.textInput.textChanged[str].connect(self.changeColor)

    @Slot()
    def saveInput(self):
        if self.textInput.text():
            userInput = self.textInput.text()
            print("user input: "+ str(userInput))
  
    @Slot()
    def changeColor(self):
        if self.textInput.text():
            self.textInput.setStyleSheet("background-color :  \
                                            rgba(255,255,255,75);")    
        else:
            self.textInput.setStyleSheet("background-color : \
                                            rgba(255,0,0,75);")
   
class TextEntryBox(UserEntryBox):

    def __init__(self,title,label):
        UserEntryBox.__init__(self,title,label)
        #self.icon // hell yeah draw my own

        #regex sucks but might be possible
#        self.regexVal = QRegExpValidator()
#        self.textInput.setValidator(self.regexVal) 
        self.textInput.textChanged[str].connect(self.readInput)


    @Slot()
    def readInput(self, ustring):
        return
        
         
class IntTextEntryBox(UserEntryBox):
    
    def __init__(self,title,label,sign=0):
        UserEntryBox.__init__(self,title,label)
        if(sign==0):
            self.dValidator = QDoubleValidator()
        elif(sign > 0):
            #max signed int
            self.dValidator = QDoubleValidator(0,math.inf,0,self)
        else:
            #lowest signed int
            self.dValidator = QDoubleValidator(-math.inf,0,0,self)
        self.dValidator.setNotation(QDoubleValidator.StandardNotation)
        self.textInput.setValidator(self.dValidator)
        self.textInput.textChanged[str].connect(self.readInput)

    @Slot()
    def readInput(self, text):
        return 
