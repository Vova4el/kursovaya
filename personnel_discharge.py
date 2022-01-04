from PyQt5 import QtCore,  QtWidgets


class pers_discharge(object):
    def __init__(self):
        self.ui = None
        self.prov = 0
        self.transaction = None
        self.centralwidget = None
        self.tableWidget = None
        self.widget = None
        self.gridLayout = None
        self.label_6 = None
        self.label = None
        self.comboBox_5 = None
        self.comboBox = None
        self.pushButton = None
        self.label_3 = None
        self.label_5 = None
        self.comboBox_3 = None
        self.comboBox_4 = None
        self.pushButton_5 = None
        self.menubar = None
        self.menu = None
        self.statusbar = None
        self.action = None
        self.action_2 = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(738, 666)
        MainWindow.setMinimumSize(QtCore.QSize(738, 666))
        MainWindow.setMaximumSize(QtCore.QSize(738, 666))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(9, 9, 721, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 500, 524, 120))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(170, 20))
        self.label_6.setMaximumSize(QtCore.QSize(170, 20))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(170, 20))
        self.label.setMaximumSize(QtCore.QSize(170, 20))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.widget)
        self.comboBox_5.setMinimumSize(QtCore.QSize(170, 30))
        self.comboBox_5.setMaximumSize(QtCore.QSize(170, 30))
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout.addWidget(self.comboBox_5, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setMinimumSize(QtCore.QSize(170, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(170, 30))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(170, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(170, 30))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(120, 20))
        self.label_3.setMaximumSize(QtCore.QSize(120, 20))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(140, 20))
        self.label_5.setMaximumSize(QtCore.QSize(140, 20))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setMinimumSize(QtCore.QSize(170, 30))
        self.comboBox_3.setMaximumSize(QtCore.QSize(170, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 3, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setMinimumSize(QtCore.QSize(170, 30))
        self.comboBox_4.setMaximumSize(QtCore.QSize(170, 30))
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout.addWidget(self.comboBox_4, 3, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(170, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(170, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Во что вывести"))
        self.label.setText(_translate("MainWindow", "Выберите таблицу из списка"))
        self.pushButton.setText(_translate("MainWindow", "Вывод таблицы"))
        self.label_3.setText(_translate("MainWindow", "Выберите пациента "))
        self.label_5.setText(_translate("MainWindow", "Выберите как вывести"))
        self.pushButton_5.setText(_translate("MainWindow", "Вывод в файл"))
        self.menu.setTitle(_translate("MainWindow", "Назад"))
        self.action.setText(_translate("MainWindow", "Окно аутентификации"))
        self.action_2.setText(_translate("MainWindow", "Окно персонала"))
        self.comboBox.addItem("Приём")
        self.comboBox.addItem("Мед книжка")
        self.comboBox_4.addItem("Все таблицы")
        self.comboBox_4.addItem("Все таблицы, но строки со мной")
        self.comboBox_4.addItem("Все таблицы, но строки с пациентом")
        self.comboBox_4.addItem("Всю таблицу")
        self.comboBox_4.addItem("Всю таблицу, но строки со мной")
        self.comboBox_4.addItem("Всю таблицу, но строки с пациентом")
        self.comboBox_5.addItem("В Docx")
        self.comboBox_5.addItem("В Xlsx")
