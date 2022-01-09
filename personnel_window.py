from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from classes import *
from personalQT import personalUI
from med_kniga_window import panel_med_kniga
from disc_window import disc_panel
import log_window
#ОКНО_ДЛЯ_ПЕРСОНАЛА#
class personal_panel(QMainWindow):
    def __init__(self, parent=None):
        super(personal_panel, self).__init__(parent)
        self.ui = personalUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.write_table())
        self.ui.pushButton_2.clicked.connect(lambda: self.exit_med_kniga())
        self.ui.pushButton_3.clicked.connect(lambda: self.exit_disc())
        self.ui.action.triggered.connect(lambda: self.exit_db_panel())
        self.write_table()

    # вывод по внешнему ключу
    def output_by_foreign_key(self,k,v,col,j):
        if k=='id_stat':
            q=session.query(user_status).filter_by(id=int(v)).first()
            self.ui.tableWidget.setItem(j, col, QTableWidgetItem(str(q.status)))
        elif k=='id_day':
            q=session.query(day).filter_by(id=int(v)).first()
            self.ui.tableWidget.setItem(j, col, QTableWidgetItem(str(q.name)))
        elif k=='id_spec':
            q=session.query(specialization).filter_by(id=int(v)).first()
            self.ui.tableWidget.setItem(j, col, QTableWidgetItem(str(q.name_spec)))
        elif k=='id_patient':
            q=session.query(patient).filter_by(id=int(v)).first()
            self.ui.tableWidget.setItem(j, col, QTableWidgetItem(str(q.name)))
        elif k == 'id_personnel':
            q = session.query(personnel).filter_by(id=int(v)).first()
            self.ui.tableWidget.setItem(j, col, QTableWidgetItem(str(q.name)))
        elif k == 'id_reception_status':
            q = session.query(reception_status).filter_by(id=int(v)).first()
            self.ui.tableWidget.setItem(j, col, QTableWidgetItem(str(q.name)))
        elif k == 'id_office':
            q = session.query(offices).filter_by(id=int(v)).first()
            self.ui.tableWidget.setItem(j, col, QTableWidgetItem(str(q.cab_num)))
        else:
            self.ui.tableWidget.setItem(j, col, QTableWidgetItem(str(v)))

    def write_table(self):
        self.ui.tableWidget.clearSelection()
        result = self.ui.comboBox.currentText()
        table = patient
        self.ui.tableWidget.setColumnCount(1)
        collums = ['name']
        self.ui.tableWidget.setHorizontalHeaderLabels(["ФИО"])
        if result == "Пациенты":
            table = patient
            self.ui.tableWidget.setColumnCount(1)
            collums = ['name']
            self.ui.tableWidget.setHorizontalHeaderLabels(["ФИО"])
        if result == "Персонал":
            table = personnel
            self.ui.tableWidget.setColumnCount(3)
            collums = ['id', 'id_spec', 'id_office', 'name']
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["Специализация персонала", "№ кабинета", "ФИО"])
        if result == "Время работы":
            table = working_hours
            self.ui.tableWidget.setColumnCount(4)
            collums = ['id', 'id_day', 'id_spec', 'work_hours', 'break_time']
            self.ui.tableWidget.setHorizontalHeaderLabels(
                [ "День", "Специализация", "Рабочее время", "Перерыв"])
        if result == "Приём":
            table = reception
            self.ui.tableWidget.setColumnCount(6)
            collums = ['id', 'id_patient', 'id_office', 'id_reception_status', 'id_personnel', 'id_spec', 'date']
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["ФИО пациента", "№ кабинета", "Статуса приёма", "ФИО персонала", "Специализация персонала", "Дата"])
        if result == "Мед книжка":
            table = med_knigа
            self.ui.tableWidget.setColumnCount(4)
            collums = ['id', 'id_patient', 'id_personnel', 'id_spec', 'diagnoz']
            self.ui.tableWidget.setHorizontalHeaderLabels(["ФИО пациента", "ФИО персонала", 'Специализация', "Диагноз"])
        line = session.query(table).count()
        self.ui.qTable = session.query(table).all()
        self.ui.tableWidget.setRowCount(line)
        sort = [0] * line
        j = 0
        for row, form in enumerate(self.ui.qTable):
            col = 0
            for c in collums:
                for k, v in vars(form).items():
                    if c == k:
                        self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(v)))
                        col += 1
        for i in session.query(table).all():
            sort[j] = i.id
            j += 1
        sort.sort()
        perem = 0
        j = -1
        for i in sort:
            j += 1
            for row, form in enumerate(self.ui.qTable):
                col = 0
                for c in collums:
                    for k, v in vars(form).items():
                        if c == k:
                            if c == 'id':
                                perem = v
                            if (c != 'id') & (perem == i):
                                self.output_by_foreign_key(k,v,col,j)
                                col += 1
        self.ui.tableWidget.resizeColumnsToContents()

    # Выход из окна персонала обратно в окно авторизации
    def exit_db_panel(self):
        print(23)
        self.hide()
        dialog = log_window.log_panel(parent=self)
        dialog.show()

    # Выход из окна персонала обратно в окно авторизации
    def exit_med_kniga(self):
        print(23)
        self.hide()
        print(24)
        dialog = panel_med_kniga(parent=self)
        print(25)
        dialog.show()

    # Выход из окна персонала
    def exit_disc(self):
        self.hide()
        dialog = disc_panel(parent=self)
        dialog.show()