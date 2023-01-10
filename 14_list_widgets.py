import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QListWidget, QVBoxLayout, QListWidgetItem, QLineEdit

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("List Widget Demo")

        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QListWidget.SelectionMode.MultiSelection)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Enter message")
        self.line_edit.returnPressed.connect(self.button_add_clicked)
        
        button_add = QPushButton("Add Item")
        button_add.clicked.connect(self.button_add_clicked)

        button_delete = QPushButton("Delete Current Item")
        button_delete.clicked.connect(self.button_delete_clicked)

        button_delete_s = QPushButton("Delete Selected Items")
        button_delete_s.clicked.connect(self.button_delete_selected_clicked)

        button_count = QPushButton("Count Item")
        button_count.clicked.connect(self.button_count_clicked)

        button_selected = QPushButton("Selected Items")
        button_selected.clicked.connect(self.button_selected_clicked)

        button_clear = QPushButton("Clear items")
        button_clear.clicked.connect(self.button_clear_clicked)

        v_layout = QVBoxLayout(self)
        v_layout.addWidget(self.list_widget)
        v_layout.addWidget(self.line_edit)
        v_layout.addWidget(button_add)
        v_layout.addWidget(button_delete)
        v_layout.addWidget(button_delete_s)
        v_layout.addWidget(button_count)
        v_layout.addWidget(button_selected)
        v_layout.addWidget(button_clear)

    def button_add_clicked(self):
        text = self.line_edit.text().strip()
        if not text:
            return
        
        self.list_widget.addItem(text)

    def button_delete_clicked(self):
        row = self.list_widget.currentRow()
        self.list_widget.takeItem(row)
    
    def button_delete_selected_clicked(self):
        items = self.list_widget.selectedItems()

        for item in items:
            row = self.list_widget.row(item)
            self.list_widget.takeItem(row)

    def button_count_clicked(self):
        item_count = self.list_widget.count()
        QMessageBox.information(self, "List Widget items", "Item Count: " + str(item_count), QMessageBox.StandardButton.Ok)

    def button_selected_clicked(self):
        items = self.list_widget.selectedItems()
        
        if len(items) < 1:
            return
        items = [item.text() for item in items]
        QMessageBox.information(self, "List Widget items", "Items Selected: " + ",".join(items), QMessageBox.StandardButton.Ok)

    def button_clear_clicked(self):
        self.list_widget.clear()
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())