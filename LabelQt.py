from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QMainWindow, QVBoxLayout
import sys
from PyQt5 import QtGui

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 window"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 100
        self.iconName = "transistor.jpg"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.vbox = QVBoxLayout()
        self.label = QLabel("This is PyQt5 Label")
        self.vbox.addWidget(self.label)
        self.label2 = QLabel("This is a bigger label")
        self.label2.setFont(QtGui.QFont("Sanserif", 20))
        self.label2.setStyleSheet("color:red")
        self.vbox.addWidget(self.label2)
        self.setLayout(self.vbox)
        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())