import sys, subprocess, os, time

p = subprocess.Popen("pyside6-uic design.ui > design.py", stdout=subprocess.PIPE, shell=True)
p.communicate()

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import *
from design import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())