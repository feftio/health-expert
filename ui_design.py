# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designLiQcjG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 462)
        MainWindow.setWindowOpacity(0.900000000000000)
        MainWindow.setStyleSheet(u".QCheckBox::indicator {\n"
"	width: 14px;\n"
"	height: 14px;\n"
"	border: 3px solid rgb(255,120,100);\n"
"	background: none;\n"
"}\n"
"\n"
".QCheckBox::indicator:checked {\n"
"	background-color: rgb(255,120,100);\n"
"}\n"
"\n"
".QCheckBox::indicator:hover {\n"
"	border-width: 5px;\n"
"}\n"
"\n"
".QCheckBox:hover {\n"
"	text-decoration: line-through;\n"
"}\n"
"\n"
".QCheckBox::text {\n"
"	color: rgb(255, 170, 0);\n"
"}")
        MainWindow.setInputMethodHints(Qt.ImhNone)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setCursor(QCursor(Qt.ArrowCursor))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	width: 5px;\n"
"	height: 24px;\n"
"	border-radius: 12px;\n"
"	background-color: rgb(0, 170, 127);\n"
"}\n"
"\n"
"* {\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 174, 401))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.shakiness = QCheckBox(self.widget)
        self.shakiness.setObjectName(u"shakiness")
        self.shakiness.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.shakiness)

        self.hunger = QCheckBox(self.widget)
        self.hunger.setObjectName(u"hunger")
        self.hunger.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.hunger)

        self.sweating = QCheckBox(self.widget)
        self.sweating.setObjectName(u"sweating")
        self.sweating.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.sweating)

        self.headach = QCheckBox(self.widget)
        self.headach.setObjectName(u"headach")
        self.headach.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.headach)

        self.diabetic_parents = QCheckBox(self.widget)
        self.diabetic_parents.setObjectName(u"diabetic_parents")
        self.diabetic_parents.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.diabetic_parents)

        self.pale = QCheckBox(self.widget)
        self.pale.setObjectName(u"pale")
        self.pale.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pale)

        self.urination = QCheckBox(self.widget)
        self.urination.setObjectName(u"urination")
        self.urination.setCursor(QCursor(Qt.PointingHandCursor))
        self.urination.setTabletTracking(False)

        self.verticalLayout.addWidget(self.urination)

        self.thirst = QCheckBox(self.widget)
        self.thirst.setObjectName(u"thirst")
        self.thirst.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.thirst)

        self.blurred_vision = QCheckBox(self.widget)
        self.blurred_vision.setObjectName(u"blurred_vision")
        self.blurred_vision.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.blurred_vision)

        self.dry_mouth = QCheckBox(self.widget)
        self.dry_mouth.setObjectName(u"dry_mouth")
        self.dry_mouth.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.dry_mouth)

        self.smelling_breath = QCheckBox(self.widget)
        self.smelling_breath.setObjectName(u"smelling_breath")
        self.smelling_breath.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.smelling_breath)

        self.shortness_of_breath = QCheckBox(self.widget)
        self.shortness_of_breath.setObjectName(u"shortness_of_breath")
        self.shortness_of_breath.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.shortness_of_breath)

        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(220, 280, 411, 121))
        self.widget1 = QWidget(self.frame)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(550, 10, 91, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.widget1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.widget1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Expert System", None))
        self.shakiness.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u043b\u043e\u0432\u043e\u043a\u0440\u0443\u0436\u0435\u043d\u0438\u0435", None))
        self.hunger.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u043b\u043e\u0434", None))
        self.sweating.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0442\u043e\u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.headach.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u043b\u043e\u0432\u043d\u0430\u044f \u0431\u043e\u043b\u044c", None))
        self.diabetic_parents.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0431\u0435\u0442 \u0443 \u0440\u043e\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u043e\u0432", None))
        self.pale.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0431\u043b\u0435\u0434\u043d\u0435\u043d\u0438\u0435", None))
        self.urination.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0437\u0443\u0440\u0438\u044f", None))
        self.thirst.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0430\u0436\u0434\u0430", None))
        self.blurred_vision.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0442\u0435\u043c\u043d\u0435\u043d\u0438\u0435 \u0432 \u0433\u043b\u0430\u0437\u0430\u0445", None))
        self.dry_mouth.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u0445\u043e\u0441\u0442\u044c \u0432\u043e \u0440\u0442\u0443", None))
        self.smelling_breath.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0430\u043b\u0438\u0442\u043e\u0437", None))
        self.shortness_of_breath.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0434\u044b\u0448\u043a\u0430", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"asda\n"
"asd\n"
"asd\n"
"a\n"
"", None))
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.pushButton.setText("")
    # retranslateUi

