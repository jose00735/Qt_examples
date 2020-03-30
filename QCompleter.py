from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLineEdit, QCompleter, QVBoxLayout, QDialog, QPushButton, QComboBox, QLabel
import sys
from PyQt5.QtGui import QIcon, QFont

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 QCompleter"
        self.top = 500
        self.left = 500
        self.width = 600
        self.height = 200
        self.iconName = "transistor.jpg"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.InitUI()


    def InitUI(self):
        vbox = QVBoxLayout()
        names = ["2n3904", "Oscar", "Lilian", "Niko", "Moderlon"]
        completer = QCompleter(names)
        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(completer)

        vbox.addWidget(self.lineedit)

        self.setLayout(vbox)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())

