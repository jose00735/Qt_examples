from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5 import QtGui


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt Window"
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 300
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("transistor.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self. width, self.height, self.width)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())

