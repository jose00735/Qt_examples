from PyQt5.QtWidgets import QApplication, QListWidget, QMenuBar, QMainWindow, QDockWidget, QTextEdit
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class DockDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 QDockAble"
        self.top = 500
        self.left = 500
        self.width = 600
        self.height = 200
        self.iconName = "transistor.jpg"
        self.setWindowIcon(QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createDockWidget()

    def createDockWidget(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        file.addAction("New")
        file.addAction("save")
        file.addAction("Close")
        self.dock = QDockWidget("Dockable", self)
        self.listwidget = QListWidget()
        list = ["Python", "C++", "java", "c#"]
        self.listwidget.addItems(list)
        self.dock.setWidget(self.listwidget)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Dock = DockDialog()
    Dock.show()
    sys.exit(App.exec())