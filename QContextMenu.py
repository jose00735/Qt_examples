from PyQt5.QtWidgets import QApplication, QMenu, QMessageBox, QFileDialog, QTextEdit, QAction, QColorDialog, QMainWindow, QFontDialog
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtCore import QFileInfo


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 ContextMenu"
        self.top = 500
        self.left = 500
        self.width = 400
        self.height = 300
        self.iconName = "transistor.jpg"
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        newAction = contextMenu.addAction("New")
        openAction = contextMenu.addAction("Open")
        quitAction = contextMenu.addAction("exit")

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAction:
            self.close()



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
