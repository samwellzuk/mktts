# -*-coding: utf-8 -*-
# Created by samwell
import time
import os
from functools import partial

from PyQt5.QtCore import Qt, QUrl, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QSizePolicy, QTabBar, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView

from tts import tts_languages
from di.cambridge import CambridgeUK, CambridgeUS
from model import DictWord
from settings import data_dir

from .ui_mainwindow import Ui_MainWindow
from .asynctask import coroutine, AsyncTask
from .utility import except_check


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
        self.verticalLayout_5.insertWidget(1, self.tabBar)


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
        default_ttslang = diobj.default_ttslang
        for k, v in tts_languages:
            if k.startswith(lang):
                self.ui.accentBox.addItem(v, k)
        for i in range(self.ui.accentBox.count()):
            k = self.ui.accentBox.itemData(i)
            if k == default_ttslang:
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
    @except_check
    def _load_finished(self, bok):
        if bok:
            url = self.ui.qwebView.page().url()
            index = self.ui.dictBox.currentIndex()
            diobj = self.dictionaries[index]
            qok, qword = diobj.check_url(url)
            if qok:
                tts_lang = self.ui.accentBox.currentData()
                wordobj, is_new = self.load_word(diobj, qword, tts_lang)
                if is_new:
                    func = partial(self.process, diobj, wordobj)
                    self.ui.qwebView.page().toHtml(func)
                else:
                    self.update_word(wordobj)

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
        rewrite closeEvent, so when mainwindows closing, can clear up
        :param event:
        :return: None
        """
        AsyncTask.check_thread()

    def load_word(self, diobj, qword, tts_lang):
        """
        load dictobj, if don't exist then create it
        :param diobj:
        :param qword:
        :return: dictobj, is_new
        """
        data_path = os.path.join(data_dir, 'dictionaries', diobj.name, qword)
        if os.path.exists(data_path) and not os.path.isdir(data_path):
            raise RuntimeError("Loading failed: [%s] is'nt directory" % data_path)
        if os.path.exists(data_path):
            try:
                wordobj = DictWord.load(data_path)
                return wordobj, False
            except Exception as e:
                QMessageBox.warning(self, 'Warning', 'Loading failed: [%s], %s' % (data_path, str(e)))
        else:
            os.makedirs(data_path, exist_ok=True)
        wordobj = DictWord(data_path=data_path, tts_lang=tts_lang, query_word=qword)
        return wordobj, True

    def update_word(self, wordobj):
        pass

    @coroutine
    def process(self, diobj, wordobj, html):
        info = '%s, parse html' % wordobj.query_word
        self._query_progress(0, info)
        yield AsyncTask(diobj.parse_html, wordobj, html)

        info = '%s, translate to voice ...' % wordobj.query_word
        self._query_progress(10, info)
        total = 0
        for w in wordobj.words:
            if not w.title_voices and w.title_text:
                total += 1
            if not w.content_voices and w.content_text:
                total += 1
        cur = 0
        for w in wordobj.words:
            if not w.title_voices and w.title_text:
                yield AsyncTask(_worker, sinfo)
                cur += 1
                progress = 10 + int(90 * cur/total)
                self._query_progress(progress, info)
            if not w.content_voices and w.content_text:
                yield AsyncTask(_worker, sinfo)
                progress = 10 + int(90 * cur / total)
                self._query_progress(progress, info)

        info = '%s, finished!' % wordobj.query_word
        self._query_progress(100, info)

        DictWord.dump(wordobj)
        self.update_word(wordobj)
        self._query_finsh()
        return
