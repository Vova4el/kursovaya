from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem
import classes
from patientQT import patientUI
from patient_reception_window import panel_receprion
from backup_bd import *
from pat_disc_window import pat_disc_panel
import log_window


#ОКНО_ПАЦИЕНТА
class patient_panel(QMainWindow):
    def __init__(self, parent=None):
        super(patient_panel, self).__init__(parent)
        self.ui = patientUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.write_table())
        self.ui.pushButton_2.clicked.connect(lambda: self.exit_reception())
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
        collums = []
        if result == "Персонал":
            table = personnel
            self.ui.tableWidget.setColumnCount(3)
            collums = ['id', 'id_spec', 'id_office', 'name']
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["Специализация", "№ кабинета", "ФИО"])
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
                ["ФИО пациента", "№ кабинета", "Статуса приёма", "фИО персонала", "Специализация", "Дата"])
        if result == "Мед книжка":
            table = med_knigа
            self.ui.tableWidget.setColumnCount(3)
            collums = ['id', 'id_patient', 'id_personnel', 'diagnoz']
            self.ui.tableWidget.setHorizontalHeaderLabels(["ФИО пациента", "фИО персонала", "Диагноз"])
        if result == "Мед книжка":
            line = session.query(table).filter_by(id_patient=classes.glob_id).count()
        else:
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
        if result == "Мед книжка":
            for i in session.query(table).filter_by(id_patient=classes.glob_id):
                sort[j] = i.id
                j += 1
        else:
            for i in session.query(table).all():
                sort[j] = i.id
                j += 1
        sort.sort()
        perem = 0
        j = -1
        f = 0
        f2 = 1
        for i in sort:
            if result == "Мед книжка":
                if f2 == 1:
                    j += 1
                    f2 = 2
            else:
                j += 1
            for row, form in enumerate(self.ui.qTable):
                col = 0
                for c in collums:
                    for k, v in vars(form).items():
                        if c == k:
                            if c == 'id':
                                perem = v
                                if result == "Мед книжка":
                                    p = session.query(table).filter_by(id=int(v)).first()
                                    if p.id_patient == classes.glob_id:
                                        f = 1
                                    else:
                                        f = 0
                            if result == "Мед книжка":
                                if (c != 'id') and (perem == i) and (f == 1):
                                    self.output_by_foreign_key(k, v, col, j)
                                    col += 1
                            else:
                                if (c != 'id') & (perem == i):
                                    self.output_by_foreign_key(k, v, col, j)
                                    col += 1
        self.ui.tableWidget.resizeColumnsToContents()

    # Выход из окна пациента обратно в окно авторизации
    def exit_db_panel(self):
        print(23)
        self.hide()
        dialog = log_window.log_panel(parent=self)
        dialog.show()

    # Выход из окна пациента в окно записи на приём
    def exit_reception(self):
        self.hide()
        dialog = panel_receprion(parent=self)
        dialog.show()

    # Выйти в окно выгрузки
    def exit_disc(self):
        self.hide()
        dialog = pat_disc_panel(parent=self)
        dialog.show()