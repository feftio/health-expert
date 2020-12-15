# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(934, 490)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"	height: 30px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label)

        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy3)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(6)
        self.spinBox_2.setValue(5)

        self.horizontalLayout_6.addWidget(self.spinBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy3.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, -1, 20, -1)
        self.checkBox_9 = QCheckBox(self.centralwidget)
        self.checkBox_9.setObjectName(u"checkBox_9")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.checkBox_9)

        self.checkBox_10 = QCheckBox(self.centralwidget)
        self.checkBox_10.setObjectName(u"checkBox_10")
        sizePolicy4.setHeightForWidth(self.checkBox_10.sizePolicy().hasHeightForWidth())
        self.checkBox_10.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.checkBox_10)

        self.checkBox_7 = QCheckBox(self.centralwidget)
        self.checkBox_7.setObjectName(u"checkBox_7")
        sizePolicy4.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.checkBox_7)

        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy4.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.checkBox_4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.checkBox_11 = QCheckBox(self.centralwidget)
        self.checkBox_11.setObjectName(u"checkBox_11")
        sizePolicy4.setHeightForWidth(self.checkBox_11.sizePolicy().hasHeightForWidth())
        self.checkBox_11.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.checkBox_11)

        self.checkBox_8 = QCheckBox(self.centralwidget)
        self.checkBox_8.setObjectName(u"checkBox_8")
        sizePolicy4.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy4)
        self.checkBox_8.setChecked(False)

        self.horizontalLayout_3.addWidget(self.checkBox_8)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy4.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy4.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.checkBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, -1, 20, -1)
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy4.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.checkBox_3)

        self.checkBox_12 = QCheckBox(self.centralwidget)
        self.checkBox_12.setObjectName(u"checkBox_12")
        sizePolicy4.setHeightForWidth(self.checkBox_12.sizePolicy().hasHeightForWidth())
        self.checkBox_12.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.checkBox_12)

        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy4.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        sizePolicy4.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.checkBox_6)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy5)
        self.textEdit.setMinimumSize(QSize(300, 100))
        self.textEdit.setMouseTracking(False)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setFrameShadow(QFrame.Sunken)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.textEdit)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy6)

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Glycemie:", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Blurred vision", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"Dry mouth", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Urination", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Headach", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"Smelling breath", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Thirst", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Sweating", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Hunger", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Shakiness", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"Shortness of breath", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Diabetic parents", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Pale", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
    # retranslateUi

