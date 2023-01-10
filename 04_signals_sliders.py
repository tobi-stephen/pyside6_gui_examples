from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider
import sys

class CustomWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('MainWindow App')

        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(33)
        slider.setValue(13)

        slider.valueChanged.connect(self.on_slider_changed)
        
        self.setCentralWidget(slider)

    def on_slider_changed(self, value):
        print('Slider: {0}'.format(value))


if __name__=='__main__':
    app = QApplication(sys.argv)

    window = CustomWindow()
    window.show()

    app.exec_()