from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPlainTextEdit, QPushButton
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #Load the UI file
        uic.loadUi("DesignerUI.ui", self)

        #Define Our Widgets
        self.label = self.findChild(QLabel, "label")
        self.plaintextedit = self.findChild(QPlainTextEdit, "plainTextEdit")
        self.button = self.findChild(QPushButton, "pushButton")
        self.button2 = self.findChild(QPushButton, "pushButton_2")

        #Load the App
        self.show()

        #Do Something
        self.button.clicked.connect(self.clicker)
        self.button2.clicked.connect(self.clicker2)

    def clicker(self):
        self.label.setText("Hello World")
        self.plaintextedit.setPlainText("Hello World")

    def clicker2(self):
        self.plaintextedit.setPlainText("")

# Inititlize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()