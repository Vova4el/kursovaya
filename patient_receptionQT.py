from PyQt5 import QtCore, QtWidgets
import sys

class receprionUI(object):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.prov = 0
        self.ui = None
        self.centralwidget = None
        self.tableWidget = None
        self.widget = None
        self.gridLayout = None
        self.label_4 = None
        self.label_2 = None
        self.label_6 = None
        self.textEdit = None
        self.pushButton_2 = None
        self.comboBox_2 = None
        self.comboBox_5 = None
        self.label_5 = None
        self.pushButton_3 = None
        self.label_3 = None
        self.label_7 = None
        self.comboBox_4 = None
        self.pushButton_4 = None
        self.comboBox_3 = None
        self.comboBox_6 = None
        self.menubar = None
        self.menu = None
        self.statusbar = None
        self.action = None
        self.action_2 = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 633)
        MainWindow.setMinimumSize(QtCore.QSize(839, 633))
        MainWindow.setMaximumSize(QtCore.QSize(839, 633))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 821, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 450, 820, 140))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(200, 20))
        self.label_4.setMaximumSize(QtCore.QSize(200, 20))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(150, 20))
        self.label_2.setMaximumSize(QtCore.QSize(150, 20))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(150, 20))
        self.label_6.setMaximumSize(QtCore.QSize(150, 20))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setMinimumSize(QtCore.QSize(200, 40))
        self.textEdit.setMaximumSize(QtCore.QSize(200, 40))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 1, 2, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.widget)
        self.comboBox_5.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_5.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout.addWidget(self.comboBox_5, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(200, 20))
        self.label_5.setMaximumSize(QtCore.QSize(200, 20))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(150, 20))
        self.label_3.setMaximumSize(QtCore.QSize(150, 20))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setMinimumSize(QtCore.QSize(150, 20))
        self.label_7.setMaximumSize(QtCore.QSize(150, 20))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 3, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_4.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout.addWidget(self.comboBox_4, 3, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_3.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 3, 2, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.widget)
        self.comboBox_6.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_6.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout.addWidget(self.comboBox_6, 3, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 21))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "???????? ????????????????????"))
        self.label_4.setText(_translate("MainWindow", "???????? ??????????"))
        self.label_2.setText(_translate("MainWindow", "???????????????? ?????? ??????????????????"))
        self.label_6.setText(_translate("MainWindow", "???????????????? ??????????????????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "?????????????????? ????????????????"))
        self.label_5.setText(_translate("MainWindow", "????????????????, ?????? ???????????? ??????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "?????????????????????? ????????????"))
        self.label_3.setText(_translate("MainWindow", "???????????????? ???????????? ???? ??????????????"))
        self.label_7.setText(_translate("MainWindow", "???????????????? ???????????? ???? ??????????"))
        self.pushButton_4.setText(_translate("MainWindow", "???????????????? ????????????"))
        self.menu.setTitle(_translate("MainWindow", "??????????"))
        self.action.setText(_translate("MainWindow", "???????? ????????????????????????????"))
        self.action_2.setText(_translate("MainWindow", "???????? ????????????????"))
        self.comboBox_4.addItem("???????????????????? ???? ??????????")
        self.comboBox_4.addItem("???????????????? ???????????? ???? ??????????")
        self.comboBox_6.addItem("???????????????????? ???? ??????????????????????")
        self.comboBox_6.addItem("???????????????????? ???? ??????????????????")
        self.comboBox_6.addItem("???????????? ???? ??????????????????????")
        self.comboBox_6.addItem("???????????? ???? ??????????????????")

