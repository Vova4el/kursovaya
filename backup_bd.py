import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import json
from classes import *
from sqlalchemy.ext.serializer import loads, dumps


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


def dump_sqlalchemy():
    meta.reflect(bind=engine)
    result = {}
    for table in meta.sorted_tables:
        result[table.name] = [dict(row) for row in engine.execute(table.select())]
    pop = json.dumps(result)
    with open('data_base.json', 'w', encoding='utf-8') as f:
        json.dump(pop, f, ensure_ascii=False, indent=4)
    filepath = "./data_base.json"
    send_email(filepath)