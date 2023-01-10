import sys
from PySide6.QtWidgets import QSizePolicy, QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stretches and Size Policies")
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.)

        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        button_4 = QPushButton("four")
        button_5 = QPushButton("five")

        label = QLabel("What:")
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Enter What here")

        # Setting the stretch unit size
        h_layout = QHBoxLayout()
        h_layout.addWidget(button_1, 2)
        h_layout.addWidget(button_2, 1)
        h_layout.addWidget(button_3, 1)

        # Setting the stretch unit size
        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(button_4, 1)
        h_layout_1.addWidget(button_5, 2)

         # Setting the stretch unit size
        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(label, 1)
        h_layout_2.addWidget(line_edit, 2)

        v_layout = QVBoxLayout(self)
        v_layout.addLayout(h_layout)
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.resize(400, 100)
    window.show()
    sys.exit(app.exec())