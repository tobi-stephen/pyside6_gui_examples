import sys
import numpy
import time
import cv2 as cv
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QPixmap, QImage, QCloseEvent
from PySide6.QtCore import QThread, Signal, Slot, SIGNAL, SLOT, Qt


class Thread(QThread):
    updateFrame = Signal(QImage)

    def run(self):
        cap = cv.VideoCapture(0)
        print("about to start capure")
        while True:
            ret, frame = cap.read()
            if ret:
                frame = cv.flip(frame, 1)
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                
                self.updateFrame.emit(p)


class Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mat to Pixmap")
        
        self.label = QLabel(self)
        self.label.setFixedSize(640, 480)
        self.label.setText("Starting Camera...")
        self.label.setAlignment(self.label.alignment().AlignCenter)

        self.th = Thread()
        self.th.updateFrame.connect(self.updateFrame)
        self.th.start()

    def updateFrame(self, image: QImage):
        self.label.setPixmap(QPixmap.fromImage(image))

    def closeEvent(self, event: QCloseEvent) -> None:
        self.th.terminate()
        self.label.clear()
        self.label.setText("Closing Camera...")
        time.sleep(1)
        return super().closeEvent(event)

def main():
    app = QApplication(sys.argv)

    widget = Widget()
    widget.show()
    
    app.exec()

if __name__=='__main__':
    main()