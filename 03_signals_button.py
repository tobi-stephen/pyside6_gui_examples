from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class CustomButtonWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('MainWindow App')

        button = QPushButton()
        button.setText('Press moi')
        button.clicked.connect(self.on_button_clicked)

        self.setCentralWidget(button)

    def on_button_clicked(self):
        print('Button clicked')


if __name__=='__main__':
    app = QApplication(sys.argv)

    window = CustomButtonWindow()
    window.show()

    app.exec_()