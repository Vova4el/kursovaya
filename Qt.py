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
        self.textEdit = None
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
        self.textEdit = None
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
        MainWindow.resize(946, 545)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(9, 9, 721, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(730, 30, 206, 466))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(200, 20))
        self.label.setMaximumSize(QtCore.QSize(200, 20))
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 20))
        self.label_2.setMaximumSize(QtCore.QSize(200, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(200, 20))
        self.label_3.setMaximumSize(QtCore.QSize(200, 20))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_3.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_3.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_3.addWidget(self.comboBox_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(200, 20))
        self.label_5.setMaximumSize(QtCore.QSize(200, 20))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_4.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_4.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout_2.addWidget(self.comboBox_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(200, 20))
        self.label_4.setMaximumSize(QtCore.QSize(200, 20))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setMinimumSize(QtCore.QSize(200, 40))
        self.textEdit.setMaximumSize(QtCore.QSize(200, 40))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Окно Админа"))
        self.label.setText(_translate("MainWindow", "Выберите таблицу из списка"))
        self.label_2.setText(_translate("MainWindow", "Выберите столбец из таблицы"))
        self.label_3.setText(_translate("MainWindow", "Выберите № ID из таблицы"))
        self.label_5.setText(_translate("MainWindow", "Выберите как изменить таблицу"))
        self.pushButton_2.setText(_translate("MainWindow", "Изменить таблицу"))
        self.pushButton_3.setText(_translate("MainWindow", "Подтвердить изменения"))
        self.pushButton_4.setText(_translate("MainWindow", "Отменить изменения"))
        self.label_4.setText(_translate("MainWindow", "Поле ввода"))
        self.pushButton.setText(_translate("MainWindow", "Вывод таблицы"))
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