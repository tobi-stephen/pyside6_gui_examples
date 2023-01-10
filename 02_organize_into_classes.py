from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class CustomButtonWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('MainWindow App')

        button = QPushButton()
        button.setText('Press moi')

        self.setCentralWidget(button)


if __name__=='__main__':
    app = QApplication(sys.argv)

    window = CustomButtonWindow()
    window.show()

    app.exec_()