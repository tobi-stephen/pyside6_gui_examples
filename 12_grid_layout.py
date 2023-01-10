import sys
from PySide6.QtWidgets import QSizePolicy, QApplication, QGridLayout, QPushButton, QWidget

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout Demo")

        ba = QPushButton("A")
        bb = QPushButton("B")
        
        bc = QPushButton("C")
        bc.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        bd = QPushButton("D")
        be = QPushButton("E")
        bf = QPushButton("F")
        bg = QPushButton("G")

        grid_layout = QGridLayout(self)
        grid_layout.addWidget(ba, 0, 0)
        grid_layout.addWidget(bb, 0, 1, 1, 2)
        grid_layout.addWidget(bc, 1, 0, 2, 1)
        grid_layout.addWidget(bd, 1, 1)
        grid_layout.addWidget(be, 1, 2)
        grid_layout.addWidget(bf, 2, 1)
        grid_layout.addWidget(bg, 2, 2)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec())