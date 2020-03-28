from PyQt5.QtWidgets import QApplication, QWidget, QDial, QLabel, QVBoxLayout
import sys
from PyQt5 import QtGui


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

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(1000)
        self.dial.setValue(30)
        self.dial.valueChanged.connect(self.dial_changed)
        vbox.addWidget(self.label)
        vbox.addWidget(self.dial)
        self.setLayout(vbox)

        self.show()

    def dial_changed(self):
        getValue = self.dial.value()
        self.label.setText(f'Dial is Changing: {getValue}')


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())