import sys
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Labels and LineEdits")

        label = QLabel("Name: ", self)
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.on_text_changed)
        self.line_edit.cursorPositionChanged.connect(self.on_cursor_changed)

        button = QPushButton("Get data")
        button.clicked.connect(self.on_button_clicked)
        self.holder_label = QLabel("HERE")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.holder_label)

        self.setLayout(v_layout)

    def on_button_clicked(self):
        text = self.line_edit.text().strip()
        if not text: return
        self.holder_label.setText(text)
        print("Name entered:", text)

    def on_text_changed(self):
        text = self.line_edit.text().strip()
        if not text: return
        self.holder_label.setText(text)

    def on_cursor_changed(self, old, new):
        print("old: ", old)
        print("new: ", new)

if __name__=='__main__':
    app = QApplication(sys.argv)
    
    widget = Widget()
    widget.show()

    app.exec()