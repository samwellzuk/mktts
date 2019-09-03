# -*-coding: utf-8 -*-
# Created by samwell
import threading

from PyQt5.QtCore import QUrl, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QSizePolicy, QProgressDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
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

        self.ui.qwebView.loadStarted.connect(self._started)
        self.ui.qwebView.loadProgress.connect(self._progress)
        self.ui.qwebView.loadFinished.connect(self._finished)
        self.progressDlg = QProgressDialog(self)
        self.progressDlg.setLabelText('Loading...')
        self.progressDlg.setCancelButtonText(None)
        self.progressDlg.setAutoReset(False)
        self.progressDlg.setAutoClose(False)
        self.ui.qwebView.load(QUrl('https://dictionary.cambridge.org/dictionary/'))
        print(threading.get_ident())

    def _started(self):
        self.progressDlg.show()
        print(threading.get_ident())

    @pyqtSlot(int)
    def _progress(self, progress):
        self.progressDlg.setValue(progress)
        print(threading.get_ident())

    @pyqtSlot(bool)
    def _finished(self, bok):
        currenpage = self.ui.qwebView.page()
        currenpage.toHtml(self._to_html)
        print(threading.get_ident())

    def _to_html(self, data):
        #self.progressDlg.close()
        print(threading.get_ident())