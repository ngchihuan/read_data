# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read_data.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(971, 695)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 931, 641))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 971, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFit = QtWidgets.QMenu(self.menubar)
        self.menuFit.setObjectName("menuFit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionChoose_Functions = QtWidgets.QAction(MainWindow)
        self.actionChoose_Functions.setObjectName("actionChoose_Functions")
        self.actionAdd_Functions = QtWidgets.QAction(MainWindow)
        self.actionAdd_Functions.setObjectName("actionAdd_Functions")
        self.actionRecent_Function = QtWidgets.QAction(MainWindow)
        self.actionRecent_Function.setObjectName("actionRecent_Function")
        self.menuFile.addAction(self.actionOpen)
        self.menuFit.addAction(self.actionChoose_Functions)
        self.menuFit.addAction(self.actionAdd_Functions)
        self.menuFit.addAction(self.actionRecent_Function)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuFit.setTitle(_translate("MainWindow", "Fit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionChoose_Functions.setText(_translate("MainWindow", "Choose Functions"))
        self.actionAdd_Functions.setText(_translate("MainWindow", "Add Functions"))
        self.actionRecent_Function.setText(_translate("MainWindow", "Recently used"))

