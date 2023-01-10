import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QCalendarWidget, QStackedWidget

class Window:
    def __init__(self):
        loader = QUiLoader()
        self.window: QMainWindow = loader.load('desktop2.ui', None)

    def show(self):
        self.window.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())