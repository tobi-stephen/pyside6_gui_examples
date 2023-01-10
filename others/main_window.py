import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QAction

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ster Plus")

        # Left Menu Layout
        self.left_menu = QWidget()
        home_button = QPushButton("Home")
        home_button.clicked.connect(lambda : self.mid_stacked.setCurrentIndex(0))

        file_button = QPushButton("File")
        file_button.clicked.connect(lambda : self.mid_stacked.setCurrentIndex(1))

        about_button = QPushButton("About")
        about_button.clicked.connect(lambda : self.mid_stacked.setCurrentIndex(2))
        
        left_layout = QVBoxLayout()
        left_layout.addWidget(home_button)
        left_layout.addWidget(file_button)
        left_layout.addWidget(about_button)
        self.left_menu.setLayout(left_layout)

        # Main Body Layout
        self.mid_stacked = QStackedWidget()
        home_stack = QWidget()
        home_dummy_button = QPushButton("Home Dummy")
        home_stack_layout = QVBoxLayout()
        home_stack_layout.addWidget(home_dummy_button)
        home_stack.setLayout(home_stack_layout)

        file_stack = QWidget()
        file_dummy_button = QPushButton("File Dummy")
        file_stack_layout = QVBoxLayout()
        file_stack_layout.addWidget(file_dummy_button)
        file_stack.setLayout(file_stack_layout)

        about_stack = QWidget()
        about_dummy_button = QPushButton("About Dummy")
        about_stack_layout = QVBoxLayout()
        about_stack_layout.addWidget(about_dummy_button)
        about_stack.setLayout(about_stack_layout)

        self.mid_stacked.addWidget(home_stack)
        self.mid_stacked.addWidget(file_stack)
        self.mid_stacked.addWidget(about_stack)
        
        # Right Menu Layout
        self.right_menu = QWidget()
        dummy_button = QPushButton("Dummy")

        right_layout = QVBoxLayout()
        right_layout.addWidget(dummy_button)
        self.right_menu.setLayout(right_layout)

        body_layout = QHBoxLayout()
        body_layout.addWidget(self.left_menu, 1)
        body_layout.addWidget(self.mid_stacked, 3)
        body_layout.addWidget(self.right_menu, 1)

        body_widget = QWidget()
        body_widget.setLayout(body_layout)
        self.setCentralWidget(body_widget)

        # Toolbar Setup
        toolbar = self.addToolBar("Menu Toolbar")
        left_menu_action = toolbar.addAction("Menu")
        left_menu_action.triggered.connect(lambda: self.left_menu.setVisible(not self.left_menu.isVisible()))
        
        toolbar.addSeparator()

        right_menu_action = toolbar.addAction("Misc")
        right_menu_action.triggered.connect(lambda: self.right_menu.setVisible(not self.right_menu.isVisible()))


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())