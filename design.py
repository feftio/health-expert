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
        MainWindow.resize(649, 358)
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
        self.options_block = QVBoxLayout()
        self.options_block.setObjectName(u"options_block")
        self.options_block.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.options_block.setContentsMargins(0, 0, 0, 0)
        self.age_row = QHBoxLayout()
        self.age_row.setObjectName(u"age_row")
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy2)
        self.label_1.setMinimumSize(QSize(0, 0))
        self.label_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.age_row.addWidget(self.label_1)

        self.age = QSpinBox(self.centralwidget)
        self.age.setObjectName(u"age")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.age.sizePolicy().hasHeightForWidth())
        self.age.setSizePolicy(sizePolicy3)
        self.age.setMinimum(1)
        self.age.setMaximum(6)
        self.age.setValue(5)

        self.age_row.addWidget(self.age)


        self.options_block.addLayout(self.age_row)

        self.glycemie_row = QHBoxLayout()
        self.glycemie_row.setObjectName(u"glycemie_row")
        self.glycemie_row.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.glycemie_row.addWidget(self.label_2)

        self.glycemie = QSpinBox(self.centralwidget)
        self.glycemie.setObjectName(u"glycemie")
        sizePolicy3.setHeightForWidth(self.glycemie.sizePolicy().hasHeightForWidth())
        self.glycemie.setSizePolicy(sizePolicy3)

        self.glycemie_row.addWidget(self.glycemie)


        self.options_block.addLayout(self.glycemie_row)

        self.option_row_1 = QHBoxLayout()
        self.option_row_1.setObjectName(u"option_row_1")
        self.option_row_1.setContentsMargins(20, -1, 20, -1)
        self.blurred_vision = QCheckBox(self.centralwidget)
        self.blurred_vision.setObjectName(u"blurred_vision")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.blurred_vision.sizePolicy().hasHeightForWidth())
        self.blurred_vision.setSizePolicy(sizePolicy4)

        self.option_row_1.addWidget(self.blurred_vision)

        self.dry_mouth = QCheckBox(self.centralwidget)
        self.dry_mouth.setObjectName(u"dry_mouth")
        sizePolicy4.setHeightForWidth(self.dry_mouth.sizePolicy().hasHeightForWidth())
        self.dry_mouth.setSizePolicy(sizePolicy4)

        self.option_row_1.addWidget(self.dry_mouth)

        self.urination = QCheckBox(self.centralwidget)
        self.urination.setObjectName(u"urination")
        sizePolicy4.setHeightForWidth(self.urination.sizePolicy().hasHeightForWidth())
        self.urination.setSizePolicy(sizePolicy4)

        self.option_row_1.addWidget(self.urination)

        self.headach = QCheckBox(self.centralwidget)
        self.headach.setObjectName(u"headach")
        sizePolicy4.setHeightForWidth(self.headach.sizePolicy().hasHeightForWidth())
        self.headach.setSizePolicy(sizePolicy4)

        self.option_row_1.addWidget(self.headach)


        self.options_block.addLayout(self.option_row_1)

        self.option_row_2 = QHBoxLayout()
        self.option_row_2.setObjectName(u"option_row_2")
        self.option_row_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.option_row_2.setContentsMargins(20, -1, 20, -1)
        self.smelling_breath = QCheckBox(self.centralwidget)
        self.smelling_breath.setObjectName(u"smelling_breath")
        sizePolicy4.setHeightForWidth(self.smelling_breath.sizePolicy().hasHeightForWidth())
        self.smelling_breath.setSizePolicy(sizePolicy4)

        self.option_row_2.addWidget(self.smelling_breath)

        self.thirst = QCheckBox(self.centralwidget)
        self.thirst.setObjectName(u"thirst")
        sizePolicy4.setHeightForWidth(self.thirst.sizePolicy().hasHeightForWidth())
        self.thirst.setSizePolicy(sizePolicy4)
        self.thirst.setChecked(False)

        self.option_row_2.addWidget(self.thirst)

        self.sweating = QCheckBox(self.centralwidget)
        self.sweating.setObjectName(u"sweating")
        sizePolicy4.setHeightForWidth(self.sweating.sizePolicy().hasHeightForWidth())
        self.sweating.setSizePolicy(sizePolicy4)

        self.option_row_2.addWidget(self.sweating)

        self.hunger = QCheckBox(self.centralwidget)
        self.hunger.setObjectName(u"hunger")
        sizePolicy4.setHeightForWidth(self.hunger.sizePolicy().hasHeightForWidth())
        self.hunger.setSizePolicy(sizePolicy4)

        self.option_row_2.addWidget(self.hunger)


        self.options_block.addLayout(self.option_row_2)

        self.option_row_3 = QHBoxLayout()
        self.option_row_3.setObjectName(u"option_row_3")
        self.option_row_3.setContentsMargins(20, -1, 20, -1)
        self.shakiness = QCheckBox(self.centralwidget)
        self.shakiness.setObjectName(u"shakiness")
        sizePolicy4.setHeightForWidth(self.shakiness.sizePolicy().hasHeightForWidth())
        self.shakiness.setSizePolicy(sizePolicy4)

        self.option_row_3.addWidget(self.shakiness)

        self.shortness_of_breath = QCheckBox(self.centralwidget)
        self.shortness_of_breath.setObjectName(u"shortness_of_breath")
        sizePolicy4.setHeightForWidth(self.shortness_of_breath.sizePolicy().hasHeightForWidth())
        self.shortness_of_breath.setSizePolicy(sizePolicy4)

        self.option_row_3.addWidget(self.shortness_of_breath)

        self.diabetic_parents = QCheckBox(self.centralwidget)
        self.diabetic_parents.setObjectName(u"diabetic_parents")
        sizePolicy4.setHeightForWidth(self.diabetic_parents.sizePolicy().hasHeightForWidth())
        self.diabetic_parents.setSizePolicy(sizePolicy4)

        self.option_row_3.addWidget(self.diabetic_parents)

        self.pale = QCheckBox(self.centralwidget)
        self.pale.setObjectName(u"pale")
        sizePolicy4.setHeightForWidth(self.pale.sizePolicy().hasHeightForWidth())
        self.pale.setSizePolicy(sizePolicy4)

        self.option_row_3.addWidget(self.pale)


        self.options_block.addLayout(self.option_row_3)


        self.verticalLayout_2.addLayout(self.options_block)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: #262626;\n"
"color: #FFFFFF;\n"
"font-family: Titillium;\n"
"font-size: 18px;")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy5)

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Glycemie:", None))
        self.blurred_vision.setText(QCoreApplication.translate("MainWindow", u"Blurred vision", None))
        self.dry_mouth.setText(QCoreApplication.translate("MainWindow", u"Dry mouth", None))
        self.urination.setText(QCoreApplication.translate("MainWindow", u"Urination", None))
        self.headach.setText(QCoreApplication.translate("MainWindow", u"Headach", None))
        self.smelling_breath.setText(QCoreApplication.translate("MainWindow", u"Smelling breath", None))
        self.thirst.setText(QCoreApplication.translate("MainWindow", u"Thirst", None))
        self.sweating.setText(QCoreApplication.translate("MainWindow", u"Sweating", None))
        self.hunger.setText(QCoreApplication.translate("MainWindow", u"Hunger", None))
        self.shakiness.setText(QCoreApplication.translate("MainWindow", u"Shakiness", None))
        self.shortness_of_breath.setText(QCoreApplication.translate("MainWindow", u"Shortness of breath", None))
        self.diabetic_parents.setText(QCoreApplication.translate("MainWindow", u"Diabetic parents", None))
        self.pale.setText(QCoreApplication.translate("MainWindow", u"Pale", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
    # retranslateUi

