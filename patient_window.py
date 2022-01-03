from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem
import classes
from patientQT import patientUI
from datetime import timedelta, datetime, time
from backup_bd import *

#ОКНО_ПАЦИЕНТА
class patient_panel(QMainWindow):
    def __init__(self, parent=None):
        super(patient_panel, self).__init__(parent)
        self.ui = patientUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.write_table())
        self.ui.pushButton_2.clicked.connect(lambda: self.change_table())
        self.ui.pushButton_3.clicked.connect(lambda: self.confirm_change())
        self.ui.pushButton_4.clicked.connect(lambda: self.undo_change())
        self.ui.pushButton_5.clicked.connect(lambda: self.autoplay_spec())

    def write_table(self):
        self.ui.comboBox_3.clear()
        self.ui.comboBox_5.clear()
        self.ui.tableWidget.clearSelection()
        result = self.ui.comboBox.currentText()
        collums = []
        if result == "Пациенты":
            table = patient
            self.ui.tableWidget.setColumnCount(3)
            collums = ['id', 'name', 'id_acc']
            self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "ФИО", "ID аккаунта"])
        if result == "День":
            table = day
            self.ui.tableWidget.setColumnCount(2)
            collums = ['id', 'name']
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["ID", "День"])
        if result == "Специализация":
            table = specialization
            self.ui.tableWidget.setColumnCount(2)
            collums = ['id', 'name_spec']
            self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Специализация"])
        if result == "Статус приёма":
            table = reception_status
            self.ui.tableWidget.setColumnCount(2)
            collums = ['id', 'name']
            self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Статус"])
        if result == "Кабинеты":
            table = offices
            self.ui.tableWidget.setColumnCount(2)
            collums = ['id', 'cab_num']
            self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Номер кабинета"])
        if result == "Персонал":
            table = personnel
            self.ui.tableWidget.setColumnCount(5)
            collums = ['id', 'id_spec', 'id_office', 'name', 'id_acc']
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["ID", "ID специализации", "ID кабинета", "ФИО", 'ID аккаунта'])
        if result == "Время работы":
            table = working_hours
            self.ui.tableWidget.setColumnCount(6)
            collums = ['id', 'id_day', 'id_spec', 'work_hours', 'free_time', 'break_time']
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["ID", "ID дня", "ID специализации", "рабочее время", "свободное время", "перерыв"])
        if result == "Приём":
            table = reception
            self.ui.tableWidget.setColumnCount(7)
            collums = ['id', 'id_patient', 'id_office', 'id_reception_status', 'id_personnel', 'id_spec', 'date']
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["ID", "ID пациента", "ID кабинета", "ID статуса приёма", "ID персонала", "id специализации", "Дата"])
        if result == "Мед книжка":
            table = med_knigа
            self.ui.tableWidget.setColumnCount(4)
            collums = ['id', 'id_patient', 'id_personnel', 'diagnoz']
            self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "ID пациента", "ID персонала", "Диагноз"])
        line = session.query(table).count()
        self.ui.qTable = session.query(table).all()
        self.ui.tableWidget.setRowCount(line)
        sort = [0] * line
        j = 0
        p = session.query(specialization).all()
        for i in range(session.query(specialization).count()):
            self.ui.comboBox_5.addItem(str(p[i].id))
        for i in range(line):
            self.ui.comboBox_3.addItem(str(i + 1))
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
        self.ui.comboBox_3.clear()
        sort.sort()
        for i in sort:
            self.ui.comboBox_3.addItem(str(i))
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
                            if ((c == 'id') & (v == i)) | ((c != 'id') & (perem == i)):
                                self.ui.tableWidget.setItem(j, col, QTableWidgetItem(str(v)))
                                col += 1
        self.ui.tableWidget.resizeColumnsToContents()

    def change_table(self):
        self.ui.statusbar.clearMessage()
        if self.ui.prov == 0:
            self.ui.prov = 1
        change = self.ui.comboBox_4.currentText()
        stlb = int(self.ui.comboBox_3.currentText())
        text = self.ui.textEdit.toPlainText()
        lis = text.split(',')
        if change == "Добавить строку":
            line = session.query(reception).count()
            tabl = session.query(reception).all()
            f = 0  # флаг
            free_id = 1  # свободный индекс
            while f == 0:
                for i in range(line):
                    if free_id == tabl[i].id:
                        f = 1
                if f == 1:
                    free_id = free_id + 1
                    f = 0
                else:
                    f = 1
            pers = session.query(personnel).filter(personnel.id == int(lis[0])).first()
            new = reception(id=free_id, id_patient=classes.glob_id, id_office=pers.id_office, id_reception_status=2, id_personnel=int(lis[0]), id_spec=pers.id_spec, date=lis[1])
            session.add(new)
        if change == "Отменить запись на приём":
            query = session.query(reception).get(stlb)
            if classes.glob_id == query.id_patient:
                query.id_reception_status = 3
            else:
                self.ui.statusbar.showMessage("Вы не можете отменить чужую запись на приём")
        self.write_table()

    def autoplay_spec(self):
        if self.ui.prov == 0:
            self.ui.prov = 1
        spec_id = int(self.ui.comboBox_5.currentText())
        dt = datetime.now()
        t2 = time(0)
        dt = datetime.combine(dt.date(), t2)
        while datetime.now() >= dt:
            dt = dt + timedelta(hours=1)
        tabl = session.query(reception).filter(reception.id_spec == spec_id).all()
        line = session.query(reception).filter(reception.id_spec == spec_id).count()
        f = 0
        while f == 0:
            f2 = 0
            while f2 == 0:
                for i in range(line):
                    if dt == datetime.strptime(tabl[i].date, '%Y-%m-%d %H:%M:%S'):
                        f2 = 1
                if f2 == 1:
                    f2 = 0
                    dt = dt + timedelta(hours=1)
                else:
                    f2 = 1
            wh = session.query(working_hours).filter(working_hours.id_spec == spec_id, working_hours.id_day == datetime.isoweekday(dt))
            line_wh = session.query(working_hours).filter(working_hours.id_spec == spec_id, working_hours.id_day == datetime.isoweekday(dt)).count()
            if line_wh != 0:
                for j in range(line_wh):
                    wh2 = datetime.strptime(wh[j].work_hours[1], '%H:%M:%S')
                    wh1 = datetime.strptime(wh[j].work_hours[0], '%H:%M:%S')
                    bt1 = datetime.strptime(wh[j].break_time[0], '%H:%M:%S')
                    bt2 = datetime.strptime(wh[j].break_time[1], '%H:%M:%S')
                    if (wh1.time() <= dt.time()) & (wh2.time() >= dt.time()) & ((bt1.time() > dt.time()) | (bt2.time() < dt.time())):
                        tabl2 = session.query(personnel).filter(personnel.id_spec == spec_id)
                        line2 = session.query(personnel).filter(personnel.id_spec == spec_id).count()
                        for k in range(line2):
                            line_l2 = session.query(reception).filter(reception.id_personnel == tabl2[k].id).count()
                            if line_l2 != 0:
                                l1 = session.query(reception).filter(reception.id_personnel == tabl2[k].id).first()
                                l2 = session.query(reception).filter(reception.id_office == l1.id_office, datetime.strptime(l1.date, '%Y-%m-%d %H:%M:%S') == dt).count()
                                if l2 == 0:
                                    res = dt
                                    d_per = tabl2[k].id
                                    n_c = tabl2[k].id_office
                                    f = 1
                            else:
                                l1 = session.query(reception).filter(reception.id_office == tabl2[k].id_office).first()
                                l2 = session.query(reception).filter(reception.id_office == l1.id_office, datetime.strptime(l1.date, '%Y-%m-%d %H:%M:%S') == dt).count()
                                if l2 == 0:
                                    res = dt
                                    d_per = tabl2[k].id
                                    n_c = tabl2[k].id_office
                                    f = 1
            dt = dt + timedelta(hours=1)
        tabl = session.query(reception).all()
        line = session.query(reception).count()
        f = 0  # флаг
        free_id = 1  # свободный индекс
        while f == 0:
            for i in range(line):
                if free_id == tabl[i].id:
                    f = 1
            if f == 1:
                free_id = free_id + 1
                f = 0
            else:
                f = 1
        new = reception(id=free_id, id_patient=classes.glob_id, id_office=n_c, id_reception_status=1, id_personnel=d_per, id_spec=spec_id, date=str(res))
        session.add(new)
        self.write_table()

    def confirm_change(self):
        if self.ui.prov != 0:
            session.commit()
            dump_sqlalchemy()
            self.ui.prov = 0
            self.write_table()
        else:
            self.ui.statusbar.showMessage("Сначала внесите изменение в таблицу")

    def undo_change(self):
        if self.ui.prov != 0:
            session.rollback()
            self.ui.prov = 0
            self.write_table()
        else:
            self.ui.statusbar.showMessage("Сначала внесите изменение в таблицу")