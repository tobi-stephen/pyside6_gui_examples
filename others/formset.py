# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formset.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)


class Ui_FormSet(object):
    def setupUi(self, FormSet):
        if not FormSet.objectName():
            FormSet.setObjectName(u"FormSet")
        FormSet.resize(478, 366)
        self.verticalLayout = QVBoxLayout(FormSet)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(FormSet)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(FormSet)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(FormSet)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.textEdit = QTextEdit(FormSet)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_3.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.clearButton = QPushButton(FormSet)
        self.clearButton.setObjectName(u"clearButton")

        self.horizontalLayout.addWidget(self.clearButton)

        self.submitButton = QPushButton(FormSet)
        self.submitButton.setObjectName(u"submitButton")

        self.horizontalLayout.addWidget(self.submitButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(FormSet)

        QMetaObject.connectSlotsByName(FormSet)
    # setupUi

    def retranslateUi(self, FormSet):
        FormSet.setWindowTitle(QCoreApplication.translate("FormSet", u"Form", None))
        self.label.setText(QCoreApplication.translate("FormSet", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("FormSet", u"Story", None))
        self.clearButton.setText(QCoreApplication.translate("FormSet", u"Clear", None))
        self.submitButton.setText(QCoreApplication.translate("FormSet", u"Submit", None))
    # retranslateUi

