# -*-coding: utf-8 -*-
# Created by samwell
import time
from functools import partial

from PyQt5.QtCore import Qt, QUrl, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QSizePolicy, QProgressDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView

from di.cambridge import Cambridge
from di.collins import Collins

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

        # init dictionary
        self.dictionaries = [Cambridge(), Collins()]
        for obj in self.dictionaries:
            self.ui.dictionaryBox.addItem(obj.name)
        self.ui.dictionaryBox.currentIndexChanged.connect(self._dictionary_change)

        # connection
        self.qwebView.loadStarted.connect(self._load_started)
        self.qwebView.loadProgress.connect(self._load_progress)
        self.qwebView.loadFinished.connect(self._load_finished)

        self.ui.dictionaryBox.setCurrentIndex(0)
        self.qwebView.load(QUrl(self.dictionaries[0].home))

    @pyqtSlot(int)
    def _dictionary_change(self, index):
        self.qwebView.load(QUrl(self.dictionaries[index].home))

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
            url = self.qwebView.page().url()
            for diobj in self.dictionaries:
                if diobj.check_url(url):
                    func = partial(self.process, diobj, url)
                    self.qwebView.page().toHtml(func)
                    break

    def _query_start(self):
        self.ui.autoplayBox.setEnabled(False)
        self.ui.titleEdit.setEnabled(False)
        self.ui.titlePlay.setEnabled(False)
        self.ui.titleStop.setEnabled(False)
        self.ui.contentEdit.setEnabled(False)
        self.ui.contentPlay.setEnabled(False)
        self.ui.contentStop.setEnabled(False)

        self.ui.groupBox_5.setVisible(True)
        self.ui.progressBar.setValue(0)
        self.ui.progressLabel.setText('')

    def _query_progress(self, val, info):
        self.ui.progressBar.setValue(val)
        self.ui.progressLabel.setText(info)

    def _query_finsh(self):
        self.ui.groupBox_5.setVisible(False)
        self.ui.autoplayBox.setEnabled(True)
        self.ui.titleEdit.setEnabled(True)
        self.ui.titlePlay.setEnabled(True)
        self.ui.titleStop.setEnabled(True)
        self.ui.contentEdit.setEnabled(True)
        self.ui.contentPlay.setEnabled(True)
        self.ui.contentStop.setEnabled(True)

    @coroutine
    def process(self, diobj, url, html):
        def _worker(inval):
            print(inval)
            time.sleep(2)

        qword = 'test'
        self._query_start()

        sinfo = '%s, parsing ...' % qword
        self._query_progress(0, sinfo)
        yield AsyncTask(_worker, sinfo)

        sinfo = '%s, query ...' % qword
        self._query_progress(30, sinfo)
        yield AsyncTask(_worker, sinfo)

        sinfo = '%s, trans to voice ...' % qword
        self._query_progress(60, sinfo)

        yield AsyncTask(_worker, sinfo)
        self._query_progress(100, '%s, finished!' % qword)

        self._query_finsh()
        return
