from PyQt5 import QtCore, QtWidgets
import sys

class personalUI:
    def __init__(self):
        self.ui = None
        self.prov = 0
        self.transaction = None
        self.textBrowser = None
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = None
        self.centralwidget = None
        self.tableWidget = None
        self.layoutWidget = None
        self.gridLayout = None
        self.pushButton = None
        self.label_7 = None
        self.comboBox = None
        self.pushButton_2 = None
        self.statusbar = None
        self.menubar = None
        self.menu = None
        self.action = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 560)
        MainWindow.setMinimumSize(QtCore.QSize(741, 560))
        MainWindow.setMaximumSize(QtCore.QSize(974, 560))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 961, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 460, 514, 58))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setMinimumSize(QtCore.QSize(150, 20))
        self.label_7.setMaximumSize(QtCore.QSize(150, 20))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setMinimumSize(QtCore.QSize(150, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(150, 30))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(95, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(95, 30))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(170, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(170, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(170, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????? ??????????????????"))
        self.label_7.setText(_translate("MainWindow", "???????????????? ??????????????"))
        self.pushButton.setText(_translate("MainWindow", "?????????? ??????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "???????????????? ???????????? ?? ?????? ????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "?????????? ?? ????????"))
        self.menu.setTitle(_translate("MainWindow", "?????????? ???? ????????????????"))
        self.action.setText(_translate("MainWindow", "?????????? ???? ??????"))
        self.comboBox.addItem("????????????????")
        self.comboBox.addItem("????????????????")
        self.comboBox.addItem("?????????? ????????????")
        self.comboBox.addItem("??????????")
        self.comboBox.addItem("?????? ????????????")
