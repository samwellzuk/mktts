# -*-coding: utf-8 -*-
# Created by samwell
import time


from PyQt5.QtCore import Qt, QUrl, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QSizePolicy, QProgressDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from .ui_mainwindow import Ui_MainWindow
from .asynctask import coroutine, AsyncTask


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # chrome init
        self.qwebView = QWebEngineView(self.ui.groupBox_3)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qwebView.sizePolicy().hasHeightForWidth())
        self.qwebView.setSizePolicy(sizePolicy)
        self.qwebView.setObjectName("qwebView")
        self.ui.verticalLayout_4.addWidget(self.qwebView)

        # hide
        self.ui.groupBox_5.setVisible(False)
        # connection
        self.qwebView.loadFinished.connect(self._finished)
        self.qwebView.load(QUrl('https://dictionary.cambridge.org/dictionary/'))

    @pyqtSlot(bool)
    def _finished(self, bok):
        if bok:
            currenpage = self.qwebView.page()
            currenpage.toHtml(self.process)

    @coroutine
    def process(self, html):
        def _worker(inval):
            print("in worker, received '%s'" % inval)
            time.sleep(2)
            return "%s worked" % inval

        self.ui.groupBox_5.setVisible(True)
        self.ui.progressBar.setValue(0)
        self.ui.progressLabel.setText('Starting task1 ...')
        out = AsyncTask(_worker, "test string")
        val = yield out

        self.ui.progressBar.setValue(30)
        self.ui.progressLabel.setText('Starting task2 ...')
        out2 = AsyncTask(_worker, "another test string")
        val2 = yield out2

        self.ui.progressBar.setValue(60)
        self.ui.progressLabel.setText('Starting task3 ...')

        out = yield AsyncTask(_worker, "Some other string")
        self.ui.progressBar.setValue(100)
        self.ui.progressLabel.setText('Finished!')
        self.ui.groupBox_5.setVisible(False)
        return
