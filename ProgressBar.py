from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QProgressBar, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal
import time

class MyThread(QThread):
    change_value = pyqtSignal(int)

    def run(self):
        cnt = 0
        while cnt < 100:
            cnt+=1
            time.sleep(0.3)
            self.change_value.emit(cnt)


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 Progress bar"
        self.top = 500
        self.left = 500
        self.width = 300
        self.height = 100
        self.iconName = "transistor.jpg"
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.init_ui()
        self.show()

    def init_ui(self):
        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        self.progressbar.setMaximum(100)
        vbox.addWidget(self.progressbar)

        self.button = QPushButton("Run Progress bar")
        self.button.clicked.connect(self.starProgressbar)
        self.button.setFont(QtGui.QFont("Sanserif", 13))
        self.button.setIcon(QtGui.QIcon(self.iconName))
        self.button.setIconSize(QtCore.QSize(50, 50))
        vbox.addWidget(self.button)

        self.setLayout(vbox)

    def starProgressbar(self):
        self.thread = MyThread()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()

    def setProgressVal(self, val):
        self.progressbar.setValue(val)



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
