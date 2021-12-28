from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtWidgets import QTableWidgetItem
from classes import *
from PyQt5 import QtCore, QtWidgets
import sys

class Ui_MainWindow:
    def __init__(self):
        self.ui = None
        self.prov = 0
        self.transaction = None
        self.textBrowser = None
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = None
        self.centralwidget = None
        self.gridLayout = None
        self.label_5 = None
        self.pushButton_2 = None
        self.pushButton_3 = None
        self.comboBox_4 = None
        self.label = None
        self.comboBox = None
        self.tableWidget = None
        self.pushButton = None
        self.textBrowser = None
        self.label_4 = None
        self.label_3 = None
        self.label_2 = None
        self.comboBox_2 = None
        self.comboBox_3 = None
        self.pushButton_4 = None
        self.menubar = None
        self.statusbar = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(200, 20))
        self.label_5.setMaximumSize(QtCore.QSize(200, 20))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 10, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 11, 2, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_4.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout.addWidget(self.comboBox_4, 9, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(200, 20))
        self.label.setMaximumSize(QtCore.QSize(200, 20))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 2, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 22, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 21, 2, 1, 1)
        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(200, 100))
        self.textBrowser.setMaximumSize(QtCore.QSize(200, 100))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 20, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(200, 20))
        self.label_4.setMaximumSize(QtCore.QSize(200, 20))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 19, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(200, 20))
        self.label_3.setMaximumSize(QtCore.QSize(200, 20))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 20))
        self.label_2.setMaximumSize(QtCore.QSize(200, 20))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 2, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 4, 2, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_3.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 6, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 12, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Панель Админа"))
        self.label_5.setText(_translate("MainWindow", "Выберите как изменить таблицу"))
        self.pushButton_2.setText(_translate("MainWindow", "Изменить таблицу"))
        self.pushButton_3.setText(_translate("MainWindow", "Подтвердить изменения"))
        self.label.setText(_translate("MainWindow", "Выберите таблицу из списка"))
        self.pushButton.setText(_translate("MainWindow", "Вывод таблицы"))
        self.label_4.setText(_translate("MainWindow", "Поле ввода"))
        self.label_3.setText(_translate("MainWindow", "Выберите строку из таблицы"))
        self.label_2.setText(_translate("MainWindow", "Выберите столбец из таблицы"))
        self.pushButton_4.setText(_translate("MainWindow", "Отменить изменения"))
        self.comboBox.addItem("Аккаунты")
        self.comboBox.addItem("Статусы пользователей")
        self.comboBox.addItem("Пациенты")
        self.comboBox.addItem("День")
        self.comboBox.addItem("Специализация")
        self.comboBox.addItem("Статус приёма")
        self.comboBox.addItem("Кабинеты")
        self.comboBox.addItem("Персонал")
        self.comboBox.addItem("Время работы")
        self.comboBox.addItem("Приём")
        self.comboBox.addItem("Мед книжка")
        self.comboBox_4.addItem("Добавить строку")
        self.comboBox_4.addItem("Удалить строку")
        self.comboBox_4.addItem("Обновить элемент")