from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Push button"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 100
        self.iconName = "transistor.jpg"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.CreateLayaut()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupBox)
        self.setLayout(self.vbox)
        self.show()

    def CreateLayaut(self):
        self.groupBox = QGroupBox("What is your favorite porn star")
        self.hboxlayout = QVBoxLayout()

        self.button1 = QPushButton("Suck", self)
        self.button1.setIcon(QtGui.QIcon(self.iconName))
        self.button1.setIconSize(QtCore.QSize(40, 40))
        self.button1.clicked.connect(self.ClickMe)
        self.button1.setMinimumHeight(40)
        self.hboxlayout.addWidget(self.button1)

        self.button2 = QPushButton("My", self)
        self.button2.setIcon(QtGui.QIcon(self.iconName))
        self.button2.setIconSize(QtCore.QSize(40, 40))
        self.button2.clicked.connect(self.ClickMe)
        self.button2.setMinimumHeight(40)
        self.hboxlayout.addWidget(self.button2)

        self.button3 = QPushButton("Dick", self)
        self.button3.setIcon(QtGui.QIcon(self.iconName))
        self.button3.setIconSize(QtCore.QSize(40, 40))
        self.button3.clicked.connect(self.ClickMe)
        self.button3.setMinimumHeight(40)
        self.hboxlayout.addWidget(self.button3)

        self.groupBox.setLayout(self.hboxlayout)

    def ClickMe(self):
        print("holi")






if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = Window()
    sys.exit(App.exec())
