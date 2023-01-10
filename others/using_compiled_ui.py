import sys
from PySide6.QtWidgets import QMessageBox, QApplication, QPushButton, QLineEdit, QWidget
from formset import Ui_FormSet

class Widget(QWidget, Ui_FormSet):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Using Compiled UI")
        self.clearButton.clicked.connect(self.clearSlot)
        self.submitButton.clicked.connect(self.submitSlot)

    def clearSlot(self):
        self.lineEdit.clear()
        self.textEdit.clear()

    def submitSlot(self):
        name = self.lineEdit.text().strip()
        if not name:
            QMessageBox.warning(self, "Submit Form", "Form incomplete")
            return

        story = self.textEdit.toPlainText().strip()
        if not story:
            QMessageBox.warning(self, "Submit Form", "Form incomplete")
            return
        
        QMessageBox.information(self, "Submit Form", str.format('{0} -> {1}', name, story))


if __name__=='__main__':
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())