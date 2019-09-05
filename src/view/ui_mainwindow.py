# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1428, 716)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(1000, 0))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.dictionaryBox = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dictionaryBox.sizePolicy().hasHeightForWidth())
        self.dictionaryBox.setSizePolicy(sizePolicy)
        self.dictionaryBox.setMaximumSize(QtCore.QSize(400, 16777215))
        self.dictionaryBox.setObjectName("dictionaryBox")
        self.verticalLayout_7.addWidget(self.dictionaryBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.loadingBar = QtWidgets.QProgressBar(self.groupBox_7)
        self.loadingBar.setObjectName("loadingBar")
        self.verticalLayout_4.addWidget(self.loadingBar)
        self.verticalLayout_7.addWidget(self.groupBox_7)
        self.groupBox_6 = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.autoplayBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.autoplayBox.setObjectName("autoplayBox")
        self.verticalLayout_5.addWidget(self.autoplayBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleEdit.sizePolicy().hasHeightForWidth())
        self.titleEdit.setSizePolicy(sizePolicy)
        self.titleEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.titleEdit.setObjectName("titleEdit")
        self.verticalLayout.addWidget(self.titleEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.titlePlay = QtWidgets.QPushButton(self.groupBox_2)
        self.titlePlay.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.titlePlay.setIcon(icon1)
        self.titlePlay.setIconSize(QtCore.QSize(32, 32))
        self.titlePlay.setObjectName("titlePlay")
        self.horizontalLayout.addWidget(self.titlePlay)
        self.titleStop = QtWidgets.QPushButton(self.groupBox_2)
        self.titleStop.setEnabled(True)
        self.titleStop.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.titleStop.setIcon(icon2)
        self.titleStop.setIconSize(QtCore.QSize(32, 32))
        self.titleStop.setObjectName("titleStop")
        self.horizontalLayout.addWidget(self.titleStop)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.contentEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.contentEdit.setObjectName("contentEdit")
        self.verticalLayout_2.addWidget(self.contentEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.contentPlay = QtWidgets.QPushButton(self.groupBox)
        self.contentPlay.setText("")
        self.contentPlay.setIcon(icon1)
        self.contentPlay.setIconSize(QtCore.QSize(32, 32))
        self.contentPlay.setObjectName("contentPlay")
        self.horizontalLayout_2.addWidget(self.contentPlay)
        self.contentStop = QtWidgets.QPushButton(self.groupBox)
        self.contentStop.setText("")
        self.contentStop.setIcon(icon2)
        self.contentStop.setIconSize(QtCore.QSize(32, 32))
        self.contentStop.setObjectName("contentStop")
        self.horizontalLayout_2.addWidget(self.contentStop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.progressLabel = QtWidgets.QLabel(self.groupBox_5)
        self.progressLabel.setObjectName("progressLabel")
        self.verticalLayout_3.addWidget(self.progressLabel)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.verticalLayout_5.addWidget(self.groupBox_5)
        self.verticalLayout_6.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Dictionary"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Dictionary"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Browser"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Loading"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Voice"))
        self.autoplayBox.setText(_translate("MainWindow", "Auto play voice"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Title"))
        self.groupBox.setTitle(_translate("MainWindow", "Content"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Progress"))
        self.progressLabel.setText(_translate("MainWindow", "TextLabel"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
import resouce_rc
