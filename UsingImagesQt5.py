from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 window"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 100
        self.iconName = "transistor.jpg"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        Vbox = QVBoxLayout()
        label_Image = QLabel(self)
        pixmap = QPixmap("Lg.jpg")
        label_Image.setPixmap(pixmap)
        Vbox.addWidget(label_Image)
        self.setLayout(Vbox)


        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())