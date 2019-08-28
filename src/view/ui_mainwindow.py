# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Wed Aug 28 20:58:32 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        self.menuquit = QtWidgets.QMenu(self.menubar)
        self.menuquit.setObjectName("menuquit")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuquit.addSeparator()
        self.menuquit.addAction(self.actionQuit)
        self.menubar.addAction(self.menuquit.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.menuquit.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuTest.setTitle(QtWidgets.QApplication.translate("MainWindow", "Test", None, -1))
        self.menu.setTitle(QtWidgets.QApplication.translate("MainWindow", "输入", None, -1))
        self.actionQuit.setText(QtWidgets.QApplication.translate("MainWindow", "Quit", None, -1))

