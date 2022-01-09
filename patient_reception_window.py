from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from patient_receptionQT import receprionUI
import classes
import patient_window
import log_window
from datetime import timedelta, datetime, time
from backup_bd import *

#Окно_ДЛЯ_работы с расписанием на приём
class panel_receprion(QMainWindow):
    def __init__(self, parent=None):
        super(panel_receprion, self).__init__(parent)
        self.ui = receprionUI()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(lambda: self.Record())
        self.ui.pushButton_3.clicked.connect(lambda: self.confirm_change())
        self.ui.pushButton_4.clicked.connect(lambda: self.undo_change())
        self.ui.action.triggered.connect(lambda: self.exit_aut())
        self.ui.action_2.triggered.connect(lambda: self.exit_patient())
        p = session.query(personnel).all()
        for i in range(session.query(personnel).count()):
                self.ui.comboBox_2.addItem(str(p[i].name))
        s = session.query(specialization).all()
        for i in range(session.query(specialization).count()):
            self.ui.comboBox_5.addItem(str(s[i].name_spec))
        self.write_table()

    # вывод по внешнему ключу
    def output_by_foreign_key(self, k, v, col, j):
        if k == 'id_stat':
            q = session.query(user_status).filter_by(id=int(v)).first()
            self.ui.tableWidget.setItem(j, col, QTableWidgetItem(str(q.status)))
        elif k == 'id_day':
            q = session.query(day).filter_by(id=int(v)).first()
            self.ui.tableWidget.setItem(j, col, QTableWidgetItem(str(q.name)))
        elif k == 'id_spec':
            q = session.query(specialization).filter_by(id=int(v)).first()
            self.ui.tableWidget.setItem(j, col, QTableWidgetItem(str(q.name_spec)))
        elif k == 'id_patient':
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
        self.ui.comboBox_3.clear()
        self.ui.tableWidget.clearSelection()
        table = reception
        self.ui.tableWidget.setColumnCount(6)
        collums = ['id', 'id_patient', 'id_office', 'id_reception_status', 'id_personnel', 'id_spec', 'date']
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ["ФИО пациента", "№ кабинета", "Статуса приёма", "ФИО персонала", "Специализация персонала", "Дата"])
        line = session.query(table).count()
        self.ui.qTable = session.query(table).all()
        self.ui.tableWidget.setRowCount(line)
        sort = [0] * line
        j = 0
        for i in range(line):
            self.ui.comboBox_3.addItem(str(i + 1))
        for i in session.query(table).all():
            sort[j] = i.id
            j += 1
        perem = 0
        j = -1
        sort.sort()
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
                                self.output_by_foreign_key(k, v, col, j)
                                col += 1
        self.ui.tableWidget.resizeColumnsToContents()

    def Record(self):
        self.ui.statusbar.clearMessage()
        if self.ui.prov == 0:
            self.ui.prov = 1
        if self.ui.comboBox_4.currentText() == "Записаться на приём":
            if self.ui.comboBox_6.currentText() == "Запись по специалисту":
                dat = datetime.strptime(self.ui.textEdit.toPlainText(), '%Y-%m-%d %H:%M:%S')
                s = session.query(specialization).all()
                spec_id = s[self.ui.comboBox_5.currentIndex()].id  # индекс специализации
                wh = session.query(working_hours).filter_by(id_spec=spec_id, id_day=datetime.isoweekday(dat)).first()
                line_wh = session.query(working_hours).filter_by(id_spec=spec_id, id_day=datetime.isoweekday(dat)).count()
                if line_wh != 0:
                    wh1 = datetime.strptime(wh.work_hours[0], '%H:%M:%S')
                    wh2 = datetime.strptime(wh.work_hours[1], '%H:%M:%S')
                    bt1 = datetime.strptime(wh.break_time[0], '%H:%M:%S')
                    bt2 = datetime.strptime(wh.break_time[1], '%H:%M:%S')
                    f = 0
                    for i in session.query(personnel).filter_by(id_spec=spec_id):
                        if f == 0:
                            if session.query(reception).filter_by(id_personnel=i.id, date=str(dat)).count() == 0:
                                if session.query(reception).filter_by(date=str(dat), id_office=i.id_office).count() == 0:
                                    if session.query(reception).filter_by(id_patient=classes.glob_id, date=str(dat)).count() == 0:
                                        free_id = 1  # свободный индекс
                                        line = session.query(reception).count()
                                        tabl = session.query(reception).all()
                                        while f == 0:
                                            for j in range(line):
                                                if free_id == tabl[j].id:
                                                    f = 1
                                            if f == 1:
                                                free_id = free_id + 1
                                                f = 0
                                            else:
                                                f = 1
                                        new = reception(id=free_id, id_patient=classes.glob_id, id_office=i.id_office, id_reception_status=2, id_personnel=i.id, id_spec=i.id_spec, date=str(dat))
                    if f == 0:
                        self.ui.statusbar.showMessage("Нет возможности записаться на эту дату")
                        return
                    session.add(new)
                else:
                    self.ui.statusbar.showMessage("Нет возможности записаться на эту дату")
                    return
            elif self.ui.comboBox_6.currentText() == "Запись по персоналу":
                dat = datetime.strptime(self.ui.textEdit.toPlainText(), '%Y-%m-%d %H:%M:%S')
                p = session.query(personnel).filter_by(id=self.ui.comboBox_2.currentIndex()+1).first()
                wh = session.query(working_hours).filter_by(id_spec=p.id_spec, id_day=datetime.isoweekday(dat)).first()
                line_wh = session.query(working_hours).filter_by(id_spec=p.id_spec, id_day=datetime.isoweekday(dat)).count()
                if line_wh != 0:
                    wh1 = datetime.strptime(wh.work_hours[0], '%H:%M:%S')
                    wh2 = datetime.strptime(wh.work_hours[1], '%H:%M:%S')
                    bt1 = datetime.strptime(wh.break_time[0], '%H:%M:%S')
                    bt2 = datetime.strptime(wh.break_time[1], '%H:%M:%S')
                    if (wh1.time() <= dat.time()) and (wh2.time() >= dat.time()) and ((bt1.time() > dat.time()) or (bt2.time() < dat.time())):
                        if (session.query(reception).filter_by(id_personnel=p.id, date=str(dat)).count() == 0):
                            if session.query(reception).filter_by(date=str(dat), id_office=p.id_office).count() == 0:
                                if session.query(reception).filter_by(id_patient=classes.glob_id, date=str(dat)).count() == 0:
                                    f = 0
                                    free_id = 1  # свободный индекс
                                    line = session.query(reception).count()
                                    tabl = session.query(reception).all()
                                    while f == 0:
                                        for i in range(line):
                                            if free_id == tabl[i].id:
                                                f = 1
                                        if f == 1:
                                            free_id = free_id + 1
                                            f = 0
                                        else:
                                            f = 1
                                    new = reception(id=free_id, id_patient=classes.glob_id, id_office=p.id_office, id_reception_status=2, id_personnel=p.id, id_spec=p.id_spec, date=str(dat))
                                    session.add(new)
                                else:
                                    self.ui.statusbar.showMessage("Нет возможности записаться на эту дату")
                                    return
                            else:
                                self.ui.statusbar.showMessage("Нет возможности записаться на эту дату")
                                return
                        else:
                            self.ui.statusbar.showMessage("Нет возможности записаться на эту дату")
                            return
                    else:
                        self.ui.statusbar.showMessage("Нет возможности записаться на эту дату")
                        return
                else:
                    self.ui.statusbar.showMessage("Нет возможности записаться на эту дату")
                    return
            else:
                self.autoplay_spec()
        if self.ui.comboBox_4.currentText() == "Отменить запись на приём":
            query = session.query(reception).get(int(self.ui.comboBox_3.currentText()))
            if session.query(patient).filter_by(id=classes.glob_id).first() == query.id_patient:
                session.query(reception).filter_by(id=int(self.ui.comboBox_3.currentText())).delete(synchronize_session=False)
            else:
                self.ui.statusbar.showMessage("Вы не можете отменить чужую запись на приём")
        self.write_table()

    def autoplay_spec(self):
        if self.ui.prov == 0:
            self.ui.prov = 1
        if self.ui.comboBox_6.currentText() == "Автозапись по специалисту":
            s = session.query(specialization).all()
            spec_id = s[self.ui.comboBox_5.currentIndex()].id  # индекс специализации
            dt = datetime.now()
            t2 = time(0)
            dt = datetime.combine(dt.date(), t2)
            while datetime.now() >= dt:
                dt = dt + timedelta(hours=1)
            tabl = session.query(reception).filter_by(id_spec=spec_id).all()
            line = session.query(reception).filter_by(id_spec=spec_id).count()
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
                wh = session.query(working_hours).filter_by(id_spec=spec_id, id_day=datetime.isoweekday(dt))
                line_wh = session.query(working_hours).filter_by(id_spec=spec_id, id_day=datetime.isoweekday(dt)).count()
                if line_wh != 0:
                    for j in range(line_wh):
                        wh1 = datetime.strptime(wh[j].work_hours[0], '%H:%M:%S')
                        wh2 = datetime.strptime(wh[j].work_hours[1], '%H:%M:%S')
                        bt1 = datetime.strptime(wh[j].break_time[0], '%H:%M:%S')
                        bt2 = datetime.strptime(wh[j].break_time[1], '%H:%M:%S')
                        if (wh1.time() <= dt.time()) and (wh2.time() >= dt.time()) and ((bt1.time() > dt.time()) or (bt2.time() < dt.time())):
                            tabl2 = session.query(personnel).filter_by(id_spec=spec_id)
                            line2 = session.query(personnel).filter_by(id_spec=spec_id).count()
                            for k in range(line2):
                                line_l2 = session.query(reception).filter_by(id_personnel=tabl2[k].id).count()
                                if line_l2 != 0:
                                    l1 = session.query(reception).filter_by(id_personnel=tabl2[k].id).first()
                                    l2 = session.query(reception).filter_by(id_office=l1.id_office, date=str(dt)).count()
                                    if l2 == 0:
                                        res = dt
                                        d_per = tabl2[k].id
                                        n_c = tabl2[k].id_office
                                        f = 1
                                else:
                                    l1 = session.query(reception).filter_by(id_office=tabl2[k].id_office).first()
                                    l2 = session.query(reception).filter_by(id_office=l1.id_office, date=str(dt)).count()
                                    if l2 == 0:
                                        res = dt
                                        d_per = tabl2[k].id
                                        n_c = tabl2[k].id_office
                                        f = 1
                dt = dt + timedelta(hours=1)
        else:
            p = session.query(personnel).all()
            p_id = p[self.ui.comboBox_2.currentIndex()].id  # индекс персонала
            spec_id = p[self.ui.comboBox_2.currentIndex()].id_spec  # индекс специализации персонала
            dt = datetime.now()
            t2 = time(0)
            dt = datetime.combine(dt.date(), t2)
            while datetime.now() >= dt:
                dt = dt + timedelta(hours=1)
            tabl = session.query(reception).filter_by(id_personnel=p_id).all()
            line = session.query(reception).filter_by(id_personnel=p_id).count()
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
                wh = session.query(working_hours).filter_by(id_spec=spec_id, id_day=datetime.isoweekday(dt))
                line_wh = session.query(working_hours).filter_by(id_spec=spec_id, id_day=datetime.isoweekday(dt)).count()
                if line_wh != 0:
                    for j in range(line_wh):
                        wh1 = datetime.strptime(wh[j].work_hours[0], '%H:%M:%S')
                        wh2 = datetime.strptime(wh[j].work_hours[1], '%H:%M:%S')
                        bt1 = datetime.strptime(wh[j].break_time[0], '%H:%M:%S')
                        bt2 = datetime.strptime(wh[j].break_time[1], '%H:%M:%S')
                        if (wh1.time() <= dt.time()) and (wh2.time() >= dt.time()) and ((bt1.time() > dt.time()) or (bt2.time() < dt.time())):
                            line_l2 = session.query(reception).filter_by(id_personnel=p_id).count()
                            if line_l2 != 0:
                                l1 = session.query(reception).filter_by(id_personnel=p_id).first()
                                l2 = session.query(reception).filter_by(id_office=l1.id_office, date=str(dt)).count()
                                if l2 == 0:
                                    res = dt
                                    d_per = p_id
                                    n_c = p[self.ui.comboBox_2.currentIndex()].id_office
                                    f = 1
                            else:
                                l1 = session.query(reception).filter_by(id_office=p[self.ui.comboBox_2.currentIndex()].id_office).first()
                                l2 = session.query(reception).filter_by(id_office=l1.id_office, date=str(dt)).count()
                                if l2 == 0:
                                    res = dt
                                    d_per = p_id
                                    n_c = p[self.ui.comboBox_2.currentIndex()].id_office
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
        new = reception(id=free_id, id_patient=classes.glob_id, id_office=n_c, id_reception_status=2,
                        id_personnel=d_per, id_spec=spec_id, date=str(res))
        session.add(new)

    # Выход из окна персонала обратно в окно авторизации
    def exit_aut(self):
        self.hide()
        dialog = log_window.log_panel(parent=self)
        dialog.show()

    # Выход из окна персонала обратно в окно авторизации
    def exit_patient(self):
        self.hide()
        dialog = patient_window.patient_panel(parent=self)
        dialog.show()

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