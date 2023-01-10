import sys
from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Combo Box Demo")
        
        self.combobox = QComboBox()
        self.combobox.addItem("blues")
        self.combobox.addItems(["jazz", "hiphop", "lofi", "afro"])

        button_A = QPushButton("Button A")
        button_A.clicked.connect(self.print_choice)

        button_B = QPushButton("Button B")
        
        layout = QVBoxLayout()
        layout.addWidget(self.combobox)
        layout.addWidget(button_A)
        layout.addWidget(button_B)

        self.setLayout(layout)

    def print_choice(self):
        print(self.combobox.currentText())

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.resize(200, 200)
    window.show()
    app.exec()