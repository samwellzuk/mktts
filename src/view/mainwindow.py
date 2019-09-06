# -*-coding: utf-8 -*-
# Created by samwell
import time
from functools import partial

from PyQt5.QtCore import Qt, QUrl, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QSizePolicy, QTabBar
from PyQt5.QtWebEngineWidgets import QWebEngineView

from tts import tts_languages

from di.cambridge import CambridgeUK, CambridgeUS

from .ui_mainwindow import Ui_MainWindow
from .asynctask import coroutine, AsyncTask


class Ui_MainWindow_Ex(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        # chrome init
        self.qwebView = QWebEngineView(self.groupBox_4)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qwebView.sizePolicy().hasHeightForWidth())
        self.qwebView.setSizePolicy(sizePolicy)
        self.qwebView.setObjectName("qwebView")
        self.verticalLayout_8.addWidget(self.qwebView)
        # tabbar init
        self.tabBar = QTabBar(self.groupBox_6)
        self.tabBar.setObjectName("tabBar")
        self.verticalLayout_5.insertWidget(0, self.tabBar)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow_Ex()
        self.ui.setupUi(self)

        # hide
        self.ui.groupBox_5.setVisible(False)
        self.ui.groupBox_7.setVisible(False)

        # init dictionary
        self.dictionaries = [CambridgeUS(), CambridgeUK()]
        for obj in self.dictionaries:
            self.ui.dictBox.addItem(obj.displayname)
        self.ui.dictBox.currentIndexChanged.connect(self._dictionary_change)

        # connection
        self.ui.qwebView.loadStarted.connect(self._load_started)
        self.ui.qwebView.loadProgress.connect(self._load_progress)
        self.ui.qwebView.loadFinished.connect(self._load_finished)

        self.ui.dictBox.setCurrentIndex(0)
        self._dictionary_change(0)

    @pyqtSlot(int)
    def _dictionary_change(self, index):
        diobj = self.dictionaries[index]
        self.ui.accentBox.clear()

        lang = diobj.language
        tts_lang = diobj.tts_language
        for k, v in tts_languages:
            if k.startswith(lang):
                self.ui.accentBox.addItem(v, k)
        for i in range(self.ui.accentBox.count()):
            k = self.ui.accentBox.itemData(i)
            if k == tts_lang:
                self.ui.accentBox.setCurrentIndex(i)
                break
        else:
            self.ui.accentBox.setCurrentIndex(0)
        self.ui.qwebView.load(QUrl(diobj.home))

    @pyqtSlot()
    def _load_started(self):
        self.ui.groupBox_7.setVisible(True)
        self.ui.dictBox.setEnabled(False)
        self.ui.accentBox.setEnabled(False)
        self.ui.dictMktts.setEnabled(False)

    @pyqtSlot(int)
    def _load_progress(self, val):
        self.ui.loadingBar.setValue(val)

    @pyqtSlot(bool)
    def _load_finished(self, bok):
        if bok:
            url = self.ui.qwebView.page().url()
            index = self.ui.dictBox.currentIndex()
            diobj = self.dictionaries[index]
            if diobj.check_url(url):
                accent = self.ui.accentBox.currentData()
                func = partial(self.process, diobj, accent, url)
                self.ui.qwebView.page().toHtml(func)
        self.ui.groupBox_7.setVisible(False)
        self.ui.dictBox.setEnabled(True)
        self.ui.accentBox.setEnabled(True)
        self.ui.dictMktts.setEnabled(True)

    def _query_start(self):
        self.ui.tabBar.setEnabled(False)
        self.ui.titleEdit.setEnabled(False)
        self.ui.titlePlay.setEnabled(False)
        self.ui.titleStop.setEnabled(False)
        self.ui.titleMktts.setEnabled(False)
        self.ui.contentEdit.setEnabled(False)
        self.ui.contentPlay.setEnabled(False)
        self.ui.contentStop.setEnabled(False)
        self.ui.contentMktts.setEnabled(False)
        self.ui.groupBox_5.setVisible(True)

        self.ui.progressBar.setValue(0)
        self.ui.progressLabel.setText('')

    def _query_progress(self, val, info):
        self.ui.progressBar.setValue(val)
        self.ui.progressLabel.setText(info)

    def _query_finsh(self):
        self.ui.groupBox_5.setVisible(False)
        self.ui.tabBar.setEnabled(True)
        self.ui.titleEdit.setEnabled(True)
        self.ui.titlePlay.setEnabled(True)
        self.ui.titleStop.setEnabled(True)
        self.ui.titleMktts.setEnabled(True)
        self.ui.contentEdit.setEnabled(True)
        self.ui.contentPlay.setEnabled(True)
        self.ui.contentStop.setEnabled(True)
        self.ui.contentMktts.setEnabled(True)

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        AsyncTask.check_thread()

    @coroutine
    def process(self, diobj, accent, url, html):
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
