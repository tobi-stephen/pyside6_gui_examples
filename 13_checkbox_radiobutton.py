import sys
from PySide6.QtWidgets import QButtonGroup, QGroupBox, QWidget, QApplication, QSizePolicy, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox, QRadioButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CheckBox/RadioButton Demo")

        osbox = QGroupBox("Choose OS")
        windows = QCheckBox("Windows")
        linux = QCheckBox("Linux")
        mac = QCheckBox("Mac")

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        osbox.setLayout(os_layout)

        drink_box = QGroupBox("Choose drink")
        fanta = QCheckBox("Fanta")
        mirinda = QCheckBox("Mirinda")
        bigi = QCheckBox("Bigi Apple")
        
        drink_layout = QVBoxLayout()
        drink_layout.addWidget(fanta)
        drink_layout.addWidget(mirinda)
        drink_layout.addWidget(bigi)
        drink_box.setLayout(drink_layout)

        state_box = QGroupBox("Choose State")
        lagos = QRadioButton("Lagos")
        ogun = QRadioButton("Ogun")
        anambra = QRadioButton("Anambra")
        kano = QRadioButton("kano")
        
        state_layout = QVBoxLayout()
        state_layout.addWidget(lagos)
        state_layout.addWidget(anambra)
        state_layout.addWidget(kano)
        state_layout.addWidget(ogun)
        state_box.setLayout(state_layout)

        button_box = QGroupBox("Choose letter")
        a = QCheckBox("A")
        b = QCheckBox("B")
        button_group = QButtonGroup(self)
        button_group.addButton(a)
        button_group.addButton(b)
        button_group.setExclusive(True)

        button_layout = QVBoxLayout()
        button_layout.addWidget(a)
        button_layout.addWidget(b)
        button_box.setLayout(button_layout)
        
        h_layout = QHBoxLayout()
        h_layout.addWidget(osbox)
        h_layout.addWidget(state_box)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(drink_box)
        v_layout.addWidget(button_box)

        self.setLayout(v_layout)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec())

