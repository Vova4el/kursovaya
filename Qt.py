from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from classes import *
from datetime import datetime, date, time
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.prov = 0
        self.transaction = None
        self.textBrowser = None
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

        self.add_func()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Выберите как изменить таблицу"))
        self.pushButton_2.setText(_translate("MainWindow", "Изменить таблицу"))
        self.pushButton_3.setText(_translate("MainWindow", "Подтвердить изменения"))
        self.label.setText(_translate("MainWindow", "Выберите таблицу из списка"))
        self.pushButton.setText(_translate("MainWindow", "Вывод таблицы"))
        self.label_4.setText(_translate("MainWindow", "Поле ввода"))
        self.label_3.setText(_translate("MainWindow", "Выберите строку из таблицы"))
        self.label_2.setText(_translate("MainWindow", "Выберите столбец из таблицы"))
        self.pushButton_4.setText(_translate("MainWindow", "Отменить изменения"))
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

    def add_func(self):
        self.pushButton.clicked.connect(lambda: self.write_table())
        self.pushButton_2.clicked.connect(lambda: self.change_table())
        self.pushButton_3.clicked.connect(lambda: self.confirm_change())
        self.pushButton_4.clicked.connect(lambda: self.undo_change())

    def write_table(self):
        self.comboBox_2.clear()
        self.comboBox_3.clear()
        self.tableWidget.clearSelection()
        result = self.comboBox.currentText()
        line = 0
        collums = []
        if result == "Пациенты":
            table = patient
            self.tableWidget.setColumnCount(2)
            collums = ['id', 'name']
            self.tableWidget.setHorizontalHeaderLabels(["ID", "ФИО"])
        if result == "День":
            table = day
            self.tableWidget.setColumnCount(2)
            collums = ['id', 'name']
            self.tableWidget.setHorizontalHeaderLabels(
                ["ID", "День"])
        if result == "Специализация":
            table = specialization
            self.tableWidget.setColumnCount(2)
            collums = ['id', 'name_spec']
            self.tableWidget.setHorizontalHeaderLabels(["ID", "Специализация"])
        if result == "Статус приёма":
            table = reception_status
            self.tableWidget.setColumnCount(2)
            collums = ['id', 'name']
            self.tableWidget.setHorizontalHeaderLabels(["ID", "Статус"])
        if result == "Кабинеты":
            table = offices
            self.tableWidget.setColumnCount(2)
            collums = ['id', 'cab_num']
            self.tableWidget.setHorizontalHeaderLabels(["ID", "Номер кабинета"])
        if result == "Персонал":
            table = personnel
            self.tableWidget.setColumnCount(4)
            collums = ['id', 'id_spec', 'id_office', 'name']
            self.tableWidget.setHorizontalHeaderLabels(
                ["ID", "ID специализации", "ID кабинета", "ФИО"])
        if result == "Время работы":
            table = working_hours
            self.tableWidget.setColumnCount(6)
            collums = ['id', 'id_day', 'id_personnel', 'work_hours', 'free_time', 'break2']
            self.tableWidget.setHorizontalHeaderLabels(["ID", "ID дня", "ID персонала", "рабочее время", "свободное время", "перерыв"])
        if result == "Приём":
            table = reception
            self.tableWidget.setColumnCount(7)
            collums = ['id', 'id_patient', 'id_office', 'id_reception_status', 'id_personnel', 'id_spec', 'date']
            self.tableWidget.setHorizontalHeaderLabels(["ID", "ID пациента", "ID кабинета", "ID статуса приёма", "ID персонала", "id специализации", "Дата"])
        if result == "Мед книжка":
            table = med_knigа
            self.tableWidget.setColumnCount(3)
            collums = ['id', 'id_patient', 'diagnoz']
            self.tableWidget.setHorizontalHeaderLabels(["ID", "ID пациента", "Диагноз"])
        line = session.query(table).count()
        self.qTable = session.query(table).all()
        self.tableWidget.setRowCount(line)
        sort = [0] * line
        j = 0
        for i in collums:
            if i != 'id':
                self.comboBox_2.addItem(i)
        for i in range(line):
            self.comboBox_3.addItem(str(i + 1))
        for row, form in enumerate(self.qTable):
            col = 0
            for c in collums:
                for k, v in vars(form).items():
                    if c == k:
                        self.tableWidget.setItem(row, col, QTableWidgetItem(str(v)))
                        col += 1
        for i in session.query(table).all():
            sort[j] = i.id
            j += 1
        self.comboBox_3.clear()
        sort.sort()
        for i in sort:
            self.comboBox_3.addItem(str(i))
        perem = 0
        j = -1
        for i in sort:
            j += 1
            for row, form in enumerate(self.qTable):
                col = 0
                for c in collums:
                    for k, v in vars(form).items():
                        if c == k:
                            if c == 'id':
                                perem = v
                            if ((c == 'id') & (v == i)) | ((c != 'id') & (perem == i)):
                                self.tableWidget.setItem(j, col, QTableWidgetItem(str(v)))
                                col += 1
        """print('44444444444444444444')
        t = session.query(reception).all()
        print('44444444444444444444')
        t2 = session.query(working_hours).all()
        print('444444444444444444442222222')
        line = session.query(reception).count()
        priyom = session.query(reception).all()
        time1 = datetime.now()
        print(f'sss=', datetime.isoweekday(time1))
        print(f'time1=', time1)
        print(f'priyom[0].date', priyom[0].date)
        for i in range(line):
            if time1 <= priyom[i].date:
                query = session.query(reception).get(i + 1)
                query.id_reception_status = 2
            else:
                query = session.query(reception).get(i + 1)
                query.id_reception_status = 1"""

        self.tableWidget.resizeColumnsToContents()



        #print(f'дата= ',t[0].date,f'     дата2- ',t[1].date)
        #d = date(2005, 7, 14)
        #t2 = time(12, 30)
        #print(f't3[0].work_hours[0]', t3[0].work_hours[0])
        #print(f'sssssssssss',datetime.combine(d, t2))
        #t1='2001-03-11 20:05:13'
        #time1=datetime.now()
        #print(time1)
        #print('3333333333')
        ##dt = datetime.combine(d,datetime.strptime(t3[0].work_hours[0],"%H:%M:%S"))
        #print('4444444444444')
        #print(dt)
        #if dt>dt:
        #    print('1111111111')
        #else:
        #    print('2222222222')

#####################     РАБОТАЕТ УДАЛЕНИЕ СТРОК
        #session.query(patient).filter_by(id=5).delete(synchronize_session=False)
        #session.commit()
#####################     РАБОТАЕТ ДОБАВЛЕНИЕ СТРОК
        #user_setting = patient(id=5, name='Билли')
        #session.add(user_setting)
        #session.commit()
#####################     РАБОТАЕТ ОБНОВЛЕНИЕ СТРОК
        #query = session.query(patient).filter(patient.id == 2).first()
        #query.name = 'Черных Владимир Сергеевич'
        #session.commit()
#####################
    def change_table(self):
        self.statusbar.clearMessage()
        if self.prov == 0:
            self.transaction = conn.begin()
            self.prov = 1
        result = self.comboBox.currentText()
        change = self.comboBox_4.currentText()
        stlb = int(self.comboBox_3.currentText())
        text = self.textBrowser.toPlainText()
        table = patient
        if result == "Пациенты":
            table = patient
        if result == "День":
            table = day
        if change == "Добавить строку":
            line = session.query(table).count()
            tabl = session.query(table).all()
            print('ssssss')
            f = 0  # флаг
            free_id = 1  # свободный индекс
            while f == 0:
                print('1')
                for i in range(line):
                    print(f'table[i].id=',tabl[i].id)
                    if free_id == tabl[i].id:
                        f = 1
                if f == 1:
                    free_id = free_id + 1
                    f = 0
                else:
                    f = 1
            print(f'free id=', free_id)
            new = patient(id=free_id, name=text)
            session.add(new)
        tabl = session.query(table).all()
        if change == "Обновить элемент":
            query = session.query(table).get(stlb)
            query.name = text
        if change == "Удалить строку":
            session.query(table).filter_by(id=stlb).delete(synchronize_session=False)
        self.write_table()

    def confirm_change(self):
        if self.prov != 0:
            self.prov = 0
            session.commit()
            self.write_table()
        else:
            self.statusbar.showMessage("Сначала внесите изменение в таблицу")

    def undo_change(self):
        if self.prov != 0:
            #self.transaction.rollback()
            session.rollback()
            self.prov = 0
            self.write_table()
        else:
            self.statusbar.showMessage("Сначала внесите изменение в таблицу")