from PyQt5.QtWidgets import QApplication, QListWidgetItem, QWidget, QHBoxLayout, QListWidget
from PyQt5.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.myListWidget1 = QListWidget()
        self.myListWidget2 = QListWidget()

        self.setWindowTitle("Drag And Drop")

        self.myListWidget2.setViewMode(QListWidget.IconMode)
        self.myListWidget1.setAcceptDrops(True)
        self.myListWidget1.setDragEnabled(True)

        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(True)

        self.setGeometry(300, 300, 500, 400)
        self.hboxlayout = QHBoxLayout()

        self.hboxlayout.addWidget(self.myListWidget1)
        self.hboxlayout.addWidget(self.myListWidget2)

        l1 = QListWidgetItem(QIcon("Cut.png"), "Cut")
        l2 = QListWidgetItem(QIcon("Copy.png"), "Copy")
        l3 = QListWidgetItem(QIcon("Paste.png"), "Paste")
        l4 = QListWidgetItem(QIcon("Save.png"), "Save")

        self.myListWidget1.insertItem(1, l1)
        self.myListWidget1.insertItem(2, l2)
        self.myListWidget1.insertItem(3, l3)
        self.myListWidget1.insertItem(4, l4)

        QListWidgetItem()



        self.setLayout(self.hboxlayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())


