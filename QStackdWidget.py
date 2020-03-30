from PyQt5.QtWidgets import QApplication, QPushButton, QStackedWidget, QDialog, QVBoxLayout, QLabel
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QFont


class StackWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 StackdWidget"
        self.top = 500
        self.left = 500
        self.width = 600
        self.height = 200
        self.iconName = "transistor.jpg"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.StackedWidget()

    def StackedWidget(self):
        vbox = QVBoxLayout()
        self.stackWidget = QStackedWidget()
        vbox.addWidget(self.stackWidget)

        for x in range (0,8):
            label = QLabel(f'Stacked child {str(x)}')
            label.setFont(QFont("Sanserif", 15))
            label.setStyleSheet("color:red")

            self.stackWidget.addWidget(label)

            self.button = QPushButton(f'Stack {str(x)}')
            self.button.setStyleSheet("background-color:green")
            self.button.page = x

            self.button.clicked.connect(self.btn_clicked)

            vbox.addWidget(self.button)

        self.setLayout(vbox)


    def btn_clicked(self):
        self.button = self.sender()
        self.stackWidget.setCurrentIndex(self.button.page - 1)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    stackwidget = StackWidget()
    stackwidget.show()
    sys.exit(App.exec())