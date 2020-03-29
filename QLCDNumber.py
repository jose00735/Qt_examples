from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QVBoxLayout
import sys
from PyQt5 import QtGui
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 QLCDnumber"
        self.top = 500
        self.left = 500
        self.width = 600
        self.height = 200
        self.iconName = "transistor.jpg"
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.InitUI()
        self.show()

    def InitUI(self):
        vbox = QVBoxLayout()
        self.lcd = QLCDNumber()
        self.lcd.setStyleSheet("background-color:green")

        vbox.addWidget(self.lcd)
        self.setLayout(vbox)

        self.button = QPushButton("Random Number Generator")
        self.button.setStyleSheet("background-color:blue")
        self.button.clicked.connect(self.LCDHandler)
        vbox.addWidget(self.button)

    def LCDHandler(self):
        random = randint(1, 200)
        self.lcd.display(random)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
