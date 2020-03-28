from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget, QLabel
import sys
from PyQt5 import QtGui

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 WhatIsThis class"
        self.top = 500
        self.left = 500
        self.width = 300
        self.height = 400
        self.iconName = "transistor.jpg"
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        label = QLabel("Focus and press shift + F1")
        hbox.addWidget(label)

        button = QPushButton("Click ME", self)
        button.setWhatsThis("this is a button")
        hbox.addWidget(button)

        self.setLayout(hbox)
        self.show()



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())