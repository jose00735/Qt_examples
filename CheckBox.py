from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QGroupBox, QVBoxLayout, QHBoxLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt CheckBox"
        self.top = 500
        self.left = 500
        self.width = 100
        self.height = 400
        self.iconName = "transistor.jpg"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("transistor.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self. width, self.height, self.width)
        self.CreateCheckbox()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)
        self.label = QLabel("")
        self.label.setFont(QtGui.QFont("Sanserif", 13))
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()

    def CreateCheckbox(self):
        self.groupbox = QGroupBox("What is your favorite porn star?")
        self.groupbox.setFont(QtGui.QFont("Sanserif", 13))
        hboxlayout = QHBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QtGui.QIcon(self.iconName))
        self.check1.setIconSize(QtCore.QSize(40, 40))
        self.check1.setFont(QtGui.QFont("Sanserif", 13))
        self.check1.toggled.connect(self.OncheckBox_Toggled)
        hboxlayout.addWidget(self.check1)

        self.check2 = QCheckBox("C++")
        self.check2.setIcon(QtGui.QIcon(self.iconName))
        self.check2.setIconSize(QtCore.QSize(40, 40))
        self.check2.setFont(QtGui.QFont("Sanserif", 13))
        self.check2.toggled.connect(self.OncheckBox_Toggled)
        hboxlayout.addWidget(self.check2)

        self.check3 = QCheckBox("C#")
        self.check3.setIcon(QtGui.QIcon(self.iconName))
        self.check3.setIconSize(QtCore.QSize(40, 40))
        self.check3.setFont(QtGui.QFont("Sanserif", 13))
        self.check3.toggled.connect(self.OncheckBox_Toggled)
        hboxlayout.addWidget(self.check3)
        self.groupbox.setLayout(hboxlayout)

    def OncheckBox_Toggled(self):
        if self.check1.isChecked():
            self.label.setText(f'you have selected {self.check1.text()}')
        if self.check2.isChecked():
            self.label.setText(f'you have selected {self.check2.text()}')
        if self.check3.isChecked():
            self.label.setText(f'you have selected {self.check3.text()}')

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())