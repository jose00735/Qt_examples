from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QListWidget, QLabel
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

        self.list = QListWidget()
        self.list.insertItem(0, "Python")
        self.list.insertItem(1, "Java")
        self.list.insertItem(2, "C++")
        self.list.clicked.connect(self.listview_clicked)

        self.label = QLabel()
        self.label.setFont(QFont("Sanserif", 12))

        vbox.addWidget(self.list)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def listview_clicked(self):
        item = self.list.currentItem()
        self.label.setText(str(item.text()))


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())

