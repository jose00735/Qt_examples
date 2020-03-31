from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QPushButton, QWizard
import sys
from PyQt5 import QtGui


class Window(QWidget):
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

        vbox = QVBoxLayout()
        button = QPushButton("Launch")
        button.clicked.connect(self.btn_clicked)
        vbox.addWidget(button)
        self.setLayout(vbox)
        self.wizard = QWizard()
        self.wizard.setWindowTitle("Launching")

    def btn_clicked(self):
        self.wizard.open()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())

