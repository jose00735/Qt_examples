from PyQt5.QtWidgets import QDialog, QLineEdit, QMessageBox, QInputDialog, QApplication, QListWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon
import sys


class ProgramingDialog(QDialog):
    def __init__(self, name, ProList = None):
        super(ProgramingDialog, self).__init__()
        self.name = name
        self.list = QListWidget()
        if ProList is not None:
            self.list.addItems(ProList)
            self.list.setCurrentRow(0)

        vbox = QVBoxLayout()

        for text, slot in (("add", self.add),
                             ("edit", self.edit),
                           ("remove", self.remove),
                           ("sort", self.sort),
                           ("close", self.close)
                            ):
            button = QPushButton(text)
            button.clicked.connect(slot)
            vbox.addWidget(button)
        hbox = QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addLayout(vbox)
        self.setLayout(hbox)
        self.setWindowTitle("PyQt5 Simple List Project")
        self.setWindowIcon(QIcon("Lg.jpg"))

    def add(self):
        row = self.list.currentRow()
        title = "Add {0}".format(self.name)
        string, ok = QInputDialog.getText(self, title, title)

        if ok and string is not None:
            self.list.insertItem(row, string)

    def edit(self):
        row = self.list.currentRow()
        item = self.list.item(row)

        if item is not None:
            title = f'Edit {self.name}'
            string, ok = QInputDialog.getText(self, title, title,
                                            QLineEdit.Normal, item.text())

            if ok and string is not None:
                item.setText(string)

    def remove(self):
        row = self.list.currentRow()
        item = self.list.item(row)

        if item is None:
            return
        reply = QMessageBox.question(self, "Remove {0}".format(self.name),
                             "Remove {0} '{1}'?".format(self.name, item.text()),
                            QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            item = self.list.takeItem(row)
            del item

    def sort(self):
        self.list.sortItems()

    def close(self):
        self.accept()



if __name__ == "__main__":
    programing = ["mariana", "papa", "mama", "moderlon"]
    App = QApplication(sys.argv)
    dialog = ProgramingDialog("Language", programing)
    dialog.exec_()