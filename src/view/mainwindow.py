# -*-coding: utf-8 -*-
# Created by samwell

from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QMainWindow, QSizePolicy
from PySide2.QtWebEngineWidgets import QWebEngineView
from .ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.qwebView = QWebEngineView(self.ui.groupBox_3)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.qwebView.sizePolicy().hasHeightForWidth())
        self.ui.qwebView.setSizePolicy(sizePolicy)
        self.ui.qwebView.setObjectName("qwebView")
        self.ui.verticalLayout_4.addWidget(self.ui.qwebView)
        self.ui.qwebView.load(QUrl('https://dictionary.cambridge.org/dictionary/'))

