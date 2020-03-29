from PyQt5.QtWidgets import QApplication, QTextEdit, QAction, QColorDialog, QMainWindow, QFontDialog
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

        copyAction = QAction(QIcon("Copy.png"), "Copy", self)
        copyAction.setShortcut("ctrl+c")
        editMenu.addAction(copyAction)

        cutAction = QAction(QIcon("Cut.png"), "Cut", self)
        cutAction.setShortcut("ctrl+x")
        editMenu.addAction(cutAction)

        pasteAction = QAction(QIcon("Paste.png"), "Paste", self)
        pasteAction.setShortcut("ctrl+v")
        editMenu.addAction(pasteAction)

        SaveAction = QAction(QIcon("Save.png"), "Save", self)
        SaveAction.setShortcut("ctrl+g")
        fileMenu.addAction(SaveAction)

        exitAction = QAction(QIcon("Exit.png"), "Exit", self)
        exitAction.setShortcut("Exit")
        exitAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exitAction)

        fontAction = QAction(QIcon("Font.png"), "Font", self)
        fontAction.setShortcut("Ctrl+f")
        fontAction.triggered.connect(self.fontDialog)
        viewMenu.addAction(fontAction)

        colorAction = QAction(QIcon("Color.png"), "Color", self)
        colorAction.triggered.connect(self.colorDialog)
        viewMenu.addAction(colorAction)

        toolbar = self.addToolBar("ToolBar")
        toolbar.addAction(copyAction)
        toolbar.addAction(cutAction)
        toolbar.addAction(pasteAction)
        toolbar.addAction(SaveAction)
        toolbar.addAction(colorAction)
        toolbar.addAction(fontAction)
        toolbar.addAction(exitAction)

    def exitWindow(self):
        self.close()

    def createEditor(self):
        self.TextEdit = QTextEdit(self)
        self.setCentralWidget(self.TextEdit)

    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.TextEdit.setFont(font)

    def colorDialog(self):
        color = QColorDialog.getColor()
        self.TextEdit.setTextColor(color)




if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
