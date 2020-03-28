from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 QDial"
        self.top = 500
        self.left = 500
        self.width = 600
        self.height = 200
        self.iconName = "transistor.jpg"
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spin_changed)
        vbox.addWidget(self.spinbox)

        self.label = QLabel()
        self.label.setFont(QtGui.QFont("sanserif", 15))
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()

    def spin_changed(self):
        spinValue = self.spinbox.value()
        self.label.setText(f'Current Value is: {spinValue}')

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

