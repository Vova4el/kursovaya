from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from personal_med_kniga_QT import Med_knigaUi
import classes
import personnel_window
import log_window
from classes import *
from backup_bd import *

#Окно_ДЛЯ_работы с мед книжкой
class panel_med_kniga(QMainWindow):
    def __init__(self, parent=None):
        super(panel_med_kniga, self).__init__(parent)
        self.ui = Med_knigaUi()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(lambda: self.change_table())
        self.ui.pushButton_3.clicked.connect(lambda: self.confirm_change())
        self.ui.pushButton_4.clicked.connect(lambda: self.undo_change())
        self.ui.action.triggered.connect(lambda: self.exit_aut())
        self.ui.action_2.triggered.connect(lambda: self.exit_personnel())
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
        self.ui.comboBox_2.clear()
        self.ui.comboBox_3.clear()
        self.ui.tableWidget.clearSelection()
        table = med_knigа
        self.ui.tableWidget.setColumnCount(4)
        collums = ['id', 'id_patient', 'id_personnel', 'id_spec', 'diagnoz']
        self.ui.tableWidget.setHorizontalHeaderLabels(["ФИО пациента", "ФИО персонала", 'Специализация', "Диагноз"])
        line = session.query(table).count()
        self.ui.qTable = session.query(table).all()
        self.ui.tableWidget.setRowCount(line)
        sort = [0] * line
        j = 0
        p = session.query(patient).all()
        for i in range(session.query(patient).count()):
                self.ui.comboBox_2.addItem(str(p[i].name))
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

    def change_table(self):
        self.ui.statusbar.clearMessage()
        if self.ui.prov == 0:
            self.ui.prov = 1
        change = self.ui.comboBox_4.currentText()
        stlb = int(self.ui.comboBox_3.currentText())
        p = session.query(patient).all()
        p_id=p[self.ui.comboBox_2.currentIndex()].id #индекс пациента
        text = self.ui.textEdit.toPlainText()
        try:
            if change == "Добавить строку":
                line = session.query(med_knigа).count()
                tabl = session.query(med_knigа).all()
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
                new = med_knigа(id=free_id, id_patient=p_id, id_personnel=classes.glob_id,
                                id_spec=(session.query(personnel).filter_by(id=classes.glob_id).first()).id_spec, diagnoz=text)
                session.add(new)
            if change == "Обновить элемент":
                query = session.query(med_knigа).get(stlb)
                if (session.query(personnel).filter_by(id=classes.glob_id).first()).id_spec == query.id_spec:
                    query.id_personnel = classes.glob_id
                    query.diagnoz = text
                    query.id_spec = (session.query(personnel).filter_by(id=classes.glob_id).first()).id_spec
                else:
                    self.ui.statusbar.showMessage("Вы должны быть той же специальности, что и врач, написавший этот диагноз")
            if change == "Удалить строку":
                query = session.query(med_knigа).get(stlb)
                if (session.query(personnel).filter_by(id=classes.glob_id).first()).id_spec == query.id_spec:
                    session.query(med_knigа).filter_by(id=stlb).delete(synchronize_session=False)
                else:
                    self.ui.statusbar.showMessage("Вы должны быть той же специальности, что и врач, написавший этот диагноз")
            self.write_table()

        except:
            self.ui.statusbar.showMessage("Произошла ошибка")

    # Выход из окна персонала обратно в окно авторизации
    def exit_aut(self):
        print(23)
        self.hide()
        dialog = log_window.log_panel(parent=self)
        dialog.show()

    # Выход из окна персонала обратно в окно авторизации
    def exit_personnel(self):
        print(1)
        self.hide()
        dialog = personnel_window.personal_panel(parent=self)
        dialog.show()

    def confirm_change(self):
        if self.ui.prov != 0:
            session.commit()
            DumpPostgreSql()
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