from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QWidget, QVBoxLayout, QDialog
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QFont


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
        self.btn = QPushButton("Open Second Dialog")
        self.btn.setFont(QFont("Sanserif", 13))
        self.btn.clicked.connect(self.openSecondDialog)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)

    def openSecondDialog(self):
        mydialog = QDialog(self)
        mydialog.show()
        #mydialog.setModal(True)
        #mydialog.exec()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())

