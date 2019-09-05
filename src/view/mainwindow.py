# -*-coding: utf-8 -*-
# Created by samwell
import time
from functools import partial

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
        self.qwebView = QWebEngineView(self.ui.groupBox_4)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qwebView.sizePolicy().hasHeightForWidth())
        self.qwebView.setSizePolicy(sizePolicy)
        self.qwebView.setObjectName("qwebView")
        self.ui.verticalLayout_8.addWidget(self.qwebView)

        # hide
        self.ui.groupBox_5.setVisible(False)
        self.ui.groupBox_7.setVisible(False)

        # connection
        self.qwebView.loadStarted.connect(self._load_started)
        self.qwebView.loadProgress.connect(self._load_progress)
        self.qwebView.loadFinished.connect(self._load_finished)
        self.qwebView.load(QUrl('https://dictionary.cambridge.org/dictionary/'))


    @pyqtSlot()
    def _load_started(self):
        self.ui.groupBox_7.setVisible(True)

    @pyqtSlot(int)
    def _load_progress(self, val):
        self.ui.loadingBar.setValue(val)

    @pyqtSlot(bool)
    def _load_finished(self, bok):
        self.ui.groupBox_7.setVisible(False)
        if bok:
            curpg = self.qwebView.page()
            print(curpg.url())
            spath = str(curpg.url().path())
            if not spath.endswith('/'):
                curpg.toHtml(self._to_html)

    def _to_html(self, data):
        spath = str(self.qwebView.page().url().path())
        qword = spath.split('/')[-1]
        self.process(qword, data)

    @coroutine
    def process(self, qword, html):
        def _worker(inval):
            print(inval)
            time.sleep(2)

        self.ui.groupBox_5.setVisible(True)

        sinfo = '%s, parsing ...' % qword
        self.ui.progressBar.setValue(0)
        self.ui.progressLabel.setText(sinfo)
        out = AsyncTask(_worker, sinfo)
        yield out

        sinfo = '%s, query ...' % qword
        self.ui.progressBar.setValue(30)
        self.ui.progressLabel.setText(sinfo)
        out2 = AsyncTask(_worker, sinfo)
        yield out2

        sinfo = '%s, trans to voice ...' % qword
        self.ui.progressBar.setValue(60)
        self.ui.progressLabel.setText(sinfo)

        yield AsyncTask(_worker, sinfo)
        self.ui.progressBar.setValue(100)
        self.ui.progressLabel.setText('%s, finished!' % qword)
        self.ui.groupBox_5.setVisible(False)
        return

