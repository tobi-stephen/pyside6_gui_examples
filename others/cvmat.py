import sys
import time
import cv2 as cv
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide6.QtGui import QImage, QPixmap, QCloseEvent
from PySide6.QtCore import QThread, Qt, Signal, Slot, SIGNAL, SLOT

class Thread(QThread):
    updateFrame = Signal(QImage)
    captureResult = Signal(int)

    def __init__(self, parent=None, v_id=0):
        QThread.__init__(self, parent)
        self.v_id = v_id
        self.status = False
        self.cap = None
    
    def run(self):
        self.cap = cv.VideoCapture(self.v_id)
        x = 0
        while self.status:
            ret, img = self.cap.read()
            if not ret:
                print("error reading v_cap", x, self.v_id)
                continue

            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

            h, w, ch = img.shape
            qimg = QImage(img, w, h, ch*w, QImage.Format.Format_RGB888)
            f_img = qimg.scaled(640, 480, Qt.AspectRatioMode.KeepAspectRatio)

            self.updateFrame.emit(f_img)
        sys.exit(-1)


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello CV Qt")

        self.th = Thread(self)
        self.th.updateFrame.connect(self.updateFrame)

        self.label = QLabel(self)
        self.label.setFixedSize(640, 480)

        self.startButton = QPushButton("Start", self)
        self.startButton.clicked.connect(self.startCapture)

        self.endButton = QPushButton("End", self)
        self.endButton.clicked.connect(self.endCapture)
        self.endButton.setEnabled(False)
        
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.startButton)
        self.layout.addWidget(self.endButton)
        
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Enter camera id")
        self.line_edit.returnPressed.connect(self.startCapture)

        self.v_layout = QVBoxLayout(self)
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.line_edit)
        self.v_layout.addLayout(self.layout)

    def closeEvent(self, event: QCloseEvent) -> None:
        # if self.th.status:
        #     self.th.cap.release()
        # cv.destroyAllWindows()
        # self.th.terminate()
        
        # # Give time for the thread to finish
        # time.sleep(1)
        self.th = None
        return super().closeEvent(event)

    @Slot()
    def startCapture(self):
        c_id = self.line_edit.text().strip()
        if not c_id: 
            QMessageBox.warning(self, "Video Capture", "Enter a valid camera id")
            return

        self.startButton.setEnabled(False)
        self.endButton.setEnabled(True)
        self.th.status = True
        self.th.v_id = int(c_id)
        self.th.start()

    @Slot()
    def endCapture(self):
        self.startButton.setEnabled(True)
        self.endButton.setEnabled(False)
        self.label.clear()
        
        self.th.cap.release()
        cv.destroyAllWindows()
        self.th.status = False
        self.th.terminate()

        time.sleep(1)

    @Slot(QImage)
    def updateFrame(self, frame: QImage):
        self.label.setPixmap(QPixmap.fromImage(frame))


def main():
    app = QApplication(sys.argv)

    widget = Widget()
    widget.show()

    sys.exit(app.exec())

if __name__=='__main__':
    main()
    