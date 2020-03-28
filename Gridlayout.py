from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QVBoxLayout, QVBoxLayout, QGridLayout
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 GreatLayout"
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
        self.CreateLayout()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupBox)
        self.setLayout(self.vbox)
        self.show()

    def CreateLayout(self):
        self.groupBox = QGroupBox("what is your favorite pussy?")
        self.gridLayout = QGridLayout()

        self.button1 = QPushButton("Python", self)
        self.button1.setIcon(QtGui.QIcon(self.iconName))
        self.button1.setIconSize(QtCore.QSize(40, 40))
        self.button1.clicked.connect(self.ClickMe)
        self.button1.setMinimumHeight(40)
        self.gridLayout.addWidget(self.button1, 0, 0)

        self.button2 = QPushButton("C++", self)
        self.button2.setIcon(QtGui.QIcon(self.iconName))
        self.button2.setIconSize(QtCore.QSize(40, 40))
        self.button2.clicked.connect(self.ClickMe)
        self.button2.setMinimumHeight(40)
        self.gridLayout.addWidget(self.button2, 0, 1)

        self.button3 = QPushButton("Java", self)
        self.button3.setIcon(QtGui.QIcon(self.iconName))
        self.button3.setIconSize(QtCore.QSize(40, 40))
        self.button3.clicked.connect(self.ClickMe)
        self.button3.setMinimumHeight(40)
        self.gridLayout.addWidget(self.button3, 1, 0)

        self.button4 = QPushButton("C#", self)
        self.button4.setIcon(QtGui.QIcon(self.iconName))
        self.button4.setIconSize(QtCore.QSize(40, 40))
        self.button4.clicked.connect(self.ClickMe)
        self.button4.setMinimumHeight(40)
        self.gridLayout.addWidget(self.button4, 2, 0)

        self.groupBox.setLayout(self.gridLayout)


    def ClickMe(self):
        print("mango")





if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())





