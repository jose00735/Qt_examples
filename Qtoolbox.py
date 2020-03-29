from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QToolBox, QVBoxLayout, QWidget
import sys
from PyQt5 import QtGui


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 Progress bar"
        self.top = 500
        self.left = 500
        self.width = 300
        self.height = 100
        self.iconName = "transistor.jpg"
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color:gray ")
        self.initUI()
        self.show()

    def initUI(self):
        vbox = QVBoxLayout()
        toolboox = QToolBox()
        vbox.addWidget(toolboox)

        label = QLabel()
        toolboox.addItem(label, "python")

        label = QLabel()
        toolboox.addItem(label, "Java")

        label = QLabel()
        toolboox.addItem(label, "C++")

        self.setLayout(vbox)



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
