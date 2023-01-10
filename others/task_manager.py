import sys
import time
import uuid
from PySide6.QtWidgets import QTextEdit, QSizePolicy, QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QToolBar, QStatusBar, QHBoxLayout, QVBoxLayout, QMessageBox, QScrollArea
from PySide6.QtCore import Signal, Slot, QUrl, Qt
from PySide6.QtGui import QAction, QPalette
from PySide6.QtUiTools import QUiLoader
from tasklabel import Ui_Form

# volatile store of tasks created
# tasks = {str(uuid.uuid4()): ["Talk to woman", time.time()], str(uuid.uuid4()): ["open youversion", time.time()]}
tasks = {}

class TaskLabel(QWidget, Ui_Form):
    def __init__(self, parent=None, task_id=None):
        super().__init__(parent)
        self.setupUi(self)
        if not task_id:
            task_id = str(uuid.uuid4())
            tasks[task_id] = ["", time.time()]
        
        self.lineEdit.setText(tasks[task_id][0])
        self.lineEdit.textChanged.connect(self.taskUpdated)
        self.taskLabel.setText(tasks[task_id][0])
        self.taskLabel.setWordWrap(True)
        self.setObjectName(task_id)

    def taskUpdated(self):
        task_detail = self.lineEdit.text().strip()
        if len(task_detail) > 0:
            self.editButton.setEnabled(True)
            self.taskLabel.setText(task_detail)
        else:
            self.editButton.setEnabled(False)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")

        self.scroll = QScrollArea(self)
        self.scroll.setWidgetResizable(True)
        self.scroll.setBackgroundRole(QPalette.ColorRole.Midlight)
        self.task_list_widget = QWidget(self)
        self.task_detail_layout = QVBoxLayout()
        self.task_list_widget.setLayout(self.task_detail_layout)
        self.scroll.setWidget(self.task_list_widget)
        self.task_list_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)

        self.update_task_list_widget()

        self.task_create_or_edit_widget = QWidget(self)
        h_layout = QHBoxLayout()
        
        self.task_edit = QLineEdit()
        self.task_edit.setPlaceholderText("Create a new task")
        self.task_edit.returnPressed.connect(self.create_new_task)
        self.task_edit.setText("Hello")

        self.task_create_button = QPushButton("Create")
        self.task_create_button.clicked.connect(self.create_new_task)

        h_layout.addWidget(self.task_edit)
        h_layout.addWidget(self.task_create_button)
        self.task_create_or_edit_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.task_create_or_edit_widget.setLayout(h_layout)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.scroll, 5)
        layout.addWidget(self.task_create_or_edit_widget, 1)
        self.main_window = QWidget(self)
        self.main_window.setLayout(layout)
        self.setCentralWidget(self.main_window)

    def create_new_task(self):
        task_det = self.task_edit.text().strip()
        if not task_det:
            QMessageBox.warning(self, "Create Task", "No text entered")
            return

        task_id = str(uuid.uuid4())
        tasks[task_id] = [task_det, time.time()]
        self.populate_task_list_widget(task_id)
        self.task_edit.clear()

    def populate_task_list_widget(self, task_id):
        label: TaskLabel = TaskLabel(self.task_list_widget, task_id=task_id)
        print(task_id, tasks[task_id])

        label.editButton.clicked.connect(lambda _: self.edit_task(task_id))
        label.deleteButton.clicked.connect(lambda _: self.delete_task(task_id))
        # label.lineEdit.textChanged.connect(lambda _: )

        self.task_detail_layout.addWidget(label)

    def delete_task(self, task_id):
        print("del task_id:", task_id)
        if task_id not in tasks: return
        
        tasks.pop(task_id)
        w: TaskLabel = self.findChild(TaskLabel, task_id)
        self.task_detail_layout.removeWidget(w)
        w.deleteLater()
        w = None

    def edit_task(self, task_id):
        print("edit task_id:", task_id)
        if task_id not in tasks: return
        
        w: TaskLabel = self.findChild(TaskLabel, task_id)
        task_detail = w.lineEdit.text().strip()
        if not task_detail: return
        print('task to edit', w.objectName())
        tasks[task_id] = [task_detail, time.time()]
        w.taskLabel.setText(task_detail)

    def update_task_list_widget(self):
        for task_id in tasks: self.populate_task_list_widget(task_id)


def main():
    app = QApplication(sys.argv)
    manager = Window()
    manager.resize(500, 300)
    manager.show()
    sys.exit(app.exec())

if __name__=='__main__':
    main()
