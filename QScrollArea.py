from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QFormLayout, QGroupBox, QLabel, QScrollArea
import sys
from PyQt5 import QtGui


class Window(QWidget):
    def __init__(self, val):
        super().__init__()
        self.title = "Pyqt5 QscrollArea"
        self.top = 500
        self.left = 500
        self.width = 600
        self.height = 200
        self.iconName = "transistor.jpg"
        self.val = val
        self.InitWindow()
        self.show()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        formLayout = QFormLayout()
        groupbox = QGroupBox("This is group box")

        labelList = []
        buttonlist = []

        for index in range(self.val):
            labelList.append(QLabel("Label"))
            buttonlist.append(QPushButton("Click me"))
            formLayout.addRow(labelList[index], buttonlist[index])

        groupbox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window(20)
    sys.exit(App.exec())