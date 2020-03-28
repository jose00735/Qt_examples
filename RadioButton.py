from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QGroupBox, QVBoxLayout, QHBoxLayout, QRadioButton
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt Window"
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
        self.radioButton()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.label = QLabel("")
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()

    def radioButton(self):
        self.groupBox = QGroupBox("What is your favorite tit ?")
        self.groupBox.setFont(QtGui.QFont("sanserif", 13))
        hboxlayout = QHBoxLayout()
        self.radiobtn1 = QRadioButton("Porn")
        self.radiobtn1.setChecked(True)
        self.radiobtn1.setIcon(QtGui.QIcon(self.iconName))
        self.radiobtn1.setIconSize(QtCore.QSize(40,40))
        self.radiobtn1.setFont(QtGui.QFont("Sanserif", 13))
        self.radiobtn1.toggled.connect(self.OnRadioBtn)
        hboxlayout.addWidget(self.radiobtn1)

        self.radiobtn2 = QRadioButton("Mango")
        self.radiobtn2.setIcon(QtGui.QIcon(self.iconName))
        self.radiobtn2.setIconSize(QtCore.QSize(40, 40))
        self.radiobtn2.setFont(QtGui.QFont("Sanserif", 13))
        self.radiobtn2.toggled.connect(self.OnRadioBtn)
        hboxlayout.addWidget(self.radiobtn2)

        self.radiobtn3 = QRadioButton("Vodka")
        self.radiobtn3.setIcon(QtGui.QIcon(self.iconName))
        self.radiobtn3.setIconSize(QtCore.QSize(40, 40))
        self.radiobtn3.setFont(QtGui.QFont("Sanserif", 13))
        self.radiobtn3.toggled.connect(self.OnRadioBtn)
        hboxlayout.addWidget(self.radiobtn3)

        self.groupBox.setLayout(hboxlayout)

    def OnRadioBtn(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label.setText("you have selected " + radioBtn.text())

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

