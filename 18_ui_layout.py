import sys
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit
from PySide6.QtUiTools import QUiLoader

class Widget:
    def __init__(self):
        loader = QUiLoader()
        self.window: QWidget = loader.load('form_layout.ui', None)
        self.window.submit_button.clicked.connect(self.submit_slot)
    
    def submit_slot(self):
        name_edit: QLineEdit = self.window.name_edit
        job_edit: QLineEdit = self.window.job_edit

        print(name_edit.text(), "-", job_edit.text())
        
    def show(self):
        self.window.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
