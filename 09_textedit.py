import sys
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton


class Widget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("TextEdit Demo")

        self.text_edit = QTextEdit(self)

        current_text_button = QPushButton("Cur Text")
        current_text_button.clicked.connect(self.current_txt_clicked)

        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.text_edit.copy)
        
        cut_button = QPushButton("Cut")
        cut_button.clicked.connect(self.text_edit.cut)
        
        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.text_edit.paste)
        
        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.text_edit.undo)

        redo_button = QPushButton("Redo")
        redo_button.clicked.connect(self.text_edit.redo)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.text_edit.clear)

        set_plain_text_button = QPushButton("Plain Text")
        set_plain_text_button.clicked.connect(self.set_plain_text)

        set_html_button = QPushButton("HTML")
        set_html_button.clicked.connect(self.set_html)

        h_layout = QHBoxLayout()
        h_layout.addWidget(current_text_button)
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(clear_button)
        h_layout.addWidget(set_plain_text_button)
        h_layout.addWidget(set_html_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)

    def set_plain_text(self):
        self.text_edit.setPlainText(self.text_edit.toPlainText())

    def set_html(self):
        # self.text_edit.setHtml("<h1>The Sky is Crying</h1><ul><li>Stevie</li><li>Ray</li><li>Vaughn</li></ul>")
        self.text_edit.setHtml(self.text_edit.toPlainText())

    def current_txt_clicked(self):
        print(self.text_edit.toPlainText())
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    app.exec()
    