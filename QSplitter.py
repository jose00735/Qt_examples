from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFrame, QHBoxLayout, QSplitter
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

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

        hbox = QHBoxLayout()
        left = QFrame()
        left.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)

        lineedit = QLineEdit()
        lineedit.setStyleSheet("background-color:green")

        splitter1.addWidget(left)
        splitter1.addWidget(lineedit)
        splitter1.setSizes([200,200])
        splitter1.setStyleSheet("background-color:blue")

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        splitter2.setStyleSheet("background-color:blue")

        hbox.addWidget(splitter2)

        self.setLayout(hbox)


        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())