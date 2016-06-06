# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Jun  6 13:00:34 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1352, 670)
        MainWindow.setMinimumSize(QtCore.QSize(1352, 670))
        MainWindow.setMaximumSize(QtCore.QSize(1352, 670))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ns_field = QtGui.QLineEdit(self.centralwidget)
        self.ns_field.setGeometry(QtCore.QRect(50, 60, 113, 20))
        self.ns_field.setObjectName(_fromUtf8("ns_field"))
        self.ns = QtGui.QLabel(self.centralwidget)
        self.ns.setGeometry(QtCore.QRect(10, 60, 21, 16))
        self.ns.setObjectName(_fromUtf8("ns"))
        self.scan = QtGui.QPushButton(self.centralwidget)
        self.scan.setGeometry(QtCore.QRect(190, 60, 81, 24))
        self.scan.setObjectName(_fromUtf8("scan"))
        self.log_text = QtGui.QTextEdit(self.centralwidget)
        self.log_text.setGeometry(QtCore.QRect(370, 60, 341, 171))
        self.log_text.setObjectName(_fromUtf8("log_text"))
        self.log = QtGui.QLabel(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(510, 40, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.log.setFont(font)
        self.log.setObjectName(_fromUtf8("log"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 200, 181, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.period_set = QtGui.QLabel(self.centralwidget)
        self.period_set.setGeometry(QtCore.QRect(110, 180, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.period_set.setFont(font)
        self.period_set.setObjectName(_fromUtf8("period_set"))
        self.hegraph = QtGui.QGraphicsView(self.centralwidget)
        self.hegraph.setGeometry(QtCore.QRect(30, 310, 371, 301))
        self.hegraph.setObjectName(_fromUtf8("hegraph"))
        self.phapgraph = QtGui.QGraphicsView(self.centralwidget)
        self.phapgraph.setGeometry(QtCore.QRect(500, 310, 361, 301))
        self.phapgraph.setObjectName(_fromUtf8("phapgraph"))
        self.dpgraph = QtGui.QGraphicsView(self.centralwidget)
        self.dpgraph.setGeometry(QtCore.QRect(960, 310, 351, 301))
        self.dpgraph.setObjectName(_fromUtf8("dpgraph"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 280, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1352, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "IMR Scan", None))
        self.ns.setText(_translate("MainWindow", "SN", None))
        self.scan.setText(_translate("MainWindow", "Scan", None))
        self.log.setText(_translate("MainWindow", "Results", None))
        self.period_set.setText(_translate("MainWindow", "Period", None))
        self.label.setText(_translate("MainWindow", "He", None))

