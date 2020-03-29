from PyQt5.QtWidgets import QApplication, QTextEdit, QPushButton, QAction, QMenuBar, QMainWindow
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 TextEdit"
        self.top = 500
        self.left = 500
        self.width = 400
        self.height = 300
        self.iconName = "transistor.jpg"
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.CreateMenu()
        self.createEditor()
        self.show()

    def CreateMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        HelpMenu = mainMenu.addMenu("Help")

        copyAction = QAction(QIcon(self.iconName), "Transistor", self)
        copyAction.setShortcut("ctrpl+c")
        fileMenu.addAction(copyAction)

        cutAction = QAction(QIcon(self.iconName), "Otravaina", self)
        cutAction.setShortcut("ctrl+x")
        editMenu.addAction(cutAction)

        exitAction = QAction(QIcon(self.iconName), "Exit", self)
        exitAction.setShortcut("Exit")
        exitAction.triggered.connect(self.exitWindow)
        HelpMenu.addAction(exitAction)

        toolbar = self.addToolBar("ToolBar")
        toolbar.addAction(copyAction)
        toolbar.addAction(cutAction)
        toolbar.addAction(exitAction)

    def exitWindow(self):
        self.close()

    def createEditor(self):
        self.TextEdit = QTextEdit(self)
        self.setCentralWidget(self.TextEdit)



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
