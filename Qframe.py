from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QHBoxLayout, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 Frame class"
        self.top = 500
        self.left = 500
        self.width = 600
        self.height = 200
        self.iconName = "transistor.jpg"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet('background-color:white')

        hbox = QHBoxLayout()
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color:blue")
        #frame.setLineWidth(0.6)
        hbox.addWidget(frame)

        btn = QPushButton("click me")
        btn.setStyleSheet("color:white")
        btn.setStyleSheet("background-color:green")
        hbox.addWidget(btn)
        self.setLayout(hbox)
        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())