import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QTabWidget, QHBoxLayout, QVBoxLayout, QListWidgetItem, QLineEdit, QLabel

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tab Widget Demo")

        tab_widget = QTabWidget(self)

        label = QLabel("Name:")
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Enter name here")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(line_edit)
        form_widget = QWidget()
        form_widget.setLayout(h_layout)

        tab_widget.addTab(form_widget, "hello")

        button_A = QPushButton("A")
        button_B = QPushButton("B")
        button_C = QPushButton("C")

        v_layout = QVBoxLayout()
        v_layout.addWidget(button_A)
        v_layout.addWidget(button_B)
        v_layout.addWidget(button_C)
        letter_widget = QWidget()
        letter_widget.setLayout(v_layout)
        tab_widget.addTab(letter_widget, "letter")



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.resize(200, 200)
    window.show()
    app.exec()