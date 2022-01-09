from personnel_window import *
from backup_bd import *
from Authentication import login_panell
import classes
from admin_window import admin_panel
from patient_window import patient_panel

#Окно входа
class log_panel(QMainWindow):
    def __init__(self, parent=None):
        super(log_panel, self).__init__(parent)
        self.ui = login_panell()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.inter_to_app())
        self.ui.pushButton_2.clicked.connect(lambda: self.create_acc())
        r = session.query(reception).all()
        for i in range(session.query(reception).count()):
            if datetime.strptime(r[i].date, '%Y-%m-%d %H:%M:%S') < datetime.now():
                r[i].id_reception_status = 1
        session.commit()
        DumpPostgreSql()

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
                        j = session.query(accounts).filter(accounts.login == log).first()
                        p = session.query(personnel).filter(personnel.id_acc == j.id).first()
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
            DumpPostgreSql()
            self.hide()
            dialog = admin_panel(parent=self)
            dialog.show()
        if n_id == 2:
            user_setting = accounts(id=free_id, login=log, password=pasw, id_stat=2)
            session.add(user_setting)
            session.commit()
            DumpPostgreSql()
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
            DumpPostgreSql()

            self.hide()
            dialog = patient_panel(parent=self)
            dialog.show()

        if n_id == 3:
            user_setting = accounts(id=free_id, login=log, password=pasw, id_stat=3)
            session.add(user_setting)
            session.commit()
            DumpPostgreSql()
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
            DumpPostgreSql()
            self.hide()
            dialog = personal_panel(parent=self)
            dialog.show()