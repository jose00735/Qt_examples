from PyQt5.QtWidgets import QApplication, QMainWindow, QSizeGrip, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 Frameless Window"
        self.top = 500
        self.left = 500
        self.width = 600
        self.height = 200
        self.iconName = "transistor.jpg"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        vbox = QVBoxLayout()
        sizegrip = QSizeGrip(self)
        vbox.addWidget(sizegrip)
        self.setLayout(vbox)
        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())