from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPlainTextEdit
import sys
from PyQt5 import QtGui


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt QplainTextEdit"
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
        plainTextEdit = QPlainTextEdit()
        vbox.addWidget(plainTextEdit)
        plainTextEdit.setPlaceholderText("This is the placeholder for the plain")
        #plainTextEdit.setReadOnly(True)
        text = "Please suck my cock"
        plainTextEdit.appendPlainText(text)
        #plainTextEdit.setUndoRedoEnabled(False)
        self.setLayout(vbox)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())

