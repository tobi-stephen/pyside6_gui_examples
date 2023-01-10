# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tasklabel.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(408, 50)
        Form.setMaximumSize(QSize(16777215, 50))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit, 0, Qt.AlignHCenter)

        self.taskLabel = QLabel(self.frame)
        self.taskLabel.setObjectName(u"taskLabel")
        self.taskLabel.setFrameShape(QFrame.Box)
        self.taskLabel.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.taskLabel)

        self.editButton = QPushButton(self.frame)
        self.editButton.setObjectName(u"editButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(self.frame)
        self.deleteButton.setObjectName(u"deleteButton")
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.deleteButton)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.taskLabel.setText("")
        self.editButton.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.deleteButton.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

