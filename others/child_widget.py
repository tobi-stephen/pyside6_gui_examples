import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication(sys.argv)

widget= QWidget()
child1 = QWidget(widget)
button1 = QPushButton("Button One", child1)

child2 = QWidget(widget)
button2 = QPushButton("Button Two", child2)
child2.move(100, 100)

child3 = QWidget(widget)
button3 = QPushButton("Button Three", child3)
child3.move(100, 150)

widget.show()

app.exec()