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
        MainWindow.resize(738, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(9, 9, 721, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 500, 721, 178))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(165, 20))
        self.label_5.setMaximumSize(QtCore.QSize(165, 20))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 2, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(150, 20))
        self.label_6.setMaximumSize(QtCore.QSize(150, 20))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(160, 20))
        self.label_2.setMaximumSize(QtCore.QSize(160, 20))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 2, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 3, 3, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.widget)
        self.comboBox_5.setMinimumSize(QtCore.QSize(150, 30))
        self.comboBox_5.setMaximumSize(QtCore.QSize(150, 30))
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout.addWidget(self.comboBox_5, 1, 1, 3, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setMinimumSize(QtCore.QSize(150, 30))
        self.comboBox_4.setMaximumSize(QtCore.QSize(150, 30))
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout.addWidget(self.comboBox_4, 2, 0, 2, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(150, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(150, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 2, 2, 2, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 3, 2, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 2, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 1, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(150, 20))
        self.label_3.setMaximumSize(QtCore.QSize(150, 20))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 2, 2, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 5, 3, 2, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(150, 20))
        self.label.setMaximumSize(QtCore.QSize(150, 20))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(150, 20))
        self.label_4.setMaximumSize(QtCore.QSize(150, 20))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setMinimumSize(QtCore.QSize(150, 30))
        self.comboBox_3.setMaximumSize(QtCore.QSize(150, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 6, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setMinimumSize(QtCore.QSize(150, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(150, 30))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 7, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setMinimumSize(QtCore.QSize(150, 30))
        self.textEdit.setMaximumSize(QtCore.QSize(150, 30))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 7, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Окно админа"))
        self.label_5.setText(_translate("MainWindow", "Выберите как изменить таблицу"))
        self.label_6.setText(_translate("MainWindow", "Во что вывести"))
        self.label_2.setText(_translate("MainWindow", "Выберите столбец из таблицы"))
        self.pushButton_2.setText(_translate("MainWindow", "Изменить таблицу"))
        self.pushButton_3.setText(_translate("MainWindow", "Подтвердить изменения"))
        self.pushButton.setText(_translate("MainWindow", "Вывод таблицы"))
        self.pushButton_5.setText(_translate("MainWindow", "Вывод в файл"))
        self.label_3.setText(_translate("MainWindow", "Выберите ID из таблицы"))
        self.pushButton_4.setText(_translate("MainWindow", "Отменить изменения"))
        self.label.setText(_translate("MainWindow", "Выберите таблицу из списка"))
        self.label_4.setText(_translate("MainWindow", "Поле ввода"))
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
        self.comboBox_5.addItem("В Docx")
        self.comboBox_5.addItem("В Xlsx")