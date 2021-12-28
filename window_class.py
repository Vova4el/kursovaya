
from classes import *
from Qt import *
from Authentication import login_panell
from personalQT import personalUI


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
            table = accounts
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
            collums = ['id', 'id_day', 'id_personnel', 'work_hours', 'free_time', 'break_time']
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["ID", "ID дня", "ID персонала", "рабочее время", "свободное время", "перерыв"])
        if result == "Приём":
            table = reception
            self.ui.tableWidget.setColumnCount(7)
            collums = ['id', 'id_patient', 'id_office', 'id_reception_status', 'id_personnel', 'id_spec', 'date']
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["ID", "ID пациента", "ID кабинета", "ID статуса приёма", "ID персонала", "ID специализации", "Дата"])
        if result == "Мед книжка":
            table = med_knigа
            self.ui.tableWidget.setColumnCount(3)
            collums = ['id', 'id_patient', 'diagnoz']
            self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "ID пациента", "Диагноз"])
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
        print('1')
        self.ui.statusbar.clearMessage()
        print('2')
        if self.ui.prov == 0:
            print('3')
            self.ui.prov = 1
        print('5')
        result = self.ui.comboBox.currentText()
        print('6')
        change = self.ui.comboBox_4.currentText()
        stlb = int(self.ui.comboBox_3.currentText())
        text = self.ui.textBrowser.toPlainText()
        table = patient
        try:
            if result == "Пациенты":
                table = patient
            if result == "День":
                table = day
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
            tabl = session.query(table).all()
            if change == "Обновить элемент":
                query = session.query(table).get(stlb)
                query.name = text
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

    def exit_db_panel(self):
        self.hide()
        self.ui.app.exit()


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
            collums = ['id', 'id_day', 'id_personnel', 'work_hours', 'free_time', 'break_time']
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["ID", "ID дня", "ID персонала", "рабочее время", "свободное время", "перерыв"])
        if result == "Приём":
            table = reception
            self.ui.tableWidget.setColumnCount(7)
            collums = ['id', 'id_patient', 'id_office', 'id_reception_status', 'id_personnel', 'id_spec', 'date']
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["ID", "ID пациента", "ID кабинета", "ID статуса приёма", "ID персонала", "id специализации", "Дата"])
        if result == "Мед книжка":
            table = med_knigа
            self.ui.tableWidget.setColumnCount(3)
            collums = ['id', 'id_patient', 'diagnoz']
            self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "ID пациента", "Диагноз"])
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
        stlb = int(self.ui.comboBox_3.currentText())
        text = self.ui.textBrowser.toPlainText()
        table = patient
        try:
            if result == "Мед книжка":
                table = med_knigа
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
                new = table(id=free_id, addname=text)
                session.add(new)
            tabl = session.query(table).all()
            if change == "Обновить элемент":
                query = session.query(table).get(stlb)
                query.name = text
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

    def exit_db_panel(self):
        self.hide()
        self.ui.app.exit()

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
                    if i.id_stat == 3:
                        print('fffffff')
                        j = session.query(accounts).filter(accounts.login== log).first()
                        print('fffffff')
                        print(j.id)
                        p = session.query(personnel).filter(personnel.id_acc== j.id).first()
                        print(p)
                        glob_id= p.id
                        print(glob_id)
                        dialog = personal_panel(parent=self)
                        dialog.show()
                else:
                    self.ui.statusbar.showMessage("Введён неверный пароль")
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
        user_setting = accounts(id=session.query(accounts).count() + 1, login=log, password=pasw,
                                stat_id=int(2))
        session.add(user_setting)
        session.commit()
        self.hide()
        dialog = admin_panel(parent=self)
        dialog.show()