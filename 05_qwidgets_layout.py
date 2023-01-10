import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Widget")
        
        buttonOne = QPushButton("Button One")
        buttonOne.clicked.connect(self.bOne_clicked)
        buttonTwo = QPushButton("Button Two")
        buttonTwo.clicked.connect(self.bTwo_clicked)
        
        layout = QVBoxLayout()
        layout.addWidget(buttonOne)
        layout.addWidget(buttonTwo)

        self.setLayout(layout)

    def bOne_clicked(self):
        print("bOne clicked")
    
    def bTwo_clicked(self):
        print("bTwo clicked")


if __name__=='__main__':
    app = QApplication(sys.argv)
    
    widget = CustomWidget()
    widget.show()

    app.exec()