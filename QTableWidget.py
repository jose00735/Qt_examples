from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QTableWidget, QTableWidgetItem
import sys
from PyQt5 import QtGui


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt QTableWidget"
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 400
        self.creatingTables()
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("transistor.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self. width, self.height, self.width)

    def creatingTables(self):
        vbox = QVBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(3)

        tableWidget.setItem(0, 0, QTableWidgetItem("Name"))
        tableWidget.setItem(0, 1, QTableWidgetItem("Email"))
        tableWidget.setItem(0, 2, QTableWidgetItem("Phone No"))
        tableWidget.setItem(1, 0, QTableWidgetItem("jhon"))
        tableWidget.setItem(1, 1, QTableWidgetItem("jhon.com"))
        tableWidget.setItem(1, 2, QTableWidgetItem("3015406513"))

        vbox.addWidget(tableWidget)
        self.setLayout(vbox)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())

