import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QStatusBar

class CustomWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom Window")
        
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        new_action = file_menu.addAction("New")
        quit_action = file_menu.addAction("Close")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")

        window_menu = menu_bar.addMenu("&Window")
        window_menu.addAction("Window")

        setting_menu = menu_bar.addMenu("&Others")
        setting_menu.addAction("Others")

        test_action = QAction("Some Act", self)
        test_action.setStatusTip("This is a test action")
        test_action.triggered.connect(self.test_action_triggered)
        
        toolbar = QToolBar("Custom Toolbar", self)
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        
        toolbar.addAction(new_action)
        toolbar.addAction(quit_action)
        toolbar.addAction(test_action)
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here", self))

        self.setStatusBar(QStatusBar(self))

    def test_action_triggered(self):
        print("test action is triggered")
        self.statusBar().showMessage("message from custom window", 5000)


    def quit_app(self):
        self.app.quit()
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    
    window = CustomWindow(app)
    window.show()

    app.exec()