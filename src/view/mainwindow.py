# -*-coding: utf-8 -*-
# Created by samwell

from PySide2.QtWidgets import QMainWindow
from .ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
