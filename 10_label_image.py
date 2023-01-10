import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel Image Demo")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("../lam_pharm.jpeg"))

        h_layout = QHBoxLayout()
        h_layout.addWidget(image_label)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)


if __name__=='__main__':
    app = QApplication(sys.argv)
    
    widget = Widget()
    widget.show()

    app.exec()