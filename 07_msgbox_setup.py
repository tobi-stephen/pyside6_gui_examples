import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class CustomWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        button = QPushButton("Click Me", self)
        button.clicked.connect(self.on_button_clicked)

        self.setCentralWidget(button)

    def on_button_clicked(self):
        # hard way of setting up message box
        msg_box = QMessageBox()
        msg_box.setMinimumSize(700, 200)
        msg_box.setWindowTitle('Message Box Setup')
        msg_box.setText('Hello and Welcome')
        msg_box.setInformativeText('Good today?')
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
        val = msg_box.exec()
        
        # convenience method for setting up message box
        # val = QMessageBox.critical(self, 'Message Box Setup', 'Good today?', QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

        if val == QMessageBox.StandardButton.Ok:
            result = "OK"
        else:
            result = "Cancel"

        print("User chose {0}".format(result))

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = CustomWindow()
    window.show()
    app.exec()