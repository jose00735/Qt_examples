from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QHBoxLayout, QLabel
import sys
from PyQt5 import QtGui


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 Line edit"
        self.top = 500
        self.left = 500
        self.width = 300
        self.height = 400
        self.iconName = "transistor.jpg"
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        hbox = QHBoxLayout()
        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont(QtGui.QFont("Sanserif", 10)))
        self.lineedit.returnPressed.connect(self.onPressed)
        hbox.addWidget(self.lineedit)
        self.label = QLabel("")
        self.label.setFont(QtGui.QFont("Sanserif",15))
        hbox.addWidget(self.label)
        self.setLayout(hbox)

        self.show()

    def onPressed(self):
        self.label.setText(self.lineedit.text())

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())