from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Push button"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "transistor.jpg"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.CreateButton()
        self.CreateButton()
        self.show()

    def CreateButton(self):
        self.button_hello = QPushButton("Hola", self)
        self.button_hello.setGeometry(QRect(100, 150, 111, 50))
        self.button_hello.setIcon(QtGui.QIcon(self.iconName))
        self.button_hello.setIconSize(QtCore.QSize(40, 40))
        self.button_hello.clicked.connect(self.ClickMe)

    def ClickMe(self):
        print("pinche puta")

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
