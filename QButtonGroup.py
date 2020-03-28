from PyQt5.QtWidgets import QApplication, QLabel, QButtonGroup, QPushButton, QVBoxLayout, QWidget
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 Qbutton group"
        self.top = 500
        self.left = 500
        self.width = 100
        self.height = 200
        self.iconName = "transistor.jpg"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        hbox = QVBoxLayout()

        self.label = QLabel("Hello")
        self.label.setFont(QtGui.QFont("Sanserif", 10))
        hbox.addWidget(self.label)
        self.buttongroup = QButtonGroup()
        self.buttongroup.buttonClicked[int].connect(self.onButton_clicked)

        button = QPushButton("Python")
        self.buttongroup.addButton(button, 1)
        button.setMinimumHeight(70)
        hbox.addWidget(button)

        button1 = QPushButton("Java")
        self.buttongroup.addButton(button1, 2)
        button1.setMinimumHeight(70)
        button1.setIcon(QtGui.QIcon(self.iconName))
        button1.setIconSize(QtCore.QSize(60, 60))
        button1.setFont(QtGui.QFont("Sanserif", 15))
        hbox.addWidget(button1)

        button2 = QPushButton("JOSE")
        self.buttongroup.addButton(button2, 3)
        button2.setMinimumHeight(70)
        hbox.addWidget(button2)

        self.setLayout(hbox)
        self.show()

    def onButton_clicked(self, id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.label.setText(button.text() + " was Clicked")

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = window()
    sys.exit(App.exec())


