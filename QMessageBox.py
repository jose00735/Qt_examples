from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog, QTextEdit, QAction, QColorDialog, QMainWindow, QFontDialog
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtCore import QFileInfo


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Pyqt5 QmessageBox"
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

        pdfAction = QAction(QIcon("Pdf.png"), "Export PDF", self)
        pdfAction.triggered.connect(self.pdfExport)
        fileMenu.addAction(pdfAction)

        printAction = QAction(QIcon("print.png"), "Print", self)
        printAction.triggered.connect(self.printDialog)
        fileMenu.addAction(printAction)

        HelpAction = QAction(QIcon("Help.png"), "Help", self)
        HelpAction.triggered.connect(self.AboutMessageBox)
        HelpMenu.addAction(HelpAction)

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

        choiceAction = QAction(QIcon("New_file.png"), "Choice Message", self)
        choiceAction.triggered.connect(self.choiceMessageBox)
        HelpMenu.addAction(choiceAction)

        toolbar = self.addToolBar("ToolBar")
        toolbar.addAction(copyAction)
        toolbar.addAction(cutAction)
        toolbar.addAction(pasteAction)
        toolbar.addAction(SaveAction)
        toolbar.addAction(colorAction)
        toolbar.addAction(fontAction)
        toolbar.addAction(printAction)
        toolbar.addAction(pdfAction)
        toolbar.addAction(HelpAction)
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

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec() == QPrintDialog.Accepted:
            self.TextEdit.print_(printer)

    def pdfExport(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf)//All Files")

        if fn != '':
            if QFileInfo(fn).suffix() == "":fn += '.pdf'
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.TextEdit.document().print_(printer)

    def AboutMessageBox(self):
        message = QMessageBox.about(self, "About Application", "this is a simple texteditor")

    def choiceMessageBox(self):
        message = QMessageBox.question(self, "Choice Message", "do you like PyQt5",
                                       QMessageBox.Yes | QMessageBox.No)
        if message == QMessageBox.Yes:
            self.TextEdit.setText("Yes I like pyQt5")
            print("Yes I like PyQt5")
        else:
            self.TextEdit.setText("No, I don't like pyQt5")
            print("No, I don't like pyQt5")

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
