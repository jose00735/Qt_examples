from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QCheckBox, QComboBox, QLabel, QDialog, QLineEdit, QTabWidget, QDialogButtonBox, QVBoxLayout, QGridLayout, QWidget, QGroupBox
import sys
from PyQt5.QtGui import QIcon

class Tab(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 tab Widget")
        self.setWindowIcon(QIcon("Lg.png"))

        vbox = QVBoxLayout()
        tabWidget = QTabWidget()

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        tabWidget.addTab(TabContact(), "Contact Details")
        tabWidget.addTab(TabPersonDetails(), "Personal Details")

        vbox.addWidget(tabWidget)
        vbox.addWidget(buttonbox)

        self.setLayout(vbox)

class TabContact(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        mainLayout = QVBoxLayout()
        groubox = QGroupBox("Select your gender: ")
        list = ["Male", "Female"]
        comobo = QComboBox()
        comobo.addItems(list)
        vbox.addWidget(comobo)

        groubox2 = QGroupBox("Select your favorites Programming Languages")
        python = QCheckBox("Python")
        Cpp = QCheckBox("Cpp")
        Java = QCheckBox("Java")
        vboxp = QVBoxLayout()
        vboxp.addWidget(python)
        vboxp.addWidget(Cpp)
        vboxp.addWidget(Java)
        groubox2.setLayout(vboxp)
        
        groubox.setLayout(vbox)
        mainLayout.addWidget(groubox)
        mainLayout.addWidget(groubox2)
        self.setLayout(mainLayout)




class TabPersonDetails(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        nameLabel = QLabel("Name: ")
        grid.addWidget(nameLabel, 0, 0)
        NameEdit = QLineEdit()
        grid.addWidget(NameEdit, 0, 1)

        Phone = QLabel("Phone: ")
        grid.addWidget(Phone, 1, 0)
        PhoneEdit = QLineEdit()
        grid.addWidget(PhoneEdit, 1, 1)

        email = QLabel("Email: ")
        grid.addWidget(email, 2, 0)
        phonEdit = QLineEdit()
        grid.addWidget(phonEdit, 2, 1)

        self.setLayout(grid)






if __name__ == "__main__":
    App = QApplication(sys.argv)
    tabDialog = Tab()
    tabDialog.show()
    App.exec()



