from Qt import *
from Authentication import login_panell
import classes
from personalQT import personalUI
from patientQT import patientUI
from datetime import timedelta,datetime, date, time

################ОКНО_АДМИНА##########################
class admin_panel(QMainWindow):
    def __init__(self, parent=None):
        super(admin_panel, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.write_table())
        self.ui.pushButton_2.clicked.connect(lambda: self.change_table())
        self.ui.pushButton_3.clicked.connect(lambda: self.confirm_change())
        self.ui.pushButton_4.clicked.connect(lambda: self.undo_change())

    def write_table(self):
        self.ui.comboBox_2.clear()
        self.ui.comboBox_3.clear()
        self.ui.tableWidget.clearSelection()
        result = self.ui.comboBox.currentText()
        line = 0
        collums = []
        if result == "Аккаунты":
            table = accounts
            self.ui.tableWidget.setColumnCount(4)
            collums = ['id', 'login', 'password', 'id_stat']
            self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Логин", "Пароль", "ID статуса"])
        if result == "Статусы пользователей":
            table = user_status
            self.ui.tableWidget.setColumnCount(2)
            collums = ['id', 'status']
            self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Cтатус"])
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
                ["ID", "ID пациента", "ID кабинета", "ID статуса приёма", "ID персонала", "ID специализации", "Дата"])
        if result == "Мед книжка":
            table = med_knigа
            self.ui.tableWidget.setColumnCount(4)
            collums = ['id', 'id_patient','id_personnel', 'diagnoz']
            self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "ID пациента", "ID персонала", "Диагноз"])
        line = session.query(table).count()
        self.ui.qTable = session.query(table).all()
        self.ui.tableWidget.setRowCount(line)
        sort = [0] * line
        j = 0
        for i in collums:
            if i != 'id':
                self.ui.comboBox_2.addItem(i)
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
        result = self.ui.comboBox.currentText()
        change = self.ui.comboBox_4.currentText()
        colona = self.ui.comboBox_2.currentText()
        stlb = int(self.ui.comboBox_3.currentText())
        text = self.ui.textEdit.toPlainText()
        lis = text.split(',')
        table = patient
        try:
            if result == "Аккаунты":
                table = accounts
                if change == "Обновить элемент":
                    query = session.query(table).get(stlb)
                    if colona == "login":
                        query.login = text
                    if colona == "password":
                        query.password = text
                    if colona == "id_stat":
                        query.id_stat = int(text)
                if change == "Добавить строку":
                    line = session.query(table).count()
                    tabl = session.query(table).all()
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
                    new = table(id=free_id, login=lis[0], password=lis[1], id_stat=int(lis[2]))
                    session.add(new)
            if result == "Статусы пользователей":
                table = user_status
                if change == "Обновить элемент":
                    query = session.query(table).get(stlb)
                    if colona == "status":
                        query.status = text
                if change == "Добавить строку":
                    line = session.query(table).count()
                    tabl = session.query(table).all()
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
                    new = table(id=free_id, status=text)
                    session.add(new)
            if result == "Пациенты":
                table = patient
                if change == "Обновить элемент":
                    query = session.query(table).get(stlb)
                    if colona == "name":
                        query.name = text
                    if colona == "id_acc":
                        query.id_acc = int(text)
                if change == "Добавить строку":
                    line = session.query(table).count()
                    tabl = session.query(table).all()
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
                    new = table(id=free_id, name=lis[0],id_acc = int(lis[1]))
                    session.add(new)
            if result == "День":
                table = day
                if change == "Обновить элемент":
                    query = session.query(table).get(stlb)
                    if colona == "name":
                        query.name = text
                if change == "Добавить строку":
                    line = session.query(table).count()
                    tabl = session.query(table).all()
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
                    new = table(id=free_id, name=text)
                    session.add(new)
            if result == "Специализация":
                table = specialization
                if change == "Обновить элемент":
                    query = session.query(table).get(stlb)
                    if colona == "name_spec":
                        query.name_spec = text
                if change == "Добавить строку":
                    line = session.query(table).count()
                    tabl = session.query(table).all()
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
                    new = table(id=free_id, name_spec=text)
                    session.add(new)
            if result == "Статус приёма":
                table = reception_status
                if change == "Обновить элемент":
                    query = session.query(table).get(stlb)
                    if colona == "name":
                        query.name = text
                if change == "Добавить строку":
                    line = session.query(table).count()
                    tabl = session.query(table).all()
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
                    new = table(id=free_id, name=text)
                    session.add(new)
            if result == "Кабинеты":
                table = offices
                if change == "Обновить элемент":
                    query = session.query(table).get(stlb)
                    if colona == "cab_num":
                        query.cab_num = int(text)
                if change == "Добавить строку":
                    line = session.query(table).count()
                    tabl = session.query(table).all()
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
                    new = table(id=free_id, cab_num=int(text))
                    session.add(new)
            if result == "Персонал":
                table = personnel
                if change == "Обновить элемент":
                    query = session.query(table).get(stlb)
                    if colona == "id_spec":
                        query.id_spec = int(text)
                    if colona == "id_office":
                        query.id_office = int(text)
                    if colona == "name":
                        query.name = text
                    if colona == "id_acc":
                        query.id_acc = int(text)
                if change == "Добавить строку":
                    line = session.query(table).count()
                    tabl = session.query(table).all()
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
                    new = table(id=free_id, id_spec=int(lis[0]), id_office=int(lis[1]), name= lis[2], id_acc=int(lis[3]))
                    session.add(new)
            if result == "Время работы":
                table = working_hours
                if change == "Обновить элемент":
                    query = session.query(table).get(stlb)
                    if colona == "id_day":
                        query.id_day = int(text)
                    if colona == "work_hours":
                        query.work_hours= [lis[0],lis[1]]
                    if colona == "free_time":
                        query.free_time = [lis[0],lis[1]]
                    if colona == "break_time":
                        query.break_time = [lis[0],lis[1]]
                if change == "Добавить строку":
                    line = session.query(table).count()
                    tabl = session.query(table).all()
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
                    new = table(id=free_id, id_day=int(lis[0]), id_spec=int(lis[1]), work_hours= [lis[2],lis[3]], free_time=[lis[4],lis[5]], break_time=[lis[6],lis[7]])
                    session.add(new)
            if result == "Приём":
                table = reception
                if change == "Обновить элемент":
                    query = session.query(table).get(stlb)
                    if colona == "id_patient":
                        query.id_patient = int(text)
                    if colona == "id_office":
                        query.id_office= int(text)
                    if colona == "id_reception_status":
                        query.id_reception_status = int(text)
                    if colona == "id_personnel":
                        query.id_personnel = int(text)
                    if colona == "id_spec":
                        query.id_spec = int(text)
                    if colona == "date":
                        query.date = text
                if change == "Добавить строку":
                    line = session.query(table).count()
                    tabl = session.query(table).all()
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
                    new = table(id=free_id, id_patient=int(lis[0]), id_office=int(lis[1]), id_reception_status= int(lis[2]), id_personnel=int(lis[3]), id_spec=int(lis[4]), date=lis[5]) #1,2,2,1,1,2006-12-14 20:15:00
                    session.add(new)
            if result == "Мед книжка":
                table = med_knigа
                if change == "Обновить элемент":
                    query = session.query(table).get(stlb)
                    if colona == "id_patient":
                        query.id_patient = int(text)
                    if colona == "id_personnel":
                        query.id_personnel= int(text)
                    if colona == "diagnoz":
                        query.diagnoz = text
                if change == "Добавить строку":
                    line = session.query(table).count()
                    tabl = session.query(table).all()
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
                    new = table(id=free_id, id_patient=int(lis[0]), id_personnel=int(lis[1]), diagnoz=lis[2])#id,id_patient, id_personnel, diagnoz
                    session.add(new)
            if change == "Удалить строку":
                session.query(table).filter_by(id=stlb).delete(synchronize_session=False)
            self.write_table()

        except:
            self.ui.statusbar.showMessage("Произошла ошибка")

    def confirm_change(self):
        if self.ui.prov != 0:
            session.commit()
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

#########################ПАНЕЛЬ_ДЛЯ_ПЕРСОНАЛА##########################################
class personal_panel(QMainWindow):
    def __init__(self, parent=None):
        super(personal_panel, self).__init__(parent)
        self.ui = personalUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.write_table())
        self.ui.pushButton_2.clicked.connect(lambda: self.change_table())
        self.ui.pushButton_3.clicked.connect(lambda: self.confirm_change())
        self.ui.pushButton_4.clicked.connect(lambda: self.undo_change())

    def write_table(self):
        self.ui.comboBox_2.clear()
        self.ui.comboBox_3.clear()
        self.ui.tableWidget.clearSelection()
        result = self.ui.comboBox.currentText()
        line = 0
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
        p = session.query(patient).all()
        for i in range(session.query(patient).count()):
                self.ui.comboBox_2.addItem(str(p[i].id))
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
        p_id = self.ui.comboBox_2.currentText()
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
                new = med_knigа(id=free_id, id_patient=p_id,id_personnel=classes.glob_id,diagnoz=text)
                session.add(new)
            if change == "Обновить элемент":
                query = session.query(med_knigа).get(stlb)
                if classes.glob_id == query.id_personnel:
                    query.diagnoz = text
                else:
                    self.ui.statusbar.showMessage("Вы должны быть той же специальности, что и врач, написавший этот диагноз")
            if change == "Удалить строку":
                query = session.query(med_knigа).get(stlb)
                if classes.glob_id == query.id_personnel:
                    session.query(med_knigа).filter_by(id=stlb).delete(synchronize_session=False)
                else:
                    self.ui.statusbar.showMessage("Вы должны быть той же специальности, что и врач, написавший этот диагноз")
            self.write_table()

        except:
            self.ui.statusbar.showMessage("Произошла ошибка")

    def confirm_change(self):
        if self.ui.prov != 0:
            session.commit()
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



#################################ОКНО_ПАЦИЕНТА######################################
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
        line = 0
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
        dt= datetime.combine(dt.date(),t2)
        while datetime.now()>=dt:
            dt = dt + timedelta(hours=1)
        tabl = session.query(reception).filter(reception.id_spec== spec_id).all()
        line = session.query(reception).filter(reception.id_spec== spec_id).count()
        f=0
        id_per = 0
        while f==0:
            f2=0
            while f2==0:
                for i in range(line):
                    if dt==datetime.strptime(tabl[i].date,'%Y-%m-%d %H:%M:%S'):
                        f2=1
                if f2==1:
                    f2=0
                    dt = dt + timedelta(hours=1)
                else:
                    f2=1
            wh = session.query(working_hours).filter(working_hours.id_spec == spec_id,working_hours.id_day==datetime.isoweekday(dt))
            line_wh = session.query(working_hours).filter(working_hours.id_spec == spec_id,working_hours.id_day==datetime.isoweekday(dt)).count()
            if line_wh!=0:
                for j in range(line_wh):
                    wh2=datetime.strptime(wh[j].work_hours[1],'%H:%M:%S')
                    wh1=datetime.strptime(wh[j].work_hours[0],'%H:%M:%S')
                    bt1 = datetime.strptime(wh[j].break_time[0], '%H:%M:%S')
                    bt2 = datetime.strptime(wh[j].break_time[1], '%H:%M:%S')
                    if (wh1.time()<=dt.time())&(wh2.time()>=dt.time())&((bt1.time()>dt.time())|(bt2.time()<dt.time())):
                        tabl2 =session.query(personnel).filter(personnel.id_spec == spec_id)
                        line2 = session.query(personnel).filter(personnel.id_spec == spec_id).count()
                        for k in range(line2):
                            l1 = session.query(reception).filter(reception.id_personnel==tabl2[k].id).first()
                            l2 = session.query(reception).filter(reception.id_office==l1.id_office,datetime.strptime(l1.date,'%Y-%m-%d %H:%M:%S')==dt).count()
                            if l2 == 0:
                                res =dt
                                d_per = tabl2[k].id
                                n_c = tabl2[k].id_office
                                f=1
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
            self.ui.prov = 0
            self.write_table()
        else:
            self.ui.statusbar.showMessage("Сначала внесите изменение в таблицу")

    def confirm_change(self):
        if self.ui.prov != 0:
            session.commit()
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



class log_panel(QMainWindow):
    def __init__(self, parent=None):
        super(log_panel, self).__init__(parent)
        self.ui = login_panell()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.inter_to_app())
        self.ui.pushButton_2.clicked.connect(lambda: self.create_acc())

    def inter_to_app(self):
        log = self.ui.textEdit.toPlainText()
        pasw = self.ui.textEdit_2.toPlainText()
        if log == "":
            self.ui.statusbar.showMessage("Введите логин")
            return
        if pasw == "":
            self.ui.statusbar.showMessage("Введите пароль")
            return
        for i in session.query(accounts).all():
            if log == i.login:
                if pasw == i.password:
                    self.hide()
                    if i.id_stat == 1:
                        dialog = admin_panel(parent=self)
                        dialog.show()
                    if i.id_stat == 2:
                        j = session.query(accounts).filter(accounts.login== log).first()
                        p = session.query(patient).filter(patient.id_acc== j.id).first()
                        classes.glob_id= p.id
                        dialog = patient_panel(parent=self)
                        dialog.show()
                    if i.id_stat == 3:
                        j = session.query(accounts).filter(accounts.login== log).first()

                        p = session.query(personnel).filter(personnel.id_acc== j.id).first()
                        classes.glob_id= p.id
                        dialog = personal_panel(parent=self)
                        dialog.show()
                else:
                    self.ui.statusbar.showMessage("Введён неверный пароль")
                    return
            self.ui.statusbar.showMessage("Введено несуществующее имя пользователя")

    def create_acc(self):
        log = self.ui.textEdit.toPlainText()
        pasw = self.ui.textEdit_2.toPlainText()
        if log == "":
            self.ui.statusbar.showMessage("Введите логин для нового пользователя")
            return
        if pasw == "":
            self.ui.statusbar.showMessage("Введите пароль для нового пользователя")
            return
        for i in session.query(accounts).all():
            if log == i.login:
                self.ui.statusbar.showMessage("Пользователь с таким логином уже существует")
                return
        n_id = int(self.ui.comboBox.currentText())
        line = session.query(accounts).count()
        tabl = session.query(accounts).all()
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
        if n_id == 1:
            user_setting = accounts(id=free_id, login=log, password=pasw, id_stat=1)
            session.add(user_setting)
            session.commit()
            self.hide()
            dialog = admin_panel(parent=self)
            dialog.show()
        if n_id == 2:
            user_setting = accounts(id=free_id, login=log, password=pasw, id_stat=2)
            session.add(user_setting)
            session.commit()
            f = 0  # флаг
            line = session.query(patient).count()
            tabl = session.query(patient).all()
            free_id2 = 1  # свободный индекс
            while f == 0:
                for i in range(line):
                    if free_id2 == tabl[i].id:
                        f = 1
                if f == 1:
                    free_id2 = free_id2 + 1
                    f = 0
                else:
                    f = 1
            user_setting = patient(id=free_id2, name=self.ui.textEdit_3.toPlainText(), id_acc=free_id)
            session.add(user_setting)
            session.commit()
            self.hide()
            dialog = patient_panel(parent=self)
            dialog.show()

        if n_id == 3:
            user_setting = accounts(id=free_id, login=log, password=pasw, id_stat=3)
            session.add(user_setting)
            session.commit()
            f = 0  # флаг
            line = session.query(personnel).count()
            tabl = session.query(personnel).all()
            free_id2 = 1  # свободный индекс
            while f == 0:
                for i in range(line):
                    if free_id2 == tabl[i].id:
                        f = 1
                if f == 1:
                    free_id2 = free_id2 + 1
                    f = 0
                else:
                    f = 1
            user_setting = personnel(id=free_id2, id_spec=int(self.ui.comboBox_2.currentText()), id_office= int(self.ui.comboBox_3.currentText()),name=self.ui.textEdit_3.toPlainText(), id_acc=free_id)
            session.add(user_setting)
            session.commit()
            self.hide()
            dialog = personal_panel(parent=self)
            dialog.show()