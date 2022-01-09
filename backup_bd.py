import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import psycopg2
import sys
from datetime import timedelta, datetime, time
from classes import *

def send_email(filepath):
    addr_to = "voff.chernih@yandex.ru"
    msg_subj = "Резервная копия базы данных"
    msg_text = "Копия: "
    addr_from = "vladimir.tchernih2020@gmail.com"
    password = "xoaljlvuprmhzwzs"
    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = msg_subj

    body = msg_text
    msg.attach(MIMEText(body, 'plain'))
    add_file(msg, filepath)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()


def add_file(msg, filepath):
    filename = os.path.basename(filepath)
    if os.path.isfile(filepath):
        ctype, encoding = mimetypes.guess_type(filepath)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        if maintype == 'text':
            with open(filepath) as fp:
                file = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
        elif maintype == 'image':
            with open(filepath, 'rb') as fp:
                file = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
        elif maintype == 'audio':
            with open(filepath, 'rb') as fp:
                file = MIMEAudio(fp.read(), _subtype=subtype)
                fp.close()
        else:
            with open(filepath, 'rb') as fp:
                file = MIMEBase(maintype, subtype)
                file.set_payload(fp.read())
                fp.close()
            encoders.encode_base64(file)
        file.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(file)

def CreateFileName(dbms):
    filename = f"{str((datetime.now()).date())}_{dbms}_dump.sql"
    return filename

def DumpPostgreSql():
    con = None
    try:
        con = psycopg2.connect(database='medical_institution', user='postgres', password='13241340', port='5432')
        cur = con.cursor()
        filename = CreateFileName('medical_institution')
        f = open(filename, 'w')
        f.write(
            "CREATE TABLE user_status(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    status text\n);\n\n")
        f.write("CREATE TABLE Accounts(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    Login VARCHAR (40) NOT NULL,\n"
                "    Password VARCHAR (11) NOT NULL,\n    id_stat BIGSERIAL NOT NULL,\n    FOREIGN KEY(id_stat) REFERENCES "
                "user_status(ID)\n);\n\n")
        f.write("CREATE TABLE patient(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    name text,\n"
                "    id_acc BIGSERIAL NOT NULL,\n    FOREIGN KEY(id_stat) REFERENCES Accounts(ID)\n);\n\n")
        f.write(
            "CREATE TABLE specialization(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    name_spec text\n);\n\n")
        f.write(
            "CREATE TABLE offices(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n   cab_num INT NOT NULL\n);\n\n")
        f.write(
            "CREATE TABLE personnel(\n    id_spec BIGSERIAL NOT NULL,\n   FOREIGN KEY(id_spec) REFERENCES specialization(id),\n    id_office BIGSERIAL NOT NULL,\n"
            "    FOREIGN KEY(id_office) REFERENCES offices(id),\n    name text,\n    id_acc BIGSERIAL NOT NULL,\n"
            "    FOREIGN KEY(id_acc) REFERENCES Accounts(ID)\n);\n\n")
        f.write(
            "CREATE TABLE reception_status(\n id BIGSERIAL NOT NULL PRIMARY KEY,\n    name VARCHAR(100) NOT NULL\n);\n\n")
        f.write(
            "CREATE TABLE day(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    name text\n);\n\n")
        f.write(
            "CREATE TABLE working_hours(\n        id BIGSERIAL NOT NULL PRIMARY KEY,\n    id_day BIGSERIAL NOT NULL,\n"
            "    FOREIGN KEY(id_day) REFERENCES day(id),\n    id_spec BIGSERIAL NOT NULL,\n"
            "    FOREIGN KEY(id_spec) REFERENCES specialization(id),\n    work_hours text[],\n    break_time text[]\n);\n\n")
        f.write(
            "CREATE TABLE med_knigа(\n        id BIGSERIAL NOT NULL PRIMARY KEY,\n       id_patient BIGSERIAL NOT NULL,\n"
            "    FOREIGN KEY(id_patient) REFERENCES patient(id),\n    id_personnel BIGSERIAL NOT NULL,\n"
            "    FOREIGN KEY(id_personnel) REFERENCES personnel(id),\n    id_spec BIGSERIAL NOT NULL,\n"
            "    FOREIGN KEY(id_spec) REFERENCES specialization(id),\n    diagnoz text\n);\n\n")
        f.write(
            "CREATE TABLE reception(\n        id BIGSERIAL NOT NULL PRIMARY KEY,\n       id_patient BIGSERIAL NOT NULL,\n"
            "    FOREIGN KEY(id_patient) REFERENCES patient(id),\n  id_office BIGSERIAL NOT NULL,\n"
            "    FOREIGN KEY(id_office) REFERENCES offices(id)\n        ON DELETE CASCADE,\n"
            "    id_reception_status BIGSERIAL NOT NULL,\n    FOREIGN KEY(id_reception_status) REFERENCES reception_status(id)\n"
            "        ON DELETE CASCADE,\n    id_personnel BIGSERIAL NOT NULL,\n    FOREIGN KEY(id_personnel) REFERENCES personnel(id)\n"
            "        ON DELETE CASCADE,\n    id_spec BIGSERIAL NOT NULL,\n    FOREIGN KEY(id_spec) REFERENCES specialization(id)\n"
            "        ON DELETE CASCADE,\n    date text NOT NULL\n);\n\n")
        for i in range(11):
            table_name = ""
            if i == 0:
                table_name = "user_status"
            if i == 1:
                table_name = "Accounts"
            if i == 2:
                table_name = "patient"
            if i == 3:
                table_name = "specialization"
            if i == 4:
                table_name = "offices"
            if i == 5:
                table_name = "personnel"
            if i == 6:
                table_name = "reception_status"
            if i == 7:
                table_name = "day"
            if i == 8:
                table_name = "working_hours"
            if i == 9:
                table_name = "med_knigа"
            if i == 10:
                table_name = "reception"
            cur.execute(f'SELECT * FROM {table_name}')
            for row in cur:
                f.write(f"insert into {table_name} values " + str(row) + ";\n")
            if i != 10:
                f.write("\n")
        f.close()
        send_email(f"./{filename}")
        os.remove(f"./{filename}")
    except psycopg2.DatabaseError(psycopg2.Error):
        print('Error %s' % psycopg2.Error)
        sys.exit(1)
    finally:
        if con:
            con.close()