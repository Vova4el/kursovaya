from PyQt5 import QtCore, QtWidgets
from admin_Qt import *
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
        self.label_3 = None
        self.label_4 = None
        self.label = None
        self.textEdit_3 = None
        self.textEdit_2 = None
        self.textEdit = None
        self.pushButton_2 = None
        self.pushButton = None
        self.comboBox = None
        self.centralwidget = None

    def setupUi(self, login_pan):
        login_pan.setObjectName("login_pan")
        login_pan.resize(375, 288)
        login_pan.setMinimumSize(QtCore.QSize(375, 288))
        login_pan.setMaximumSize(QtCore.QSize(375, 288))
        self.centralwidget = QtWidgets.QWidget(login_pan)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(127, 12, 75, 16))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(11, 31, 350, 30))
        self.textEdit.setMinimumSize(QtCore.QSize(350, 30))
        self.textEdit.setMaximumSize(QtCore.QSize(350, 30))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(127, 67, 82, 16))
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(11, 86, 350, 30))
        self.textEdit_2.setMinimumSize(QtCore.QSize(350, 30))
        self.textEdit_2.setMaximumSize(QtCore.QSize(350, 30))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(11, 122, 321, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(11, 141, 350, 30))
        self.textEdit_3.setMinimumSize(QtCore.QSize(350, 30))
        self.textEdit_3.setMaximumSize(QtCore.QSize(350, 30))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(55, 177, 24, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(145, 177, 76, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(285, 177, 43, 16))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(11, 196, 110, 30))
        self.comboBox.setMinimumSize(QtCore.QSize(110, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(110, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(255, 196, 110, 30))
        self.comboBox_3.setMinimumSize(QtCore.QSize(110, 30))
        self.comboBox_3.setMaximumSize(QtCore.QSize(110, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(133, 196, 110, 30))
        self.comboBox_2.setMinimumSize(QtCore.QSize(110, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(110, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(11, 232, 150, 30))
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(215, 232, 150, 30))
        self.pushButton.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButton.setObjectName("pushButton")
        login_pan.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(login_pan)
        self.statusbar.setObjectName("statusbar")
        login_pan.setStatusBar(self.statusbar)

        self.retranslateUi(login_pan)
        QtCore.QMetaObject.connectSlotsByName(login_pan)

    def retranslateUi(self, login_pan):
        _translate = QtCore.QCoreApplication.translate
        login_pan.setWindowTitle(_translate("MainWindow", "Окно авторизации"))
        self.label_2.setText(_translate("MainWindow", "Введите логин"))
        self.label.setText(_translate("MainWindow", "Введите пароль"))
        self.label_3.setText(_translate("MainWindow", "При регистрации введите ФИО, если вы пациент/из персонала"))
        self.label_4.setText(_translate("MainWindow", "Роль"))
        self.label_5.setText(_translate("MainWindow", "специализация"))
        self.label_6.setText(_translate("MainWindow", "Кабинет"))
        self.pushButton_2.setText(_translate("MainWindow", "Создать аккаунт"))
        self.pushButton.setText(_translate("MainWindow", "Войти"))
