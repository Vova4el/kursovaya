from PyQt5 import QtCore, QtWidgets
from Qt import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from classes import *
import sys


class login_panell:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.login_pan = None
        self.ui = None
        self.statusbar = None
        self.label_2 = None
        self.label = None
        self.textEdit_2 = None
        self.textEdit = None
        self.pushButton_2 = None
        self.pushButton = None
        self.centralwidget = None

    def setupUi(self, login_pan):
        login_pan.setObjectName("login_pan")
        login_pan.resize(385, 210)
        login_pan.setMinimumSize(QtCore.QSize(385, 210))
        login_pan.setMaximumSize(QtCore.QSize(385, 210))
        self.centralwidget = QtWidgets.QWidget(login_pan)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 150, 180, 34))
        self.pushButton.setMinimumSize(QtCore.QSize(180, 34))
        self.pushButton.setMaximumSize(QtCore.QSize(180, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 150, 180, 34))
        self.pushButton_2.setMinimumSize(QtCore.QSize(180, 34))
        self.pushButton_2.setMaximumSize(QtCore.QSize(180, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 40, 351, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 110, 351, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 131, 16))
        self.label_2.setObjectName("label_2")
        login_pan.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(login_pan)
        self.statusbar.setObjectName("statusbar")
        login_pan.setStatusBar(self.statusbar)

        self.retranslateUi(login_pan)
        QtCore.QMetaObject.connectSlotsByName(login_pan)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("login_pan", "Вход"))
        self.pushButton.setText(_translate("login_pan", "Войти в аккаунт"))
        self.pushButton_2.setText(_translate("login_pan", "Создать новый аккаунт"))
        self.label.setText(_translate("login_pan", "Поле ввода пароля"))
        self.label_2.setText(_translate("login_pan", "Поле ввода логина"))