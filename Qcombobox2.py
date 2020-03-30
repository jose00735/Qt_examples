from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QDialog, QPushButton, QComboBox, QLabel
import sys
from PyQt5.QtGui import QIcon, QFont

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 Combobox"
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
        items = ["java", "python", "C++", "C#"]
        self.combo = QComboBox()
        self.combo.addItems(items)
        self.combo.currentTextChanged.connect(self.ComboChange)

        self.label = QLabel("Henlo")
        self.label.setFont(QFont("Sanserif", 15))
        self.label.setStyleSheet("color:red")

        vbox.addWidget(self.label)
        vbox.addWidget(self.combo)

        self.setLayout(vbox)

    def ComboChange(self):
        text = self.combo.currentText()
        self.label.setText(f'You have selected {text}')


if __name__ == "__main__":
    App = QApplication(sys.argv)
    ComboBox = Window()
    ComboBox.show()
    sys.exit(App.exec())

