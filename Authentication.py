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
        login_pan.resize(375, 311)
        login_pan.setMinimumSize(QtCore.QSize(0, 0))
        login_pan.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.centralwidget = QtWidgets.QWidget(login_pan)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 352, 272))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 2)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setMinimumSize(QtCore.QSize(350, 30))
        self.textEdit.setMaximumSize(QtCore.QSize(350, 30))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_2.setMinimumSize(QtCore.QSize(350, 30))
        self.textEdit_2.setMaximumSize(QtCore.QSize(350, 30))
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 3, 0, 1, 4)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 4)
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_3.setMinimumSize(QtCore.QSize(350, 30))
        self.textEdit_3.setMaximumSize(QtCore.QSize(350, 30))
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.textEdit_3, 5, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setMinimumSize(QtCore.QSize(110, 40))
        self.comboBox.setMaximumSize(QtCore.QSize(110, 40))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 7, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(110, 40))
        self.comboBox_2.setMaximumSize(QtCore.QSize(110, 40))
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 7, 1, 1, 2)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setMinimumSize(QtCore.QSize(110, 40))
        self.comboBox_3.setMaximumSize(QtCore.QSize(110, 40))
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 7, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 8, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 40))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 2, 1, 2)
        login_pan.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(login_pan)
        self.statusbar.setObjectName("statusbar")
        login_pan.setStatusBar(self.statusbar)

        self.retranslateUi(login_pan)
        QtCore.QMetaObject.connectSlotsByName(login_pan)

    def retranslateUi(self, login_pan):
        _translate = QtCore.QCoreApplication.translate
        login_pan.setWindowTitle(_translate("MainWindow", "Вход"))
        self.label_2.setText(_translate("MainWindow", "Введите логин"))
        self.label.setText(_translate("MainWindow", "Введите пароль"))
        self.label_3.setText(_translate("MainWindow", "При регистрации введите ФИО, если вы пациент/из персонала"))
        self.label_4.setText(_translate("MainWindow", "Роль"))
        self.label_5.setText(_translate("MainWindow", "специализация"))
        self.label_6.setText(_translate("MainWindow", "Кабинет"))
        self.pushButton_2.setText(_translate("MainWindow", "Создать аккаунт"))
        self.pushButton.setText(_translate("MainWindow", "Войти"))
        self.comboBox.addItem("1")
        self.comboBox.addItem("2")
        self.comboBox.addItem("3")
        p = session.query(offices).all()
        for i in range(session.query(offices).count()):
            self.comboBox_2.addItem(str(p[i].id))
        p = session.query(specialization).all()
        for i in range(session.query(specialization).count()):
            self.comboBox_3.addItem(str(p[i].id))