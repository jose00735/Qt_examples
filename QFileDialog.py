from PyQt5.QtWidgets import QPushButton ,QVBoxLayout, QApplication, QLabel, QDialog, QFileDialog
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap

class Window(QDialog):
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
        self.btn = QPushButton("Browse Image")
        self.btn.clicked.connect(self.browseImage)
        vbox.addWidget(self.btn)

        self.label = QLabel("")
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def browseImage(self):
        Fname = QFileDialog.getOpenFileName(self, "Open File", '~/', "Image files(*.jpg *.png)")
        imagePath = Fname[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())

