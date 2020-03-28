from PyQt5.QtWidgets import QApplication, QGroupBox, QHBoxLayout, QRadioButton, QLabel, QButtonGroup, QPushButton, QVBoxLayout, QWidget
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 QGroupBox"
        self.top = 500
        self.left = 500
        self.width = 600
        self.height = 200
        self.iconName = "transistor.jpg"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        groupbox = QGroupBox("Select your favorite ass")
        groupbox.setFont(QtGui.QFont("Sanserif", 15))

        hbox.addWidget(groupbox)

        vbox = QVBoxLayout()

        radio1 = QRadioButton("Amaranta Hank")
        vbox.addWidget(radio1)

        radio2 = QRadioButton("Mandy Muse")
        vbox.addWidget(radio2)

        radio3 = QRadioButton("Anaconda")
        vbox.addWidget(radio3)

        groupbox.setLayout(vbox)
        self.setLayout(hbox)
        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
